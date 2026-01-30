### Introduccion
A continuacion se describen las principales caracteristicas de lo que podria
llegar a ser una integracion entre PPL.NET y FPA Portfolio 5.0.  
Practicamente todos los puntos detallados a continuacion pueden ser
adaptadados para ajustarse a las necesidades/preferencias del cliente.  

  
\***nota:** Se asumen conocimientos sobre [PPL.NET](Intro-PPL.NET) y [PPL Studio](Intro-PPL-Studio).

###	Como se integra PPL.NET con FPA Portfolio 5.0?
El engine de PPL.NET puede ser hosteado en cualquier proceso que corra sobre
.NET Framework (4.0 o superior). Dentro de este grupo de procesos, podemos
incluir: Aplicaciones WinForms, Servicios Windows, Servicios Web, entre otros...
Esta caracteristica permite que sea posible integrar PPL.NET con practicamente
cualquier aplicaicon .NET, incluyendo, FPA Portfolio 5.0.

A continuacion se puede ver un posible diagrama de despliegue para esta 
integracion:

![Imagen deploy v5 pplnet](/core/img/deploy_v5_ppl_net.png)

### Como afectan las dependencias de FPA Portfolio 5.0 a PPL.NET?
Dado que PPL.NET es autocontenido y corre en el AppDomain de 
Portfolio 5.0, no tenemos ningun inconveniente con las dependencias 
de esta aplicacion (Como ser ATDirector, ContextDelivery, entre otras....).
Al momento en el que PPL.NET entra en accion, todas las dependencias
ya fueron resueltas por Portfolio 5.0 y pueden ser utilizadas por PPL.NET
de forma transparente.

### PPL Studio
Si bien es cierto que para ejecutar scripts PPL solo necesitamos hostear el 
engine y el runtime de PPL.NET en algun proceso .NET, para poder desarrollar 
estos scripts es recomendable contar con la herramienta de desarrollo 
PPL Studio.
Como se puede ver en el diagrama de despliegue, esta herramienta se instala 
en lo que llamamos **Dev Client**.  
Es importante tener en cuenta que este cliente de desarrollo puede ser 
instalado a la par de FPA Portfolio 5.0 y convivir con el aplicativo 
sin ningún problema. (En el diagrama de despliegue se utilizan dos 
equipos diferentes unicamente a modo ilustrativo).


### Donde se instalan los scripts PPL?
Los scripts PPL se publican en la base de datos utilizando el asistente de
publicacion que forma parte de la herramienta PPL Studio.  
Se asume que el esquema de la base de datos cuenta con las siguientes tablas:
* ABMS
* EVENTOS
* INFORMES
* FORMULAS
* FUNCIONES
* TIPOSORDEN
* TIPOSOPERACION
* TIPOSMINUTABOLSA
* TIPOSTRANSACCION2

![Imagen integracion scripts v5 pplnet](/core/img/inte_gal_pub_scripts.png)

### Como funciona la ejecucion de scripts?
Los scripts son recuperados desde la base de datos, compilados y ejecutados
por los distintos modulos que conforman PPL.NET. En este caso la tarea de
Portfolio 5.0 se limita a informarle al engine de PPL.NET el tipo (
ABM, Informe, etc...) y el codigo del objeto que quiere ejecutar el usuario. De
ahi en mas, todas las acciones quedan en manos de PPL.NET.  
Por supuesto que de cara al usuario, este mecanismo en transparente.

![Imagen integracion ejecucion scripts v5 pplnet](/core/img/inte_gal_exec_script.png)

### Es necesario instalar componentes adicionales?
No. Para utilizar PPL.NET no es necesario instalar componentes adicionales.
Todas las dependencias se instalan junto con el runtime.


### Hay diferencias entre las dos versiones a nivel de look & feel?
Si. Si bien desde el punto de vista de la experiencia de usuario las dos 
versiones son practicamente identicas, hay algunas diferencias en la estetica
de los componentes. (Estas diferencias son menores, pero se notan).


### Hay cambios a nivel de autorizacion/autenticacion de usuarios?
No. En este sentido la integracion es completamente transparente.

### La aplicacion cuenta con algun mecanismo para versionar scripts PPL?
Si. Utilizando PPL Studio es posible versionar los scripts PPL por medio
de una integracion con GIT.  
Si se activan esta caracteristica, deben instalar GIT en la PC donde
vayan a utilizar PPL Studio.


