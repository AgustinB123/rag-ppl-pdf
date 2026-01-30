function readScript(onSuccess) {
	fs = require('fs');
	fs.readFile('auths.dat', 'utf8', function (err,data) {
		if (err) {
			console.log('Error read auths.dat');
			return console.log(err);
		}
		onSuccess(data);
	});
}


function getAuthorizations(onSuccess){
	readScript(function (data) {
		var auths =  [];
		var lines = data.split('\n');
		lines.forEach(function(line) {
			line = line.trim();
			if(line !== '') {
			    var args = line.split('|');
				var user = args[0];
				var perfiles = [];
				for (i=1; i < args.length; ++i) {
					perfiles.push(args[i].trim());
				}
				var auth = {User : user, Perfiles : perfiles};
				auths.push(auth);
			}
		});
		console.log("Authorizations loaded...")
		console.log(auths);
		onSuccess(auths);
	});
}


function Authenticate(xml, response) {
	var parseString = require('xml2js').parseString;
	parseString(xml, function (err, result) {
		var auth = result['soap:Envelope']['soap:Body'][0].Authenticate[0];
		var user = auth.UserId[0];
		console.log("Login request user "+user);
		getAuthorizations(function (auths){
			var success = false;
			auths.forEach(function(auth){
				console.log("Checking user "+auth.User);
				if(auth.User===user){
					console.log("User authorized "+user);
					response.end(successXml(auth.Perfiles));
					success = true;
					return;
				}
			});
			if(!success) {
				console.log("User NOT authorized "+user);
				response.end(errorXml());
			}
		});
	});
	return;
}


function successXml(perfiles){
	var xml = '<?xml version="1.0" encoding="utf-8"?> <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"> <soap:Body> <AuthenticateResponse xmlns="http://tempuri.org/TranService/Security"> <AuthenticateResult> <SecurityProviderServer xmlns=""> <Status>OK</Status> <SessionID>AACCb0113312006052301130442</SessionID> <UserID>b011331</UserID> <FirstName>Eduardo</FirstName> <LastName>de la Rua</LastName> <Office> </Office> <Companies> <Company> <Name>0072</Name> </Company> </Companies> <Groups>';
	for (i=0; i < perfiles.length; ++i) {
		xml += '<Group><Id>'+perfiles[i]+'</Id></Group>';
	}
	xml += '</Groups> <Properties> <Property> <Decimals>0</Decimals> <Description>Canal</Description> <Length>4</Length> <Name>CANAL</Name> <RefTableCodeCol/> <RefTableDesCol/> <RefTableName/> <ValueType>System.String</ValueType> <User>B011331</User> <Value>ACC</Value> </Property> </Properties> <Infos><Info><Id>1</Id><Name>ORASAM</Name><TypeId>1</TypeId><TypeCode>DB</TypeCode><TypeDesc>BASE DE DATOS</TypeDesc><Values><Value><Def_Id>3</Def_Id><FieldValue>SAM</FieldValue></Value><Value><Def_Id>4</Def_Id><FieldValue>SAM</FieldValue></Value></Values></Info></Infos> </SecurityProviderServer> </AuthenticateResult> </AuthenticateResponse> </soap:Body> </soap:Envelope>';
	return xml;
}


function errorXml(){
	return '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body> <AuthenticateResponse xmlns="http://tempuri.org/TranService/Security"> <AuthenticateResult> <SecurityProvider xmlns=""> <Status>ERROR</Status> <ErrorCode>0</ErrorCode> <ErrorMessage>El usuario no esta dado alta en el simulador de Security Provider</ErrorMessage> <FriendlyErrorMessage>El usuario no esta dado alta en el simulador de Security Provider</FriendlyErrorMessage> </SecurityProvider> </AuthenticateResult> </AuthenticateResponse> </soap:Body> </soap:Envelope>';
}


function editScript(response) {
	console.log("Edit form request...");
	readScript(function(script) {
		response.end(editView(script));
	});
}


function editView(script) {
	var html = '<html> <head> <title>Editar Script - Security Provider Simulator</title> </head> <body> <h1>Editar Script - Security Provider Simulator</h1> <ul> <li>Este script contiene los usuarios que seran autorizados.</li><li>Una linea por usuario a autenticar</li> <li>Parametros separador por pipe "|"</li> <li>Primer parametro nombre de usuario</li> <li>A partir del segundo parametro, los perfiles que tendra el usuario.</li> <li>Ejemplo: "SAM|BACKOF|TRADER"</li> </ul> <form action="save" method="post"> <textarea name="script" id="" cols="100" rows="20">';
	html += script;
	html += '</textarea> <input type="submit" value="Guardar" /> </form> </body> </html>';
	return html;
}


function saveScript(script, response){
	console.log("Save form request...");
	console.log("Script: \n" + script);
	var fs = require('fs');
	fs.writeFile("auths.dat", script, function(err) {
		if(err) {
			console.log('Error write auths.dat');
			return console.log(err);
		}
		console.log("Auth script saved!");
	}); 
	response.end("<h1>Script modificado correctamente!</h1>");
}


function getRequestBody(request, onSuccess) {
	var body = [];
	request.on('data', function(chunk) {
		body.push(chunk);
	}).on('end', function() {
		body = Buffer.concat(body).toString();
		//console.log('Body: '+body);
		onSuccess(body);
	})
	
}


var http = require('http');
var server = http.createServer(function (request, response) {
	console.log('URL: '+request.url);
	console.log('Method: '+request.method);
	console.log('Headers: '+request.headers);
	
	if (request.method === 'POST' && request.url === '/sp') {
		//Request de autenticacion
		getRequestBody(request, function(body){
			response.setHeader('Content-Type', 'application/xml');
			Authenticate(body, response);
		});
	} else {
		if (request.method === 'GET' && request.url === '/edit') {
			//Request de formulario de edicion de script
			editScript(response);
		} else {
			if (request.method === 'POST' && request.url === '/save') {
				//Request de save form
				getRequestBody(request, function(body){
					var qs = require('querystring');
					var script = qs.parse(body).script;
					saveScript(script, response);
				});
			} else {
				//No existe
				response.statusCode = 404;
				response.end();
			}
		}
		
	}
});

var ip = '10.15.3.137';
server.listen(1313, ip);
console.log("SecurityProvider Simulator running at http://"+ip+":1313/");