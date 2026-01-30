---
title: Oracle de 64 bits: Pros y contras de los distintos clientes.
description: 
published: true
date: 2020-08-31T01:01:13.011Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:54:15.886Z
---

A continuación se detallan los distintos clientes de Oracle que probamos para ver si es posible compilar y distribuir la aplicación en 64 bits. En todos los casos incluimos una breve descripción con los pros y las contras de cada uno de ellos.

### ODP.NET (managed) 64 bits
Funciona correctamente, y según la gente de Oracle, la performance de este driver es mejor que la del driver que hace MSFT. En base a las pruebas realizadas (en nuestro caso) esto no es así. En promedio, son más o menos iguales. 
La contra de este componente es que tiene que ser instalado por un administrador, modifica el archivo de configuración global de aplicaciones .NET (“machine.config”), el GAC y el registro de la PC del usuario. (Y por lo que vi en los foros de Oracle, dependiendo del SO, también puede llegar a tener algunos issues).

### ODP.NET (managed) 64 bits XCopy
Al tratar de abrir la conexión arroja “Null Reference blah, blah, blah…”. Esto es un problema interno de la librería y por lo que cuentan en los foros de Oracle se da cuando en una PC tenemos instalados clientes de 32 y 64 bits.
Esta limitación hace que el uso de esta librería sea inviable, porque justamente la gracia de un cliente que se instala via xcopy, es que no hay que tocar la PC del usuario final. Para que esta variante funcione, el usuario tendría que desinstalar la versión de 32 bits. No tiene sentido.

### System.Data.OracleClient
Funciona correctamente si la PC tiene instalado el cliente nativo de 64 bits de Oracle. La contra de este driver es que esta “deprecado” por MSFT. Si de todas formas vamos a tener que instalar un cliente Oracle, creo que nos conviene utilizar el cliente que desarrolla y mantiene la gente Oracle.

_\*Nota: Hay una especie de mito acerca del driver de MSFT y es que muchos piensan que no require que la PC del usuario tenga instalado un cliente de Oracle. Tener en cuenta que esto **no es así**. Si o si, tiene que haber un cliente instalado o distribuido con bin de la app (si es que soporta deploy via xcopy)_.

### Devart Connector
Funciona de diez y se puede instalar via xcopy. En base a las pruebas realizadas, la única “contra” que tiene este driver es que es un componente pago. A simple vista no es caro, pero habría que estudiar bien el modelo de licencias, y obviamente, validar con el cliente si lo pueden instalar o no.

### Data Direct Connector
Tenemos buenas referencias (de las misma gente que recomienda Devart) pero no llegamos a probarlo... A simple vista, la principal contra de este componente es que en ningún lado se puede ver el precio o el modelo de licencias. Es muy probable que este alineado al modelo de licencias de Oracle, donde solo sabes el precio a la hora de comprar y suele ser carísimo. Por ahora, queda descartado.

### Conclusión
A menos que el cliente esté dispuesto a instalar alguno de los drivers de 64 bits (y probablemente, desinstalar el 32), la única opción viable es el conector de Devart, que en base a las pruebas realizadas, puede ser distribuido vía xcopy y puede convivir con versiones de 32 bits.
