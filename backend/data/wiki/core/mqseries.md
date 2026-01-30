---
title: MQ Series (IBM)
description: Implementacion en PPL del conector a MQSeries de IBM
published: true
date: 2023-03-23T18:05:52.284Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:46:33.209Z
---

## MQ Series 
IBM MQ es una familia de productos de middleware de mensajería que IBM lanzó en diciembre de 1993. IBM MQ fue originalmente llamado MQSeries, y fue rebautizado como WebSphere MQ en 2002 para unificar un conjunto de productos en la suite WebSphere. En abril de 2014, volvió a cambiar de nombre a IBM MQ. Los productos que está incluidos en la familia MQ son IBM MQ, IBM MQ Advanced, IBM MQ Appliance, IBM MQ para z/OS, e IBM MQ en IBM Cloud.

MQ permite que aplicaciones independientes y potencialmente no concurrentes en un sistema distribuido puedan comunicarse con seguridad con otras, usando mensajes. MQ está disponible sobre un gran número de plataformas (tanto IBM como no IBM), incluyendo z/OS (mainframe), OS/400 (IBM System i o AS/400), TPF, UNIX (AIX, HP-UX, Solaris), HP <i>NonStop</i>, OpenVMS, Linux, y Windows de Microsoft.

https://es.wikipedia.org/wiki/IBM_MQ

## Componente MQ en PPL

### **Funciones VOID**

Estas funciones corresponden al objeto *MQIC32.DLL* de IBM en la implementacion C (DLL de 32 bits), existe un componente NET similar. 
https://www.ibm.com/docs/en/ibm-mq/9.0?topic=applications-developing-net


```MQS.MQConectar(sQManager)```  // Crea una conexion con el MQ.

Utiliza funcion C de MQIC32.DLL:

```
MQCONN(FPQMName,                 //* queue manager                  */
             @FHcon,                   //* connection handle              */
             @FCompCode,               //* completion code                */
             @FCReason);               //* reason code                    */
 

```


```MQS.MQDesconectar``` // Cierra una conexion con el MQ
Utiliza funcion C 
```
MQDISC(@FHcon,                   //* connection handle            */
         @FCompCode,               //* completion code              */
         @FCReason);               //* reason code                  */

```

```MQS.MQAbrir(sTargetQueue, bModoLectura)``` // primer parametro define la cola a la que se va a leer o escribir, y el modo lectura es un integer que si es 1 
Utiliza funcion C 
```
if Lectura then
      FO_options := MQOO_INPUT_AS_Q_DEF     // open queue for input
                           + MQOO_FAIL_IF_QUIESCING// but not if MQM stopping
     else
       FO_options := MQOO_OUTPUT              // open queue for output
                     + MQOO_FAIL_IF_QUIESCING // but not if MQM stopping
                     + MQOO_SET_ALL_CONTEXT;
 
     MQOPEN(Self.FConexion.Handle,     //* connection handle            */
           @od,                       //* object descriptor for queue  */
           FO_options,                //* open options                 */
           @Hobj,                     //* object handle                */
           @OpenCode,                 //* MQOPEN completion code       */
           @Reason);                  //* reason code                  */
```



```MQS.MQCerrar``` // Cierra la cola abierta con Abrir
Utiliza funcion C 
```
  	if Self.FEstaAbiertoElCanal then begin
    FEstaAbiertoElCanal := false;
     od := MQOD_DEFAULT;                  // Object Descriptor
     md := MQMD_DEFAULT;                  // Message Descriptor
     gmo := MQGMO_DEFAULT;                // get message options
     pmo := MQPMO_DEFAULT;                // put message options
 
     if FLongBuffer >= 0 then begin
       FillChar(Buffer,SizeOf(buffer),#0);
       FLongBuffer := -1;
       FLongRec := -1;
     end;
 
     C_options := 0;                 // no close options
     MQCLOSE(Self.FConexion.Handle,  // connection handle
            @Hobj,                  // object handle
            C_options,
            @CompCode,              // completion code
            @Reason);               // reason code
 
```

```MQS.MQLeer(Trans)``` //  Trans parametro booleano, la funcion deja en DialogoOK un valor booleano. 
Utiliza funcion C 
```
>   gmo.Options := MQGMO_WAIT        //* wait for new messages           */
>                {+ MQGMO_CONVERT}; //* convert if necessary            */
> 
>                                  // se puede usar MQWI_UNLIMITED
>   gmo.WaitInterval := FTimeOut;      //* 15 second limit for waiting     */
> 
>   if Transaccion then
>     gmo.Options := gmo.Options + MQGMO_SYNCPOINT;
> 
>   //****************************************************************/
>   //*                                                              */
>   //*   In order to read the messages in sequence, MsgId and       */
>   //*   CorrelID must have the default value.  MQGET sets them     */
>   //*   to the values in for message it returns, so re-initialise  */
>   //*   them before every call                                     */
>   //*                                                              */
>   //****************************************************************/
> 
>   StrLCopy(md.MsgId, MQMI_NONE, sizeof(md.MsgId));
>   StrLCopy(md.CorrelId, MQCI_NONE, sizeof(md.CorrelId));
> 
>   //****************************************************************/
>   //*                                                              */
>   //*   MQGET sets Encoding and CodedCharSetId to the values in    */
>   //*   the message returned, so these fields should be reset to   */
>   //*   the default values before every call, as MQGMO_CONVERT is  */
>   //*   specified.                                                 */
>   //*                                                              */
>   //****************************************************************/
> 
>   md.Encoding       := MQENC_NATIVE;
>   md.CodedCharSetId := MQCCSI_Q_MGR;
> 
>   MQGET(Self.FConexion.Handle,//* connection handle               */
>        Hobj,                //* object handle                   */
>        @md,                 //* message descriptor              */
>        @gmo,                //* default options (datagram)      */
>        FLongBuffer,         //* buffer length                   */
>        @Buffer[0],          //* message buffer                  */
>        @FLongRec,           //* message length                  */
>        @CompCode,           //* completion code                 */
>        @Reason);            //* reason code                     */
> 
> 
```



```MQS.MQLeerGrupo(Trans)``` //  Trans parametro booleano, la funcion deja en DialogoOK un valor booleano. 
Utiliza funcion C 
```
>   gmo.Options := MQGMO_WAIT        //* wait for new messages           */
>                {+ MQGMO_CONVERT}; //* convert if necessary            */
> 
>                                  // se puede usar MQWI_UNLIMITED
>   gmo.WaitInterval := FTimeOut;      //* 15 second limit for waiting     */
> 
>   if Transaccion then
>     gmo.Options := gmo.Options + MQGMO_SYNCPOINT;
> 
>   //****************************************************************/
>   //*                                                              */
>   //*   In order to read the messages in sequence, MsgId and       */
>   //*   CorrelID must have the default value.  MQGET sets them     */
>   //*   to the values in for message it returns, so re-initialise  */
>   //*   them before every call                                     */
>   //*                                                              */
>   //****************************************************************/
> 
>   md.Version  := MQMD_VERSION_2;
>   gmo.Version := MQGMO_VERSION_2;
>   gmo.Options := gmo.Options + MQGMO_LOGICAL_ORDER;
> 
>   StrLCopy(md.MsgId, MQMI_NONE, sizeof(md.MsgId));
>   StrLCopy(md.CorrelId, MQCI_NONE, sizeof(md.CorrelId));
> 
>   //****************************************************************/
>   //*                                                              */
>   //*   MQGET sets Encoding and CodedCharSetId to the values in    */
>   //*   the message returned, so these fields should be reset to   */
>   //*   the default values before every call, as MQGMO_CONVERT is  */
>   //*   specified.                                                 */
>   //*                                                              */
>   //****************************************************************/
> 
>   md.Encoding       := MQENC_NATIVE;
>   md.CodedCharSetId := MQCCSI_Q_MGR;
> 
>   MQGET(Self.FConexion.Handle,//* connection handle               */
>        Hobj,                //* object handle                   */
>        @md,                 //* message descriptor              */
>        @gmo,                //* default options (datagram)      */
>        FLongBuffer,         //* buffer length                   */
>        @Buffer[0],          //* message buffer                  */
>        @FLongRec,           //* message length                  */
>        @CompCode,           //* completion code                 */
>        @Reason);            //* reason code                     */
> 
> 
```


```MQS.MQEscribir(ReplyToQ, ReplyToQMgr, ApplOriginData)``` // 
Utiliza funcion C 
```
>   CompCode := OpenCode;        //* use MQOPEN result for initial test */
>   StrLCopy(md.Format, PChar(MQFMT_STRING)//* character string format         */
>           , MQ_FORMAT_LENGTH);
> 
>   //****************************************************************/
>   //*                                                              */
>   //*   Put each buffer to the message queue                       */
>   //*                                                              */
>   //****************************************************************/
>   if (FLongBuffer > 0) then begin
>     StrLCopy(md.MsgId,   //* reset MsgId to get a new one    */
>             MQMI_NONE, SizeOf(md.MsgId));
> 
>     StrLCopy(md.MsgId,   //* reset MsgId to get a new one    */
>             MQMI_NONE, SizeOf(md.MsgId) );
> 
>     StrLCopy(md.CorrelId, //* reset CorrelId to get a new one */
>             MQCI_NONE, SizeOf(md.CorrelId) );
> 
>     if ReplyToQ <> '' then // Agregado por JCP
>       StrPCopy(md.ReplyToQ, ReplyToQ);
>     if ReplyToQMgr <> '' then // Agregado por JCP
>       StrPCopy(md.ReplyToQMgr, ReplyToQMgr);
>     if ApplOriginData <> '' then
>       StrPCopy(md.ApplOriginData, ApplOriginData);
> 
>     md.Priority := 0;          // Este campo es importante!!!!!!!
> 
>     MQPUT(Self.FConexion.Handle,//* connection handle               */
>          Hobj,                //* object handle                   */
>          @md,                 //* message descriptor              */
>          @pmo,                //* default options (datagram)      */
>          FLongBuffer,         //* buffer length                   */
>          @Buffer[0],          //* message buffer                  */
>          @CompCode,           //* completion code                 */
>          @Reason);            //* reason code                     */
> 
```


```MQS.MQEscribirGrupo(ReplyToQ, ReplyToQMgr, ApplOriginData, MsgId, CorrelId, GroupId) ``` // 
Utiliza funcion C 
```
>   md.Version  := MQMD_VERSION_2;
>   pmo.Version := MQPMO_VERSION_2;
> 
>   pmo.Options := MQPMO_LOGICAL_ORDER;
> 
>   if not Self.FEstaAbiertoElCanal then
>     raise EMQError.Create('No se hizo OPEN de MQ');
> 
>   if Self.FEsLectura then
>     raise EMQError.Create('MQ fue abierto para lectura');
> 
>   if Self.FLongBuffer <= 0 then
>     raise EMQError.Create('No hay espacio para datos en el buffer de MQ');
> 
>   CompCode := OpenCode;        //* use MQOPEN result for initial test */
>   StrLCopy(md.Format, PChar(MQFMT_STRING)//* character string format         */
>           , MQ_FORMAT_LENGTH);
> 
>   //****************************************************************/
>   //*                                                              */
>   //*   Put each buffer to the message queue                       */
>   //*                                                              */
>   //****************************************************************/
>   if (FLongBuffer > 0) then begin
> 
>     if MsgId <> '' then // Agregado por JCP
>       StrPCopy(md.MsgId, MsgId);
> 
>     if CorrelId <> '' then // Agregado por JCP
>       StrPCopy(md.CorrelId, CorrelId);
> 
>     if GroupId <> '' then // Agregado por JCP
>       StrPCopy(md.GroupId, GroupId);
> 
>     md.MsgSeqNumber := MsgSeqNumber;
> 
>     if MsgFlags <> 0 then
>       md.MsgFlags := MsgFlags;
> 
>     if ReplyToQ <> '' then // Agregado por JCP
>       StrPCopy(md.ReplyToQ, ReplyToQ);
>     if ReplyToQMgr <> '' then // Agregado por JCP
>       StrPCopy(md.ReplyToQMgr, ReplyToQMgr);
>     if ApplOriginData <> '' then
>       StrPCopy(md.ApplOriginData, ApplOriginData);
> 
>     md.Priority := 0;          // Este campo es importante!!!!!!!
> 
>     MQPUT(Self.FConexion.Handle,//* connection handle               */
>          Hobj,                //* object handle                   */
>          @md,                 //* message descriptor              */
>          @pmo,                //* default options (datagram)      */
>          FLongBuffer,         //* buffer length                   */
>          @Buffer[0],          //* message buffer                  */
>          @CompCode,           //* completion code                 */
>          @Reason);            //* reason code                     */
> 
> 
```


```MQS.MQLongBuffer(iLongBuffer)``` // Hace SetLongBuffer con el valor
Setea el parametro LongBuffer que se usa en Todas las Escrituras. 


 ```MQS.MQEscribirCampo(sValor, iLongitud, iTipo)``` // Pone en el Buffer de MQ el valor pasado como parametro, procesandolo segun el tipo: 
-  0: rellena la string hasta (iLongtud) con blancos, padea al final, seria
-  1: Empaqueta el campo
-  2: Convierte el campo de Ascii a EBCDIC
-  3: Pasa el numero de hexadecimal a string --> '20' = 20h 


```MQS.MQTimeOut(iTiempoSegundos)``` // Setea la propiedad de timeout en segundos, multiplica por 1000 porque el valor en la DLL de MQ es milisegundos. El default de la conexion es 15.000 miliseconds (si, 15 segundos). 
No corresponde a funcion C, porque la utiliza en cada funcion de Lectura. 

```MQS.MQCommit``` // Hace commit de la transaccion.
Utiliza funcion C 
```
>   MQCMIT(Self.FConexion.Handle, //* connection handle               */
>           @CompCode,             //* completion code                 */
>           @Reason);              //* reason code                     */
> 
```


```MQS.MQRollBack``` // Hace rollback de la transaccion. 
Utiliza funcion C 
```
>   MQBACK(Self.FConexion.Handle, //* connection handle               */
>           @CompCode,             //* completion code                 */
>           @Reason);              //* reason code                     */
> 
```


```MQS.MQExportaAltamira``` // Pasa a Altamira los datos del buffer de MQ; 

### Funciones Numericas

```MQS.MQUltNroError``` // Devuelve el ultimo error de la funcion llamada con anterioridad. 

### Funciones String

```MQS.LeerCampo(iPosicion, iLongitud, iTipoi)``` // Devuelve del buffer, la string que empieza en iPosicion, con iLongitud de caracteres y convertidas segun el iTipo
-  1: Desempaqueta el campo
-  2: Convierte el campo de EBCDIC a ASCII
-  3: Pasa el numero de hexadecimal a string --> 20h  = '20'
-  4: 
```
            // Se fija donde está el fin de registro (FFh) y lo anterior lo
            // convierte a EBCDIC y lo posterior lo pasa a blanco.
            // El fin de registro lo deja intacto
             x := System.Pos(Chr(255), StrPas(S));
             if x <> 0 then begin
               Temp := StringOfChar(' ', Longitud - x);
               Move(Temp[1], S[x], Longitud - x);
             end;
             Ebcdic2Ascii(S, Copy(S, 0, x -1));
```


## Componente MQ en NET
Componente que permite interactuar con [IBM MQ (MQSeries)](https://es.wikipedia.org/wiki/IBM_MQ)  desde el core de v6.
Este componente respeta, por compatibilidad, la interfaz existente en el Componente MQ para PPL.

> Existen diferentes API de IBM MQ (MQSeries) para .NET. 
En este caso utilizamos [amqmdnet](https://www.ibm.com/docs/en/ibm-mq/9.0?topic=applications-developing-net) v9.0.0.3 que tiene la interfaz mas parecida al Componente MQ en PPL pre-existente.
Esta librería se puede [descargar](https://www.ibm.com/support/pages/downloading-ibm-mq-900-older-fix-packs#fp9003) desde la página oficial de IBM. 
{.is-info}

> Se hizo Upgrade a la versión v9.2.2.0. 
La librería [amqmdnetstd](https://www.ibm.com/docs/en/ibm-mq/9.2?topic=applications-developing-net) se puede [descargar](https://www.ibm.com/docs/en/ibm-mq/9.2?topic=net-installing-mq-classes-standard) desde la página oficial de IBM. 
También esta disponible para [descargar](https://www.ibm.com/docs/en/ibm-mq/9.2?topic=imcns-downloading-mq-classes-net-standard-from-nuget-repository) desde el repositorio de NUGET   {.is-success}

> Cabe mencionar que en el Servicio [FPA.IME](/ime/inicio) desarrollado para Galicia se utilizó otra API: [IBM.XMS](https://www.ibm.com/docs/es/ibm-mq/9.0?topic=ssfksj-9-0-0-com-ibm-mq-xms-doc-xms-cgetstd-intronet-htm) {.is-info}

### Funciones 
Las siguientes funciones se encuentran agrupadas dentro del componente MQS.

#### MQConectar
Crea una conexión con el gestor de colas (Queue Manager). 
```
MQS.MQConectar(string queueMng)
MQS.MQConectar(string queueMng, string host, string port, string channel, string usr, string password)
```
|#|Param.|Descripción|
|---|---|---|
|1|queueMng (string)| Nombre del Queue Manager. Obligatorio. |
|2|host (string)| Host. Propiedad para conexión al Queue Manager. |
|3|port (string)| Puerto. Propiedad para conexión al Queue Manager. |
|4|channel (string)| Canal. Propiedad para conexión al Queue Manager. |
|5|usr (string)| Usuario. Propiedad para conexión al Queue Manager. |
|6|password (string)| Password. Propiedad para conexión al Queue Manager. |
```
MQS.MQConectar("QM_PPL","10.15.3.232", "1413", "PPL.CHANNEL", "mercados", "UsrMerca*123")
ACN(e1, MQS.MQUltNroError())
ACT(e2, MQS.MQUltMensajeError())
if Val(e1) > 0
  MESSAGEBOX("ERROR al Conectar. <"~Val(e1)~" : "~Val(e2)~"> ")
else
  MESSAGEBOX('CONECTO OK!!')
endif
MQS.MQDesconectar()
```

Los parámetros de conexión podrán definirse en el **config.json**
```json
        "mq_host": "10.15.3.232",
        "mq_port": "1413",
        "mq_channel": "PPL.CHANNEL",
```
En cuanto a las credenciales (usuario y password) podrán definirse en un archivo encriptado, previamente generado con la aplicación [**FPA Credentials**](http://wiki.fpasoft.com.ar/es/instalacion/fpa-credentials).
El archivo deberá existir en el directorio de instalación con el nombre **mq.cred** y deberá estar encriptado con el cifrado *RSA*.

```
MQS.MQConectar("QM_PPL")

```

#### MQDesconectar
Cierra la conexión con el gestor de colas (Queue Manager). 
```
MQS.MQDesconectar()
```

#### MQAbrir
Accede a una cola (Queue) del gestor de colas (Queue Manager) inicializado, en modo lectura o escritura.
```
MQS.MQAbrir(string queue, int modo)
```
|#|Param.|Descripción|
|---|---|---|
|1|queue (string)| Nombre de la cola (Queue). Obligatorio. |
|2|modo (int)| 1:input(lectura) - else output(escritura). Obligatorio. |

#### MQCerrar
Cierra la conexión con la cola (Queue).
```
MQS.MQCerrar()
```

#### MQLeer
Obtiene un mensaje de la cola (Queue).
El mensaje queda almacenado en el Buffer.
```
MQS.MQLeer()
MQS.MQLeer(bool transaction = false)
MQS.MQLeer(bool transaction = false, string msgID = "", string correlID = "")
```
|#|Param.|Descripción|
|---|---|---|
|1|transaction (bool)| Realiza la acción de manera transaccional. La Recepción del mensaje debe confirmarse ejecutando el Commit o Rollback. Default false. Setea en las opciones del mensaje MQGMO_SYNCPOINT|
|2|msgID (string)| Permite buscar un mensaje específico. Establece la propiedad del mensaje [MsgId](https://www.ibm.com/docs/es/ibm-mq/9.1?topic=mqmd-msgid-mqbyte24). Parámetro Opcional. |
|3|correlID (string)| Permite buscar un mensaje especifico. Establece la propiedad del mensaje [CorrelId](https://www.ibm.com/docs/es/ibm-mq/9.1?topic=mqmd-correlid-mqbyte24). Parámetro Opcional. |

#### MQLeerGrupo
Obtiene un mensaje de la cola (Queue).
El mensaje queda almacenado en el Buffer.
Setea en el mensaje propiedades de agrupación (MQGMO_LOGICAL_ORDER - MQGMO_VERSION_2).
```
MQS.MQLeerGrupo()
MQS.MQLeerGrupo(bool transaction = false)
MQS.MQLeerGrupo(bool transaction = false, string msgID = "", string correlID = "", string groupID = "")
```
|#|Param.|Descripción|
|---|---|---|
|1|transaction (bool)| Idem MQLeer |
|2|msgID (string)| Idem MQLeer |
|3|correlID (string)| Idem MQLeer |
|4|groupID (string)| Establece la propiedad del mensaje [GroupId](https://www.ibm.com/docs/en/ibm-mq/9.1?topic=mqmd-groupid-mqbyte24). Parámetro Opcional.  |

#### MQEscribir 	
Escribe el mensaje almacenado en el Buffer en la cola (Queue).
```
MQS.MQEscribir()
MQS.MQEscribir(string replyToQ = "", string replyToQMgr = "", string applOriginData = "")
MQS.MQEscribir(string replyToQ = "", string replyToQMgr = "", string applOriginData = "", string msgID = "", string correlID = "", bool transaction = false)
```
|#|Param.|Descripción|
|---|---|---|
|1|replyToQ (string)| Establece la propiedad del mensaje [ReplyToQ](https://www.ibm.com/docs/en/ibm-mq/9.1?topic=mqmd-replytoq-mqchar48). Parámetro Opcional. |
|2|replyToQMgr  (string)| Establece la propiedad del mensaje [ReplyToQMgr](https://www.ibm.com/docs/en/ibm-mq/9.1?topic=mqmd-replytoqmgr-mqchar48). Parámetro Opcional. |
|3|applOriginData  (string)| Establece la propiedad del mensaje [ApplOriginData](https://www.ibm.com/docs/en/ibm-mq/9.1?topic=mqmd-applorigindata-mqchar4). Parámetro Opcional. |
|4|msgID (string)| Establece la propiedad del mensaje [MsgId](https://www.ibm.com/docs/es/ibm-mq/9.1?topic=mqmd-msgid-mqbyte24). Parámetro Opcional. |
|5|correlID (string)| Establece la propiedad del mensaje [CorrelId](https://www.ibm.com/docs/es/ibm-mq/9.1?topic=mqmd-correlid-mqbyte24). Parámetro Opcional. |
|6|transaction (bool)| Realiza la acción de manera transaccional. La Escritura del mensaje debe confirmarse ejecutando el Commit o Rollback. Default false. Setea en las opciones del mensaje MQGMO_SYNCPOINT|

#### MQEscribirGrupo
Escribe el mensaje almacenado en el Buffer en la cola (Queue).
Setea en el mensaje propiedades de agrupación (MQGMO_LOGICAL_ORDER - MQGMO_VERSION_2).
```
MQS.MQEscribirGrupo()
MQS.MQEscribirGrupo(string replyToQ = "", string replyToQMgr = "", string applOriginData = "")
MQS.MQEscribirGrupo(string replyToQ = "", string replyToQMgr = "", string applOriginData = "", string msgID = "", string correlID = "")
MQS.MQEscribirGrupo(string replyToQ = "", string replyToQMgr = "", string applOriginData = "", string msgID = "", string correlID = "", string groupID = "", int msgSeq = 0, int msgFlags = 0, bool transaction = false)
```
|#|Param.|Descripción|
|---|---|---|
|1|replyToQ (string)| Idem MQEscribir |
|2|replyToQMgr  (string)| Idem MQEscribir |
|3|applOriginData  (string)| Idem MQEscribir |
|4|msgID (string)| Idem MQEscribir |
|5|correlID (string)| Idem MQEscribir |
|6|groupID (string)| Establece la propiedad del mensaje [GroupId](https://www.ibm.com/docs/es/ibm-mq/9.1?topic=mqmd-groupid-mqbyte24). Parámetro Opcional. |
|7|msgSeq (string)| Establece la propiedad del mensaje [MsgSeqNumber](https://www.ibm.com/docs/es/ibm-mq/9.1?topic=mqmd-msgseqnumber-mqlong). Parámetro Opcional. |
|8|msgFlags (string)| Establece la propiedad del mensaje [MsgFlags](https://www.ibm.com/docs/es/ibm-mq/9.1?topic=mqmd-msgflags-mqlong). Parámetro Opcional. |
|9|transaction (bool)| Realiza la acción de manera transaccional. La Escritura del mensaje debe confirmarse ejecutando el Commit o Rollback. Default false. Setea en las opciones del mensaje MQGMO_SYNCPOINT|

#### MQLongBuffer
Establece la longitud del buffer que se usa en las Escrituras / Lecturas.
Se utiliza en *MQEscribirCampo* y *MQLeerCampo*, solo en el caso de que no se especifique el parámetro *longitud*.
```
MQS.MQLongBuffer(int longBuffer)
```
|#|Param.|Descripción|
|---|---|---|
|1|longBuffer (int)| Longitud.|

#### MQObtenerLongBuffer
Recupera la longitud del buffer que se usa en las Escrituras.
```
MQS.MQObtenerLongBuffer()
```

#### MQTimeOut
Setea la propiedad de timeout en segundos (Tiempo máximo de espera de mensajes). Default 15 segundos.
```
MQS.MQTimeOut(int seconds)
```
|#|Param.|Descripción|
|---|---|---|
|1|seconds (int)| Tiempo máximo de espera de mensajes.|

#### MQCommit 	
Confirma la transacción de lectura o escritura
Los mensajes escritos dentro de la transacción están disponibles para otras aplicaciones. 
Los mensajes leídos en la trasacción se eliminan de la cola (Queue). 
```
MQS.MQCommit()
```

#### MQRollBack
Recupera los mensajes que se leyeron o escribieron dentro de la transacción.
Los mensajes escritos dentro de la transacción no se agregan a la cola (Queue). 
Los mensajes leídos en la trasacción se restablecen en la cola (Queue).
```               
MQS.MQRollBack()
```

#### MQExportaAltamira 	
Método no implementado. No está disponible el componente Altamira.

#### MQUltNroError
Devuelve un número con el último código de error de la función llamada con anterioridad. (0:OK)
```
MQS.MQUltNroError()
```

#### MQUltMensajeError
Devuelve el último mensaje de error de la función llamada con anterioridad. 
```
MQS.MQUltMensajeError()
```

#### MQEscribirCampo
Escribe en el buffer el valor pasado como parámetro, procesándolo según el tipo.
```
MQS.MQEscribirCampo(string valor)
MQS.MQEscribirCampo(string valor, int longitud = 0, int tipo = 0)
```
|#|Param.|Descripción|
|---|---|---|
|1|valor (string)| Valor a escribir en el buffer.|
|2|longitud (int)| Longitud del valor a grabar en el buffer. Se usa solo si tipo = 0.|
|3|tipo (int)| Formato con el cual se graba el valor. Valores posibles 0-1-2-3 (ver detalle).|

**Parámetro Tipo**
+ **0**: Rellena el valor hasta alcanzar la *longitud* con blancos o corta el valor si sobrepasa la *longitud*.
+ **1**: Empaqueta el valor. El valor original debe ser un número entero. 
Se toman de a 2 dígitos. Se representa cada uno en 4 bits. Se agrupan para completar los 8 bits y obtener el # del ascii. 
Ejemplo, sea el valor 21, se representa cada dígito en 4 bits 0010 0001, se agrupan y se obtiene ascii #33: '!'. Se usan 4 bits extras para representar el signo del valor.
+ **2**: Convierte el valor de Ascii a EBCDIC.
+ **3**: Convierte el valor de Ascii a Hex.

#### MQLeerCampo
Lee del buffer el valor, procesándolo según el tipo.
```
MQS.MQLeerCampo()
MQS.MQLeerCampo(int posicion = 0, int longitud = 0, int tipo = 0)
```
|#|Param.|Descripción|
|---|---|---|
|1|posicion (int)| Posición inicial del valor a devolver. Se usa solo si tipo = 0..|
|2|longitud (int)| Longitud del valor a devolver. Se usa solo si tipo = 0.|
|3|tipo (int)| Formato con el cual se lee el valor. Valores posibles 0-1-2-3 (ver detalle).|

**Parámetro Tipo**
+ **0**: Rellena el valor hasta alcanzar la *longitud* con blancos o corta el valor si sobrepasa la *longitud*. Iniciando en *posicion*.
+ **1**: Desempaqueta el valor devolviendo el número entero original. 
+ **2**: Convierte el valor de EBCDIC a Ascii.
+ **3**: Convierte el valor de Hex a Ascii.

#### MQLimpiarCampo
Blanquea el valor del buffer y la longitud asignada con *MQLongBuffer*.
```
MQS.MQLimpiarCampo()
```

### Ejemplos 
#### Caso 1
**Escribe el mensaje 'FPA' en la cola.**
```
**  Codigo a modo de ejemplo
**  Para una mejor comprension se evitan las validaciones de cada 
**  metodo que deberian existir en un codigo productivo

 MQS.MQConectar("QM_PPL","10.15.3.232", "1413", "PPL.CHANNEL", "mercados", "UsrMerca*123")
 MQS.MQAbrir("PPL.QUEUE",0)
 MQS.MQLongBuffer(3)
 MQS.MQEscribirCampo('FPA', 3, 0)
 MQS.MQEscribir()
 MQS.MQCerrar()
 MQS.MQDesconectar()
```

#### Caso 2
**Lee el mensaje de la cola y lo muestra.**
```
**  Codigo a modo de ejemplo
**  Para una mejor comprension se evitan las validaciones de cada 
**  metodo que deberian existir en un codigo productivo

MQS.MQConectar("QM_PPL","10.15.3.232", "1413", "PPL.CHANNEL", "mercados", "UsrMerca*123")
MQS.MQAbrir("PPL.QUEUE",1)
MQS.MQLongBuffer(3)
MQS.MQTimeOut(3)
MQS.MQLeer()
messagebox(MQS.LeerCampo(0, 3, 0))
MQS.MQCerrar()
MQS.MQDesconectar()
```
