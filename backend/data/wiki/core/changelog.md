---
title: Changelog
description: Detalle de cambios y versiones realizadas del core version 6
published: true
date: 2026-01-28T13:30:00.099Z
tags: 
editor: markdown
dateCreated: 2022-03-06T21:45:24.195Z
---

# 6.7.56.0 | 6.8.4.0
> Fecha: 28/1/2026| Compilacion: 6.7.56.0 | 6.8.4.0 | [Trello](https://trello.com/c/47QlP7Jl) {.is-info}

>  Las versiones 6.8.X mantendrán la versión con CEF nuevo, mientras que las 6.7.X mantendrán la versión con CEF viejo.
{.is-warning}


- En eventos e informes, el FullScript no desglosa fórmulas ni funciones con prefijo '@'  [#1900](https://trello.com/c/QrvqGFLp)

- Grilla no toma los filtros definidos en ABM [#2176](https://trello.com/c/fE8MTFeh)
# 6.7.55.0 | 6.8.3.0
> Fecha: 7/1/2026| Compilacion: 6.7.55.0 | 6.8.3.0 | [Trello](https://trello.com/c/c5S50gM5) {.is-info}

>  Las versiones 6.8.X mantendrán la versión con CEF nuevo, mientras que las 6.7.X mantendrán la versión con CEF viejo.
{.is-warning}


- Error de validacion  Fecha Tipo Cambio de Referencia! en FXC con v6.7.53 [#2184](https://trello.com/c/Z778ZzFz)

- Al avanzar operacion arroja error No se puede convertir el STR a Fecha [#2183](https://trello.com/c/FxAAGazb)
# 6.7.54.0 | 6.8.2.0
> Fecha: 30/12/2025 | Compilacion: 6.7.54.0 | 6.8.2.0 | [Trello](https://trello.com/c/pC5BTLkk/2179-instalador-682-6754) {.is-info}

>  Las versiones 6.8.X mantendrán la versión con CEF nuevo, mientras que las 6.7.X mantendrán la versión con CEF viejo.
{.is-warning}


- Agregar procedure SetearUsuarioFPA para auditoria con sigla GALICIA [#2166](https://trello.com/c/aifD7etY/)

- Nueva funcion GrabarGrilla2 [#2174](https://trello.com/c/U9rPvxG2/)

- Filtro de Últimos 30 días configurable en grilla operaciones [#2175](https://trello.com/c/U9FfEk3B/)

- Movimientos de Comisiones se generan con más de 2 decimales [#2156](https://trello.com/c/wwTbMHxN/)

- Error no encuentra funcion SND_MAIL [#2177](https://trello.com/c/xTIleuDn/)

# 6.7.53.0 | 6.8.1.0
> Fecha: 28/11/2025 | Compilacion: 6.7.53.0 | 6.8.1.0 | [Trello](https://trello.com/c/fY5FRgLr) {.is-info}

>  Las versiones 6.8.X mantendrán la versión con CEF nuevo, mientras que las 6.7.X mantendrán la versión con CEF viejo.
{.is-warning}


- Tipo de Documento en Msjs adjuntos de Operaciones [#2111](https://trello.com/c/75dw9llM)

- Actualización de librerías ICSharpCode y NewtonSoft [#2170](https://trello.com/c/xpDaX5BP)

# 6.7.52.1
> Fecha: 11/11/2025 | Compilacion: 6.7.52.1 | [Trello](https://trello.com/c/gpuCVFI0) {.is-info}

- Restablecimiento de versión CEF a versión 79 [#2164](https://trello.com/c/teUrA0AO)

# 6.7.51
> Fecha: 30/10/2025 | Compilacion: 6.7.51.0 | [Trello](https://trello.com/c/D41tyjpE) {.is-info}

- Se genera cuota cuando se edita una operación desde grilla [#2134](https://trello.com/c/vj2J0Ocl)
- Error con ItemLista [#2138](https://trello.com/c/fO4sEuzc)
- Cotizacion y CotizacionC para historicos. [#2140](https://trello.com/c/tRCqZbtM)
- No toma variable INTENTOS para limitar logines fallidos [#2145](https://trello.com/c/I0Cf4k9Q)
- La cantidad de intentos fallidos no audita con el usuario de conexion [#2146](https://trello.com/c/HpKLZ3ZL)
- EjecutarEvento2 no responde y queda colgado en CMF Produccion [#2152](https://trello.com/c/ZLIpgSwb)
- Sección CUOTAS/COMISIONES no se graban al modificar en una Instancia especifica [#2155](https://trello.com/c/8sPZ1j4y)
- Al editar un campo de la Operacion MMCAUP se esta borrando el recalculo de Cuotas [#2160](https://trello.com/c/d74xJfZb)


# 6.7.50.2
> Fecha: 22/10/2025 | Compilacion: 6.7.50.2 | [Trello](https://trello.com/c/gNcmklW3) {.is-info}

> Se agregó una nueva solución al problema de los reportes en blanco que no quedó 100% solucionado con la versión 6.7.50.1

- Error reporte en blanco [#2149](https://trello.com/c/ulVVnp1x)

# 6.7.50.1 
> Fecha: 30/09/2025 | Compilacion: 6.7.50.1 | [Trello](https://trello.com/c/qmfsCJ8c) {.is-info}

- Error reporte en blanco [#2149](https://trello.com/c/ulVVnp1x)

# 6.7.50
> Fecha: 05/09/2025 | Compilacion: 6.7.50.0 | [Trello](https://trello.com/c/lNY5QzHs) {.is-info}

- No deshabilita usuario ni pone CantIntentos > 0 al entrar con mal password. [#2124](https://trello.com/c/eg20C4vZ)
- Error en consola con formato fechas para Oracle [#2117](https://trello.com/c/FF9aINe6)
- Error desde consola con formato de fecha al sumar X dias. [#2118](https://trello.com/c/X6nDaxXq)
- Poder deshabilitar Mensajes desde config [#2131](https://trello.com/c/l5Q7Mx86)
- Informes salen en blanco usando MultiSession [#2139](https://trello.com/c/OqOwAcVj)
- Instancia no habilita un campo para un Usuario [#2136](https://trello.com/c/jtHaugfM)

# 6.7.49
> Fecha: 08/08/2025 | Compilacion: 6.7.49.0 | [Trello](https://trello.com/c/SGRURtnf) {.is-info}

- Crear sección SALDOSREM [#2135](https://trello.com/c/saKQcKKC)
- Campo Combo en Operacion no recalcula [#2121](https://trello.com/c/v79jEWRv)
- ABM pone mal nombre de la columna [#2128](https://trello.com/c/PlH6yOT8)
- Portfolio se cierra al ejecutar informe con 2 sesiones abiertas con mismo usuario [#2125](https://trello.com/c/P6YmnOPP)
- Incluír posibilidad de extender longitud visual a campos de tipo "Archivo" [#2133](https://trello.com/c/StlvSuMx)

# 6.7.48
> Fecha: 21/07/2025 | Compilacion: 6.7.48.0 | [Trello](https://trello.com/c/WB9ScAkg) {.is-info}

- No permite avanzar cuando la operación está en instancias paralelas [#2127](https://trello.com/c/CbfaHbON)

# 6.7.47
> Fecha: 30/06/2025 | Compilacion: 6.7.47.0 | [Trello](https://trello.com/c/Bq1eRTJp) {.is-info}

- Error al hacer doble click en grilla [ORACLE] [2116](https://trello.com/c/E4l5TBmq)

# 6.7.46.1 [Actualización de CEF]
> Fecha: 12/06/2025 | Compilacion: 6.7.46.1 | [Trello](https://trello.com/c/zh3xGDLv) {.is-info}

- Actualización de componente CEF a versión 126.2.70.0, versión x86
- Se pierden linea de menues al generar informe. [2060](https://trello.com/c/w7RRKNcQ)

# 6.7.46
> Fecha: 10/06/2025 | Compilacion: 6.7.46.0 | [Trello](https://trello.com/c/AzfU19Ey) {.is-info}

- STDCORP fallo en el Cierre y Apertura Portfolio 6.7.35 en adelante [#2109](https://trello.com/c/gFfctLxf)
- Error SQL en carga y avance de operacion [#2110](https://trello.com/c/CrIgHO9F)

# 6.7.45
> Fecha: 30/05/2025 | Compilacion: 6.7.45.0 | [Trello](https://trello.com/c/gOAhoNu9) {.is-info}

- No permite escribir letras en solapa CUOTAS/COMISIONES de operaciones [#2047](https://trello.com/c/rHnChuBx)
- Revisar __PPLRC al importar un objeto en PPL Studio [#2064](https://trello.com/c/nL97Bj6d)
- Llamada al evento INVIMV desde una operación MMPCCM da error con versión 6.7.43 [#2090](https://trello.com/c/55hqDd44)
- Para sigla XXX no usar HASP [#2089](https://trello.com/c/CZjC9mJu)
- Oracle lanza error por no poder obtener una conexión disponible [#2097](https://trello.com/c/8WN6DVx5)
- Error en version 6.7.44 valor null en Listbox [#2100](https://trello.com/c/fmnnLBv2)
- Validar simultaneidad en instancias de operaciones y tranzacciones [#2095](https://trello.com/c/mfLTOVwS)

# 6.7.44
> Fecha: 15/04/2025 | Compilacion: 6.7.44.0 | [Trello](https://trello.com/c/9cv2blfT) {.is-info}

- NO se actualiza grilla con boton actualizar [#2087](https://trello.com/c/8iedwvq5)
- Funcion SCN con inclusion de num() da error [#2088](https://trello.com/c/jueWPxj9)
- No se recalculan campos en alta de OPERACION. [#2091](https://trello.com/c/M3ASsAvb)

# 6.7.43
> Fecha: 21/03/2025 | Compilacion: 6.7.43.0 | [Trello](https://trello.com/c/EfBydWcn) {.is-info}

- Actualizar librería iTextSharp por advertencia de seguridad [#2081](https://trello.com/c/qeKe0RYX)
- Función Num() no detecta decimales cuando el número pasado por parámetro usa separador de decimales ". (punto)" [#2085](https://trello.com/c/BvnnTRS3)
- Campo UsuarioEje no loguea el usuario en MovEjecutados automáticos [#2084](https://trello.com/c/yMP6Kp7S)
- Al "Ver" una operación e intentar mover de instancia, no se valida que la instancia de la misma no se haya modificado. [#2083](https://trello.com/c/PjYowQty)
- Error al editar campos en operaciones [#2075](https://trello.com/c/WfOSgMEh)
- Grillas de Instancias no están funcionando los filtros default [#2068](https://trello.com/c/htT28JIa)
- ListBox no setea celdas con datos iniciales [#2067](https://trello.com/c/FNOq664M)
- Problema con seccion BeforeShowDialog en modo VIEW [#2080](https://trello.com/c/PyvwIOXV)

# 6.7.42
> Fecha: 27/02/2025 | Compilacion: 6.7.42.0 | [Trello](https://trello.com/c/fx5iWous) {.is-info}

- Cuadro de Movimientos Automáticos se sigue mostrando al cambiar de fecha aunque no haya datos en la tabla [#1811](https://trello.com/c/cGU1uP72)
- PPL Studio arroja error por no cerrar día / fecha distinta a hoy [#2070](https://trello.com/c/K6YK4Jkv)
- Valor de listas en consulta no se visualizan - Variable INSTANCIA [#2073](https://trello.com/c/ml3L19BQ)
- Valor default Fechas [#2074](https://trello.com/c/6ttaHpPV)

# 6.7.41
> Fecha: 03/02/2025 | Compilacion: 6.7.41.0 | [Trello](https://trello.com/c/75Om5Ayu) {.is-info}

- Anulacion Manual GAOTI - Seccion Baja [#2056](https://trello.com/c/GmT6QnWi)
- Verificar en función ACLxx que exista el objeto a mostrar [#2054](https://trello.com/c/2hYiYAr0)
- Recálculos de campos numéricos que no sufrieron actualizaciones [#2059](https://trello.com/c/XoDaQAGx)
- Recalculo de Cuotas1 no lo toma en seccion Lista [#2061](https://trello.com/c/ViFwyYI8)
- Modificar tamaño visible de un texto en evento [#2051](https://trello.com/c/wZVROD9T)

# 6.7.40
> Fecha: 10/01/2025 | Compilacion: 6.7.40.0 | [Trello](https://trello.com/c/2MgqoGOS) {.is-info}

- Usar Certificado para firmar Binarios. [#2036](https://trello.com/c/AswaicQP)
- Labels no se muestran correctamente en Alta ni en Modificación de operaciones [#2053](https://trello.com/c/wkj0hfQX)
- Validación en grillas si operación esta en la instancia previo a realizar cualquier acción [#2050](https://trello.com/c/tmrH50jv)
- Llave HASP, durante refresco "heartbit" si no encuentra servicio apaga al cliente V6 [#1781](https://trello.com/c/o8HOHJt8)
- Servicio HASP. Cierra aplicacion por heartbit [#1978](https://trello.com/c/F5kCim7v)

# 6.7.39
> Fecha: 19/12/2024 | Compilacion: 6.7.39.0 | [Trello](https://trello.com/c/xQi1VLd1) {.is-info}

- TipoOp FXC - Diferencia entre los recalculos de v3 y v6 [#2032](https://trello.com/c/VEZ1sRh7)
- Funcion ExportarXLS() parametro Merge en false deja basura. [#2045](https://trello.com/c/MqOxdNK0)
- Función ValorColumna no toma por fecha mas próxima [#2048](https://trello.com/c/jjG4XAx1)
- Funcion SaldoD2 anda distinto, no toma un parametro [#2035](https://trello.com/c/XxwuQEoQ)

# 6.7.38
> Fecha: 12/12/2024 | Compilacion: 6.7.38.0 | [Trello](https://trello.com/c/2c12nmsf) {.is-info}

- Longitud en campo Directorio [#1840](https://trello.com/c/NAPXOwzM)
- Excepcion de null reference en DropDownList al capturar grafico [#2037](https://trello.com/c/b6g8q3zp)
- Limitar longitud de campos de caracteres por BD cuando no tengan una longitud especificada [#2039](https://trello.com/c/LKNFYJ9s)
- SIGLA XXX - Desactivar llave HASP + AD [#2034](https://trello.com/c/8TRfyzE9)
- Mensaje incorrecto ante fallo en la carga de perfiles [#2044](https://trello.com/c/XpRF9Uqj)
- Al Agregar Operacion con OK# mostrar que se agrego algo. [#2040](https://trello.com/c/x2623p5S)
- Funcion 'VerificaAcceso' para V6 [#2042](https://trello.com/c/jdPunadj)
- Agregar permiso especial "Cargar Ops.Fecha valor mayor a 5 dias" para BNP [#2043](https://trello.com/c/NCAoSxbi)

# 6.7.37
> Fecha: 28/11/2024 | Compilacion: 6.7.37.0 | [Trello](https://trello.com/c/EtreUED3) {.is-info}

- Limitar inputs a cantidad máxima de caracteres según BD [#2033](https://trello.com/c/YUqWDvl1)
- Error en batch SQL en carga de operacion, no limpia lista de SQLs [#2027](https://trello.com/c/LxVDk5a5)
- Proceso apertura del Dia no actualiza bien los Movimientos [#2025](https://trello.com/c/TMjE4qwm)
- Campo tipo LOOKUP, agrego espacio adelante y no valida al campo. [#2026](https://trello.com/c/xmdNccQq)
- PPL Studio arroja error por no cerrar día [#2028](https://trello.com/c/VoTTw2Ew)

# 6.7.36
> Fecha: 20/11/2024 | Compilacion: 6.7.36.0 | [Trello](https://trello.com/c/hUMTd8fA) {.is-info}

- Avanzar Operacion en Version 36 da Error de SQL [#2024](https://trello.com/c/P9bRZmLx)
- En la grilla de Operaciones al minimizar se solapan los filtros con los iconos. [#1965](https://trello.com/c/TpO4L5iv)
- Error al usar format en un campo de PPLRC  [#2002](https://trello.com/c/ZtXE81Um)
- TECO - Cambio Esquema de seguridad - Parametro adicional Dominio en el config [#1984](https://trello.com/c/hk1lmygn)
- BNP reporta que se solapa componente de filtro en ventana con otros botones. [#2016](https://trello.com/c/jkY1IpEc)
- Error con EjecutarEvento2() pipe is busy [#2017](https://trello.com/c/r4pDYa88)
- Sección BAJA no reconoce valores de campos de diálogos [#2021](https://trello.com/c/9fHQooSx)
- Seccion CAMPOS dentro de una instancia <> 0  no abre dialogo. [#2019](https://trello.com/c/IkizL1vL)
- Error al compilar emitircartavisible [#2022](https://trello.com/c/9VHyRJf2)

# 6.7.35.1
> Fecha: 24/10/2024 | Compilacion: 6.7.35.1 | [Trello](https://trello.com/c/dvzWwzqZ) {.is-info}

- Error al ejecutarEvento2 sin parámetros [#2014](https://trello.com/c/QXAvFsHH)

# 6.7.35
> Fecha: 24/10/2024 | Compilacion: 6.7.35.0 | [Trello](https://trello.com/c/W7vorOUU) {.is-info}

- Error en EjecutarEvento2: “Access to the path is denied” [#2012](https://trello.com/c/wYpxatOm)

# 6.7.34.2 [DERIVA DE 6.7.32]
> Fecha: 18/10/2024 | Compilacion: 6.7.34.2 | [Trello](https://trello.com/c/MvcwHLVo) {.is-info}

> En esta versión se incluyen los siguientes issues que pertenecían a la versión 6.7.34.0. 
En la posterior (6.7.35.0), se terminan de incluír todos los issues de la versión 6.7.34.0, quedando incorporados en la 6.7.35.0 todos los issues resueltos a excepción de la actualización de CEF de la 6.7.33.0
{.is-warning}


- IIF resuelve distinto a IF [#1997](https://trello.com/c/CocEnPKj)
- EjecutarEvento4 - Subprocesos PPL [#1996](https://trello.com/c/brNRAQDl)
- Cuadro de Mensajes individual por proceso. [#1994](https://trello.com/c/jl3wBwJD)
- BNP - Credenciales encriptadas para PM Console [#1993](https://trello.com/c/jfxhTSCV)

# 6.7.34.1
> Fecha: 16/10/2024 | Compilacion: 6.7.34.1 | [Trello](https://trello.com/c/MkRQCaEc) {.is-info}

- Version 6.7.33 / 6.7.34: No escala automáticamente el DPI de la pantalla [#2008](https://trello.com/c/EsKohcf3)

# 6.7.34
> Fecha: 03/10/2024 | Compilacion: 6.7.34.0 | [Trello](https://trello.com/c/z9LufTN3) {.is-info}

- No reconoce siempre el día abierto desde PPLStudio [#2001](https://trello.com/c/NJNECvTt)
- Función $.SetWhere [ABMs] no funciona para algunos tipos de campo cuando debería [#2000](https://trello.com/c/bgilgfow)
- IIF resuelve distinto a IF [#1997](https://trello.com/c/CocEnPKj)
- EjecutarEvento4 - Subprocesos PPL [#1996](https://trello.com/c/brNRAQDl)
- Permitir serializar y deserealizar JSON [#1995](https://trello.com/c/uVhBseKO)
- Cuadro de Mensajes individual por proceso. [#1994](https://trello.com/c/jl3wBwJD)
- BNP - Credenciales encriptadas para PM Console [#1993](https://trello.com/c/jfxhTSCV)
- Incorporar sintaxis de diccionarios y listas [#1988](https://trello.com/c/al30PuUL)
- Memory Leak para clientes Oracle [#1983](https://trello.com/c/Nnx07Obi)
- Error en adjuntos de mensajes con bases Oracle [#1982](https://trello.com/c/PlIgjcvb)

# 6.7.33.1
> Fecha: 02/06/2025 | Compilacion: 6.7.33.1 | [Trello](https://trello.com/c/kiSNOjK5) {.is-info}

- Inclusión de sigla CMF en versión 33 [#2107](https://trello.com/c/nkHJprae)

# 6.7.33 [CEF]
> Fecha: 23/08/2024 | Compilacion: 6.7.33.0 | [Trello](https://trello.com/c/MpeGTw1C) {.is-info}

> En esta versión **surge** un error que hace que no se escale automáticamente el DPI de la pantalla en la que se corre el programa (corregido en 6.7.34.1).
{.is-danger}
- Upgrade CefSharp 126 [#1874](https://trello.com/c/INmd78fK)

# 6.7.32
> Fecha: 08/08/2024 | Compilacion: 6.7.32.0 | [Trello](https://trello.com/c/u6jq5v77) {.is-info}

- Logs de USUARIOSACTIVOS parametrizable [#1977](https://trello.com/c/3Ooq3c7C)
- NO toma los valores de campo de un creardialogo para el recalculo. [#1976](https://trello.com/c/nxVcnkEZ)
- Error con Fstr desde V 6.7.30 [#1972](https://trello.com/c/3YStSQSs)
- Transaccion2 con Campo RB3 con valor string da error [#1970](https://trello.com/c/DlNVFsM7)
- Redondeo en Numeros asignados a celda Numerica [#1905](https://trello.com/c/YwIYKGuX)

# 6.7.31
> Fecha: 03/07/2024 | Compilacion: 6.7.31.0 | [Trello](https://trello.com/c/EPsPLa3h) {.is-info}

- Funcion para conocer cantidad de Recorrer SQL pendientes [#1968](https://trello.com/c/Gg35nQ8k)
- Duplica Select dando error de sintaxis - funciona desde 6.7.20 hasta 6.7.29.1 [#1962](https://trello.com/c/It12He0D)
- Error indefinido en Operacion, Transaccion2 cuando RBx tiene string no numerica, Da error tambien en AtualizarMovimientosT [#1959](https://trello.com/c/6vXOxqYr)
- Archivos Ascii. Incorporar distintas codificaciones [#1955](https://trello.com/c/pHzrCyOo)
- Valor default de campos fecha vacios [#1951](https://trello.com/c/xXh2VRnO)
- Campo NrSecuencia de solapa ejecuciones limita cantidad de caracteres [#1904](https://trello.com/c/DslXRVQJ)
- Devengados se duplican si dos personas ejecutan en simultáneo el cuadro de movimientos automáticos [#1895](https://trello.com/c/nVj7USJ8)

# 6.7.30
> Fecha: 06/06/2024 | Compilacion: 6.7.30.0 | [Trello](https://trello.com/c/8ePsou4Y) {.is-info}

> En esta versión **surge** un error en los 'Recorrer SQL' que se soluciona en la versión posterior.
{.is-danger}


- Error en funcion max() [#1958](https://trello.com/c/LdTmjt2a)
- Redondeo en Funcion FSTR() parte entera [#1954](https://trello.com/c/ZKSxugB3)
- Crear lista CANJES igual a CUOTAS/PRENCANCELACION [#1948](https://trello.com/c/YwCgqXht)
- Sin Permiso EX011 permite modificar Jerarquias en ABMs con ese campo [#1944](https://trello.com/c/edSrjzXP)
- NO propaga los datos de un select despues de procesar otro subproceso con select. [#1943](https://trello.com/c/49DXiPmx)
- Doble click de ACLO en informe da error la primera vez que se realiza. con click solo no da error. [#1942](https://trello.com/c/wiWfS64D)
- Validacion en una Operacion no da el valor correcto [#1941](https://trello.com/c/y0a4IvnR)
- RecorrerSql anidado arroja null reference [#1939](https://trello.com/c/JiI3YBOi)
- Funcion con Crear Dialogo da error al utilizar los campos post visualizacion del mismo [#1935](https://trello.com/c/naEfSoqo)
- Filtros de Usuario da error [#1933](https://trello.com/c/zJnfQ4Vl)

# 6.7.29.1
> Fecha: 31/05/2024 | Compilacion: 6.7.29.1 | [Trello](https://trello.com/c/kWon47SB) {.is-info}

- [HOT FIX] Error al intentar limpiar carpeta subprocess [#1952](https://trello.com/c/X3Mk9Yt8)

# 6.7.29
> Fecha: 23/05/2024 | Compilacion: 6.7.29.0 | [Trello](https://trello.com/c/gurmhAym) {.is-info}

- Campo fecha con valor erroneo no da error [#1940](https://trello.com/c/dnRSUEeF)
- Funcion Round() debe tomar valores AwayFromZero del estandar de .NET [#1936](https://trello.com/c/tTeS7Tvk)
- Uso de celda numérica como fecha da error en CotizacionC si se le pasa una operacion [#1932](https://trello.com/c/Bxr9aon5)
- Parametro 'Selecciona Todos',SI,NO en listbox() no funciona [#1930](https://trello.com/c/WJ8AJ2VP)
- Permitir extensiones en adjuntos de mensajes con case insensitive [#1927](https://trello.com/c/wh2BKAcm)
- Limpieza directoris Scrpts Subprocess [#1922](https://trello.com/c/hxrALws3)
- Mensajes en una operacion con ACLO [#1920](https://trello.com/c/qGh1gP6q)
- Socket.Recibir - Error ORA-00923: FROM keyword not found where expected [#1918](https://trello.com/c/bI3v0iMu)
- Crear lista PRECANCELACION igual a CUOTAS [#1916](https://trello.com/c/ateLACzF)
- LogInformes de procesos con error [#1211](https://trello.com/c/ALfdDw5h)

# 6.7.28
> Fecha: 02/05/2024 | Compilacion: 6.7.28.0 | [Trello](https://trello.com/c/7MRe3Cb0) {.is-info}

- EjecutarEvento2 funcione como EjecutarEvento - parametrizable [#1919](https://trello.com/c/gFGFJFK5) 
- Diferencias entre algoritmo de hashing de v3 y v6 [#1924](https://trello.com/c/kVJifQV8)

# 6.7.27
> Fecha: 26/04/2024 | Compilacion: 6.7.27.0 | [Trello](https://trello.com/c/AtVJ3nsG) {.is-info}

- Funcion PyC funciona de distinta manera en V3 y V6 #1913 [#1913](https://trello.com/c/XWxYyYZQ)

# 6.7.26
> Fecha: 08/04/2024 | Compilacion: 6.7.26.0 | [Trello](https://trello.com/c/U9YZ0aPL) {.is-info}

- Loop infinito en PPLStudio al validar scripts que usen en forma anidada un mismo script [#1912](https://trello.com/c/cE3TkKL9)

- No se reconocen movimientos automáticos de posiciones2 al cambiar de fecha [#1908](https://trello.com/c/teovVFEX)

- Error en decimales al multiplicar por 10 [#1907](https://trello.com/c/axPiobDM)

# 6.7.25
> Fecha: 03/04/2024 | Compilacion: 6.7.25.0 | [Trello](https://trello.com/c/IHWOflp6) {.is-info}

- Campo char() en null no da Vacio, Funcionamiento distinto a V3 [#1901](https://trello.com/c/somQiVGD)

- Calculo numerico como condicion de en un if no funciona [#1897](https://trello.com/c/ybXjO2E9)

- Actualizacion de objetos dentro de otros objetos [#1893](https://trello.com/c/9uBWOH0G)

- Logueo de excepciones en tabla LOGERRORES [#1756](https://trello.com/c/YbM7U7Q1)

- En los campos Radio, cuando no se declaran las opciones, no muestra el campo en la minuta [#710](https://trello.com/c/t4cYACIW)

# 6.7.24
> Fecha: 07/03/2024 | Compilacion: 6.7.24.0 | [Trello](https://trello.com/c/ZFC6ZEsX) {.is-info}

- Graba mal Operaciones para campos Radio y Check que no se cambio valor [#1894](https://trello.com/c/6hIi4AWo)

- Informe CORCUP Campo Entero2 [#1892](https://trello.com/c/8JcYk1kV)

- Funcion InteresEspecie() difiere entre V3 y V6 [#1891](https://trello.com/c/c1oaWU00)

- Problema en calculo con formula [#1890](https://trello.com/c/ITYl8i9k)

- Grillas con 'LinkearHoja' dejan la memoria tomada incluso después de cerrarse [#1886](https://trello.com/c/7SiiT1bM)

- Búsqueda en listas numericas por teclado [#1882](https://trello.com/c/D2lBnHu3)

# 6.7.23
> Fecha: 01/03/2024 | Compilacion: 6.7.23.0 | [Trello](https://trello.com/c/VhEUSuGL) {.is-info}

- Definición en campos RB (radio Button) en OPERACIONES [#1888](https://trello.com/c/kJnCaz9u)

# 6.7.22
> Fecha: 06/02/2024 | Compilacion: 6.7.22.0 | [Trello](https://trello.com/c/8laROpsl) {.is-info}

- Cotizacion() tiene parametro 8 y da resultado distinto en BNP [#1885](https://trello.com/c/a4I7DV2D)
- NUM() da otro resultado en BNP con Windows en Ingles [#1884](https://trello.com/c/CRe0cEM7)
- Campos de Fecha sin datos. Mal formato en ABM [#1883](https://trello.com/c/McgSvxCp)
- Socket Iniciar [#1881](https://trello.com/c/KEiocSUI)
- LimConsumidos agregar filtro TipoPosicion [#1875](https://trello.com/c/qH9x3oB7)
- Migración de PPLStudio, Portfolio Y Console Server a .NET Framework 4.8 [#1874](https://trello.com/c/ywcPmRfY)
- Función @‌CUENTAS2 no funciona en V6 [#1868](https://trello.com/c/geP387jG)
- Desarrollar ListaCuotas custom para sigla IRSA (V6) [#1866](https://trello.com/c/7v4nnn28)
- Campos en Operaciones , Transacciones [#1865](https://trello.com/c/jbyaUQbV)

# 6.7.21
> Fecha: 27/12/2023 | Compilacion: 6.7.21.0 | [Trello](https://trello.com/c/uXwtYaDC) {.is-info}

- Funcion ImprimirOperacion sobreescribe la informacion del reporte - IMPOPE [#1835](https://trello.com/c/PjpS01a3)
- Al darle OK++ a una operacion no se blanquean las cuotas ni comisiones. [#1841](https://trello.com/c/M874VQQH)
- Funcion EliminarFilas, elimina el formato seteado antes con SetFont - IRSA V6 [#1843](https://trello.com/c/2Z0mD9Sh)
- ABMs, bloque when_change procesa siempre [#1844](https://trello.com/c/pys1DAzw)
- Error en BACS - SQL Deadlock [#1845](https://trello.com/c/CDyNdOme)
- En Mensajes permitir que no se escriba un mensaje ya que se está usando para adjuntar. [#1846](https://trello.com/c/srSadE6a)
- Index was out of range. en Listbox [#1847](https://trello.com/c/x8qPnOhC)
- Agregar filtro en instancias, además de la supergrilla [#1849](https://trello.com/c/eR7sCylg)
- Permitir múltiples archivos adjuntos en un mismo mensaje [#1850](https://trello.com/c/i15I63uy)
- Fullscript genera error al incluir parte de una funcion [#1854](https://trello.com/c/PoqTIrn1)
- Nueva sigla para IRSA [#1855](https://trello.com/c/FEWkVwr3)
- Agregar parámetro de configuración para establecer máximo tamaño permitido para archivos adjuntos en mensajes [#1856](https://trello.com/c/vZHhUWfA)
- Archivos .PDF adjuntos en mensajería se abren por detrás de la ventana modal de la operación [#1857](https://trello.com/c/cCsyAhqm)
- Identificar con distintos índices los archivos duplicados en la carpeta TMP [#1858](https://trello.com/c/frBo2pjh)
- Definir INSTANCIA=0 cuando se utiliza Ver o Editar desde la grilla. [#1862](https://trello.com/c/yZnhLosK)
- Editar operación da error si operación tiene sección MTMDIARIO [#1863](https://trello.com/c/fvb12cfQ)
- Creación de botón en ventana de mensajes de operaciones que visualice archivos adjuntos [#1864](https://trello.com/c/LYk6WDwh)

# 6.7.20.1 [HOT FIX]
> Fecha: 14/12/2023 | Compilacion: 6.7.20.1 | [Trello](https://trello.com/c/P18E2Rnl) {.is-info}

- Corrección de permisos para entrar al portfolio (siglas BFSA y PCR) [#1859](https://trello.com/c/FaRbbjkh)

# 6.7.20
> Fecha: 23/11/2023 | Compilacion: 6.7.20.0 | [Trello](https://trello.com/c/sHgne0BO) {.is-info}

- Lista Cuotas - Op. Prestamos [#1821](https://trello.com/c/ac4e5sLL)
- Ejecucion de funcion con select genera consulta con select anterior y actual [#1822](https://trello.com/c/0gKsFPIO)
- Permitir usar variables del tipo Var() en nombres de columnas de Listbox [#1823](https://trello.com/c/bgN9nav2)
- Quitar menú "Órdenes" de sigla PCR [#1827](https://trello.com/c/xynSntyJ)
- Añadir sigla PCR a la funcionalidad "Permisos al ingresar al sistema" [#1830](https://trello.com/c/IwkQAG0H)
- MontoGastos() error en BNP2 [#1832](https://trello.com/c/U5uNUM6B)
- SendMail - Mailing compatibilidad v3 / v6 [#1836](https://trello.com/c/QXWaBh6A)
- Error Filtro grilla de Operaciones(Todas) - IRSA V6 [#1837](https://trello.com/c/WMaa4T4O)

# 6.7.19
> Fecha: 31/10/2023 | Compilacion: 6.7.19.0 | [Trello](https://trello.com/c/XwWnGk9m) {.is-info}

- Función PYC() no anda correctamente [#777](https://trello.com/c/lZWyHjDp)
- IfDef en ABMS da error de "se espera constante" cuando hay variables definidas [#1709](https://trello.com/c/ml70tOLF)
- Permisos al ingresar al sistema [#1760](https://trello.com/c/Q7wii3cD)
- Máscara no toma en cuenta si solo quiero un número entero seguido de decimales [#1776](https://trello.com/c/AFv7t9dw)
- Error al cerrar Portfolio: No libera usuario de tabla USUARIOSACTIVOS [#1779](https://trello.com/c/KKACgaxF)
- Función CleanCache cancela desde eventos [#1796](https://trello.com/c/l0WjK2Ss)
- Modificar Función GenerarAsientoOp para que grabe nuevos campos en los asientos [#1806](https://trello.com/c/UymTQj0I)
- La Grilla de Ordenes deberá ser SuperGrilla [#1809](https://trello.com/c/tCUtoFdD)
- GenerarAsientoOp() pincha cuando se le pasa un valor 'fijo' a Alias9 [#1817](https://trello.com/c/Q2aymcRC)
- Sumarmeses no admite cálculo en uno de sus items [#1824](https://trello.com/c/2Kw2boWu)
- Error en función Cotizacion() [#1826](https://trello.com/c/VqM4SaFL)

# 6.7.18
> Fecha: 08/09/2023 | Compilacion: 6.7.18.0 | [Trello](https://trello.com/c/E9a1ALYu) {.is-info}

- Comisiones2 - Varios [#1783](https://trello.com/c/2tKp2SQx)
- Controlar visibilidad de Mensajes desde Perfiles [#1789](https://trello.com/c/5vqROHVU)
- Al clickear "Actualizar" en cualquier solapa del ABM de perfiles, se borran todos los permisos [#1804](https://trello.com/c/Wii5H0bQ)
- Sección cuotas no genera recálculos si no sufre modificaciones [#1805](https://trello.com/c/bQkEem4E)
- Definir INSTANCIA=0 cuando se utiliza Ver , Agregar o Editar desde la grilla. [#1755](https://trello.com/c/wk7l5Y6x)
- Funciones v3 setxxxInicial Actual [#1795](https://trello.com/c/i9Ij09YB)
- AbrirAscii no respeta parametros [#1793](https://trello.com/c/VOsoSyKP)
- ExportarPdf no genera saltos de hoja [#1787](https://trello.com/c/EpWKpcqu)
- Corregir el before_save en ABMs embebidos [#1807](https://trello.com/c/Hhqvxmlf)
- Evento MAE Online cancela al cerrar Portfolio [#1810](https://trello.com/c/70ss64PT)

# 6.7.17.1 *(HOT FIX)*
> Fecha: 03/08/2023 | Compilacion: 6.7.17.1 | [Trello](https://trello.com/c/e87cP6ty) {.is-info}

- Corrección de labels en campos de tipo 'Lista' [#1802](https://trello.com/c/dgg4WhS4)

# 6.7.17
> Fecha: 27/07/2023 | Compilacion: 6.7.17.0 | [Trello](https://trello.com/c/306ho3Xk) {.is-info}

- Setear fecha del sistema en base a días hábiles y/o tabla 'Feriados' [#1797](https://trello.com/c/yiorWpMi)
- EjecutarEvento2 + DirsPerUser, provoca bloqueos en carpetas de archivos temporales [#1799](https://trello.com/c/WzHtaoSu)
- Error en PPLRC al abrir el dia. [#1801](https://trello.com/c/akxpvElA)


# 6.7.16
> Fecha: 07/07/2023 | Compilacion: 6.7.16.0 | [Trello](https://trello.com/c/pfj1yk6v) {.is-info}

- Al exportar a EXCEL no convierte correctamente los colores de fondo de celdas [Trello #1786](https://trello.com/c/WCVEKeR2)
- V3 permite concatenación en leyendas de Campos de Operaciones, pero V6 no [Trello #1276](https://trello.com/c/QSEmJnKr)
- Ventana de Cupones a Vencer al iniciar el cliente de la aplicacion. [Trello #1757](https://trello.com/c/FFz3d52c)
- Función "Hora" no admite parámetros de tipo "Double" o flotante [Trello #1791](https://trello.com/c/fQlOWBLi)
- PPLStudio muestra "Supergrilla" para órdenes pero Portfolio, no [Trello #1766](https://trello.com/c/9T6T6pVy)
- No reconoce TIPOOP dentro de un TipoOp [Trello #1551](https://trello.com/c/g73UQc54)
- AgendaCupones no graba campo TNA para teco [Trello #1775](https://trello.com/c/SS0RaHuz)
- Sigla PCR (igual que BFSA con AD) [Trello #1785](https://trello.com/c/vcC7Pl35)
- No funciona sentencia If en Nombre de campo [Trello #1466](https://trello.com/c/cwfDRu7x)

# 6.7.15
> Fecha: 21/06/2023 | Compilacion: 6.7.15.0 | [Trello](https://trello.com/c/1E7OoD6F) {.is-info}

- Error al cerrar Portfolio: No libera usuario de tabla USUARIOSACTIVOS [Trello #1779](https://trello.com/c/KKACgaxF)
- Sigla BACS no borra USUARIOSACTIVOS al salir [Trello #1697](https://trello.com/c/WXg9wXxU)
- Exportación a Excel con solapas cambia formato después de la primera hoja [Trello #1780](https://trello.com/c/TXaRs3us)


# 6.7.14
> Fecha: 06/06/2023 | Compilacion: 6.7.14.0 | [Trello](https://trello.com/c/OV69FdO5) {.is-info}

- Movs devengados duplica registros. [Trello #1775](https://trello.com/c/oAgMn7RS)
- Funcion AgregarCupon cancela en ORACLE. [Trello #1774](https://trello.com/c/AIpUnImG)
- Operación no esta devengando bien con Base 30360. [Trello #1772](https://trello.com/c/oq2bAG2s)
- Funcion Ascendientes Ordenamiento. [Trello #1767](https://trello.com/c/4e8QIGFE)
- Posibilidad de anidar IFDEF e IFNDEF en Operaciones y Abms. [Trello #1763](https://trello.com/c/ZHquem6Q)
- Casos de IFDEF dan overflow (anidar IFDEF en eventos e informes). [Trello #1337](https://trello.com/c/tIppuqa0)
- TasaProducto2 arroja resultados diferentes a v3. [Trello #1751](https://trello.com/c/Xohg145j)
- Modificacion al Dialogo de Publish y Alta de ABMs. [Trello #1572](https://trello.com/c/ByJ2gHO8)

# 6.7.13
> Fecha: 11/05/2023 | Compilacion: 6.7.13.0 | [Trello](https://trello.com/c/xC6CbmJ9) {.is-info}

- Modificación en mensajería - Nuevos canales y configuraciones. [Trello #1752](https://trello.com/c/d7GX5cjS)
- Campo de Op con IFDEF se evalúa para otra sigla y pincha. [Trello #1699](https://trello.com/c/XKZmPQt7)
- La publicación de ABMs falla si hay un ABM con número de orden o menú en 999. [Trello #1768](https://trello.com/c/KP6VISVl)

# 6.7.12
> Fecha: 05/05/2023 | Compilacion: 6.7.12.0 | [Trello](https://trello.com/c/tnNWBT7D/) {.is-info}
- Sentencia Repetir cancela en v6.7.12. [Trello #1764](https://trello.com/c/BGIRBviv/)
- CrearDialogo cancela en v6.7.12. [Trello #1761](https://trello.com/c/EeS5c6Nz/)
- Movdevengados diferencias con parámetro Base 30360. [Trello #1754](https://trello.com/c/m1FDW9A8/)
- CotizacionC no considera ModoEspecies. [Trello #1753](https://trello.com/c/aM6YD9Qc/)
- Error Interprete con funcion ACN. [Trello #1749](https://trello.com/c/xY812GmT/)
- EjecutarEvento2 - Se esperaba ScriptId, ScriptType y setUp. [Trello #1747](https://trello.com/c/b0XRUutS/)
- Se cuelga el PPL Studio cuando el include es muy largo. [Trello #1744](https://trello.com/c/HNEbIzff/)
- Debugger no respeta los Stops. [Trello #1743](https://trello.com/c/6YBfKOZB/)
- Sentencia ifndef da overflow. [Trello #1738](https://trello.com/c/yKuJzb6e/)
- Extraer dependencia RankeadorNIIF. [Trello #1487](https://trello.com/c/lQJbOm3S/)

# 6.7.11
> Fecha: 30/03/2023 | Compilacion: 6.7.11.0 | [Trello](https://trello.com/c/AyOkpK2Z) {.is-info}
- Parser da error con funciones en Crearlistbox. [Trello #1734](https://trello.com/c/WqErPRP5)
- Seleccionar Canal de Mensajes en Pantalla de OP. [Trello #1742](https://trello.com/c/ceim5cUX)
- Valor funcion AHORA, cacheda. [Trello 1267](https://trello.com/c/NmK5lynk)
- ExportarPPL debe soportar Tab como separador de registros. [Trello 1739](https://trello.com/c/MvN3nZX0)
- Búsqueda en listas por teclado no es como debería ser [Trello 1530](https://trello.com/c/Brz5T9HN)
- Doble Confirmacion - Incorporar embebidos. [Trello 1080](https://trello.com/c/rPNzmPpq)
- Envía a supervisión de ABM's Sin haber hecho cambios. [Trello 1628](https://trello.com/c/N5bQ77dX)
- Funcionalidad de marcar como leido configurable. Explicito o implicito. [Trello 1492](https://trello.com/c/Il552eGB)
- Canales en EnviarMensajes. [Trello 1736](https://trello.com/c/4z7spHvU)
- Funciones ascendientes / descendientes. [Trello 1741](https://trello.com/c/2ziPLV43)
- MQ parametros de Conexion. [Trello 1740](https://trello.com/c/gk68ftB4)

# 6.7.10
> Fecha: 06/03/2023 | Compilacion: 6.7.10.0 | [Trello](https://trello.com/c/U73c0UWf/) {.is-info}
- Se pierde el default de las listas. [Trello #1730](https://trello.com/c/6g6YuDTy) 
- Funcion Sigla para Operaciones. [Trello #1729](https://trello.com/c/mxV1Tm4f) 
- Super Grilla para Transacciones. [Trello #1727](https://trello.com/c/EhLKqo3J) 
- Exportar a Excel cambia el formato de porcentaje. [Trello #1725](https://trello.com/c/SI4qzw96) 
- Tree View para ABMs con Jerarquia. [Trello #1720](https://trello.com/c/1rmJHNXT) 
- Agregar similar no permite modificar las cuotas de la op original. [Trello #1647](https://trello.com/c/FDFyGT3T) 
- Modo Debug - GetNumerador y BuscarCampo pinchan en debug. [Trello #1624](https://trello.com/c/SVeScdPh) 
- Exportar a Excel con Hoja Editable. [Trello #1461](https://trello.com/c/ObqPcfUh) 
- ABM da error en campos numericos. [Trello #870](https://trello.com/c/UK6K6zsY) 
- Doble Confirmaion: Opciones Aprobar todos y Rechazar todos. [Trello #294](https://trello.com/c/3wT5mw8V) 

# 6.7.9
> Fecha: 10/01/2023 | Compilacion: 6.7.9.0 | [Trello](https://trello.com/c/lDQFUJeR) {.is-info}
- Error en Trigger MovEjecutados duplica Saldos. [Trello #1724](https://trello.com/c/mHbcJw8C) 
- Error en cabecera hppl cambia formatos. [Trello #1723](https://trello.com/c/ed5Satgj) 
- Error en llamada a funcion comentada. [Trello #1722](https://trello.com/c/5XElAsqN) 
- Mensajes con Adjuntos en ORACLE. [Trello #1719](https://trello.com/c/d6JuvqP8) 
- Nombre de campo como variable en Listbox. [Trello #1611](https://trello.com/c/8g38cyFL) 
- Modificacion dialogo de Publish y Alta de ABMs. [Trello #1572](https://trello.com/c/ByJ2gHO8) 
- Integracion MQSeries. [Trello #1371](https://trello.com/c/MdWMid6S) 

# 6.7.8
> Fecha: 21/12/2022 | Compilacion: 6.7.8.0 | [Trello](https://trello.com/c/lDQFUJeR) {.is-info}
- SaltarHoja en Impresion PDF [Trello #1717](https://trello.com/c/EiN708BF) 
- Funcion InteresEspecie - parametro MODO [Trello #1716](https://trello.com/c/jh2gQfzR) 
- AgregarCupon cambia FechaCorte si es feriado [Trello #1631](https://trello.com/c/XXkSd0sk) 

# 6.7.7
> Fecha: 01/12/2022 | Compilacion: 6.7.7.0 | [Trello](https://trello.com/c/uXFuY32k) {.is-info}
- Funcion FactorDIAS [Trello #1715](https://trello.com/c/qXpAS19S) 
- Devengados parametro Base 30360 [Trello #1712](https://trello.com/c/tUK3RiX3) 
- Funcion ABT - Asignar Bloque Texto [Trello #1710](https://trello.com/c/b54ZMFVn) 

# 6.7.6
> Fecha: 09/11/2022 | Compilacion: 6.7.6.0 | [Trello](https://trello.com/c/r0T6GCNz) {.is-info}
- Funcion FormatSTR [Trello #1711](https://trello.com/c/ejNSJlsA) 
- Validacion case sensitive de campos [Trello #1708](https://trello.com/c/oMj5anGt) 
- Fix Seccion CondicionesCuotas [Trello #1706](https://trello.com/c/alC1OC4g) 
- Fix Null Reference en impresion PDF [Trello #1704](https://trello.com/c/47F8Dbo3) 
- Error CondicionesCuotas [Trello #1701](https://trello.com/c/8XONhMi8) 
- Performance Eval FullScript [Trello #1645](https://trello.com/c/5hQFwCdK) 
- Crearlistbox no admite funciones [Trello #1610](https://trello.com/c/wWe1HWDG) 
- Descripcion mensaje de error en ABMs [Trello #1549](https://trello.com/c/0TVywERP) 



# 6.7.5
> Fecha: 05/10/2022 | Compilacion: 6.7.5.0 | [Trello](https://trello.com/c/DZjUoqwL) {.is-info}
- Error Login en CAPSA con AD [Trello #1700](https://trello.com/c/ZruUNXgR)
- Habilitar Ordenes para sigla BFSA [Trello #1695](https://trello.com/c/Ctu9mt0E)
- Fix en Grilla de Ordenes [Trello #1693](https://trello.com/c/mvoVS6Ad)
- Error al eliminar transacciones desde grilla de instancias [Trello #1637](https://trello.com/c/7HZgkyL7)
- Adjunto en Mensajes [Trello #1604](https://trello.com/c/QoxRtfTO)


# 6.7.4
> Fecha: 25/08/2022 | Compilacion: 6.7.4.0 | [Trello](https://trello.com/c/L3CrmqeF) {.is-info}
- Se agrega mas detalle de error en modelos de asiento [Trello #1690](https://trello.com/c/tyzKyJql) 
- Error con Cuadro de mensajes llamado desde Operaciones [Trello #1689](https://trello.com/c/zC4HrBpG) 
- Sigla CAPSA - Cambia Login [Trello #1686](https://trello.com/c/vmprqxUl) 
- Funcion FirmarPDF [Trello #1685](https://trello.com/c/6zSHnXgu) 
- ABMs: Campo DateTime no se actualiza [Trello #1684](https://trello.com/c/lYoDEyNB) 
- Recalculo del set de las listas [Trello #1681](https://trello.com/c/rTgCsce1) 
- Problema con función ValorAnterior [Trello #1679](https://trello.com/c/uzMTvpb7) 
- Cuadro de Mensajes toma el foco principal [Trello #1678](https://trello.com/c/WpNMq18v) 
- Campo que depende de OperacionRef no se puede editar [Trello #1677](https://trello.com/c/p9ah6lPz) 
- Funcion DIFM [Trello #1676](https://trello.com/c/33YysZ9o) 
- Tamano Oficio en hojas de impresion [Trello #1675](https://trello.com/c/OBTO2a2v) 
- Bloque TRY CATCH capturar error completo [Trello #1673](https://trello.com/c/QspT8nRr) 
- Mas detalle en mensajes de errores de Login [Trello #1671](https://trello.com/c/CC6YR4gR) 
- Sigla BACS [Trello #1667](https://trello.com/c/22vAUa4C) 
- Exportar PDF: Funcion Setprintfit [Trello #1666](https://trello.com/c/QphA9PIB) 
- No actualiza lista de cuotas si la cantidad es cero [Trello #1656](https://trello.com/c/XM8A3o9X) 
- Reporte no termina de ejecutarse [Trello #1531](https://trello.com/c/Gamfgnpn) 
- Exportar con formato XLSX [Trello #1527](https://trello.com/c/ekluDwOD) 


# 6.7.3
> Fecha: 29/06/2022 | Compilacion: 6.7.3.0 | [Trello](https://trello.com/c/9oxaYo7i) {.is-info}
- FPA.Consola nuevo parametro J [Trello #1670](https://trello.com/c/xnffNmL2) 
- Funciones Supervision de abms [Trello #1665](https://trello.com/c/vclzUOvf)
- Error en recalculo de campos Lista [Trello #1664](https://trello.com/c/jpN4Pn7J) 
- ExportarXls poder especificar la hoja de la planilla [Trello #1659](https://trello.com/c/oJvfZXE4) 
- Ventana de Cancelar queda fuera de foco [Trello #1658](https://trello.com/c/5kWMWkyj)
- Parametrizar font de control Lista [Trello #1646](https://trello.com/c/UkOrdzD9) 
- Funciones doblarcomillas y sacaenters [Trello #1632](https://trello.com/c/NlDTGuIU)


# 6.7.2
> Fecha: 01/06/2022 | Compilacion: 6.7.2.0 | [Trello](https://trello.com/c/KiGK0Zwq) {.is-info}
- Funciones Buscar cancelan cuando son NULL [Trello #1636](https://trello.com/c/xBTb5AYa) 
- Performance funcion EsTerminal [Trello #1639](https://trello.com/c/Rumo2XUs) 
- SendMail: Encriptar usuario y password [Trello #1640](https://trello.com/c/1EeIg5n3) 
- SendMail: Encriptar usuario y password (*duplicado*) [Trello #1556](https://trello.com/c/408VfTX3)
- BookValido: TipoOp no debe ser obligatorio [Trello #1648](https://trello.com/c/ceGerIEf) 
- LookUp: No carga descripcion del valor default  [Trello #1655](https://trello.com/c/vN5vWHbx) 
- Funcion LNG para convertir a tipo de dato long [Trello #1521](https://trello.com/c/eeMvL8qA)
- Grabar en INSTANCIASOP la direccion [Trello #1349](https://trello.com/c/IGdhO3la)
- Fix control numerico en blanco [Trello #1653](https://trello.com/c/JZbVueWI)
-  GenerarAsientoOp - Error converting data type varchar to real [Trello #1662](https://trello.com/c/wDnQC2P)
- Orden de funcion Ascendientes para clientes corporate [Trello #1661](https://trello.com/c/ursSzfNZ)
-  ListBox: mascara en fechas vacias o null [Trello #1649](https://trello.com/c/QRxuqGRS)
- Error Recorrer SQL [Trello #1601](https://trello.com/c/BZClTkdk)


# 6.6.26
> Fecha: 06/05/2022 | Compilacion: 6.6.26.0 | [Trello](https://trello.com/c/LxkPyxxG) {.is-info}
- Auditoria Setear usuario FPA [Trello #1644](https://trello.com/c/EbdDHUgX) 
- Error al Avanzar Instancia en la 6.6.25 [Trello #1643](https://trello.com/c/oYzCEKLp) 
- Error con campo NULL no convierte a 0 en Modelos de Asientos [Trello #1602](https://trello.com/c/IJTlMrRL) 
- Renombrar evento EXPPL [Trello #1621](https://trello.com/c/AegeUdkF) 

# 6.6.25
> Fecha: 22/04/2022 | Compilacion: 6.6.25.0 | [Trello](https://trello.com/c/OQJLBMkU) {.is-info}
- Customs para CAPSA [Trello #1599](https://trello.com/c/l3qqyFsK) 
- Diferencia en función LimConsumidos en V6 y V3 [Trello #1600](https://trello.com/c/WLk3utLM) 
- Funciones Encriptar2 y DesEncriptar2 [Trello #1618](https://trello.com/c/cg0F3dCp) 
- Funciones SQL2 y EXEC3 [Trello #1619](https://trello.com/c/UCvXNk3a) 
- Agrega campo Direccion en INSTANCIASOP [Trello #1622](https://trello.com/c/fQLx6ANv) 
- CAPSA NO usa DELDEVENGADOS [Trello #1623](https://trello.com/c/QYMxycfD) 
- Incorporar funciones ExportarPMG ImportarPMG GrabarPMG LeerPMG [Trello #1456](https://trello.com/c/WLk3utLM) 
- Validaciones en filas vacias de ListBox.  [Trello #1510](https://trello.com/c/dMJOXRKQ) 
- Función AuditPerfilChanges para ORACLE [Trello #1614](https://trello.com/c/CBnQvYBH) 
- No valida campos de un dialogo si estoy en una instancia <> 0 [Trello #1615](https://trello.com/c/bXYxtyVg) 
- Funcion TasasClientes no funciona [Trello #1625](https://trello.com/c/ZnTLbOMf) 
- Incorporar la funcion LTSTR en OPERACIONES [Trello #1627](https://trello.com/c/7KuZ5mWX) 
- Sigla BIND_QA [Trello #1617](https://trello.com/c/qgFnDIJu) 
- Campos Custodia y Concepto en RelacionCuenta [Trello #1626](https://trello.com/c/AdZOTdQS) 
- Incorporar la funcion CotizacionDirecta en OPERACIONES [Trello #1630](https://trello.com/c/ioQXhRZx) 

# 6.6.24
> Fecha: 16/03/2022 | Compilacion: 6.6.24.0 | [Trello](https://trello.com/c/La4cDbsx) {.is-info}
- Regeneracion de Movimientos LISTASAL [Trello #1581](https://trello.com/c/mxZCkTvR)
- Llevar variables definidas en el script al RootScope. [Trello #1393](https://trello.com/c/9djwkMRg)
- Funcion Ascendientes trae elementos desordenados [Trello #1574](https://trello.com/c/pMvyGgWQ)
- Error al modificar jerarquias [Trello #1561](https://trello.com/c/9BsDlchk)
- Fix Supervision de abm [Trello #1568](https://trello.com/c/H4JaYvyN)
- Combo en dialogo ignora seleccion [Trello #1566](https://trello.com/c/xjkUYCfr)
- Funcion TasaCliente [Trello #1596](https://trello.com/c/CbmzyMDt)
- Item Menu ExportarPPL [Trello #1484](https://trello.com/c/Egbl5gsX)
- Funcion Exp [Trello #1597](https://trello.com/c/u0G2JbYL)
- Funcion Ascii no acepta espacios [Trello #1584](https://trello.com/c/alDtdhhu)
- Funcion raiz cuadrada (SQRT) para operaciones [Trello #1582](https://trello.com/c/H1U2jP1N)
- Error al eliminar items en las listas de Operaciones [Trello #1547](https://trello.com/c/8IAOKNtf)
- Agregar parametros a seccion MOVMTMDIARIO [Trello #1598](https://trello.com/c/xWh7y83A)
- Fix Funcion BookValido [Trello #1603](https://trello.com/c/fScSGYI0)
- Fix Funcion SQL() para BNP + Validacion en funcion CerrarHoja [Trello #1608](https://trello.com/c/aZfEIPgt)
- Control ComboBox no ejecuta recalculos [Trello #1613](https://trello.com/c/rqwSzsan)


# 6.6.23.1
> Fecha: 20/12/2021 | Compilacion: 6.6.23.1 | [Trello](https://trello.com/c/zLG7fMj8) {.is-info}
- Fix: funcion GtStr en la comparacion de strings que no sean de tipo hora:segundos. [Trello #1508](https://trello.com/c/TnffK9eT)

# 6.6.23
> Fecha: 21/10/2021 | Compilacion: 6.6.23.29038 | [Trello](https://trello.com/c/oVgvaQUP) {.is-info}

- Fix: error en mascara de exclamacion. [Trello #1514](https://trello.com/c/v4VJ8dP5)
- Fix: error al definir la celda io:xx. [Trello #1498](https://trello.com/c/vKi2EtlU)
- Fix: cerrar informe padre desde un informe hijo abierto con ACL. [Trello #1455](https://trello.com/c/x0kVT0AO)

# 6.6.22
> Fecha: 05/10/2021 | Compilacion: 6.6.22.18176 | [Trello](https://trello.com/c/2XueRuD5) {.is-info}

- Fix: ExisteTemporalPendiente() para oracle [Trello #1522](https://trello.com/c/Dvv4XWIz)
- Fix: ocultar cuadro de mensajes al ejecutar evento por POSTEDICION [Trello #1518](https://trello.com/c/yCfvwMgU)
- Fix: error al actualizar super grillas de instancias que no sean de operaciones [Trello #1519](https://trello.com/c/lscX0lKu)
- SendMail: se agrega la posibilidad de enviar mas de un attach. [Trello #1528](https://trello.com/c/hI2ObOTY)
- Feature: Plugin para modificar la propiedad Where de un campo Autocomplete en Abms. [Trello #1457](https://trello.com/c/LMwTSEeB)
- Sigla BIND: en PPLStudio login debe ser editable **Critico** [Trello #1363](https://trello.com/c/0yjqQgEe)
- Implementacion sigla FPA **Critico** [Trello #1363](https://trello.com/c/0yjqQgEe)

# 6.6.21
> Fecha: 24/09/2021 | Compilacion: 6.6.21.28418 | [Trello](https://trello.com/c/IvtoXtms) {.is-info}

- Configuracion de ABMs que requieren supervision por PPLRC [Trello #1504](https://trello.com/c/IoE2f0b0)
- SupAbms: Cambio de Observacion por Motivo [Trello #1512](https://trello.com/c/AyTjx66K)
- Funcion Raiz Cuadrada SQRT. [Trello #1497](https://trello.com/c/PsqD1XGT)
- Funcion DiasSemestre. [Trello #1509](https://trello.com/c/6mnEcbOA)
- Soporte supervision de ABMs en Oracle **Critico** [Trello #1476](https://trello.com/c/Ojm0NR7x)
- Funciones para acceder a la Info de una Supervision de ABM. [Trello #1477](https://trello.com/c/njVMDwEV)

# 6.6.20
> Fecha: 09/09/2021 | Compilacion: 6.6.20.27252 | [Trello](https://trello.com/c/LTkC3zcx) {.is-info}

- Fix: no tomaba el guion bajo en los campos string del dialogo cuando se utiliza una mascara. **Critico** [Trello #1495](https://trello.com/c/eXZI4n2B)
- Se desarrolla funciones LTrim y RTrim. [Trello #1489](https://trello.com/c/HFDBGGvQ)
- Feature: Implementacion de observaciones en ABMs supervisados. [Trello #1460](https://trello.com/c/VyzvCLPI)
- Fix: null reference al parsear scripts de interprete [Trello #1462](https://trello.com/c/367sdunm)
- SendMail: se agrega funcionalidad de CC, adjunto y soporte HTML. [Trello #1481](https://trello.com/c/NzLqiqMT)
- Log de version de base de datos en SessionInfo [Trello #1403](https://trello.com/c/qhpkAL6c)
- Fix: Si un evento padre con modoreproceso en si llama a un informe sin especificar todos los parametros del dialogo, no muestra todos los campos. [Trello #1469](https://trello.com/c/tpI39rcD)
- Buildserver: cambio en workflow de generaci├│n alpha/beta [Trello #1395](https://trello.com/c/8ndI0emd)
- Fix: No importa todas las celdas del archivo excel si se hace un importarXls de una hoja con celdas con error. [Trello #1453](https://trello.com/c/I3hh6i7v)
- Fix: error si no se especifican parentesis en la llamada a una funcion core en los params de un campo en interprete. [Trello #1428](https://trello.com/c/wYAS9RKp)

# 6.6.19
> Fecha: 28/07/2021 | Compilacion: 6.6.19.27944 | [Trello](https://trello.com/c/L5BwgNs3) {.is-info}

- Nuevas caracteristicas para sigla BFSA. [Trello #1471](https://trello.com/c/hC4VN8K9)
- SendMail: se agrega parametro attach. [Trello #1470](https://trello.com/c/YXWR0CRI)
- En PPL se definen por default las constantes de compilacion condicional correspondiente a la sigla [Trello #1439](https://trello.com/c/9KQYp16M)
- Fix: Lookup no actualiza su valor al editarse con blanco luego de un recalculo. [Trello #1463](https://trello.com/c/ufRBjRAS)
- Fix: error al llamar una funcion local PPL cuando se evalua un subcodigo PPL entre la definicion y llamada a la funcion [Trello #1465](https://trello.com/c/AhoCSgf0)
- Compatibilidad: Si un Evento con modoreproceso(condialogo) hace un linkearhoja, el informe llamado debe mostrar el dialogo cuando se hace refresh. [Trello #1443](https://trello.com/c/UOry6krh)
- Fix: error al llamar una funcion ppl global desde operaciones con casing diferente al de la definicion [Trello #1441](https://trello.com/c/SQOFQxTj)
- Fix: Funciones PPL definidas dentro de un include en PPLRC no se comportaban como globales [Trello #1440](https://trello.com/c/KZO8SZB7)
- Compatibilidad: HojaEditable no permite editar la grilla. **Critico** [Trello #1444](https://trello.com/c/QVY4EeXi)
- Implementacion sigla BFSA [Trello #1436](https://trello.com/c/sbwDxidc)
- PPLStudio: Buscar en Tablas [Trello #1423](https://trello.com/c/8Xo35MXp)
- Fix: funciones locales definidas dentro de includes [Trello #1442](https://trello.com/c/mGytOaWI)
- Fix: AgregarMarco [Trello #1434](https://trello.com/c/xo5vcRm5)
- Compatibilidad: la funcionalidad MODI debe estar disponible en listbox. [Trello #1421](https://trello.com/c/6RHz7dCw)
- Implementacion funcion CuitValido en operaciones. [Trello #1435](https://trello.com/c/mw7BpOY5)
- Error conversion Numeros a Letras [Trello #1418](https://trello.com/c/hDA5so8j)
- Fix: Formula de recalc de un campo que usa SUM(lista, colidx), siempre da 0. [Trello #1408](https://trello.com/c/rk22ig7c)
- Fix: PPLStudio borra directorio de scripts. [Trello #1413](https://trello.com/c/r88oWodG)
- Fix: EXE2 no contempla null param. [Trello #1416](https://trello.com/c/Oc1Ssd36)
- Fix: session info cotizaciones settings cuando se configura por PPLRC [Trello #1417](https://trello.com/c/mUPcwbCe)
- Funcionalidad Ranking Cotizaciones desactivada por default para BOFA [Trello #1417](https://trello.com/c/mUPcwbCe)
- Feature: implementacion del return explicito en lambdas. [Trello #1411](https://trello.com/c/hmuVPcLq)
- PPLCache: PMFuncs para gestion de cache en PPL [Trello #1402](https://trello.com/c/Ptie1lh7)
- Compatibilidad: implementacion de la funcion exe2. [Trello #1232](https://trello.com/c/EUFxXgcT)
- Ejecutar funciones definidas en PPLRC desde Operaciones+ [Trello #998](https://trello.com/c/A9duc8LA)
- Feature: Implementacion PMFunc monitor [Trello #1264](https://trello.com/c/pPt21u8y)

# 6.6.18
> Fecha: 31/05/2021 | Compilacion: 6.6.18.31736 | [Trello](https://trello.com/c/YzpXzjzC) {.is-info}

- Fix: Posibilidad de correr 2 app servers en la misma maquina. [Trello #1406](https://trello.com/c/zKJY3OtD)
- Feature: Se agrega funcionalidad mensajes para transacciones y ordenes. [Trello #1190](https://trello.com/c/MbWrefaI)

# 6.6.17
> Fecha: 14/05/2021 | Compilacion: 6.6.17.19813 | [Trello](https://trello.com/c/b6WwlivR) {.is-info}

- Fix: PerfilManager ignora campos identity para TECO por usar oracle 10. [Trello #1390](https://trello.com/c/gccYLVQs)
- Fix: se modifica funcion Descendientes para que sea compatible con la tabla ESTADOSCUSTODIA de TECO. [Trello #1351](https://trello.com/c/vcF58zvb)
- Fix: Cuando esta bloqueado o caido el servicio HASP, se quedaba colgado esperando una respuesta. [Trello #1380](https://trello.com/c/ZsYu87HB)
- Compatibilidad: Se configura que en BNP los items del menu utilitarios arranquen en 800. [Trello #1374](https://trello.com/c/gPxitfYW)
- Fix: el full script en informes y eventos tenia en cuenta las funciones comentadas. [Trello #1301](https://trello.com/c/Bn3qMLp9)
- Compatibilidad: Se agregan mas mascaras de campos string en inf y ev para que sea compatible con V3. [Trello #1387](https://trello.com/c/Tac0nhcG)
- Fix: cambios en ComCorredor2. [Trello #1382](https://trello.com/c/jGhvNbZ8)
- Fix: Si el campo SmartCardUser es null or empty no debe realizar la StrongValidation, tambien se agrego el param -B para la consola. Estos cambios solo aplican a BNP. [Trello #1364](https://trello.com/c/49T0STdZ)

# 6.6.16
> Fecha: 06/05/2021 | Compilacion: 6.6.16.31368 | [Trello](https://trello.com/c/fPbqGIxv) {.is-info}

- Fix: Titulo Login PPLStudio [Trello #1312](https://trello.com/c/rBVMT96Y)
- Fix: EjecutarEvento3 esta mostrando la ventana del proceso q crea para impersonarse con el usuario definido en subprocess.cred. [Trello #1366](https://trello.com/c/34cAmMJr)
- Feature: implementacion de EjecutarEvento3 [Trello #1340](https://trello.com/c/bvA5Q7OE)
- Fix: Al usar la funcion EjecutarEvento2, se genera una carpeta de log con el nombre del entorno. [Trello #1356](https://trello.com/c/iKkTpVLx)

# 6.6.15
> Fecha: 16/04/2021 | Compilacion: 6.6.15.21613 | [Trello](https://trello.com/c/VEjX3qoU) {.is-info}

- Fix: Si el campo UsuarioSmartCard es null, no debe realizar la StrongValidation, esto es solo para BNP. [Trello #1360](https://trello.com/c/OqVnExbS)

# 6.6.14
> Fecha: 15/04/2021 | Compilacion: 6.6.14.22753 | [Trello](https://trello.com/c/zZPp9WTm) {.is-info}

- Fix: EjecutarEvento2 no esta pasando el usuarioactivo que ejecuta el evento causando que se genere una carpeta de log con el nombre de usuario del db.cred. [Trello #1352](https://trello.com/c/9tpKoAHc)
- Fix: PPL.NET.Subprocess no esta teniendo en cuenta el PPLRC. [Trello #1350](https://trello.com/c/MwoB7V3F)
- Fix: ICBC no esta logueando en USUARIOSACTIVOS. [Trello #1353](https://trello.com/c/dmKVjs6i)
- Fix: Super Grilla de Trans y Ord en Oracle. [Trello #1302](https://trello.com/c/B7V9Zm9e)
- MontoArancel: implementacion nueva opcion en parametro 6. [Trello #1329](https://trello.com/c/JST32aLw)
- Implementacion de las caracteristicas de seguridad de ICBC. [Trello #1335](https://trello.com/c/J0Ilp9d8)
- Fix: mascaras en campos string, con la X ahora permite caracteres especiales tambien. [Trello #1257](https://trello.com/c/lFdQwN6I)
- Fix: se agrega trim en el control de campos string de dialogos que tienen mascara. [Trello #1229](https://trello.com/c/rFUUHd8y)
- Fix: error no manejado de autenticacion [Trello #1324](https://trello.com/c/Hu2ReK99)
- Caso de prueba nueva funcion RenombrarArchivo [Trello #917](https://trello.com/c/3fsHfN3G)
- Metodos para manejo de archivos y directorios [Trello #837](https://trello.com/c/o7imFopR)

# 6.6.13
> Fecha: 17/03/2021 | Compilacion: 6.6.13.21645 | [Trello](https://trello.com/c/rzhU0oXx) {.is-info}

- Fix: Alias en grilla de abm embebido + null reference [Trello #1321](https://trello.com/c/DDmMoBIt)
- RelacionCuenta: nuevo parametro Mercado [Trello #1320](https://trello.com/c/8Z79nGuA)
- Fix: Error en recalculo inicial en Ord, Tr, OpMin y MinBol cuando se avanza mostrando dialogo **Critico** [Trello #1318](https://trello.com/c/hYJ8zv6p)
- Fix: error no controlado al ingresar una comilla simple en campos lookup en op, tr, ord, etc. [Trello #1127](https://trello.com/c/dXnJyMRZ)
- Abms Embebidos: definir alias en la grilla. [Trello #1299](https://trello.com/c/CYXgTTAm)
- Fix: MontoArancelC por tipo Cliente. [Trello #1315](https://trello.com/c/tRXjk0kD)
- Error de Parse al comentar funciones inexistentes. [Trello #1297](https://trello.com/c/3NECeXz0)
- Fix: en algunos casos no se generaba el log de los errores + boton copiar del TextDialog en splash [Trello #1307](https://trello.com/c/eDlmHZv5)
- Fix: valor default de campos VFEC al avanzar o retroceder [Trello #1310](https://trello.com/c/5cRk4kHW)
- Implementacion de caracteristicas de seguridad para la sigla BNP. [Trello #1309](https://trello.com/c/54AwEhza)

# 6.6.12
> Fecha: 08/02/2021 | Compilacion: 6.6.12.26914 | [Trello](https://trello.com/c/vvdFR427) {.is-info}

- Fix: Abm, campos fechas se utilizaba como string para set, get, comparaciones y operaciones **Critico** [Trello #1270](https://trello.com/c/Epvx5p9c)
- ABM Perf de Usuario: por default se deshabilita el campo Script. **Critico** [Trello #1303](https://trello.com/c/1QqDI25X)
- Fix: si se utilizaba un campo tipo fecha que no estaba definido en el dialogo de la op,tr,or al avanzar o retrocer, devolvia la fecha 0 PPL. [Trello #1293](https://trello.com/c/8p6c14v9)
- Fix: Si el valor de OPREF es null or empty, no debe disparar los recalculos. **Critico** [Trello #1221](https://trello.com/c/lXiCOULQ)
- Funcion Modificar Orden [Trello #1230](https://trello.com/c/HCq90OVE)
- Compatibilidad: Si un campo de op del tipo check recibe un entero menor a 0, debe mostrarse des-seleccionado. [Trello #1203](https://trello.com/c/IF9wyl1z)
- Fix: variable de contexto ESEVENTUAL en Operaciones [Trello #1284](https://trello.com/c/VUqKNl0x)
- Fix: Abm en Oracle, error al validar claves duplicadas al modificar un registro [Trello #1239](https://trello.com/c/Nia9ms0b)
- Feature: seguridad custom en FPA.Console para BIND. [Trello #1289](https://trello.com/c/3nMFfzoA)
- Feature: Nuevas funciones IvaGastos y CodigoGastos. [Trello #1274](https://trello.com/c/aKlKMQNx)
- Fix: En abms los campos full_tab_text deshabilitados deben ser readonly [Trello #1202](https://trello.com/c/Nou9FIL3)
- Feature: solapa Script readonly
- Feature: Se agrega columna Tipo en lookup Open scripts. [Trello #798](https://trello.com/c/GV8xfIZl)
- Compatibilidad: Nueva Funcion 'FechaValida'. [Trello #1279](https://trello.com/c/NMxjMuuz)
- Fix: error al levantar filtros en super grilla de Transacciones y Ordenes [Trello #1185](https://trello.com/c/0sZz7Olj)
- Fix: Error con validacion del Abrir Dia en TECO, BYMA y BIND. [Trello #1247](https://trello.com/c/iX74Medm)
- Fix: includes (Funciones y Formulas) anidadas en operaciones [Trello #1268](https://trello.com/c/bhLJttKw)
- Integracion de SIP en PPLStudio [Trello #1244](https://trello.com/c/odsg0beB)
- Mostrar ventana de error con mas detalle durante la inicializacion de la aplicacion [Trello #1251](https://trello.com/c/RPNXjNYn)

# 6.6.11
> Fecha: 22/12/2020 | Compilacion: 6.6.11.20482 | [Trello](https://trello.com/c/adMoygBL) {.is-info}

- Funcion RelacionCuenta considerar lista campo Book [Trello #1262](https://trello.com/c/ffASkEyM)
- ActualizarMovimientos de ordenes. [Trello #1231](https://trello.com/c/JW8hPK6S)
- Funcion RelacionCuenta considerar lista los campos Sector y Moneda. **Critico** [Trello #1254](https://trello.com/c/rl2Jhzpv)
- ABMs: Validacion campos autocomplete + Plugins. [Trello #1250](https://trello.com/c/bqaUvzKw)
- Ajustes en la funcionalidad de control de excepciones PPL [Trello #1260](https://trello.com/c/2w1LHbqL)
- Fix: La funcion AFI debe ignorarse si el nro de columna es 0 o menos. [Trello #1258](https://trello.com/c/9joq566h)
- Feature: sintaxis de funcionalidad de Lock() (resta implementaci¾n de funcionalidad). [Trello #1227](https://trello.com/c/PWmZjFwR)

# 6.6.10
> Fecha: 17/11/2020 | Compilacion: 6.6.10.23690 | [Trello](https://trello.com/c/YmR5HnpR) {.is-info}

- Compatibilidad: Implementacion de la caracteristica de Refresco de V3. [Trello #1200](https://trello.com/c/YI7LvlPY)
- Compatibilidad: implementacion de RefrescoOps y refrescoAbms. [Trello #1196](https://trello.com/c/VsBJvP40)
- Fix: Conversion de Cotizaciones - TC en TIC [Trello #1238](https://trello.com/c/Espxcbth)
- Metodos para el manejo de campos datetime en ops **Critico** [Trello #1237](https://trello.com/c/Rd0VubpQ)
- Recalculo de ops con campos datetime + boton de confirmacion en control datetime **Critico** [Trello #1237](https://trello.com/c/Rd0VubpQ)
- Fix: cuando la mascara de un textfield es muy larga no se ven las opciones del dropdownlist. **Critico** [Trello #1153](https://trello.com/c/dvId3Agl)
- ABM's: evitar lanzar error de campo inexistente. (SIN EFECTO, SE HIZO ROLLBACK) [Trello #944](https://trello.com/c/EGHfpHZO)
- Fix: Error al abrir dia en TECO [Trello #1226](https://trello.com/c/kz9UNV1C)
- Nueva sigla para BIND. **Critico** [Trello #1164](https://trello.com/c/KiPJaiWB)
- Error campo Fecha en CrearListBox [Trello #1165](https://trello.com/c/7nQQZTmR)
- Fix: ventana de mensajes queda abierta al ejecutar eventos automaticos [Trello #1198](https://trello.com/c/ghLNCZld)
- Fix: cuadro de mensajes se muestra atras del splash en eventos automaticos de apertura [Trello #1198](https://trello.com/c/ghLNCZld)
- Implementacion de funciones IdxDateTime **Critico** [Trello #1173](https://trello.com/c/CXeKaRQP)
- Fix: ventanas de eventos/informes se mostraban atras del splash **Critico** [Trello #1199](https://trello.com/c/Fw3n1pk5)
- Fix: campos datetime en abms **Critico** [Trello #1173](https://trello.com/c/CXeKaRQP)
- Implementacion campos datetime en operaciones **Critico** [Trello #1173](https://trello.com/c/CXeKaRQP)
- Implementacion campos datetime en operaciones **Critico** [Trello #719](https://trello.com/c/FDraRAps)
- Funciones DetallePerfil() y DetalleItemPerfil() implementacion grupo 11 de canales de mensajes [Trello #1189](https://trello.com/c/5UskkbU7)
- Implementacion de Ranking Cotizaciones **Critico** [Trello #984](https://trello.com/c/S8gS3x8W)

# 6.6.9
> Fecha: 28/10/2020 | Compilacion: 6.6.9.26657 | [Trello](https://trello.com/c/s94xgZaN) {.is-info}

- Rollback: habilitacion de botones de pasar instancia en dialogo de visualizacion de op [Trello #1222](https://trello.com/c/qgFcPFPS)
- Fix: Transacciones, Orden , MinutaBolsa, Eventuales , permiso de todas transacciones cuando ninguna esta tildada en permisos. **Critico** [Trello #1218](https://trello.com/c/hQExmGWb)
- Fix: Permiso en carga de op y tr con todas destildadas en el perfil. **Critico** [Trello #1213](https://trello.com/c/fVV7bdtd)
- Compatibilidad: Los botones de mover instancia del dialogo de visualizacion de operaciones ahora se habilita usando el mismo criterio que en la grilla de instancia [Trello #1214](https://trello.com/c/Ha8DmlkN)

# 6.6.8
> Fecha: 23/10/2020 | Compilacion: 6.6.8.19233 | [Trello](https://trello.com/c/RmuZhA41) {.is-info}

- Fix: error en control de permiso especial EX20 al pasar de instancia. **Critico** [Trello #1212](https://trello.com/c/n4mPvsIh)
- Fix: permisos de acciones en op y tr desde grilla. **Critico** [Trello #1208](https://trello.com/c/EF1xVJaF)
- Fix: reglas de validacion con permisos especiales. **Critico** [Trello #1206](https://trello.com/c/P550uwJO)
- Fix: error en EjecutarEvento2(), no encuentra el archivo PPL.NET.Subprocess.exe. [Trello #1204](https://trello.com/c/gsmiznNz)
- Fix: permite cargar op y tr con el dia cerrado. [Trello #1201](https://trello.com/c/F24SbVtP)
- Fix: Error al ejecutar eventos automaticos al abrir dia. [Trello #1194](https://trello.com/c/zNVozzTP)
- Abm de perfiles: ajuste layout de control de mensajes [Trello #1129](https://trello.com/c/iDfiCdNq)
- Compatibilidad: en las funciones ActualizarMovimientos, la variable PPL INSTANCIA siempre vale 0 para CARGILL. [Trello #1181](https://trello.com/c/m5YnipqN)
- Implementacion de funciones de PPLRC para configurar HardLimit y OrderBy en grillas de operaciones eventuales [Trello #1187](https://trello.com/c/fr0hvuQK)
- Fix: Si a un radio se le setea un valor negativo siempre debe valer -1 y no seleccionar ninguna de las opciones. **Critico** [Trello #1183](https://trello.com/c/npFYs5ml)
- Fix: Funciones HardLimitInstanciaOp no soportaba limite mayor a un Int16 [Trello #1184](https://trello.com/c/Ykc0u0wd)
- Fix: No termina la ejecucion del script al Terminar el proceso desde la ventana de procesos. [Trello #1177](https://trello.com/c/cyRTD8a6)
- Feature: Posibilidad de habilitar el logueo de los mensajes de la consola de CEF. [Trello #1156](https://trello.com/c/7fhUvQOl)
- Feature: Ahora se pueden copiar (ctrl+c) hasta 10 mil filas de un reporte y pegarlas (ctrl+v) en excel. [Trello #1178](https://trello.com/c/f6z5heDl)
- Fix: Buscador de grillas, error al buscar valores con formatos numericos y de fecha [Trello #1175](https://trello.com/c/RaP9DouI)
- Fix: la super grilla no aplicaba formatos numericos ni de fecha [Trello #1175](https://trello.com/c/RaP9DouI)
- Fix: En super grilla, daba error en el buscador al seleccionar TODAS las columnas + Fix: mostraba un item en blanco en el combo de columnas  [Trello #1174](https://trello.com/c/CyH5Bliz)
- PPLRC: implementacion de funciones para configurar HardLimit y OrderBy en grillas de instancias. [Trello #1167](https://trello.com/c/9gIbsIqI)
- Carta: al completar tablas ignora el borde superior de la fila de formato de ejemplo [Trello #1172](https://trello.com/c/xNQNCJUr)
- Cartas: se actualizan las variables definidas en el encabezado y pie de pagina del template. [Trello #1171](https://trello.com/c/QvRqCxRk)
- Fix: Error al ejecutar en el recalculo de un campo al depender de la seccion estrategias en una instancia distinta de 0. [Trello #1161](https://trello.com/c/lfAGuIMv)
- Fix: Oracle, en las grillas de operaciones se seteaba mal el limite de registros (rownum <=) [Trello #1148](https://trello.com/c/1xN8cE6k)
- Fix: Error en abms, la grilla no respetaba los formatos numericos definidos en el script. [Trello #1055](https://trello.com/c/EdTNbs7a)

# 6.6.7
> Fecha: 18/09/2020 | Compilacion: 6.6.7.29491 | [Trello](https://trello.com/c/FUhOlRmM) {.is-info}

- Fix: error en grillas tipo listas cuando una columna tipo STRING tiene como valor null. [Trello #1144](https://trello.com/c/axuGY34f)
- Fix: las mascaras del tipo XXXX en los campos string son para admitir caracteres alfanumericos. [Trello #1145](https://trello.com/c/r4N5zTbA)

# 6.6.6
> Fecha: 14/09/2020 | Compilacion: 6.6.6.28816 | [Trello](https://trello.com/c/BSHByfYJ) {.is-info}

- fix: al levantar los datos de una columna tipo CHAR con un seccion de tipo LISTA. **Critico** [Trello #1132](https://trello.com/c/EqRCeh5Z)
- Log de los queries de grillas en PPLStudio y en Portfolio modo debug [Trello #1147](https://trello.com/c/G6ahDLeU)
- Flags especificos para habilitar Ordenes, MinutasBolsa o OpMinoristas segun sigla [Trello #1140](https://trello.com/c/a5Zs4pMl)
- Titulo dialogo de Ops Eventuales [Trello #1126](https://trello.com/c/WVAMgHNi)

# 6.6.5
> Fecha: 26/08/2020 | Compilacion: 6.6.5.31367 | [Trello](https://trello.com/c/5LFWoOb9) {.is-info}

- Fix: grillas de instancia cero no debe chequear permisos relacionados a la instancia + Fix menu oculto. **Critico** [Trello #1137](https://trello.com/c/ek7oXCzC)
- Fix: al ingresar valor numerico negativo en ListBox de Eventos [Trello #1135](https://trello.com/c/VjlTJIE5)
- Fix: los campos tipo lista no estan devolviendo su valor de forma correcta. **Critico** [Trello #1133](https://trello.com/c/vKTexf4q)
- Fix: por default no se podian copiar mas de 1000 filas de un informe para poder pegarlas en excel. [Trello #1125](https://trello.com/c/42XoCHgi)
- Fix: en oracle, el query de la super grilla debe aplicar el OrderBy y despues el limite de registros [Trello #1111](https://trello.com/c/06v5HoJj)
- Fix: Abm, campos autocomplete_arlist_chk no debe trimmear los items de la lista al cargar el dialogo [Trello #1123](https://trello.com/c/oTUhK0tf)
- Cargill: Valida licencias por HASP Virtual [Trello #1117](https://trello.com/c/jdSVHY8b)
- Implementacion de sigla STD_CORP [Trello #1089](https://trello.com/c/8AguAjje)
- Implementacion de las funciones DurationEspecie y Power. [Trello #1112](https://trello.com/c/FVcuuZhU)
- Fix: al tener un campo label en una seccion campos de una instancia, al avanzar o retroceder, da error de que el no existe en la tabla. [Trello #1104](https://trello.com/c/orismws0)
- Fix: los radios no estan disparando recalculos cuando se setea su valor cuando se edita un campo de los que depende. [Trello #1103](https://trello.com/c/16qvyUuE)
- Fix: cuando los radios recibian null value daba object reference. [Trello #1101](https://trello.com/c/ussax1Nu)
- Fix: error al parsear PrecioCotizacionDeterminada de CotizacionNIIF de Galicia [Trello #1098](https://trello.com/c/NBLHjU72)
- SuperGrilla: parametrizar por PPLRC el OrderBy y el HardLimit [Trello #1091](https://trello.com/c/qUMtwXrO)
- Fix: Cuando se ejecuta emitircartavisible y el informe tiene HojaVisible en NO, el informe no es agregado a ultimas acciones. [Trello #1088](https://trello.com/c/vUwRpozv)

# 6.6.4
> Fecha: 17/07/2020 | Compilacion: 6.6.4.29922 | [Trello](https://trello.com/c/Tq8nCczP) {.is-info}

- Fix: error de formato al persistir un valor de tipo decimal en GenerarAsientoOp (Oracle) [Trello #1085](https://trello.com/c/jTivgWew)
- Mensajes: soporte Oracle y Cargill [Trello #1047](https://trello.com/c/hH6WWpZ6)
- Fix: Al visualizar una operacion los botones de mover instancia no tenian en cuenta los permisos del perfil [Trello #1084](https://trello.com/c/YGzDTBs5)
- Fix: abm campo autocomplete_arlist_chk no completaba con espacios correctamente. [Trello #1069](https://trello.com/c/D8FvhJcY)
- Abm: campos autocomplete_arlist_chk calcula tama├▒o de item [Trello #1069](https://trello.com/c/D8FvhJcY)
- Contabilidad: campo SubLedger se debe evaluar [Trello #1073](https://trello.com/c/VnDVb3E7)
- Fix: error en la llamada a Fecha(FSys). [Trello #1082](https://trello.com/c/CQ88pZjP)

# 6.6.3
> Fecha: 25/06/2020 | Compilacion: 6.6.3.29217 | [Trello](https://trello.com/c/bSJ9N1gY) {.is-info}

- Implementacion de las caracteristicas de seguridad de CARGILL en FPA.Console. [Trello #1076](https://trello.com/c/xeOxbOpK)
- Fix: Error al persistir un valor decimal en un item de asiento contable [Trello #1070](https://trello.com/c/A5el46eT)
- Fix: la password de la conexion a la db se esta encriptando en GALICIA. [Trello #1074](https://trello.com/c/axvmszNc)
- Fix: para GALICIA la variable INSTANCIA debe valer 1 al crear una op,tr,or,etc. [Trello #1067](https://trello.com/c/2kcnUWfz)
- Fix: Abm, campos autocomplete_arlist_chk no funcionaba correctamente el lookup [Trello #1063](https://trello.com/c/aySRCObD)
- Se agrego grupo 9 (TipoTransacciones) y 10 (TipoOrdenes) a la funcion DetallePerfil() [Trello #1065](https://trello.com/c/VkIRSPaT)

# 6.6.2
> Fecha: 02/06/2020 | Compilacion: 6.6.2.22524 | [Trello](https://trello.com/c/QwAmsckK) {.is-info}

- Fix: En el path donde se genera el pdf de salida se esta generar un archivo de mas (source.html). [Trello #1064](https://trello.com/c/QdOSGzT2)
- Fix: para CARGILL el PPLStudio debe respetar el mismo esquema de seguridad que el Portfolio. [Trello #1062](https://trello.com/c/q4PbjPrn)
- Fix: error de alineado al exportar a pdf. [Trello #1059](https://trello.com/c/UnC2v3aO)
- Fix: implementacion de ExportarPdfLite(). [Trello #1060](https://trello.com/c/wAkIWACV)
- Emitir carta: tablas dinamicas + fix celdas combinadas y archivos bloqueados [Trello #1058](https://trello.com/c/ONHbXoiC)
- Fix: Al cambiar o seleccionar el mismo nrop en un campo OPREF, siempre deben dispararse los recalculos. [Trello #1051](https://trello.com/c/COvKwHTe)
- Nuevo parametro IntraUnit en funcion RelacionCuenta() [Trello #1057](https://trello.com/c/CHgDRmcf)
- Funciones nuevas para manejo de archivos [Trello #1050](https://trello.com/c/W6zEdpoX)
- Feature: implementacion de los controles tipo FilePath y DirectoryPath. [Trello #1050](https://trello.com/c/W6zEdpoX)
- Modelos de asiento: campos Subledger, TipoSubledger y TipoCC deben ser fijos y definirse antes que los variables [Trello #1049](https://trello.com/c/HoH7oXsD)
- Fix: Implementacion de SetPrintFit(1). [Trello #1010](https://trello.com/c/9s1QYJrQ)
- Features de cartas. Implementacion de funcion AbrirDocumento() y EmitirCartaVisible() [Trello #1044](https://trello.com/c/lzfNvDaI)
- Fix: al mostrar el valor de un checkbox en un campo texto, muestra False o True en vez de 1 o 0. [Trello #1046](https://trello.com/c/e0Z9l77T)
- Nuevos campos a tener en cuenta para items de modelos asientos [Trello #1041](https://trello.com/c/PMxq6rqH)
- Opcion de mostrar TipoOp y NrOperacion en la cabecera del dialogo segun preferencia de usuario (aplica tambien a Ordenes, Transacciones, OpMinoristas y MinutasBolsa) [Trello #1045](https://trello.com/c/wfedwbQu)
- Opcion de copiar captura de ventana en Operaciones [Trello #1045](https://trello.com/c/wfedwbQu)
- Fix: cuando se concatena un campo CB con un string, en operaciones, pone como valor string un false o true en vez de 0 o 1. [Trello #1042](https://trello.com/c/3PaUCNFy)
- Fix: La funcion EsTerminal devuelve un default distinto en Operaciones que en Informes y Eventos [Trello #1033](https://trello.com/c/Y3Jx8CsR)
- Fix: Las celdas numericas en los listbox de interprete no borraban las comas al editar su valor como lo hacen los campos de los dialogos. [Trello #1037](https://trello.com/c/vvtmnHkP)

# 6.6.1
> Fecha: 24/04/2020 | Compilacion: 6.6.1.27257 | [Trello](https://trello.com/c/YfSYUgMY) {.is-info}

- Se agrega la constante TIPOSESTRATEGIA para Operaciones [Trello #1022](https://trello.com/c/qQfxGJ1Z)
- Fix: la variable INSTANCIA debe valer 0 en el alta de Ordenes, Transacciones y Minutas bolsa [Trello #1012](https://trello.com/c/t3ZISeZq)
- Cargill: menu de transacciones con ordenes y minutas bolsa [Trello #1007](https://trello.com/c/Oak5pInf)
- Ajustes de seguridad para facilitar el uso del launcher con todas las instalaciones. [Trello #1011](https://trello.com/c/FYDfGuIW)
- Fix: crearListBox - En los campos de tipo fecha, la ventana que se abre al darle doble click, no se esta visualizando correctamente. [Trello #1008](https://trello.com/c/lx4JuH6k)
- Fix: soporte de mascaras para passwords en campos del dialogo de eventos e informes. [Trello #1004](https://trello.com/c/x05CaPgO)
- Fix: mejor logueo de ejecucion de eventos por consola. [Trello #1001](https://trello.com/c/QC244axZ)
- Fix: la opcion Agregar similar de abms no estaba cargando los valores de los embebeidos. [Trello #847](https://trello.com/c/EORwqK8o)
- Fix: no se deben eliminar los espacios que tienen los strings en las celdas ACT cuando se renderizan. [Trello #952](https://trello.com/c/qclblDFZ)
- Fix: correccion de blanqueo de celda en listbox cuando un recalculo devuelve null. [Trello #1000](https://trello.com/c/aK2c5jdS)
- Implementacion de esquema de seguridad personalizado para CARGILL. [Trello #1003](https://trello.com/c/k1aCgqcW)
- Cotizacion por moneda debe estar activado por default para STD y BYMA y la cantidad de dias debe ser 2 [Trello #1002](https://trello.com/c/GQplVd0W)
- Para Cargill la password no debe ser case sensitive (siempre uppercase) [Trello #996](https://trello.com/c/QS8EEo3X)
- Abm: implementacion de parametro Order/Group by para campos autocomplete [Trello #864](https://trello.com/c/VKIGjpvQ)
- Fix: funcion IdxDate sumaba un dia cuando se le pasaba una fecha con hora pm [Trello #972](https://trello.com/c/PPBqdura)
- Fix: error en funciones xml.cargararchivo y xml.fbn. [Trello #993](https://trello.com/c/MBGa6BOP)
- SuperGrid: Filtro default de ultimos 30 dias. [Trello #1030](https://trello.com/c/uC51CLDJ)
- Fix: en cargill, cuando el resultado de un recalculo en una celda de un listbox es null, debe blanquear la celda. [Trello #980](https://trello.com/c/UPCgvEkp)
- Fix: al utilizar ACT con una fecha con hora incluida, debe utilizarse un formato especifico por default. [Trello #977](https://trello.com/c/jRpeWCXp)
- Fix: si se tiene valor -1 en la celda de una columna combo en listbox, no debe dar error, debe mostrar vacio. [Trello #959](https://trello.com/c/qR9oCfRO)
- Fix: los listbox en eventos no validaban correctamente el valor de una celda. [Trello #923](https://trello.com/c/k7xBX3b7)
- Fix: al utilizar la funcion ExportarXLS, las celdas numericas no muestran todos los decimales que el valor posee. [Trello #899](https://trello.com/c/NNZ1gRwT)
- Fix: no se parseaban correctamente los scripts de perfiles con saltos de linea y comentarios [Trello #968](https://trello.com/c/A8rAq5XG)
- Fix: AvanzarOperacion() cuando la instancia origen no esta definida en el script [Trello #970](https://trello.com/c/KDuU7p0J)
- Fix: en los campos text y lookup no recalcula la lista de opciones al cambiar un valor de un campo del cual depende. [Trello #966](https://trello.com/c/BArRtaxj)
- Fix: error al exportar a pdf un informe que tiene graficos. [Trello #982](https://trello.com/c/NUIqrVrI)
- Implementacion de Filtros en informes. [Trello #856](https://trello.com/c/U0NDYYnj)
- Fix/refactor: funcion LimTotalizado4() [Trello #958](https://trello.com/c/13wSolYO)
- Fix: cuando se usa un Recorrer con FAC dentro de un RecorrerSQL, se debe actualizar el FAC del recorrer en cada iteracion del RecorrerSql. [Trello #898](https://trello.com/c/dE7bHnJf)
- Fix: bug param. CallPut de Movimientos [Trello #961](https://trello.com/c/I2ByrMKi)
- Implementacion RecorrerXML. [Trello #930](https://trello.com/c/dDoNpB1K)
- Refactor: limpieza de recursos no necesarios. [Trello #910](https://trello.com/c/b6xykS5R)
- Consolidaci¾n de recursos CSS y JS. [Trello #910](https://trello.com/c/b6xykS5R)
- Implementacion de funcion PrecioPromedio() para CARGILL [Trello #866](https://trello.com/c/eJ5vMOGR)
- Fix: para CARGILL la funcion FBN() no debe trimmear valores de campos tipo VARCHAR [Trello #954](https://trello.com/c/c9fLJKFo)
- Fix: condicion de seccion REFERENCIA [Trello #960](https://trello.com/c/Dan0S0Cv)
- No funcionaba la funcion Padre() en operaciones [Trello #955](https://trello.com/c/vEiVEdpz)
- Implementacion de la Sigla BYMA. [Trello #925](https://trello.com/c/cnhOnlF6)
- Para Cargill se deben generar los movimientos definidos en una instancia aunque no haya dialogo [Trello #933](https://trello.com/c/0IGgVqyd)
- Cargill: formato especial para AlterSession y DateTime To String [Trello #908](https://trello.com/c/ZTt1uE4F)
- Implementacion de la funcion DesciendedeTipoEstrategia. [Trello #947](https://trello.com/c/1NL0fcvX)
- Se quita la validacion por vehiculo en la funcion GenerarAsientoOp() [Trello #931](https://trello.com/c/2KRz1fRw)
- Fix: en informes no centraba el texto cuando el ancho de columna es mas chico [Trello #873](https://trello.com/c/XlnephZD)
- Upgrade CefSharp 49 -> 79 [Trello #928](https://trello.com/c/gTWUBWSA)
- Fix: implementacion de mascaras V3 en controles text de V6 de eventos e informes. [Trello #895](https://trello.com/c/ez8fFqNH)
- Implementacion de seccion ESTRATEGIAS para Cargill. [Trello #866](https://trello.com/c/eJ5vMOGR)
- Implementacion de la funcion ACLV. [Trello #901](https://trello.com/c/izMr0Yzz)
- Fix: error en OrdenarFilas cuando pasaban por parametro ordenar por una columna que todavia no habia sido agregada a la grilla. [Trello #884](https://trello.com/c/niDNV5AV)
- Upgrade .NET Framework 4.6.1 [Trello #910](https://trello.com/c/b6xykS5R)
- Las funciones PPL Require e Import deben lanzar error si reciben parametros invalidos [Trello #728](https://trello.com/c/0b54aFdO)
- Implementacion de funcion PPL GetDataBase() [Trello #902](https://trello.com/c/IAmaE6Lu)
- Fix: la hoja del excel creado con ExportarXls debe tener el mismo nombre del archivo. [Trello #907](https://trello.com/c/bf6UNLIo)
- Implementacion de la seccion POSTEDICIONBAJA. [Trello #882](https://trello.com/c/1clgORhC)
- Funcion GenerarAsientoOp() soporte de lista de vehiculos en modelos de asiento [Trello #883](https://trello.com/c/PATD2iiE)
- Fix: interprete, algunos colores no se parseaban correctamente [Trello #880](https://trello.com/c/efYwc80g)
- Fix: funciones DesciendeDe...() cuando se ingresan valores validos iguales [Trello #886](https://trello.com/c/uemkWns8)
- Ajustes varios especificos por compatibilidad para Cargill. [Trello #866](https://trello.com/c/eJ5vMOGR)
- Fix: la implementacion de CRO en PPLStudio no funcionaba correctamente. [Trello #850](https://trello.com/c/FPnbXJpl)
- Implementacion de funciones CotizacionNIIF() y ValuacionNIIF() utilizando la libreria RankeadorNIIF. [Trello #835](https://trello.com/c/hHhpU9zv)
- Mostrar nombre de entorno en StatusBar [Trello #842](https://trello.com/c/q7OuWfoi)
- Mensajes: ajustes varios y features nuevos [#1031](https://trello.com/c/diAowp7a)
- Implementacion de dialogo de preferencias de usuario. [Trello #738](https://trello.com/c/7AitDJUu)
- Abm: soporte campos identity [Trello #839](https://trello.com/c/RlhT60IJ)
- Fix: PPL.NET.Subprocess.exe algunas veces queda vivo causando el error de 'All pipes are busy'. [Trello #838](https://trello.com/c/mjulWKUa)
- Fix: bugs en agregarsimilar de ABMs. [Trello #818](https://trello.com/c/Nsxa2Wv2)
- Fix: los asientos contables, al generarse, estan contemplando la hora en las fechas y no deben hacerlo. [Trello #809](https://trello.com/c/RquiQeAG)
- Fix: no se estaban seteando las variables ABM y ESINICIO. [Trello #771](https://trello.com/c/zAW2Q0oV)
- Nuevos features de Carga Rapida [Trello #768](https://trello.com/c/uozT2jXR)
- Implementacion de la opcion 'Agregar similar' en grillas de instancia, supergrilla y Abms. [Trello #732](https://trello.com/c/pFWhmkOj)
- Ajustes varios de dise±o en Portfolio y PPLStudio. (Logo, Splash, Iconos, Login, About, etc.) [Trello #708](https://trello.com/c/05h465u7)

# 6.5.143 
> [Trello](https://trello.com/c/KRjt7Tsb) {.is-info}

- Fix: soporte de mascaras para passwords en campos del dialogo de eventos e informes. [Trello #1004](https://trello.com/c/x05CaPgO)
- Fix: Ajustes de cambios en Consola para TECO con seguridad integrada. [Trello #985](https://trello.com/c/DaOHVvvh)
- Fix: mejor logueo de ejecucion de eventos por consola. [Trello #1001](https://trello.com/c/QC244axZ)
- Fix: implementacion setprinfit(1). [Trello #919](https://trello.com/c/141QforZ)
- Feature: Las mascaras enteras definidas para controles numericos por pplrc afectan al tama├▒o del control. [Trello #971](https://trello.com/c/OwViXstW)
- Fix: Al utilizar la funcion GRILLAVISIBLE(NO) en un informe, los espacios en blanco de las celdas son borrados. [Trello #952](https://trello.com/c/qclblDFZ)
- Fix: En Operaciones, cuando un control es del tipo RADIO, no muestra la bandera con el error de la validacion del campo. [Trello #994](https://trello.com/c/ZPrBjwmb)
- Fix: Al tener 2 columnas en un listbox, una numerica y la otra texto, una vez que ingreso numeros en la numerica no me deja ingresar texto en la que es de texto. [Trello #992](https://trello.com/c/m6GSuGMy)
- Fix: error al recalcular columna tipo COMBO dependiente de otra. [Trello #981](https://trello.com/c/Y7Wvz6xs)
- Fix: no estaba desarrollada la funcion HOY para Operaciones. [Trello #974](https://trello.com/c/oKag9yUO)
- Fix: los campos COMBO o RADIO no estan seteando bien su valor cuando reciben null. **Critico** [Trello #973](https://trello.com/c/6MaHzIuf)
- Fix: Error de parse en operaciones cuando hay una seccion de MOVIMIENTOS vacia [Trello #965](https://trello.com/c/eEXa2gPd)
- Fix: Ahora el tama±o de los controles son configurables por pplrc limitando su input. [Trello #964](https://trello.com/c/DTV86wCY)
- Fix: En operaciones los campos no toman el recalculo de la lista COMISIONES2 en un totalizador (funcion SUM). [Trello #962](https://trello.com/c/6JfykGac)
- Fix: Condicion de seccion REFERENCIA [Trello #960](https://trello.com/c/Dan0S0Cv)
- Implementacion: Nueva funcion COMCORREDOR2. [Trello #951](https://trello.com/c/oeRPGB3Y)
- Fix: al exportar a excel desde el boton del contenedor del informe, la hoja de calculo no tiene el nombre del archivo. [Trello #949](https://trello.com/c/KRO2bh0y)
- Fix: Error al verificar permisos sobre un TipoTr en ISBAN [Trello #948](https://trello.com/c/LaHEwh78)
- Implementacion de compilacion condicional PPL [Trello #894](https://trello.com/c/4hYs8C8E)
- Fix: FPA.Console no debe validar si el usuario tiene o no permisos para ejecutar un evento. Esto aplica solo para TECO por el momento. [Trello #919](https://trello.com/c/141QforZ)

# 6.5.142 
> [Trello](https://trello.com/c/YOvCPZu7) {.is-info}

- Fix: no se deben recalcular los campos si el dialogo no se muestra en el avance o retroceso de una op. [Trello #932](https://trello.com/c/k6EAzE8Q)
- Fix: FPA Console no permite correr -F y -H a la vez. [Trello #922](https://trello.com/c/H95pc4w1)

# 6.5.141 
> [Trello](https://trello.com/c/AlYTNARG) {.is-info}

- Rollback: implementacion de compatibilidad para setprintfit(1) y setprintfit(2) (Issue 909). [Trello #920](https://trello.com/c/8YpvjP6T)

# 6.5.140 
> [Trello](https://trello.com/c/XbhLONbD) {.is-info}

- Fix: La password ingresada en la consola, debe encriptarse igual que en el cliente. [Trello #914](https://trello.com/c/CDlDpXrA)
- Fix: Implementacion de compatibilidad para setprintfit(1) y setprintfit(2). [Trello #909](https://trello.com/c/V11p9VRm)
- Fix: al avanzar o retroceder la op se deben recalcular los campos, si y solo si el dialogo es mostrado. [Trello #912](https://trello.com/c/KcAc3f1w)
- Fix: la hoja del excel creada con ExportarXls debe tener el mismo nombre del archivo. [Trello #907](https://trello.com/c/bf6UNLIo)
- Fix: Ajustes por issues surgidos en ISBAN relacionados a los permisos en los Tipos de Transaccion [Trello #881](https://trello.com/c/GIbvnXgn)
- Fix: error al loguearse al PPLStudio en TECO. [Trello #900](https://trello.com/c/mJ17CU7c)
- Fix: FPA.Console no limpiaba directorio de scripts temporales y no ejecutaba PPLRC [Trello #893](https://trello.com/c/tgy9pDQ0)

# 6.5.139 
> [Trello](https://trello.com/c/hojur2J9) {.is-info}

- El script que se encarga correr los eventos automaticos no debe generar log [Trello #890](https://trello.com/c/aX6gQXXb)
- Ajustes de seguridad y autenticacion por Active Directory para TECO [Trello #767](https://trello.com/c/cTFyNXDi)
- Fix: ProximoArchivo no debe dar error si no existen archivos. [Trello #887](https://trello.com/c/foKiJL0k)
- Fix: func PrimerArchivo() daba error cuando el directorio no existe [Trello #887](https://trello.com/c/foKiJL0k)
- Fix: FPA.Console error al abrir dia [Trello #885](https://trello.com/c/Fa6jMRwS)
- Fix: Abms embebidos en Oracle [Trello #877](https://trello.com/c/AOn8mdeq)
- Fix: Abm Embebidos error al abrir dialogo en modal en el Cliente [Trello #878](https://trello.com/c/8EcmoUia)
- Implementacion de FPA.Console [Trello #879](https://trello.com/c/AuzMR2LQ)
- Autenticacion por credenciales en archivos (FPA.Credentials) [Trello #786](https://trello.com/c/r8RjupWq)
- Implementacion de Format String y comentarios multilinea en interprete [Trello #876](https://trello.com/c/myE1R8rw)
- Fix: Abms embebidos, la grilla no tomaba correctamente la mascara default para campos numericos [Trello #868](https://trello.com/c/17Waie4q)
- Fix: Abms embebidos, la regla validates_uniqueness no funcionaba correctamente al editar m├ís de un registro [Trello #868](https://trello.com/c/17Waie4q)

# 6.5.138 
> [Trello](https://trello.com/c/OrsD23Xs) {.is-info}

- ABM: Refactor de embebidos, implementacion de seccion fkey [Trello #855](https://trello.com/c/Rd0NmXLm)
- Fix: validate_uniqueness en abms embebidos [Trello #858](https://trello.com/c/GBb0ojrh)
- Fix: formato de celdas datetime y numeric en grilla de abms embebidos [Trello #858](https://trello.com/c/GBb0ojrh)
- Fix: excepcion al editar valor del lookup de los campos listatabla si se utilizaba como separador de campos una coma. [Trello #853](https://trello.com/c/dpdygx0I)
- Fix: ABM, el helper validates_uniqueness_of_set no funcionaba correctamente [Trello #848](https://trello.com/c/bzSYxyCF)
- Fix: las formulas no soportan comentarios. [Trello #844](https://trello.com/c/FNhWppyA)
- Mostrar nombre de entorno en StatusBar [Trello #842](https://trello.com/c/q7OuWfoi)
- Fix: PPL.NET.Subprocess.exe algunas veces queda vivo causando el error de 'All pipes are busy'. [Trello #838](https://trello.com/c/mjulWKUa)

# 6.5.137 
> [Trello](https://trello.com/c/Jzp0Rnce) {.is-info}

- Fix: el orden de la solapa partida debe ser por los campos FechaDesde y NrOperacion. [Trello #834](https://trello.com/c/8CN5aY9L)
- Fix: IdxDateTime() habia casos donde sumaba un dia cuando la hora era posterior a las 12 [Trello #833](https://trello.com/c/6k8JLTny)
- Fix: Ajustes LOGINFORMES, variable NOLOGUEAR + Escapa de comilla simple en campo 'Datos' + Utilizar fecha de base de datos [Trello #827](https://trello.com/c/Xjzs2NhX)
- Fix: PPLStudio, error al actualizar un reporte en modo debug [Trello #829](https://trello.com/c/cWul2HuT)
- Fix: la referencia de la op en la tabla PARTIDAS debe guardarse en el campo NrPartida. [Trello #828](https://trello.com/c/EJ2I0SWq)
- Performance: Mejora de performance en el query que devuelve el ultimo mensaje recibido por SocketPPL.Recibir(). [Trello #826](https://trello.com/c/vseRguSQ)

# 6.5.136 
> [Trello](https://trello.com/c/TR9rNC1g) {.is-info}

- Fix: al exportar a pdf cuadno se tiene un marco sobre la primer fila, el borde superior no es visible. [Trello #801](https://trello.com/c/r3cuFgLA)
- Fix: SendMail() habia parametros que daban error si no se especificaban. Implementacion tag en config para especificar puerto y ssl [Trello #820](https://trello.com/c/xuUY2AvY)
- implementacion de la seccion lista PARTIDAS. [Trello #817](https://trello.com/c/YMcLTs6I)
- Fix: Habia un error al intentar logear la ejecucion de PPLRC [Trello #815](https://trello.com/c/Mq2R3OS1)
- Fix: PPLStudio, error al sincronizar scripts cuando no existen las tablas TIPOSOPERACIONMIN o TIPOSMINUTABOLSA. [Trello #814](https://trello.com/c/k9Z0UgTD)

# 6.5.135 
> [Trello](https://trello.com/c/FOzytq35) {.is-info}

- Fix: los asientos contables, al generarse, estan contemplando la hora en las fechas y no deben hacerlo. **Critico** [Trello #809](https://trello.com/c/RquiQeAG)
- Fix: las grillas no se estan inicializando correctamente cuando abrimos una op en edicion o en modo vista. [Trello #808](https://trello.com/c/pYcO5R5B)
- Compatibilidad: la funcion MontoGastos no tiene todos los parametros que tiene V3. [Trello #796](https://trello.com/c/RR2Wo9Rq)

# 6.5.134 
> [Trello](https://trello.com/c/0AfCsuTS) {.is-info}

- Fix: en eventos e informes, los campos numericos no varian su tama├▒o en base a la mascara. [Trello #791](https://trello.com/c/r7iwOnIL)
- Fix: los campos virtuales de listas no toman la fdefault. [Trello #806](https://trello.com/c/oBcEqQt3)
- Feature: Ahora se puede establecer por PPLRC si se agregan o no por default el nro de pagina y la fecha hora en la impresion de reportes. [Trello #790](https://trello.com/c/J7sMyt5k)
- Fix: Implementacion de EQSTRLI y correccion de EQSTRL en operaciones. [Trello #802](https://trello.com/c/7J7WPUIJ)
- Fix: en los campos tipo radio no se soportaba la asignacion del valor -1. [Trello #795](https://trello.com/c/lOw5qZZP)

# 6.5.133 
> [Trello](https://trello.com/c/fEI28lLE) {.is-info}

- Fix: al agregar el logo a un informe, se agradaba la celda que lo contenia, haciendo que todo lo que se escribia al lado se vea mucho mas abajo. [Trello #789](https://trello.com/c/XLqUkBJv)
- Implementacion de la funcion AFI. [Trello #788](https://trello.com/c/RCocxULg)
- Fix: al usar la funcion exportar a excel desde el contenedor de informes, se agrega una fila de mas al ppio. [Trello #783](https://trello.com/c/1MqUNdIy)
- Implementacion de la funcion EqstrLI. [Trello #781](https://trello.com/c/9TdbJUcv)
- Fix: error en TECO cuando abren un ABM que tiene una columna Datetime. [Trello #778](https://trello.com/c/7BYRR7Nk)
- Implementacion de columnas virtuales en secciones del tipo LISTA. [Trello #772](https://trello.com/c/Qr7tlTlF)
- Tag report_numeric_pyc del config para forzar cultura numerica en los reportes. [Trello #774](https://trello.com/c/BFy6aXlX)
- Fix: Bug en las celdas que linkean op,tr,etc cuando el informe esta paginado. [Trello #769](https://trello.com/c/MXqXBlhg)
- Fix: HASP, al llegar el limite de conexiones, el proceso no finalizaba correctamente [Trello #766](https://trello.com/c/O0m5tH6n)
- Fix: SQLEditor no permitia agrandar las columnas, no se veia la scrollbar horizontal de la grilla de resultados, ni tampoco permitia agrandar las dimensiones de la misma. [Trello #763](https://trello.com/c/2ESLn34q)

# 6.5.132 
> [Trello](https://trello.com/c/HifbNzvy) {.is-info}

- Implementacion de funcion ppl CerrarAplicacion() [Trello #756](https://trello.com/c/PEzHO5wx)
- Implementacion de funcion ppl Sigla() [Trello #756](https://trello.com/c/PEzHO5wx)
- Fix: Habia casos donde no se desconectaba HASP correctamente [Trello #756](https://trello.com/c/PEzHO5wx)
- Se agrego data de HASP en SessionInfo [Trello #756](https://trello.com/c/PEzHO5wx)
- Hasp se activa unicamente por sigla [Trello #756](https://trello.com/c/PEzHO5wx)

# 6.5.131 
> [Trello](https://trello.com/c/rT4zu5xc) {.is-info}

- Implementacion de la seccion CUOTASMTM. [Trello #753](https://trello.com/c/TyUvnEr1)
- Implementacion de funcion EscribirCampo(). [Trello #755](https://trello.com/c/SC8KOnup)
- Fix: Algunos mensajes de error durante la inicializacion se ven detras del splash [Trello #751](https://trello.com/c/i2YTZiVQ)

# 6.5.130 
> [Trello](https://trello.com/c/HONrnMM4) {.is-info}

- Fix: error cuando se ejecutaba desde el cliente de V5 un informe que no tenia dialogo. [Trello #730](https://trello.com/c/rWdapZcq)
- Fix:si se hace un ACT de un FBN numerico y luego se lo muestra por un listbox en un evento, la columna del listbox no aplica correctamente la mascara. [Trello #729](https://trello.com/c/kCyecXxc)
- Implementacion de un nuevo parametro (UDN) en la funcion RelacionCuenta. [Trello #725](https://trello.com/c/PcffSMLK)
- Fix: valida el control numerico unicamente si doy tab. [Trello #720](https://trello.com/c/qyQVfm0H)

# 6.5.129 
> [Trello](https://trello.com/c/MGNRb7xQ) {.is-info}

- Implementacion de series en graficos. [Trello #701](https://trello.com/c/Ulalr1LC)
- Implementacion de campos/controles DateTime (con hora incluida) y funcion IdxDateTime() [Trello #716](https://trello.com/c/Wx4neIJP)
- Implementacion de esquemas de CRO por PPLRC. [Trello #628](https://trello.com/c/lBb0x8Ud)
- Fix: Al abrir una op que tiene un radio, que en la base el radio vale null, da error. [Trello #712](https://trello.com/c/bmiJqktx)
- PPLStudio: Opcion FullScript para eventos e informes [Trello #705](https://trello.com/c/Mo9G4XxT)
- Fix: al editar una orden con ejecuciones y que la condicion de la seccion Ejecucion es false, borra las ejecuciones al dar ok. [Trello #709](https://trello.com/c/eFBxRFoF)

# 6.5.128 
> [Trello](https://trello.com/c/wrfi94on) {.is-info}

- Fix: Error GENDEVENGADOS al eliminar una operacion cuando no existe la tabla [Trello #707](https://trello.com/c/BTQUsr4W)
- Fix: agrego mas info de debug en los errores emitidos en los campos debido a un valor de tipo incorrecto. [Trello #697](https://trello.com/c/SD8SC64t)

# 6.5.127 
> [Trello](https://trello.com/c/4qzg71Xk) {.is-info}

- Fix: agregar parametro opcional a exportarxls para que tenga en cuenta los formatos. [Trello #698](https://trello.com/c/7uWr0eVm)

# 6.5.126 
> [Trello](https://trello.com/c/5DkjYedI) {.is-info}

- Fix: La funcion ExportarXLS no exporta los ACO ni los formatos de celda. [Trello #692](https://trello.com/c/sgHPX938)
- Fix: Deshabilitar la interpretacion del parametro Grabavacio en las secciones tipo LISTA. [Trello #694](https://trello.com/c/031kEKDy)
- Fix: Cuando se tilda 'Modificar' desaparecen los graficos. [Trello #691](https://trello.com/c/XffzlIzm)

# 6.5.125 
> [Trello](https://trello.com/c/gsL9FhBr) {.is-info}

- Fix: En los CrearListBox no se puede agrandar las columnas dinamicamente. [Trello #684](https://trello.com/c/EBzlf3Ub)
- Fix: los radios que tienen muchas opciones no salen completos, salen cortados. [Trello #683](https://trello.com/c/N3Kwzf2B)
- Fix: Al definir 2 graficos seguidos en un informe, el segundo pisa al primero causando que solo quede visible el segundo en la posicion del primero. [Trello #672](https://trello.com/c/AKTddoxp)
- PPLStudio: al crear un script nuevo, emite un warning si ya existe en la base de datos. [Trello #671](https://trello.com/c/Zsjffxep)
- PPLStudio: en el 'go to definition', si el script no existe localmente, pregunta si se desea importarlo [Trello #654](https://trello.com/c/ZkbMpVUw)
- Se agregeron los campos NrExterno, IDSisExterno, ConceptoFail en operaciones para STD. [Trello #667](https://trello.com/c/IBjjPSOd)
- Fix: Bug en la renderizacion de los graficos cuando se minimiza y maximiza el reporte. [Trello #662](https://trello.com/c/OkO74Ul1)
- Fix: Se renombro la Funcion RenderChart por GraficarCeldas2. [Trello #666](https://trello.com/c/SWVVZIhb)
- Fix: Error al recuperar por primera vez una variable desde el cache de op. [Trello #664](https://trello.com/c/XX00iEH5)
- Implementacion de precondiciones. [Trello #651](https://trello.com/c/TyWXdk8X)

# 6.5.124 
> [Trello](https://trello.com/c/NWQb7TMF) {.is-info}

- Fix: Corta el grafico por la mitad si el mismo queda dentro de un salto de pagina. [Trello #657](https://trello.com/c/9z4uEu4Q)
- Implementacion de acceso a campos de cuotas de la operacion de referencia. (OPREF.CUOTASL) [Trello #647](https://trello.com/c/Zrnq3RHN)
- Compatibilidad: implementacion de la funcion MODI para campos del dialogo en interprete. [Trello #606](https://trello.com/c/aDSMyikv)
- Feature: Poder establecer el valor default del parametro GrabaVacio de las secciones Listas. [Trello #646](https://trello.com/c/4Ekf5EJK)
- Implementacion de graficos en V6 usando chartjs. [Trello #622](https://trello.com/c/3N11M2nh)
- Se agrego el boton 'hoy' al control de selecciona de fechas [Trello #356](https://trello.com/c/jLita8ES)

# 6.5.123 
> [Trello](https://trello.com/c/QtCIZSp8) {.is-info}

- Fix: Abm, el before_show_dialog no se ejecutaba en la baja y se ejecutaba dos veces en la modificaci├│n. [Trello #639](https://trello.com/c/Jo6lPRKt)
- Fix: Error al logguear SessionInfo cuando se ejecuta desatendido [Trello #641](https://trello.com/c/Cj8qzFOm)
- Fix:Implementacion de mascara con parentesis en grillas de eventos,informes y op. **Critico** [Trello #534](https://trello.com/c/jrtvwyq9)

# 6.5.122 
> [Trello](https://trello.com/c/QFyx6Enu) {.is-info}

- Fix: Al ejecutar evento automatico con dialogo, debe frenar la ejecucion hasta el cierre del mismo. [Trello #633](https://trello.com/c/uGJtQaX0)
- Fix: agregamos la ejecucion de PPLRC para el framework de V6 para V5. [Trello #636](https://trello.com/c/UynMYqzN)
- Fix: En interprete las letras deben funcionar como constantes para ser utilizadas en direcciones de celda. [Trello #616](https://trello.com/c/HFMFrFpa)
- Implementacion de funcion Habiles2() [Trello #619](https://trello.com/c/mZUG6CmS)
- Funciones de fecha: ahora soporta lista separada por pipes en el parametro de tabla de feriado. [Trello #619](https://trello.com/c/mZUG6CmS)
- Abms: Implementacion TabIndex por fila (opcion tab_row) [Trello #618](https://trello.com/c/eKANxug9)

# 6.5.121 
> [Trello](https://trello.com/c/0RV7f3Nt) {.is-info}

- Fix: Error al ejecutar acciones sobre cualquier tipo de script desde grillas del cliente. [Trello #630](https://trello.com/c/MuVCgVfK)
- Fix: al dar OK en una op en edicion que tenia Excepciones daba error porque se ejecutaba la validacion de esa grilla como si fuera de una seccion del tipo LISTA. [Trello #629](https://trello.com/c/10EFR4tM)

# 6.5.120 
> [Trello](https://trello.com/c/ITcbTNeA) {.is-info}

- Implementacion de la funcion BorrarFila. [Trello #601](https://trello.com/c/o01ip6x0)
- Fix: excepcion no controlada en recalculo de operaciones [Trello #620](https://trello.com/c/sBuXpTJs)
- Eventuales: ajustes [Trello #603](https://trello.com/c/lWyzPM0U)
- Implementacion de ACLN y ACLBN. [Trello #609](https://trello.com/c/oYPR1LhI)
- Implementacion de operaciones minoristas. [Trello #612](https://trello.com/c/8Il5VKE9)
- Fix: Error param 'desde' de Recorrer cuando se setea el resultado de una funcion. [Trello #604](https://trello.com/c/L8gH7cf9)

# 6.5.119 
> [Trello](https://trello.com/c/ZKkYM9XC) {.is-info}

- Fix: las columnas que tiene que fijar deben ser menor al nro pasado por parametro en la funcion FijarCol. [Trello #611](https://trello.com/c/1p1YY1HA)
- Fix: al recuperar el valor de una variable con la funcion VAR en OPERACIONES con el PPLStudio (Con el cliente funciona OK), la misma se recupera con todos los espacios que se guarda en la DB. [Trello #610](https://trello.com/c/QWg2jLSC)
- Implementacion de parametro 'Modo' de func IteresEspecie() con impacto en PrecioaRecidual() y PrecioaNominal() [Trello #608](https://trello.com/c/o9J2xWwY)
- Implementacion de parametro ProcesaEventosAutoamticos de func AbrirDia() [Trello #605](https://trello.com/c/NMS5xJ6x)
- Implementacion de la Funcion FechaJul. [Trello #602](https://trello.com/c/bIY1U8M8)
- Implementacion parametro ProcesaMovimientosAuto9maticos de func AbrirDia() [Trello #605](https://trello.com/c/NMS5xJ6x)
- Fix: PPLStudio, error 'parameter not valid' (Cruz roja en el editor) [Trello #596](https://trello.com/c/CAJCcchg)
- Fix: No estaba implementado la edicion de Ejecuciones. [Trello #593](https://trello.com/c/Q4S2G0DS)
- Abm: Implementacion de campos datetime [Trello #584](https://trello.com/c/BHeyZuZK)
- Fix: Se agregan los campos de tipo TEXT Autosupervisada y TipoCotizacion para operaciones. [Trello #585](https://trello.com/c/DnBIIFKu)

# 6.5.118 
> [Trello](https://trello.com/c/cj9uvy10) {.is-info}

- Fix: Error al querer abrir un registro de ABM con un campo Decimal. [Trello #579](https://trello.com/c/bPndGpm9)
- Fix: la condicion que hacia ejecutar la seccion CONDICIONESCUOTAS estaba invertida, haciendo que la seccion no se ejecute nunca. [Trello #582](https://trello.com/c/4EZ4MdPb)
- Posibilidad de definir mascaras numericas en PPLRC [Trello #540](https://trello.com/c/ezMIVcGy)
- PPLStudio: Implementacion de debugger paso a paso para interprete [Trello #568](https://trello.com/c/1voZLosj)
- PPLStudio: Macros de ingreso de valores en dialogo de Operaciones [Trello #535](https://trello.com/c/2FcEinGP)
- PPLStudio: DebugMonitor, Orden de columnas por tiempo, buscador, exportar y otros ajustes. [Trello #565](https://trello.com/c/bn0qym4k)
- Refactor de las mascaras de los controles NUMERIC en operaciones. Antes estaban hardcodeadas, ahora se definen en el OPERACIONES.cfg (de core). [Trello #116](https://trello.com/c/Un7DizGt)

# 6.5.117 
> [Trello](https://trello.com/c/PQ8IdKmP) {.is-info}

- Fix: En operaciones, transacciones y ordenes, la funcion Instancia la toma siempre en 1. [Trello #570](https://trello.com/c/vq8t1R8K)
- Fix: Cast de parametros cuando se ejecuta un evento por POSTEDICION [Trello #571](https://trello.com/c/E69PeDfn)
- Fix:Exportar a PDF de un informe cuando tiene un ACN ACT o ACD de una celda mayor a LimitesVIsion definido anteriormente da error. [Trello #572](https://trello.com/c/yMUSbEqV)
- Fix: mejora en mensaje de error que se emite cuando se edita la grilla luego de establecer el limitesvision. [Trello #564](https://trello.com/c/oVEcpLT7)

# 6.5.116 
> [Trello](https://trello.com/c/jDu2jXnZ) {.is-info}

- Fix: Abms, el helper validates_uniqueness no funcionaba correctamente al editar un registro [Trello #549](https://trello.com/c/Vq5wrhY9)
- Fix: Abms, fallba el query del helper validates_uniqueness_of cuando los valores de ciertos campos estaban en null. [Trello #550](https://trello.com/c/KtYLdfzN)
- Fix: Abms, fallaba el helper validates_uniqueness_of cuando la primer clave es null [Trello #550](https://trello.com/c/KtYLdfzN)
- Implementacion de la seccion CondicionesCuotas. [Trello #529](https://trello.com/c/umONWhJF)
- Fix: En los campos lookup de operaciones, da error en el parametro de doble click cuando se usa un sub select. [Trello #547](https://trello.com/c/m0x6qwG7)
- Fix: Si la condicion de la seccion lista es false (el tab no se ve) igual valida las condiciones de las columnas. [Trello #530](https://trello.com/c/mp62AbRT)

# 6.5.115 
> [Trello](https://trello.com/c/lj10ZTET) {.is-info}

- Fix: PPLStudio, no se veian correctamente los items del menu Abms [Trello #528](https://trello.com/c/4KhJ4xuf)
- Fix: Las operaciones matematicas no eran exactas en los scripts de operaciones en determinadas situaciones. [Trello #490](https://trello.com/c/dsS5ZYQv)
- Fix: PPLStudio, error al verificar version de script local/db [Trello #525](https://trello.com/c/YOwkSUn6)

# 6.5.114
> [Trello](https://trello.com/c/BKykzHpX) {.is-info}

- SessionInfo: Exportar como archivo [Trello #498](https://trello.com/c/afFXDoaO)
- PPLRC: Nuevas funcionalidades [Trello #481](https://trello.com/c/sMwjrgoU)
- Fix: PPLStudio, al recuperar scripts reservados, le da prioridad a los que estan publicados en la base de datos [Trello #60](https://trello.com/c/kOE8VzAY)
- Fix: Abms, mensaje de registro existente [Trello #300](https://trello.com/c/xjZt6VtI)
- Abm: Posibilidad de definir alias a las columna de la grilla principal [Trello #502](https://trello.com/c/6G5DgGuk)
- Fix: al hacer shift+tab o alt+shift+tab no mostraba cuando el foco quedaba en la solapa, haciendo que usuario crea que se perdio el foco. [Trello #520](https://trello.com/c/n9PsMX75)
- Fix: La funcion Habiles() no debe dar error si hay una fecha invalida en la tabla FERIADOS [Trello #489](https://trello.com/c/zqW2PyP7)
- Campo AfectaTen de Operaciones para Galicia. [Trello #519](https://trello.com/c/SDJA0ykd)
- Implementacion de funcion Desatendido() [Trello #516](https://trello.com/c/NI1lEtTD)
- Fix: si la mascara de un control numerico no soporta decimales, no se debe permitir el ingreso de los mismos. [Trello #511](https://trello.com/c/CxY7oJNx)
- PPLStudio: Al abrir un script se verifica si la version publicada en la base de datos es distinta [Trello #503](https://trello.com/c/LzwC2FxT)

# 6.5.113
> [Trello](https://trello.com/c/6t0dTF9J) {.is-info}

- Fix: Error al obtener filtro para grilla de instancia. [Trello #500](https://trello.com/c/XBrIJ9l9)
- Fix: Abm, comparacion de DbNull con enteros + Plugin $.Vacio() [Trello #501](https://trello.com/c/C3S1MEfo)
- Fix: Dialogos, al estar en el primer campo y presionar shift+tab para recorrer los controles en orden inverso, el input se pierde y si o si debo presionar tab para volver al primer control. [Trello #448](https://trello.com/c/UTNT4opD)

# 6.5.112
> [Trello](https://trello.com/c/9w812jr5) {.is-info}

- Fix: Los campos tipo texto con mascaras con un tama├▒o muy largo, hacen que el campo se vea cortado. [Trello #497](https://trello.com/c/9hyc4Sk6)
- Posibilidad de habilitar validacion de concurrencia de usuarios por config [Trello #495](https://trello.com/c/rbMsqETn)
- Fix: no se liberaba el usuario activo cuando el cliente se cerraba por inactividad [Trello #494](https://trello.com/c/GoFfNJua)
- Ajustes realizados en PPLStudio (Find All References y Find All Usages) [Trello #492](https://trello.com/c/HWo2qRYj)
- Fix: La grilla ppl debe poder superar los 16bits (65536) de filas. [Trello #459](https://trello.com/c/PFJJFE0z)
- Fix: La funcion ModificarOperacion no recalculaba correctamente los campos al tener el parametro recalcularCampos en SI. [Trello #483](https://trello.com/c/xSqMuEvW)
- Se agregaron para los dialogos de eventos los campos Plazo[1-4]. [Trello #491](https://trello.com/c/JzSR4fxn)
- Opcion de config que permite armar directorios temporales y de scripts por usuario [Trello #487](https://trello.com/c/QLAygRmM)
- Fix: Ahora al fallar el recalculo de las dependencias de un campo, mostramos cual fue el que fallo para resolver mas rapido el problema. [Trello #486](https://trello.com/c/tAnLIzuU)
- Fix: No se debe exportar el logo a excel. [Trello #482](https://trello.com/c/AykC9dRq)
- Cache de valores defaults para Operaciones, Transacciones y Ordenes [Trello #409](https://trello.com/c/0bZPtz7T)
- PmFuncs optimizadas con BuscarCampo: Caracteristica(), ValorTeorico(), EspecieDiasAnio(), EspecieDiasMes() y CotizaEn() [Trello #409](https://trello.com/c/0bZPtz7T)
- Fix: Cuando se ejecuta el actualizarmovimientos, se deben recalcular los campos virtuales y sus dependientes. [Trello #275](https://trello.com/c/OGkJuMcb)
- PPLStudio: Debug de scripts de operaciones [Trello #82](https://trello.com/c/bSSKVwSn)

# 6.5.111
> [Trello](https://trello.com/c/Cv9G758D) {.is-info}

- Ventanas de abms como MDI. Se puede revertir con el tag float_abms. [Trello #478](https://trello.com/c/Z0e35HKi)
- Posibilidad de configurar path que utiliza internamente Pechkin para la exportacion a PDF [Trello #480](https://trello.com/c/V6wcURcT)
- Se agregan los campos Contacto, NrBoleto1 y NrBoleto2 tipo texto para GALICIA. [Trello #479](https://trello.com/c/dEN8rjOE)
- Fix: Error al querer recuperar un valor numerico muy grande de la base (ORACLE). [Trello #446](https://trello.com/c/Dur5902M)
- Fix: si definimos un rangotitulo con cantidad de filas mayor al que existe en el informe da error al exportar a pdf o al imprimir. [Trello #476](https://trello.com/c/L6f8rZvA)

# 6.5.110
> [Trello](https://trello.com/c/sOBdShuV) {.is-info}

- Fix: deteccion de dependencias cuando se hace un delete y la instancia actual tiene definido un dialogo. [Trello #469](https://trello.com/c/6UMEY7IB)
- Campos Operaciones: Cartera1 y Cartera2 deben apuntar a la tabla CARTERASBCRA. (Solo para Galicia) [Trello #468](https://trello.com/c/MO48UzcR)
- Campos Operaciones: MonedaLiq y FechaAltaCV. Pedidos para Galicia [Trello #467](https://trello.com/c/JnZV9CnJ)
- Campos Operaciones: Mercado5/6, PrecioMayorista, PorArancel3 y Portfolios1. Pedidos para Galicia [Trello #462](https://trello.com/c/g1jGvW2B)
- Implementacion de seccion DIALOG_SIZE para Operaciones que permite definir el tamano del dialogo [Trello #466](https://trello.com/c/YuUVKOba)
- Fix: Se debe validar el lookup del control autocomplete_ar_list antes de agregar el item a la lista. [Trello #463](https://trello.com/c/vL5RjtDq)
- En informes y eventos el modo debug se propaga a traves de ACL(), LinkearHoja y EjecutarEvento [Trello #452](https://trello.com/c/XoNXjWUr)

# 6.5.109
> [Trello](https://trello.com/c/Rk7OGsV0) {.is-info}

- Fix: en ABMs al ingresar un nro mayor a 999.99 en un control numerico, siempre se graba 0. [Trello #460](https://trello.com/c/uE99WDfj)
- Fix: Si se tiene el paginado de datos activados, al exportar a excel debe dar la opcion de exportar todo o solo la pagina actual, al exportar a pdf y teniendo paginado de datos solo se exporta la pagina actual. [Trello #442](https://trello.com/c/pk7YzwIJ)
- Fix: Si el contenido texto de una celda terminaba con un espacio y tenia alineado 'C', al exportar a pdf, el mismo quedaba mal posicionado afectando a la impresion. [Trello #457](https://trello.com/c/xLUuIHyk)

# 6.5.108
> [Trello](https://trello.com/c/Z2SvC7rc) {.is-info}

- Fix: Si se exporta a pdf (Desde el contenedor de informes o desde la funcion ExportarPdf) y la configuracion de impresion tiene un tipo de hoja que no sea A4 ni Carta, forzamos a tipo de hoja Carta para que se pagine el informe correctamente. [Trello #454](https://trello.com/c/OPtBrVFH)
- Fix: al actualizar la fecha automaticamente al iniciar el cliente FSys se seteaba con la hora, haciendo que las comparaciones en los scripts de OPERACIONES den mal. [Trello #451](https://trello.com/c/VBCiW85X)

# 6.5.107
> [Trello](https://trello.com/c/sSKecjjo) {.is-info}

- Fix: al desplegar el calendario en el control y seleccionar una fecha, es necesario hacer 3 veces tab para pasar el foco al siguiente control. [Trello #447](https://trello.com/c/pWYM16Do)
- Fix: FijarCol() habia casos donde quedaban filas desalineadas [Trello #328](https://trello.com/c/W2CVSSsj)
- Fix: no se podia ejecutar mas de un script de Operaciones, Transacciones y Ordenes al mismo tiempo (PortfolioClient) [Trello #440](https://trello.com/c/aH6BzEN0)
- Fix: imprimir sin depender de la configuracion de la impresora en Windows. [Trello #424](https://trello.com/c/jlf7ABJ4)

# 6.5.106
> [Trello](https://trello.com/c/ftdOE8ni) {.is-info}

- Funcionalidad de paginado, para resolver inconvenientes en informes con gran cantidad de filas. [Trello #75](https://trello.com/c/3lDKoyIe)
- Funcionalidad para paginar informes. [#176](https://trello.com/c/nioGxKC1)
- Fix: Ajustes para evitar escribir mensajes de debug y cef por consola (Para GALICIA) [Trello #441](https://trello.com/c/kLUPX3sg)
- Fix: Hay problemas con algunos default de seteo de pagina en la impresion. [Trello #439](https://trello.com/c/zAoCKszc)

# 6.5.105
> [Trello](https://trello.com/c/dUAtiCrN) {.is-info}

- Fix: los scripts Transacciones y MinBolsa no estaban agregando el campo implicito UsrInput causando un desfasaje en el seteo del foco. [Trello #434](https://trello.com/c/nEkpK2aa)
- Fix: Sale mal el paginado en ancho, esto ocurre por un bug al guardar el default para generar la impresion. [Trello #436](https://trello.com/c/RXmFEXWE)
- Fix: Cuando se ejecuta un script de forma desatendida en GALICIA, no se muestra el output por consola [Trello #435](https://trello.com/c/BpdJ0y7u)

# 6.5.104
> [Trello](https://trello.com/c/I4OYgWJN) {.is-info}

- Fix: Escribir archivos .ppl y .hppl de forma mas segura para evitar locks de file system [Trello #428](https://trello.com/c/vJgveLPn)
- Fix: Si teniamos una hoja que sea distinta a A4 o carta, se emitia un error que no soportabamos el paginado en esos tipos de hoja [Trello #427](https://trello.com/c/61foUwIX)
- Fix: En Oracle cerramos todo el pool de conexiones despues de cambiar de password [Trello #139]
- Fix: error aleatorio en login (OnMouseMoved) [Trello #426]
- Fix: Las transacciones de actualizar, mover,crear y borrar una op,tr,etc ahora contemplan reintentos en caso que hayan sido canceladas por deadlocks [Trello #422](https://trello.com/c/51mBILyK)
- Se agrego (NOLOCK) en los queries que alimentan las grillas de instancias para minimizar deadlocks [Trello #422](https://trello.com/c/51mBILyK)

# 6.5.103
> [Trello](https://trello.com/c/IpV8xZUi) {.is-info}

- Fix: una pagina de ancho....dos paginas. [Trello #144](https://trello.com/c/CNSX2Lqs)

# 6.5.102
> [Trello](https://trello.com/c/hvAKdJA9) {.is-info}

- Fix: al imprimir, si el contenido excede la hoja, la achicamos al tama├▒o de pagina. [Trello #416](https://trello.com/c/ERlkvMgq)
- Fix: valores negativos en controles numericos [Trello #417](https://trello.com/c/BQC8AAKA)

# 6.5.101
> [Trello](https://trello.com/c/g3RKFJ4N) {.is-info}

- Perfil: implementacion de permisos a Tipos Orden [Trello #411](https://trello.com/c/E1x0Sp2x)
- Perfil: Implementacion de permisos de items de menu intancias Ordenes [Trello #411](https://trello.com/c/E1x0Sp2x)
- Fix: al hacer click en el boton imprimir del contenedor de informes, no se imprime el pie de pagina ('confidencial'). [Trello #413](https://trello.com/c/Zw3wyVeA)
- Fix: GetNumerador() si no existe, lo crea. [Trello #352](https://trello.com/c/aY13Ti0d)
- Status en Splash para Portfolio. Nos permite ver el estado de todo el proceso de inicializacion de la aplicacion [Trello #374](https://trello.com/c/QX9wtojH)
- Fix: configuracion de items de menu dinamicos se debe ejecutar asincronicamente [Trello #374](https://trello.com/c/QX9wtojH)

# 6.5.100
> [Trello](https://trello.com/c/6HuHjsbu) {.is-info}

- Fix: Habia casos donde no se registraba el movimiento del mouse como actividad en la ventana principal [Trello #404](https://trello.com/c/eB8bqdJy)
- Fix: Habia casos donde se registraba actividad con el puntero del mouse quieto [Trello #404](https://trello.com/c/eB8bqdJy)
- Fix: Los campos autocomplete_arlist_chk muestran solamente un check. [Trello #403](https://trello.com/c/RgfArWRY)
- Fix: InterfaceV6, Cambiaron las firmas de los siguientes metodos: ExecuteEditOp, ExecuteEditTr y ExecuteEditOrden para pasar por parametro NrInstancia. [Trello #401](https://trello.com/c/CW7G2bH9)

# 6.5.99
> [Trello](https://trello.com/c/UfBYPAwg) {.is-info}

- Fix: el borde derecho de las ultimas celdas de la derechar establecida por el limitesvision no es visible. [Trello #392](https://trello.com/c/X3aKpfJb)
- Campo NrOpMinorista para eventos e informes y firmas de algunas funciones sin implementar. [Trello #399](https://trello.com/c/rgF5izor)
- Implementacion de bloqueo y cierre de aplicacion por inactividad. (Cliente Portfolio) [Trello #325](https://trello.com/c/LEvKlFKa)
- Fix: no se procesaban correctamente los movimientos automaticos de la seccion POSICIONFUT [Trello #396](https://trello.com/c/UvSYtQuR)
- Fix: los movimientos de cashflow deben ejecutarse dependiendo de la existencia de la tabla MOVCASHFLOW. [Trello #398](https://trello.com/c/0LpUdx1v)

# 6.5.98
> [Trello](https://trello.com/c/Z4PsuqJM) {.is-info}

- Fix: Problema de precision con decimales en ABMs. [Trello #389](https://trello.com/c/NFmERJFD)

# 6.5.97
> [Trello](https://trello.com/c/zx9ApqFN) {.is-info}

- Fix: MOVCUOTAS - Agregar los parametros CallPut, FechaEj y PrecioEj. [Trello #384](https://trello.com/c/lqhDj3UC)

# 6.5.96
> [Trello](https://trello.com/c/3xUbDwJZ) {.is-info}

- Fix: Se generan solamente hasta 3 registros de movimientos de MTMDIARIO de una operaci├│n. [Trello #380](https://trello.com/c/ih1ifykB)
- Fix: Actualizar movimientos, habia casos donde al ajustar el saldo pendiente, generaba movimientos con cantidad cero. [Trello #381](https://trello.com/c/xrknNXto)
- Cuando hay error de inicializacion, se agrega el mensaje de la excepcion. [Trello #355](https://trello.com/c/PuDECC3m)
- Fix: En ISBAN daba error al intentar conectarse a hasp server cuando el usuario no tenia permisos sobre el directorio 'bin' [Trello #378](https://trello.com/c/5oYNTntJ)
- Fix: Orden de campos para ModificarOperacion(). [Trello #371](https://trello.com/c/RXFcBRdI)

# 6.5.95
> [Trello](https://trello.com/c/pF1H406D) {.is-info}

- Fix: error en la op con GenObj / null. [Trello #377](https://trello.com/c/twEuG4zD)
- Fix: daba error al ejecutar items del menu Herramientas desde la busqueda contextual del cliente [Trello #372](https://trello.com/c/qurK6Rnz)

# 6.5.94
> [Trello](https://trello.com/c/q6tWGDWS) {.is-info}

- Fix: Error al recalcular el campo LABEL1. [Trello #369](https://trello.com/c/oreW5qRw)
- Fix: Actualizar grillas cuando se avanza una operacion desde el dialogo de visualizacion [Trello #368](https://trello.com/c/8Who5bDy)
- Fix: En TECO, cuando se ingresa a FPA y muestra que la nueva fecha va a ser la del dia, no modifica la fecha del sistema. [Trello #363](https://trello.com/c/irpBvlWQ)
- Fix: Se acumulaban excepciones al cargar operaciones con OK# o OK++ [Trello 
> #361](https://trello.com/c/oYyS8y4Z) {.is-info}
- SupAbms: contempla los cambios de Jerarquia [Trello #367](https://trello.com/c/uYqjNE4c)
- SupAbms: En la grilla de supervision se incluye las tablas donde el usuario tiene acceso (En necesario actualizar abm __SUP) [Trello #365](https://trello.com/c/pyorsrpc)

# 6.5.93
> [Trello](https://trello.com/c/TRrfZ0qk) {.is-info}

- Fix: Id de procesos repetidos. Provocaba que la barra de proceso quedara activa [Trello #357](https://trello.com/c/Buv4gHV6)
- Fix: errores al ejecutar Escritorios inteligentes. Sincronizacion de threads al ejecutar informes simultaneamente. [Trello #357](https://trello.com/c/Buv4gHV6)
- Fix: Error el campo LABEL1 no existe en la tabla OPERACIONES. [Trello #360](https://trello.com/c/wIL9yIac)
- Fix: Las declaraciones que se hacian en la seccion SQL de la op no estaban agregando el separador de comandos para ORACLE. [Trello #358](https://trello.com/c/mFthN9cX)
- Fix: Interprete, error convert parametros object a string [Trello #354](https://trello.com/c/6zMjloet)
- SupAbms: permitir modificar valores de campos claves [Trello #353](https://trello.com/c/QhUGkPEo)
- PPLStudio: contingencia ante conflicto de archivo hppl [Trello #296](https://trello.com/c/QmflBMaV)
- Portfolio: boton de Estilo como item de menu en Herramientas [Trello #307](https://trello.com/c/Q7X3XlfH)
- Fix: PPLSync acumulaba scripts ya sincronizados [Trello #350](https://trello.com/c/f4QjOvvf)
- Fix: Error al cambiar fecha. No cachear valor de fecha real [Trello #346](https://trello.com/c/KR2rcHl0)
- Fix: Abm, error al recuperar registro con string vacio en algun campo clave [Trello #348](https://trello.com/c/5ybxL1ap)
- Fix: No ocultar items de menu con Cod. Menu duplicados [Trello #293](https://trello.com/c/fCs2Ls4e)
- Fix: No funciona escala Logo y se superpone al titulo. [Trello #322](https://trello.com/c/FNfYiWw8)
- Fix: No sale la imagen de logo si utilizamos FijarFilas. [Trello #304](https://trello.com/c/RO8paX5Z)

# 6.5.92
> [Trello](https://trello.com/c/oNllm7It) {.is-info}

- Fix: Desconfiguracion de formato de Fechas en converts implicitos al ejecutar una op. [Trello #343](https://trello.com/c/uJDoUkoE)

# 6.5.91
> [Trello](https://trello.com/c/ju4m7LFd) {.is-info}

- Fix: ERROR Coleccion modificada; puede que no se ejecute la operacion de enumeracion. [Trello #341](https://trello.com/c/JV6TcnnE)
- Fix: El log de errores tiene una entrada de info por cada vez que se ejecuta un EjecutarEvento2. [Trello #340](https://trello.com/c/FB7PiYqI)
- Fix: Error en DBMeta con EjecutarEvento2. [Trello #339](https://trello.com/c/nNNIYIzm)

# 6.5.90
> [Trello](https://trello.com/c/LWU11PDZ) {.is-info}

- Fix: Etiquetas de colores no funcionan. [Trello #324](https://trello.com/c/dGQiFhdH)
- Fix: OverloadInfoCache evitar colision de HashCode (Clave) [Trello #324](https://trello.com/c/dGQiFhdH)

# 6.5.89
> [Trello](https://trello.com/c/MplHF909) {.is-info}

- Fix: error con Recorrer SQL anidados + SQL.GenerarAsientoOp() [Trello #318](https://trello.com/c/qLniBs07)

# 6.5.88
> [Trello](https://trello.com/c/QBQ0JK36) {.is-info}

- Fix: correccion de la guncion GetNumerador para que funcione igual a V3. [Trello #314](https://trello.com/c/8UNkEXRx)

# 6.5.87
> [Trello](https://trello.com/c/YJ9UwVZK) {.is-info}

- Mensaje de control cruzado al supervisar abm no debe aparecer como error [Trello #313](https://trello.com/c/WgFdU1MG)
- Control cruzado de abms activo por default en BOFA [Trello #311](https://trello.com/c/xIrwYYeS)

# 6.5.86
> [Trello](https://trello.com/c/DezPtFBg) {.is-info}

- Implementacion de funcion PPL CotizacionNIIF() (Migracion desde V5 Galicia) [Trello #236](https://trello.com/c/VA6Xdi1V)

# 6.5.85
> [Trello](https://trello.com/c/JnWnDng2) {.is-info}

- Implementacion de la funcion EjecutarEvento2 que es un fix para el Out Of Memory del evento ONLMAE de BOFA. [Trello #298](https://trello.com/c/GHsAkNQH)

# 6.5.84
> [Trello](https://trello.com/c/hmaz1tzM) {.is-info}

- Fix: Func BorrarArchivo() [Trello #305](https://trello.com/c/qGz9ohsQ)
- Func DobleConf(), nos permite saber si un abm tiene activada la DobleConfirmacion [Trello #280](https://trello.com/c/CuZZ4rGy)
- Func AltaTemporal(), permite insertar un registro en temporales (pendiente de supervision) [Trello #280](https://trello.com/c/CuZZ4rGy)

# 6.5.83
> [Trello](https://trello.com/c/CoSfT8Xs) {.is-info}

- SupAbms: ejecutar validate_uniqueness al momento de aprobar un registro [Trello #292](https://trello.com/c/3dYK9q0w)
- Fix: AgregarBmp() Se agrego mas soporte a imagenes con distintos encodings. En BOFA paso que usaban un BMP de logo con un formato no comun y no se exportaba a PDF. [Trello #279](https://trello.com/c/datcpuZh)

# 6.5.82
> [Trello](https://trello.com/c/TYonVmq5) {.is-info}

- Implementacion de la seccion POSCUOTASACCION. [Trello #288](https://trello.com/c/qDkJKLrV)
- Fix: la funcion CotizacionFut() no esta teniendo en cuenta cotizaciones con fecha anterior a la de consulta. [Trello #291](https://trello.com/c/lqwEPtv0)
- RelacionCuenta: nuevo parametro (20) TipoLiquidacion [Trello #290](https://trello.com/c/d4MOrDHT)
- Fix: GenerarAsientoOp, no tomaba correctamente CentroCosto fijo [Trello #289](https://trello.com/c/toAzDKIq)

# 6.5.81
> [Trello](https://trello.com/c/NboiGCaO) {.is-info}

- SupAbms: Fix, no se debe ejecutar after_save cuando rechazan un registro [Trello #285](https://trello.com/c/WmswVRE4)
- Fix: Abms, no se debe resetear variables de contexto cuando se valida con before_save [Trello #283](https://trello.com/c/BoQHsdOE)
- SupAbm: La regla validate_uniqueness chequea tambien contra los registros pendientes de supervision. [Trello #282](https://trello.com/c/FftbSqdZ)
- Fix: Acceso a campos Modelo.Moneda* [Trello #281](https://trello.com/c/xILQe9eo)
- Fix: Campo a editar al iniciar dialogo. [Trello #217](https://trello.com/c/NHIeCSii)
- Se agregaron campos TipoLimite y TipoPosicion para eventos e informes [Trello #276](https://trello.com/c/2mu6oaev)
- Interprete: cuando el campo del dialogo no existe, mostrar nombre en el mensaje de error [Trello #276](https://trello.com/c/2mu6oaev)
- Implementacion de la funcion PPL CotizacionFut. [Trello #270](https://trello.com/c/nZeypGmO)
- Fix: Habia casos donde no se cerraba correctamente el Cuadro de mensajes (cuando hay muchos procesos abiertos) [Trello #273](https://trello.com/c/3khGn6bK)

# 6.5.80
> [Trello](https://trello.com/c/mtbzhFl0) {.is-info}

- Implementacion de funcion ppl ExisteTemporalPendiente() [Trello #272](https://trello.com/c/gSXwHlW8)
- SupAbms: Ejecutar callback after_save al aprobar registro de abm [Trello #272](https://trello.com/c/gSXwHlW8)
- Funcion GenerarJerarquiaByRef contempla registros temporales pendientes de supervision [Trello #272](https://trello.com/c/gSXwHlW8)
- Fix: En oracle los items de menu de INFORMES/EVENTOS con Tipo null o vacio se colocaban al final y no al principio [Trello #266](https://trello.com/c/mobez4Py)

# 6.5.79
> [Trello](https://trello.com/c/9mdWHbXE) {.is-info}

- Campo CodErrorMAE como TEXT en lugar de NUMERIC [Trello #264](https://trello.com/c/N1a8D8hN)

# 6.5.78 (
> [Trello](https://trello.com/c/tneyf85N) {.is-info}

- Fix: SupAbms, error al chequear permiso de DobleConf [Trello #260](https://trello.com/c/6yalPN2G)
- Fix: Error cast 'CacheableDataBase'. Provocaba error al publicar script con App Server [Trello #256](https://trello.com/c/91IGJRTr)
- Fix: Supervision de abms. Da error al supervisar registros en campos fecha, con determinados valores [Trello #255](https://trello.com/c/VaVDqCWi)
- Fix: Error en grilla de abm embebido. Creaba columnas de mas y habia casos donde daba error el validate_uniqueness [Trello #252](https://trello.com/c/FeOK7vF1)
- Fix: Se ajusto el orden por el cual se asignan las propiedades de Modelo.* en GenerarAsientoOp() [Trello #249](https://trello.com/c/7XnF7CrR)
- Fix: En los dialogos de Eventos e informes, no funciona el doble click en los campos ListaTabla. [Trello #251](https://trello.com/c/1SyrkXsZ)
- Fix: SQL.ADD() se cortaba el string cuando se utilizaba doble guion en un literal. [Trello #250](https://trello.com/c/fiKJHnxw)
- Contabilidad: La propiedad Modelo.TablaRC se debe asignar antes que la cuenta [Trello #249](https://trello.com/c/7XnF7CrR)

# 6.5.77
> [Trello](https://trello.com/c/lDjmNGdk) {.is-info}

- Fix: La funcion RelacionCuenta() no filtraba correctamente por Especie. [Trello #246](https://trello.com/c/JYVL3ynk)

# 6.5.76
> [Trello](https://trello.com/c/QTMVz7Ca) {.is-info}

- Para ISBAN no se usan los filtros de Ordenes y MinutasBolsa en solapa Instancias de abm de perfiles [Trello #239](https://trello.com/c/UYWVBaKU)
- Fix: Error al guardar campo Orden en header de scripts de Eventos e Informes [Trello #244](https://trello.com/c/Z0JcfMRB)
- Fix: Error al hacer doble click en header de listbox [Trello #242](https://trello.com/c/ZUNVzcjE)
- Fix: Exportar Excel, error alineacion de celdas [Trello #243](https://trello.com/c/RQ6jhBwm)
- Campo lookup NrTrans[1-2] para OPERACIONES [Trello #240](https://trello.com/c/gvW7tQeL)
- Fix: Abm, ajuste de tama±o de control check_grid [Trello #239](https://trello.com/c/UYWVBaKU)
- Abm: implementacion plugin Concat() [Trello #239](https://trello.com/c/UYWVBaKU)
- Deshabilito funcionalidad de items migrados/deshabilitados (solo la usaba ISBAN) [Trello #159](https://trello.com/c/WG0OW1EU)

# 6.5.75
> [Trello](https://trello.com/c/mGQTbrrM) {.is-info}

- Exportar Excel: Reutilizacion de estilos [Trello #221](https://trello.com/c/er3h8SCY)
- Fix: orden de parametros de func RelacionCuenta [Trello #235](https://trello.com/c/Ycnvemxm)
- Fix: Abm, inicializacion de campos combos al reutilizar dialogo [Trello #228](https://trello.com/c/44Jn0MlY)
- Se deshabilito cache de funcion Query() para Operaciones [Trello #233](https://trello.com/c/XkGZm8ox)
- Fix: Importar y Publicar campo Orden en Eventos e Informes [Trello #232](https://trello.com/c/8MtB7rmQ)
- Fix: ListBox error al parsear fecha con cultura US [Trello #229](https://trello.com/c/gRmcTeFW)
- Se agrego descripcion de entorno en StatusBar [Trello #215](https://trello.com/c/59s3jYyL)
- Refactor StatusBar (textos mas acotados y tooltips) + ProgressBar en PPLStudio [Trello #230](https://trello.com/c/y5oomw6b)
- Se agrega descripcion de entorno en ventana de info de sesion [Trello #215](https://trello.com/c/59s3jYyL)

# 6.5.74
> [Trello](https://trello.com/c/b8b8Xshd) {.is-info}

- Fix: Abm, error al ejecutar callback when_change de un campo autocomplete cuando se selecciona un valor desde el lookup. [Trello #224](https://trello.com/c/eQCv0a2w)
- Fix: Listbox param RecalcFila [Trello #223](https://trello.com/c/qjsws9z8)
- Fix: Cuadro de mensajes se cierra cuando terminan todos los procesos [Trello #220](https://trello.com/c/1S9LAabT)
- Fix: func Buscar3TablasEnTabla debe tener el cuenta el contexto en donde se utiliza la tabla, tiene que ser un query [Trello #222](https://trello.com/c/Vn3xumth)
- Fix: Listbox: param AutoRecalc [Trello #219](https://trello.com/c/nJXGumPx)
- Fix: Error en ListBox, restaurar FLB al finalizar recalculos [Trello #219](https://trello.com/c/nJXGumPx)
- En caso de error al realizar  cualquier accion sobre un script (guardar, borrar, importar, exportar, etc.), muestro un mensaje de error mas completo [Trello #202](https://trello.com/c/YFW51Vzl)
- Fix: Abms comparacion de enteros con null [Trello #214](https://trello.com/c/Nuu0FdGo)

# 6.5.73
> [Trello](https://trello.com/c/gXZsRmsK) {.is-info}

- Fix: En los listbox la celdas de tipo fecha, por default debe traer la fecha del sistema sin la hora. [Trello #212](https://trello.com/c/aylUarfe)
- Implementacion funcion TIREspecie() [Trello #213](https://trello.com/c/kGhJf5oH)
- Abms: se agrego un parametro en campos autocomplete para especificar ancho del control [Trello #207](https://trello.com/c/VmLvEpbI)
- Fix: Error al monitorear proceso de sub-evento con dialogo. (Al correr el CIERRE pareciera que no terminara) [Trello #182](https://trello.com/c/lcSvqGS5)
- Fix: error al ocultar cuadro de mensajes cuando lo muestra un sub-evento [Trello #211](https://trello.com/c/pEPJxuYW)
- Fix: error en el calculo del campo porRenta de los cupones. [Trello #209](https://trello.com/c/nwSE0014)
- Implementacion de la funcion Buscar3TablasEnTabla. [Trello #204](https://trello.com/c/BDXfashi)
- Fix: ajustes en la funcion AgregarCupon. [Trello #203](https://trello.com/c/UisaNOEc)

# 6.5.72
> [Trello](https://trello.com/c/0lDA3axf) {.is-info}

- Fix: Error al utilizar formula como condicion de bloque 'if' en Interprete [Trello #185](https://trello.com/c/HLQS5fe0)
- Fix: Al leer la ultima linea con LeerAscii la variable OK debe estar en SI, se pone en NO al querer leer y ya no tiene filas. [Trello #184](https://trello.com/c/i1pA3dE4)
- Fix: funcion PPL Posicion() cuando se usa el 3er parametro sin el 4to. [Trello #181](https://trello.com/c/8YERD7Bv)
- Implementacion de la funcion BuscarComandoEnTablas. [Trello #174](https://trello.com/c/xCYc3i3P)
- Warning al ejecutar un informe/evento de forma desatendida sin especificar todos los parametros del dialogo [Trello #121](https://trello.com/c/xTT5uSA8)
- Fix: Abm error al eliminar registros de un abm con embebidos [Trello #183](https://trello.com/c/8qvNotOW)

# 6.5.71
> [Trello](https://trello.com/c/kFlpSJj3) {.is-info}

- Fix: los radios en operaciones hacen que no se vean los controles que estan debajo de ellos. [Trello #175](https://trello.com/c/JwHl9fvU)
- Fix: Abm embebidos, error cuando la grilla no tiene items [Trello #177](https://trello.com/c/NmVkECpv)
- Implementacion de las funciones BuscarEnTablas, BuscarLinkearHojas, BuscarEjecutarEventos, BuscarFunciones y BorrarArchivo para Oracle. [Trello #158](https://trello.com/c/Fh62UzRw)
- Implementacion de func PPL ShowSessionInfo() para poder mostrar la ventana desde PPL [Trello #166](https://trello.com/c/6dKOBkYS)
- Fix: Filtros de usuario en grilla. No andaba el operador distinto '<>' [Trello #142](https://trello.com/c/iceluAH2)
- Implementacion de func PPL DetalleItemPerfil() [Trello #172](https://trello.com/c/2Ez00yc8)

# 6.5.70
> [Trello](https://trello.com/c/cpNW8phk) {.is-info}

- Implementacion de func SelectFile() [Trello #126](https://trello.com/c/cZWzkMBR)
- Abm: Plugin NewExtendedPPL() para usar funciones de interprete en abms [Trello #126](https://trello.com/c/cZWzkMBR)
- Abms: implementacion de campo 'button' [Trello #126](https://trello.com/c/cZWzkMBR)

# 6.5.69
> [Trello](https://trello.com/c/KYah7utZ) {.is-info}

- Fix: Rango titulo no esta funcionando correctamente. [Trello #165](https://trello.com/c/2NSFMbzf)

# 6.5.68
> [Trello](https://trello.com/c/3upHe9gI) {.is-info}

- Ajustes en funcionalidad de Supervision de ABMs (Doble Confirmacion) [Trello #130](https://trello.com/c/6fpI3JDt)
- Implementacion de los campos Cantidad9 y Cantidad10 en ORDENES. [Trello #157](https://trello.com/c/dIxqJ7ol)
- Implementacion de mejora para mostrar error cuando se define un campo que no existe en la base. [Trello #161](https://trello.com/c/5MWTervk) 
- Fix: correccion de la funcion posicion. [Trello #127](https://trello.com/c/uIPfUEOA)
- Implementacion log de Cantidad de intentos fallidos. (Solo para BOFA con seguridad integrada) [Trello #125](https://trello.com/c/qOZUaatf)
- Fix: Error al bajar un informe que tiene una columna con un ACO superior a 130 a excel. [Trello #119](https://trello.com/c/EYzcvgZY)
- Fix Abm embebidos: No permitia editar registros no confirmados [Trello #103](https://trello.com/c/WG1RsuIF)
- Fix: Funciones ACLO y similares traian el script con espacios a la derecha. (Provocaba error al Cargar una Operacion OEQC en GALICIA usando el Ok+ - a verificar-). [Trello #136](https://trello.com/c/DvZUQ0Yx)
- Fix: Ejecucion de POSTEDICION cuando se creaba una operacion con 'OK+' o 'OK#' y luego se cerraba el dialogo con la 'X' [Trello #137](https://trello.com/c/DMRwcPEi)


# 6.5.67

- Fix: Lista EJECUCIONES para Ordenes. Las claves deben ser NrOrden y NrEjecucion (incremental). [#112]
- Ahora se puede especificar por config una descripcion para el entorno que aparece en el login.
- Fix: Se agrega mas informacion al mensaje de error que se emite cuando no se puede convertir un nro de oracle en .NET, ahora muestra cual es el valor y la columna del query que genera el problema. [#46]
- Se agrego campo Cupon1 en el configuration de Ordenes (Cross) [#131]
- Fix: Problema al generar jerarquias en Abm Especies (solo en PPLStudio) [#128]
- Fix filtros de abms para abms que no tienen campo Acceso (se emite warning) [#140]
- ABMS: Implementacion de plugins Alta, Baja y Modificacion [#124]
- Implementacion de funcion AuditPerfilChanges() para auditar modificaciones en items de perfil. [#124]
- Implementacion de BuscarLinkearHojas, BuscarEjecutarEventos y BuscarFunciones [#98]
- Fix: la funcion buscarEnTablas debe escapar las comillas simples [#118]

# 6.5.66

- Tag 'db_timeout' del config para parametrizar el tiempo de espera en la ejecucion de commandos en SQLServer.
- Implementacion de la funcion ExportarPdf() - recibe por parametro la ruta completa del PDF a generar.
- Fix: Lanzar error al definir campos duplicados en Operaciones (Trans, Ord, etc.)
- Implementacion persistencia seccion EJECUCIONES para Ordenes
- Fix: los campos TCbioPos y TCbioPosUnidad deben permitir ingresar mas de 1 digito (ORDENES - GALICIA)
- Implementacion de funcion AvanzarOperacion()
- Implementacion de funcion BuscarEnTablas()
- Fix: Implementacion de sobrecarga para ImprimirOperacion
- Fix: Overflow en cotizacionc
- Para ISBAN, por default no se debe pasar a mayuscula la password ingresada en el login.
- PPLStudio: Implementacion de Cambiar Fecha
- Fix: cuando ordenan la grilla en abms u ops por alguna columna, al ejecutar cualquier accion (create,read, update o delete) se pierde el orden que tenia anteriormente
- Implementacion de ventana de errores y warnings + Mejora en mensajes de errores de ejecucion y compilacion de scripts PPL.
- Fix: funcion PrimerArchivo() cuando no encuentra el path
- En Instaladores de PPLStudio y Portfolio se agrega un checkbox para acceso directo en escritorio

# 6.5.65

- Implementacion func ValidaCuit()
- Fix: se agrega la funcion Valor()
- Fix: Agregar los campos TCbioPos y TCbioPosUnidad en configuration de ORDENES (SOLO PARA GALICIA)
- Fix: PPLSync, error al detectar dirty repo
- Fix: Falla el CrearListBox si se setea una celda en vez de un rango de celdas en la definicion de la columna
- Fix: error cuando hacian referencia a una columna de una lista en un recalculo de una columna de una lista. Esto se saba con EJECUCIONES y MTMDIARIO
- Fix: se agrega el campo Cuotas1 para ORDENES
- Fix: no funcionaba la funcion sum sobre las grillas EJECOL y MTM

# 6.5.64

- Fix: no esta funcionando bien el resize de los radios en base a las opciones definidas
- Fix: el tag cotizacion_por_moneda debe ser true por default en BOFA si el mismo no esta definido en el config.json

# 6.5.63

- Fix: no se estaba actualizando el tama├▒o del radio control en base a la cantidad de elementos que muestra
- Fix: Si en el texto del Radio especificaban un texto que empezaba con pipe, borraba la primera opcion.
- Fix: agrego colores de v3 que no estaban implementados en v6
- Fix: Se corrige como se emiten las excepciones de la funcion ProcesarAgenda
- Fix: subo otra mejora para las funciones del tipo sql.actualizarmovimientos
- Fix: subo mejora de performance para las funciones del tipo sql.actualizarmovimientos
- InterfaceV6: Ejecucion de Abms
- PPLStudio: validacion de espacios en blanco en codigo de script
- PPLStudio: Los scripts nuevos por default estan habilitados
- Fix: ProcesarAgenda() ahora verifica q el nrCupon maximo generado no sea mayor a 999.

# 6.5.62

- Implementacion de la funcion IncFilaActual()
- Implementacion de licencias HASP por archivo (.pplic)
- Mejora de performance en la ejecucion de items de modelos asientos y formulas
- Fix: cuando se edita una celda de un ListboxControl los recalculos deben iniciar desde la primer columna de esa fila
- Fix: MONTOARANCELC, cuando el arancelcliente valia 0, siempre devolvia erroneamente el valor del arancel
- Fix: error en operaciones con la funcion DiasAnio2 cuando recuperaba un dato de la base que no se podia convertir a numero
- Fix: Cuando un nro tiene una mascara para resaltar en rojo los negativos, la funcion colorCeldas no lo debe afectar
- PPLStudio: Fix, habia casos donde la ayuda contextual de PMFuncs quedaba fija y era dificil sacar
- PPLStudio: Al cerrar un script sin guardar, se agrego la opcion de cancelar cuando pregunta si se desea guardar los cambios
- PPLStudio: Shorcut de cerrar editor de script con: Control + W
- PPLStudio: Fix error en PPLStudio, hacia un zoom no deseado al tipear corchetes
- PPLStudio: Posibilidad de cambiar codigo de script al editar header
- PPLStudio: Fix en PPLExplorer, al abrir un script con la tecla enter, provocaba un salto de linea no deseado en el script
- Implementacion de propiedad 'habilitado' en los scripts PPL
- Implementacion de propiedad 'orden' para scripts PPL de Eventos e Informes. Ver script: add_orden_informes_eventos.sql
- PPLStudio: PPLExpplorer: Filtro de scripts des/habilitados
- Portfolio: Orden de items de menu de Eventos e informes segun campo 'Orden'
- PPLStudio: PPLSync ignora scripts no habilitados
- PPLStudio: Warning al intentar publicar script no habilitado

# 6.5.61

- Fix: si en el parametro where de un lookup tiene un subselect, da error.
- Fix: se corrigio el msj de error que se emite cuando falla una formula o funcion, tambien se agrego el trace de scripts de funciones y formulas que son llamados por un script padre
- Fix: Funcion DiasAnio2() cuando el campo DiasAnio de la especie es string vacio
- Implementacion DetallePerfil()
- Fix: cuando habia un string literal del tipo '---' se lo interpretaba como un comment.
- Fix: Error que ocurria cuando se utilizaba una funcion sin parentensis como parametro de otra funcion. (Habiles(Hoy, 1))

# 6.5.60

- Definicion de campos de eventos e informes: TipoNegocio, Tabla, Operador2, Responsable y RazonSocial
- Agrego campos TotalImpuesto[1-2] para transacciones

# 6.5.59

- Nuevas definiciones de campos. Campo NIF de Operaciones especifico para ISBAN. (#50)
- Fix: Oracle, mejora en el mensaje de error que se emite cuando se recupera un valor numerico de la db que excede el maximo numero representable en .NET.
- Fix: Cuando no se encuentra un arancelcliente debo devolver el arancel correspondiente (MONTOARANCELC)

# 6.5.58

- Fix: los radio de interprete mostraban una opcion mas si la lista ppl especificada en el label tenia un | al final.
- Fix: subo modificacion final de la funcion MONTOARANCELC.
- Fix: audit setvariable.
- Fix: Mapper de operacion ejecuta transaction con ExecuteScalar() para que audite en los casos que se usa con app server.
- Fix: Funcion CargaJerarquia de PMJerarquia2. Faltaba traer uno de los ascendientes.
- Fix: Al publicar un script ya existente en ISBAN generaba mal la sentencia update.

# 6.5.57

- Fix: cuando teniamos controles no visibles y el siguiente control era un check o radio, no actualizaba bien su valor
- Fix: Actualizar StatusBar cuando se cancela el dialogo de un Informe/Evento
- Implementacion de la seccion MOVMTMDIARIO
- Fix: Al publicar un script ya existente en ISBAN generaba mal la sentencia update

# 6.5.56

- Fix: control autocomplete de PPLStudio, no seteaba correctamente el valor. (No aparecia el 'Tipo' al publicar un script)
- Fix: Error al guardar el valor de un campo si el casing de la definicion no coincide con el de la base de datos.
- Fix: Se agrego la firma de la sobrecarga de la funcion ImprimirOperacion
- Fix: En los dialogos de Op, Tr, Ord, etc los campos que no tienen posicion asignada varian segun tipo de script.
- Campos NrBTrans para Eventos e Informes
- Campos UDN como lookup para Op, Tr y Ord
- Apertura de items de menu Transacciones, Ordenes y Minutas Bolsa en Portfolio.
- Fix: Caso donde una Orden no ponia el flag OK en true si tenia condiciones de tipo warning y provocaba que no se ejecute seccion POSTEDICION.
- Implementacion de LOGINGRESOS y refactor USUARIOSACITVOS.

# 6.5.55

- Fix: El autosize de los radios hacen que algunos controles no se vean en el evento AGECUP (STD)
- Implementacion de la seccion DEVENGADOSCOMISIONES
- Implementacion de Modelo.TablaRC como propiedad 'Fija' del asiento item
- Campo CARTERA de Op es Radio, Cartera1 y 2 es lookup
- Fix: Ahora las formulas PPL soportan saltos de linea

# 6.5.54

- Fix: error al comparar un campo fecha en eventos e informes contra fsys
- Implementacion final de la nueva funcionalidad de las funciones Cotizacion y CotizacionC

# 6.5.53

- Fix: Habia casos donde al cerrar dialogo de una orden desde la 'X' ejecutaba la postedicion
- Fix: Error en la funcion RelacionCuenta cuando el parametro Plazo era un string vacio
- Fix: las columnas del tipo check en los listbox no toman el parametro width especificado
- Fix: los controles de tipo radio salen recortados si excede cierta longitud
- Fix: Mantener fila seleccionada al actualizar grillas de Operaciones, Trans, etc.
- PPLSync: Errores al sincronizar formulas. Ajustes en Log e interfaz
- Configuracion de campos especificos para ISBAN

# 6.5.52

- Campos de Operaciones RB de 1 a 4 ahora son radios/combos en lugar de checks
- Para GALICIA el campo CuentaComitente de ORDENES debe ser TEXT.
- Configs de definicion de campos (*.cfg) ahora son embebidos y distribuidos por cliente (segun sigla). Quedan obsoletos estos archivos en el directorio de instalacion, como asi tambien el tag 'fields_configuration' de config.json.
- Fix: error al usar la funcion PPL Fecha() dentro de un campo de la seccion LISTA
- Fix: Comparacion de Val() string con Val() null
- Fix: la funcion LiqHabitual arrojaba exception cuando el cliente no existia
- Fix: Error que se daba al comparar un valor string de la base como numero
- Implementacion funcs BookDefault2Tr() y BookDefault2Ord()
- Funcion PPL BookDefault: si se especifica TipoOp, se le da prioridad al book que lo tiene asignado explicitamente.
- Fix: ahora se puede especificar el nro inicial con el que quiero generar la agenda de cupones
- Fix: Error cuando fallaba el insert de una orden, se ejecutaba la seccion POSTEDICION
- Refactor de ventanas Lookups (Autocomplete, F2) Ahora por default se cargan los datos y la busqueda es interactiva. Si se supera el limite de 2000 registros (config 'lookup_limit'), se activa la busqueda directa a la base de datos. 

# 6.5.51

- Flag Initialized para InterfaceV6
- Funcion PPL LogWrite() para escribir en applog
- ISBAN: LoginRacf no se muestra para PPLStudio

# 6.5.50

- Fix: Error al inicializar dialogo de Interprete de forma desatendida (Se daba con InterfaceV6)
- Flag UnattendedUI para evitar mostrar elementos de la UI
- Implementacion de param EstadoCustodia en func RelacionCuenta()
- Fix: RelacionCuenta() habia un error donde en algunos casos no devolvia la cuenta
- InterfaceV6: Se agrego sobrecarga con parametro para ejecutar evento sincronico

# 6.5.49

- InterfaceV6: Agrego metodo para ejecutar evento con FieldSetup
- Fix: Abm de Modelos contables. cuando se selecciona una formula del lookup debe agregar '#'
- Fix: Formula PPL como boolean
- SuperGrid: Filtro Compliance solo para STD y BOFA
- Cuando falla ejecuci¾n de formula, mostrar el codigo
- Fix: PPLLogger no actualizaba path de usuario activo en algunos casos
- Mejoro mensajes de error cuando no se puede inicializar config

# 6.5.48

- Fix: No se mostraba mensaje de error al no poder inicializar config.json

# 6.5.47

- Fix: Seccion Reproceso fallaba cuando hay una grilla abierta.
- Concurrencia de Usuarios: chequear campo Version de USUARIOSACTIVOS
- ISBAN: Ajustos mensajes y log de SecurityProvider
- ISBAN: PPLStudio no autentica por SecurityProvider
- ISBAN: Permiso MODODESA para habilitar SuperUsr
- ISBAN: LoginRacf despues de login + Permiso especial
- Fix: '_' es un char valido para el nombre de las formulas y funciones.
- Fix: GenerarAsientoOp() Error convert int param numerador

# 6.5.46

- Warning de flag_v6 (PERFILES) solo se tiene que mostrar para ISBAN
- Fix: si en un control textbox escribiamos un valor con un espacio vacio al final, no tomaba el valor ingresado
- Fix: Error de 'no existen credenciales para el pid ...' esto se daba de forma aleatoria en BOFA (a veces en recalculos)
- Fix: los ACD estaban mostrando la hora cuando se exportaba a excel y no deben hacerlo
- Fix: se agrega el campo NrOrden hasta NrOrden4 en eventos e informes
- Ahora para versionar usamos ProductVersion del Assembly en lugar de ProductName (Sacamos nro de Build)
- Fix: Parser interprete. Habia un error aleatorio.
- Fix: Func SQLAhora como datetime devuelve la fecha de la base
- Fix: Cambiar fecha, error en validacion de fecha distinta al calendario. Ajuste fecha default.
- Fix: La funcion SqlFechaStr estaba convirtiendo las fechas en smalldatetime, haciendo que se pierdan los segundos
- Fix: Ahora por default todos los informes tienen autofit en NO, unicamente tendra valor SI si se especifica la instruccion SetPrintFit con un porcentaje menor a 100
- Fix: Cuando se realiza la validacion del control Radio, no se debe setear el foco, sino no se ve el mensaje de la validacion(banderita roja)

# 6.5.45

- Se agrego mas informacion de log (warnings) en caso de no poder interpretar el tipo de hoja que se eligio en la configuracion de impresion o en caso que la impresora no soporte el tipo de hoja seleccionado.
- Fix: Habia casos en donde la carpeta de log se creaba como archivo si no existia previamente
- Fix: Error Flag RunningOnPPLStudio, provocaba error en sincronizacion de scripts
- Fix: Se agreg¾ mas informacion de log cuando no se pueden recuperar los datos de la tabla CLAVES.
- Fix: Mensaje de Usuario no existe no se mostraba correctamente
- Perfiles: chequear permiso sobre una operacion al realizar una accion sobre ella, y tener en cuenta el permiso especial 20.
- Fix: Los eventos/Informes llamados desde operaciones no chequean permisos de perfil

# 6.5.44

- Fix: Error en ModificarOperacion cuando teniamos campos datetime con valor vacio
- Fix: Las ventanas MDI aveces no se activaban al hacer click en alguna parte del formulario.
- Fix: Cuando se exportaba a pdf lo acentos se veian con un caracter raro, tambien se eliminaron algunos bordes que se veian de la grilla al exportar a pdf
- Abm: El usuario puede hacer resize de columnas
- Portfolio: se agregaron las siguientes opciones al item de menu Actualizar aplicacion: Transacciones, Ordenes. funciones y Formulas
- Fix: Error en ABM de Perfiles al aplicar cambios.
- Fix: la funcion ModificarOperacion no recalculaba algunos campos
- Fix: Se hicieron ajustes relacionados a como se muestran los MessageBox para evitar que queden en segundo plano.
- Se holdea la implementacion de SetPrintFit por problemas de compatibilidad.
- Fix: La funcion modificarOperacion no estaba seteando el valor de la variable OK despues de su ejecucion
- Fix: La sobrecarga de la funcion ImprimirHoja(bool) no estaba ejecutando la impresion
- Funcion PPL EscritorioInteligente() devuelve true si se ejecute desde un E.Inteligente.

# 6.5.43

- Fix: La funcion ModificarOperacion no estaba recalculando bien algunos campos

# 6.5.42

- Fix: Los comandos sql ejecutados con el sql.exec no estaban siendo auditados con App server
- PPLStudio: Se agregan features de debug. Se pinta la linea de algunos errores de compilaci¾n y ejecuci¾n.
- Fix: ModificarOperacion no funcionaba correctamente el parametro que recalcula los campos
- Modificaci¾n de algunos abms reservados (Se agrega validacion de campos claves)
- Fix: Se solucionaron algunos errores relacionados a la impresi¾n (SumatraPDF)
- Fix: No se cachea ast de operaciones en PPLStudio. (No tomaba cambios de funciones)
- Fix: Se agrego funcionalidad al boton VaciarCaches del Portfolio para que borre los scripts.

# 6.5.41

- Fix: Errores al editar una Orden con Cuotas
- Fix: La funcion ImprimirHoja no hacia autofit del informe causando problemas en la impresion

# 6.5.40

- Fix: funcion ImprimirHoja no se estaban agregando los estilos al informe haciendo que se imprima sin formato
- Se agrega campo TipoOrd para Eventos/Informes
- Fix: Errores relacionados al manejo de ventanas en el Portfolio
- Ajustes de UI en busqueda contextual del Portfolio
- Se agregan los campos CuentaComitente y MinArancel para ORDENES

# 6.5.39

- Fix: Copiar SumatraPDF en directorio temporal. Provocaba error al imprimir.
- Operaciones: Truncar valores de campos numericos seg·n mßscara (enteros y decimales)
- Ordenes: Implementacion seccion de lista EJECUCIONES
- Fix: Error en Grillas con filtros cuando no hay registros
- Fix: Error configuracion de impresion al parsear tipo de hoja
- Carga rapida: Recalcular dependencias de campos seteados
- Fix: Escritorios inteligentes ejecutaba un informe con ventana maximizada
- Fix Interprete: Cancelar() dentro de funciones
- Fix Operaciones: Habia campos que no se recalculaban cuando se editaba operacion.
- Fix: Funciones de cotizacion por moneda. Contemplar parametro zero.
