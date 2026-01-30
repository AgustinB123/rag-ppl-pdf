---
title: Integración de PPL con .NET
description: Cómo importar liberias de .NET (dll)
published: true
date: 2024-04-30T13:39:42.293Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:51:47.267Z
---

# Introducción

En PPL.​NET es posible importar librerías de terceros y utilizarlas directamente en los scritps del interprete (Eventos e informes).

A continuación veremos algunos ejemplos utilizando las librerías de testing del core de v6.

# Require

Para poder utilizar funciones de una librería de terceros, lo primero que tenemos que hacer es **referenciarla**. 

Tener en cuenta que la DLL de .NET debe compilarse para **Framework 4.8** (o el mismo qeu tenga el Core que la va a invocar). 

La clase a utilizar debe ser **public class**.

Para esto, vamos a utilizar la función **require**, que le indica al interprete la ubicación del archivo que tiene que inspeccionar para generar la metadata necesaria para poder importar los tipos de datos definidos en ese librería.

```
* La siguiente llamada importa la librería que contiene el set de pruebas del
* interprete de v6. 
require '../Src/PPLI.Tests/bin/Debug/PPLI.Tests.dll'
```

_nota: La ruta del la dll es relativa a la ubicación del ejecutable que este corriendo el script._

_nota: En el caso de la función **require** los paréntesis son opcionales._

De alguna manera la función **require** es similar al comando *Add Reference* de Visual Studio. En lugar de ser una acción contextual, es una instrucción en el script, pero básicamente, terminan haciendo lo mismo.

# Import

Una vez que le indicamos al interprete cuales son los assemblies adicionales que vamos a utilizar en el script, tenemos que indicarle cuales son los tipos de datos que vamos a necesitar. Para esto, se utiliza la función **import**.

```
import Bar, 'PPLI.Test.Bar'
```

_nota: En el caso de la función **import** los paréntesis son opcionales._

Esta función recibe dos parámetros, por un lado tenemos que especificar el **ID** que vamos a utilizar para hacer referencia a la clase (generalmente, el nombre de la clase) y por el otro **el nombre completo de la clase** (namespace.clase).

# Operador New

Una vez que agregamos la referencia e importamos los tipos de datos que vamos a utilizar, podemos empezar a crear instancias de los tipos de datos importados utilizando el operador **new**.

```
let &b new Bar('Hello World') 
```

# Ejemplo

```
* Referenciamos la libreria que contiene el set de pruebas 
* del interprete de PPL.NET.

require '../test/bin/ppli.tests.dll'

import Bar, 'PPLI.Test.Bar'

let &b new Bar('Hello World') 

let res, &b.Baz()
```

# Acceso a datos

Para facilitar el acceso a datos desde una libreria, es posible utilizar una instancia de **IDataBase** de PPL.​NET.

Esta instancia permite acceder a los mismos metodos que utiliza el core para obtener recursos de la base de datos.

Para esto es necesario que la libreria referencie a **PPL.NET.Common.dll**.
Esta dll deberia actualizarse y la versión deberia estar alineada a la utilizada en la aplicación de PPL.​NET.

> En caso de que la libreria se distribuya en el mismo directorio que la aplicación de **PPL.​NET**, no es necesario incluir **PPL.NET.Common.dll**

## Ejemplo

### Desde .NET

Una vez que se agregue como referencia a **PPL.NET.Common.dll**, podemos utilizar el tipo de dato **IDataBase**.

De esta manera es posible definir un metodo (en este ejemplo el constructor de la clase) para recibir como parametro una instancia de la base de datos.

```csharp
using System;
using PPL.NET.Common.Data;

namespace Evento.Test {
    public class Main {
        private readonly IDataBase _db;
        
        public Main(IDataBase db) {
            _db = db;
        }

        public void ExecuteDbFuncs() {
            // Ejemplo de como obtener un scalar.
            var date = _db.GetScalar("Select GetDate()");
            Console.WriteLine($"GetScalar result: {date}");

            // Cómo obtener un registro.
            var row = _db.GetSingleRow($"Select TOP 1 * from {_db.Dbo}.VARIABLES");
            Console.WriteLine($"GetSingleRow result: {row["Codigo"]}");

            // Cómo obtener más de un registro.
            var rows = _db.GetRows($"Select TOP 1 * from {_db.Dbo}.OPERACIONES");
            foreach (var r in rows) {
                Console.WriteLine($"GetRows result: {r["NrOperacion"]}");
            }
            
            // Ejecutar un comando (sentencia comentada '--')
            _db.ExecuteCmd($"-- UPDATE {_db.Dbo}.OPERACIONES ...");
        }

        public void GetParams(string str, double dbl, DateTime dt) {
            Console.WriteLine($"GetParam string: {str}");
            Console.WriteLine($"GetParam double: {dbl}");
            Console.WriteLine($"GetParam datetime: {dt}");
        }
    }
}
```

### Desde PPL

El siguiente ejemplo nos muestra como consumir e interactuar con la clase que definimos en **.NET**.

Utilizamos la función PPL **GetDataBase()** para obtener la instancia de la base de datos que va a utilizar la libreria.

```ruby
** Referencio la libreria a consumir
** En este caso, suponemos que la dll se encuentra en el mismo directorio que el exe del PPLStudio.
require 'Evento.Test.dll'

** Importamos la clase a instanciar y le asignamos el Alias 'Test'
import Test, 'Evento.Test.Main'

** Utilizamos un Dialogo de PPL para solicitarle datos al usuario
** y enviarlos como parametros al objeto de .NET
CrearDialogo
   String1: 'STRING'
   Cantidad1: 'DOUBLE'
   Fecha1: 'DATE'
FinDialogo

** Instanciamos la clase Test.Main
** La funcion PPL GetDataBase() nos devuelve la instancia de base de datos
** que utiliza el scope de ejecución actual
let &evento new Test(GetDataBase())

** Ejecutamos el metodo ExecuteDbFuncs() del objeto Test.Main
&evento.ExecuteDbFuncs()

** Ejecutamos el metodo GetParams() del objeto Test.Main
** Le pasamos como parametros los valores obtenidos del dialogo de PPL.
** Es necesario utilizar las funciones STR(), DBL() y DAT() 
** para convertir los valores a un tipo de dato primitivo de .NET
&evento.GetParams(STR(Dialogo.String1), DBL(Dialogo.Cantidad1), DAT(Dialogo.Fecha1))
```


[Ver Ejemplo de Consulta de Memoria](/core/consulta-estado-de-memoria-desde-ppl-usando-memory-utils-dll)

# Algunos tips

1. La DLL .NET debe ser creada en el mismo framework donde va a ser hosteada, por ejemplo .NET 4.6.1 (Ademas el proyecto tiene que esta definido como .NET Framework y no .NET Standard)
1. Los metodos a exponer en la DLL deben ser *public*. 
1. Puede usarse dotPeek de JetBrains para navegar la libreria y ver los metodos disponibles y sus parametros. 
1. Si se pasan como parametros string rutas con directorios, las barras invertidas se toman como caracter de scape (ver solucion a esto). 
1. Castear los parametros que se le pasa al metodo. PPL tiene como tipo de dato un standard que no se castea solo a .NET. 

```
int >> Int(object val)
long >> Lng(object val)
double >> Dbl(object val)
decimal >> Decimal(object val) 
string >> Str(object val)
bool >> Bln(object val)
DateTime >> Dat(object val)
```

Ejemplo: 
Fuente clase C#

```ruby
using System;
using iTextSharp.text.pdf;
using iTextSharp.text;
using iTextSharp;
using iTextSharpSign;

namespace iTextSharpSign
{
    public class FPAPDFSign
    {
        public void FirmarPDF(string source, string destination, string certificate, string password, bool visible,
              string reason, string contact, string location, string title)
        {

            Cert myCert = null;
            myCert = new Cert(certificate, password);

            //Adding Meta Datas
            MetaData MyMD = new MetaData();
            MyMD.Author = "FPA Portfolio v6";
            MyMD.Title = title;
            MyMD.Subject = "";
            MyMD.Keywords = "";
            MyMD.Creator = "iTextSharp";
            MyMD.Producer = "Evento PPL";

            PDFSigner pdfs = new PDFSigner(source, destination, myCert, MyMD);
            pdfs.Sign(reason, contact, location, visible);
        }
    }
}
```

Ejemplo llamada desde PPL

```ruby
require '../lib/FPASign.dll'

import FPAPDFSign, 'iTextSharpSign.FPAPDFSign'

let &S new FPAPDFSign()

&S.FirmarPDF("C:\FPA\AA.pdf" , "C:\FPA\BB.pdf", "C:\FPA\new_sin_pass.pfx", "", true,"Firma", "FPA Software", "Palm Springs", "Contador")

** &firmaPDF.FirmarPDF(Str(Dialogo.Archivo1), Str(Dialogo.Archivo2), Str(Dialogo.Archivo3), Str(''), true, Str(" ") , Str(" ") , Str(" "), Str(" "))
```
