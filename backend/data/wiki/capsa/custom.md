---
title: CAPSA - Custom
description: CAPSA - Funcionalidades Custom
published: true
date: 2022-04-28T19:34:11.053Z
tags: capsa, sql2, exec3, dbconfig
editor: markdown
dateCreated: 2022-04-05T21:15:45.157Z
---

# Archivo *dbconfig.json*
El archivo ***dbconfig.json*** permite configurar los datos de conexión a bases de datos secundarias, diferentes a la principal. Estas bases de datos se utilizan en otras funciones custom, como por ejemplo SQL2 y EXEC3.
El archivo ***dbconfig.json*** debe existir en el directorio de instalación de la aplicación, y tiene el siguiente formato:

```json
{
  "Environments": [
    {
      "ID": "bde",
      "ProviderName": "System.Data.SqlClient",
      "ConnectionString": "Server=FPA019;Database=STDC;"
    },
    {
      "ID": "orc",
      "ProviderName": "System.Data.OracleClient",
      "ConnectionString": "SERVER =(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST = 10.15.3.128)(PORT = 1521))(CONNECT_DATA =(SERVICE_NAME = oracle)));"
    }
  ]
}
```
Tener en cuenta que si el nombre del servidor tiene una contra barra ej: FPA017\FPA017, se debe poner doble contra barra quedando de esta manera el nombre del servidor: FPA017\\\FPA017



# SQL2
Ejecuta una consulta SQL apuntando a una base de datos, diferente a la principal, con usuario y password. 
Sirve para obtener un escalar, pero no para recorrer ni para obtener un set de datos.

|#|Param.|Descripcion|
|-|------|-----------|
|1|sentencia (string)| Consuta SQL a ejecutar |
|2|alias (string)| ID de la base de datos a utilizar. Debe existir en el archivo **dbconfig.json** |
|3|usuario (string)| Credenciales de conexión a la base de datos |
|4|password (string)| Credenciales de conexión a la base de datos |

```
    ACT(A:1,"SELECT COUNT(NrOperacion) FROM dbo.OPERACIONES WHERE TipoOp = 'TIC'")
    ACN(A:2,SQL2(VAL(A1),"BDE","FPA","FPA"))
    MESSAGEBOX(VAL(A2))
```

# EXEC3
Ejecuta una transacción SQL apuntando a una base de datos, diferente a la principal, con usuario y password. 
Sirve para para ejecutar comandos INSERT / DELETE / UPDATE.

|#|Param.|Descripcion|
|-|------|-----------|
|1|alias (string)| ID de la base de datos a utilizar. Debe existir en el archivo **dbconfig.json** |
|2|usuario (string)| Credenciales de conexión a la base de datos |
|3|password (string)| Credenciales de conexión a la base de datos |

```
SQL.ADD("UPDATE dbo.VARIABLES set Valor = '1' where Codigo = 'VAR001'")
SQL.NEW
SQL.ADD("UPDATE dbo.VARIABLES set Valor = '2' where Codigo = 'VAR002'")
SQL.NEW
SQL.EXEC3("BDE","FPA","FPA")
```
