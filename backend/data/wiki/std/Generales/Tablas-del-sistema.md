---
title: Tablas del Sistema
description: 
published: true
date: 2025-11-20T12:44:35.732Z
tags: 
editor: markdown
dateCreated: 2022-03-06T22:01:08.535Z
---

# Manual de Usuario
## Tablas del sistema

### Indice

[Administración de tablas del sistema](#Adm)	

[Doble Confirmación](#DobConf)	
 * [Activación](#Acti)
 * [Configuración](#Conf)	
 * [Uso](#Uso)
 
[Principales tablas del sistema](#Ptsis)	

[Mercados](#merc)

 * [Objetivo](#Obj)	
 * [Campos](#Camp)
 * [Ejemplos:](#Ej)

[Estados de Custodia](#EstCus)	

 * [Objetivo](#obj)
 
[Cuentas](#Cuentas)

 * [Objetivo](#obj0)	
 * [Selección de cuentas](#SCuentas)
 * [Campos](#camp)
 * [Ejemplos:](#EJ)
	
[Especies](#Esp) 

 * [Objetivo](#obj1)	
 * [Campos](#Camp1)	
 
[Agenda Cupones](#Agenda)


 * [Objetivo	](#obj2)
 
[Modo especies](#ModEsp)

 * [Objetivo](#obj3)
 
[Cotizaciones](#Coti)
  * [Objetivo](#obj4)	
  * [Campos](#cmp)	
  
[Tipos Tasa](#Tipotasa)	
 * [Objetivo](#obj5)
 * [Campos](#cmp2)	

[Tasas Día](#tasa)
 
 * [Objetivo](#obj6)	
 * [Campos](#cmp3)	
 * [Actualización de tasas](#Actasas)
 
[Cotizaciones Futuro](#Cotfuturo) 

 * [Objetivo](#obj7)	

[Plazos Mercado](#Plamer)	
 * [Objetivo](#obj8)
 * [Campos](#cmp4)	
 * [Solapa General](#solgen)	
 
### Administración tablas del sistema {: #Adm}

Desde el menú **Archivo** el usuario puede administrar, dependiendo de los permisos asignados, las altas, bajas, modificaciones que desee efectuar sobre las tablas del sistema. 

También se puede acceder por el buscador:
![ingreso_abm.png](/ingreso_abm.png)

Las tablas se agrupan por funcionalidad.:
![agrupar_abm.png](/agrupar_abm.png)


### Doble Confirmación {: #DobConf}
 **Activación** {: #Acti} 

Para activar esta característica es necesario habilitar el flag **"sup_abms"** en el archivo de configuración **config.json** (Por default, es false.) Para que un usuario no pueda aprobar sus propias modificaciones (control cruzado), también se debe habilitar el flag **"ctrl_abms"** (Por default, es false).

**Configuración** {: #Conf} 

Una vez activada la funcionalidad, el usuario debe habilitar la supervisión de abms.
En la variable **DOBLECONF** se ingresan los códigos de los ABMS que desean doble supervisar (Separados por espacios) .
A los usuarios supervisores les asignan los siguientes permisos:
 * Item de menú **Supervisión**
 * Permiso 'Doble' sobre las tablas que el usuario puede supervisar. (Solapa Tablas de abm de Perfiles).

**Uso** {: #Uso} 

Al realizar una modificación en un ABM:

 * Si el código del abm está incluido en la variable **DOBLECONF**, cuando el usuario realice una acción (Alta, Baja o Modificación) se emite el siguiente mensaje:

* “El cambio realizado no estará disponible hasta que sea Aprobado por el supervisor.”

Al supervisar un cambio:

* Accediendo al ítem de menú **Supervisión** se muestra la grilla de supervisión.:
* Por default, viene aplicado el filtro de usuario **Pendientes** 
* En esta grilla, solo se puede visualizar los registros que el usuario puede supervisar.
* Desde aquí se puede Aprobar o Rechazar el cambio.

Información que se puede visualizar en la grilla:

* **Id:** Clave única del registro en supervisión.

* **Nombre:** Nombre del ABM.

* **Claves:** Valor de las claves del registro. 

* **Estado:**
   * Pendiente: Aún no fue aprobado ni rechazado
   * Aprobado: Los cambios realizados ya fueron impactados en la base.
   * Rechazado: Los cambios fueron descartados.

* **Acción:**
   * Alta: Es un registro nuevo de la tabla.
   * Mod: Se realizaron cambios sobre un registro existente.
   * Baja: El registro fue eliminado.

* **CreadoPor:** Autor del cambio realizado. (Alta, Baja o Modificación)
* **FechaCreacion:** Cuando se produjo los cambios a supervisar.
* **SupervisadoPor:** Quien aprobó o rechazó el cambio.
* **FechaSupervision:** Cuando se aprobó o rechazó el cambio.
* **Codigo:** Código del ABM.
* **Tabla:** Tabla del registro.

Al hacer doble click sobre una fila, se puede visualizar el registro con los cambios a supervisar:
Si es una modificación (no es Baja ni Alta) también, se resaltan los campos que sufrirán cambios al aprobar el registro.
Al hacer click sobre esos campos, aparece un tooltip con el valor actual en la base de datos.

### Principales tablas del sistema {: #Ptsis}
### Mercados {: #merc}

**Objetivo** {:  #Obj}

Definir los mercados de negociación, liquidación y custodia de todas las operatorias

![ndfmer_abm.png](/ndfmer_abm.png)

**Campos** {: #Camp}

**Código:** Mnemotécnico, lo elige el usuario

**Descripción:** Nombre del mercado

**Observación:** Tipos de negocio en los que puede operar el mercado. Los tipos de negocio están parametrizados por  FPA y son los definidos en la tabla Tipos de Negocio. Los valores posibles son:

![tiposnego_abm.png](/tiposnego_abm.png)

**Productos:** Productos que puede operar el mercado. Están parametrizados por  FPA y son los definidos en la tabla Tipos de Negocio. 
Los valores posibles son:

Validación: Que exista en la tabla de Tipos de Negocio

**Cliente:** Cliente contra el que se va a liquidar. Sólo se completa si el mercado es de neteo (Maeclear) o la liquidación es contra el mercado.(Rofex)
Validación: Que exista en tabla de Clientes. 

**Neteo:** Define si la liquidación se realiza siempre en forma neteada contra el mercado de liquidación . Ejemplos de mercado de Neteo: Maeclear, Argenclear

**Regulado:** Define si el mercado es regulado o no. Se utiliza exclusivamente para los futuros de moneda, para diferenciar las operaciones concertadas en los mercados regulados como Rofex y MAE de los NDF. 

**MTM:** Define si se calcula el Mark to market de forma manual (Se ingresa el MTM calculado en sistema externo)  o automatica (toma cotizaciones de mercado).  Se utiliza exclusivamente para los futuros de monedas, tasa y títulos.  Los valores posibles son:

 * No aplica
 * Automatico (Liquida)
 * Manual (No liquida)


**Frec.Liq.MTM:** Frecuencia de liquidación del MTM. Sólo es editable si en MTM se definió Liquida. Los valores posibles son:

 * Diario
 * Mensual
 * Vto
 * No liquida
 
 **Mercado Cot.:** Define el mercado de las cotizaciones que se utilizaran para el calculo automatico de MTM en mercados **NO REGULADOS**.

**Especie Fix:** Especie de fixing a utilizar en el cálculo de MTM a la fecha de vencimiento. 
Validación: Que exista en tabla de Especies. 

**Cant.DiaCotiz:** Define la cantidad de días hacia atrás que se deben considerar para calcular la fecha de fixing de la operación a partir de la fecha de vto. Sólo es editable si el mercado es no regulado.

**Tipo Dia Cotiz:** Define si Cant.Dia Cotiz corresponde a días hábiles o corridos. Sólo es editable si el mercado es no regulado.

**Tamaño del Lote:**  Define la cantidad de cada contrato. La cantidad de contratos multiplicado por el tamaño del lote da como resultado el campo V.N de las operaciones de futuro. 

**Feriados:** Define la tabla de feriados a considerar en el cálculo de fecha fixing.
Validación: Que exista en tabla de Feriados. 

**Codigo Externo1:** Define el código de conversión en el sistema externo si lo hubiera.

**Ejemplos** {: #Ej} 

Mercado de negociación - MAE:

![mae_abm.png](/mae_abm.png)

Mercado de negociación - ROFEX: 

![1rofex.png](/1rofex.png)

Mercado de negociación - BYMA:

![byma_abm.png](/byma_abm.png)

Mercado de negociación - NDF:

![ndfmer_abm.png](/ndfmer_abm.png)

Mercado de liquidación neteo - Maeclear, Mercado de Valores:

![maeclear_abm.png](/maeclear_abm.png)

Mercado de liquidación no neteo - Caja de Valores:

![cv.png](/cv.png)

Mercado de liquidación de títulos y moneda no neteo - Euroclear, CRYL:

![eu_abm.png](/eu_abm.png)

Mercado de liquidación de moneda en el exterior no neteo - SWIFT:

![swift_abm.png](/swift_abm.png)

Mercado de liquidación de moneda en mercado local  no neteo - BCRA:

![bcra_abm.png](/bcra_abm.png)

A efectos de diferenciar las operaciones de dólares divisa y dólar MEP en mercado local el usuario debe crear un mercado adicional para registrar las operaciones de dólar MEP. 



### Estados de Custodia {: #EstCus} 
 **Objetivo** {: #obj}
 
 Definir los estados en los que se puede encontrar una custodia. Los tres estados básicos son: libre disponibilidad, bloqueado o en garantía.

Libre disponibilidad: La custodia en este estado puede venderse y transferirse. 
No se le pueden asignar sub-estados.

Bloqueado:  Este es un tipo de estado, las custodias pueden tener alguno de los subestados que dependen de este tipo. Algunos tipos están parametrizados por FPA, como el bloqueo por ventas, bloqueo oficio judicial o bloqueo CV. Se utiliza para registrar las custodias que se encuentran bloqueadas por algún concepto. El usuario puede dar de alta nuevos tipos de bloqueo.

Garantía: Este es un tipo de estado, las custodias pueden tener alguno de los subestados que dependen de este tipo. Algunos tipos están parametrizados por FPA, como garantía Rofex o garantía MAE. Se utiliza para registrar las custodias que se encuentran en garantía por alguna operatoria. El usuario puede dar de alta nuevos tipos de garantía

![estcus_abm.png](/estcus_abm.png)

Cuando se da de alta un nuevo tipo de estado de bloqueo o garantía el sistema asigna automáticamente un número de saldo.
El usuario debe actualizar las variables relacionadas a los estados custodia. 



### Cuentas {: #Cuentas}
**Objetivo** {: #obj0}

Definir las cuentas de liquidación de clientes, instrucciones permanentes de contrapartes y cuentas propias de la entidad.

**Selección de cuentas** {: #SCuentas}

Cuando el sistema asigna por default una cuenta en la carga de operaciones o en los eventos de liquidación sigue los siguientes criterios:

Busca entre las cuentas que cumplen con los parámetros de cada caso: Cliente, Mercado, Especie, Tipo de cuenta, Tipo de operación, que esté habilitada.
El orden de selección es el siguiente:
 *  	Dentro de las cuentas que cumplan todos los parámetros seleccionará primero entre las cuentas que tengan el campo “Cta. Default” en “SI” 
 *  	Si más de una cuenta tiene la marca, toma la primera ordenada por código en forma ascendente.
 *  	Si no existe ninguna con la marca de “Cta. Default” selecciona la primera dentro de todas las que no tengan la marca, ordenadas por código en forma ascendente

**Definición de cuenta default**
El usuario puede definir una cuenta como default marcándola en la solapa General:

![ctadef_abm.png](/ctadef_abm.png)

Cuando el usuario marca una cuenta default,  ésta cuenta tiene prioridad respecto a otras del mismo tipo en la carga de operaciones y en los eventos de liquidación.


Ejemplos:

![ejemplos.png](/ejemplos.png)

**Campos** {: #camp} 

**Solapa General**

![cuentas_abm.png](/cuentas_abm.png)

**Código:** Memotécnico definido por el usuario, se visualiza en las operaciones y transacciones.

**Nombre:** Nombre de la cuenta, descripción

**Número:** Número de cuenta 

**Cliente:** Cliente de la tabla de Clientes al que pertenece la cuenta. Puede ser un cliente de la entidad, una contraparte o la entidad.

**Merc./ Cle:**  Mercado o Clearing house a la que pertenece la cuenta.

**Depositante:** Nombre del depositante de la cuenta en la clearing house.  Debe ser un cliente de la tabla de Clientes. Sólo aplica en cuentas custodia.

**Comitente:** Número de comitente en CV. Sólo aplica en cuentas custodia en CV.

**Corresponsal destino:** Corresponsal de la cuenta. Debe existir en la tabla de Corresponsales. Sólo aplica en cuentas tipo Swift. 

**Tit.Alternativo:** Títular alternativo.Sólo aplica en cuentas tipo Swift. 

**Interfase Automática:** Identifica las cuentas que se reciben por una interfaz y no se ingresan manualmente.

**Tipo Operación:** Tipos de operación que se liquidan por esta cuenta. Si la cuenta no tiene restricciones por tipo de operación es vacío.

**Especies:** Especies que se liquidan por esta cuenta. Si la cuenta es bimonetaria se ingresan las dos monedas, sino se ingresa la moneda de la cuenta. En caso de los títulos se ingresa la jerarquía de títulos. Si se quisiera usar una cuenta distinta para los bonos y para las acciones se generan dos cuentas y a cada una se le asigna una jerarquía distinta. En el caso de los mercados que liquidan títulos y moneda se ingresan las jerarquías y las monedas.

**Tipo transacción:** Tipos de transacción  que se liquidan por esta cuenta. Si la cuenta no tiene restricciones por tipo de transacción es vacío. Se refiere a las transacciones manuales, no a las transacciones operativas (generadas por la liquidación de operaciones)

**Solapa Adicional**

![cuentas2_abm.png](/cuentas2_abm.png)

**Estado:**  Define el estado de la cuenta. Los estados posibles son: 

* Habilitada
* Suspendida
* Cerrada 
* Pendiente

Las cuentas habilitadas son las únicas que se pueden seleccionar en la carga de operaciones y en eventos de liquidación.

**Alias 1:** Define si la cuenta es o no de CP. Si es cartera propia debe contener CP. Si es de terceros debe contener TER.

**Sub cuenta CV:** Subcuenta en CV. Se utiliza en la interfase a CV

**Alias 3:**  Descripción de la cuenta

**ABA:**  Código que identifica a bancos estadounidenses

**Chip:** Código que identifica el banco de la cuenta

**Fedwire:** Sin uso

**Repetitivo:** Sin uso

**M.Liquidación:**  Se usa exclusivamente para identificar a esta cuenta para la operatoria de dólar MEP.
 
**Cta.Contable:**  Cuenta contable donde se desea registrar un movimiento correspondiente a esta cuenta operativa.

*Cta.Contable 2:** Sin uso

**Tipo:** Identifica el tipo de cuenta.  Los valores posibles son:
* Cuenta corriente
* Caja de ahorro
* Custodia
* Vista
* C.Propia
* Caja
* Inversor
* F.Común
* Cta.Cte
* Otros


**Solapa Integrantes**
Sin uso

**Ejemplos:**  {: #EJ}

Cuenta propia en CV:
![ctacv_abm.png](/ctacv_abm.png)![ctacv2_abm.png](/ctacv2_abm.png)

Cuenta propia en EU
![ctaeu_abm.png](/ctaeu_abm.png)![ctaeu2_abm.png](/ctaeu2_abm.png)

Cuentas de liquidación dólar MEP
![cuentaliquidaciondolarmep.png](/cuentaliquidaciondolarmep.png)

### Especies {: #Esp}
**Objetivo**  
Definir las especies que se utilizan en la operatoria de la entidad. En esta tabla se ingresan distintos tipos de especies:
 * Monedas
 * Títulos
 * Índices

Esa es la jerarquía básica. Dentro de esas jerarquías el usuario puede abrir subjerarquias con el objetivo de categorizar las especies.

En el caso de los dólares y euros se dan de alta dos especies: divisa y billete.

Cuando se ingresa una especie por primera vez se le otorga automáticamente un número de Jerarquía que describe su posición respecto al resto de las especies. La correcta clasificación de la especie también influye en el funcionamiento de restricciones operativas e informes.

Para dar un alta se puede presionar el botón de “Agregar” (signo más verde) o también al hacer  “click” con el botón derecho del Mouse sobre la grilla se despliega un menú con las opciones de:

* Alta: Se abre ventana para dar de alta una nueva especie
* Agregar Similar: Se genera una nueva especie con los mismos datos que la seleccionada, con el código en blanco. El usuario debe ingresarlo para dar de alta la especie.
* Baja:Se abre ventana para confirmar la baja de la especie.
* Modificación: Se abre ventana para modificar la especie
* Buscar: Se abre ventana para ingresar parámetro de búsqueda
* Quitar Filtros: Permite quitar los filtros existentes
* Jerarquía: Permite reubicar la especie en otra jerarquía
* Copiar Especie

Algunas opciones pueden faltar, ya que esto depende del perfil del usuario.

![especies_abm.png](/especies_abm.png)

**Campos** {: #Camp1}

Los datos de las especies se encuentran agrupados en solapas que describen sus distintos aspectos. Estas son: General, Adicional, Datos, Variables, Series, Cupones y Observaciones. Determinados datos deben ser cargados para que el sistema se comporte correctamente. 

**Solapa General** 

![solapageneralespecies1.png](/solapageneralespecies1.png)

**Jerarquía:**  Jerarquía a la que pertenece la especie.  
**Nombre:**  Nombre de la jerarquía. 
Las jerarquías y nombres de las jerarquías predeterminadas no son editables.

**Código Especie:** Código mnemotécnico elegido por el usuario

**Nombre:** Nombre resumido de la especie

**Cupón:** Cupón vigente de la especie. Cuando se da de alta se puede optar por poner el cupón 1 o el vigente.  Si se ingresa el cupón 1 el usuario debe generar la agenda a partir del cupón 1 y hacer todas las actualizaciones de especie  hasta la fecha de alta. Si se ingresa el cupón vigente  el usuario debe generar la agenda a partir de este cupón. En este caso el sistema no va a permitir operar fecha valor. 

**Nom.Extendido:** Nombre extendido de la especie

**Cotiza en:** Moneda de cotización de la especie de la tabla Especies

**Fecha emisión:**  Fecha de emisión

**Fecha maduración:** Fecha de vto de la especie

**Grupo Especies:**  Grupo de especies de la tabla de Grupo Especies

**Mon Emisión:** Moneda de emisión de la especie de la tabla Especies

**Estado PME:**  Dato proveniente de PME 

**Cod.Sist.Externo:** Código de relación con Raiden

**Tenor Sist.Externo:** Se usa para ICL

**Status:** Habilitada/Deshabilitada. Para operar debe estar habilitada

**Cotiza:** Clean/Dirty. Si la especie es clean en el alta de la operación el sistema calcula los intereses corridos y calcula el precio dirty. Si la especie es dirty el precio ingresado se considera dirty. Lo mismo aplica para el ingreso de las cotizaciones
 
**Cotiza Mae:** Clean/Dirty. Define cómo se informa el precio al MAE. 

**Country:** Define el country para la afectación del Límite country. El country es un cliente de la jerarquía países de la tabla Clientes 
**Issuer:**  Define el issuer para la afectación del Límite issuer.  El issuer es un cliente de la tabla Clientes.

**País:** Define el  país para la afectación del Límite país. El país pertenece a la tabla Países.

**Indexado:** Indica si el bono es indexado o no

**Índice:** Se despliega sólo si el bono es indexado. Es una especie de la jerarquía Índices de la tabla Especies.

**Tasa:** Indica si la tabla es fija o variable: 

El detalle de estos campos para cada los diferentes tipos de títulos se encuentra en el Manual de eventos corporativos.

**Solapa Adicional**

![solapaadicionalespecies_01g](/solapaadicionalespecies_01.png)

**Tamaño del lote:** Es el tamaño del lote de la especie. Actualmente sin uso. 

**Valor residual:** Valor residual del bono. Al dar de alta se ingresa el correspondiente al cupón ingresado, se actualiza automáticamente al ejecutar el evento Actualización de Especies. Debe ser 1 si la especie no amortizo.

**Mercado Liq.:** Mercado de liquidación más usual. Se toma como default en el alta de operación.

**ISIN:** Código ISIN de la especie

**CUSIP:** Código CUSIP de la especie

**Cedel:** Código Cedel de la especie

**Euroclear:** Código Euroclear de la especie

**SWIFT:** Código SWIFT de la especie

**Mes:** Mes utilizado en el cálculo de intereses. Valores posibles: 30; real; 30E; 30E+1
[](/mesespecie.png)
**Año**: Año utilizado en el càlculo de intereses. Valores posibles: 360; 365; real
[](/añoespecie.png)
**F.Cambio Tasa:** Sin uso

**Tasa Vigente:** Sin uso

**Tasa Anterior:** Sin uso

**F. ini. tenencia:** campo utilizado para la generación de Titofin

**Solapa Datos**
![solapadatosespecies1.png](/solapadatosespecies1.png)

**Código BYMA ARP:** Código BYMA de la especie

**Cod.Num.Caja:** Código de bolsa numérico de la especie

**Lámina Mínima:** Lámina mínima, en el alta de operación se valida que el VN sea múltiplo de este valor.

**Porcentaje aforo:** Porcentaje de aforo en pases

**Aforo pesos:** Sin uso

**Aforo dólares:** Sin uso

**Cod. MAE Contado:** Código MAE de la especie. Este código se usa en las interfases con Siopel.

**Especie Fixing:** Sin uso. Se reemplazó por información tabla Mercados

**Especie Rofex:** Sin uso. Se reemplazó por información tabla Mercados

**ISO:** Sin uso

**MLCode:** Código propio de MLASA. Se utiliza en las vistas

**BBG Code:** Código Bloomberg. Se utiliza en las interfases con Raiden y PME.

**Tipo:** Tipo de especie.
[](/tipoespecie.png)
**Tipo EC:** Escritular o Cartular

**Tipo Cartera:** Tipo de cartera de la especie. Es informativo. Valores posibles: Agresiva/Moderada/Conservadora

**Plazo Vto:** Plazo de vencimiento habitual de la especie. Se usa como default en el alta de operaciones. Se especifica en horas

**Tipo de títulos:** Tipo de título interno de MLASA. Valores posibles:

![tipodetitulos.png](/tipodetitulos.png)

**Solapa Variables**

![solapavariablesespecie1.png](/solapavariablesespecie1.png)

**Especie Cupón:** En el caso de títulos indica la especie cupón asociada. En el caso de la especie cupón indica la especie original.

**Tipo Neg.Licita:** Se usa en  la operatoria de Licitaciones

**Solapa Series**

Sin uso en MLASA. Se utiliza en Opciones

**Solapa Cupones** 

![solapacuponesespecie1.png](/solapacuponesespecie1.png)

**Es cupón:** Indica si la especie es cupón.

**Zero coupon:** Indica si la especie es zero cupón. 

**Generar cupón:** Al dar de alta una especie se puede generar el cupón en forma automática tildando este campo. Una vez dada de alta la especie este campo no tiene utilidad. Si no se tildó en el alta no se puede generar cupón modificándolo posteriormente.

El resto de  los campos no se ingresan manualmente. Se modifican en cada proceso de actualización de especie.


 **Solapa Observaciones**

El usuario puede ingresar un texto informativo.

### Agenda Cupones {: #Agenda}

**Objetivo**

Definir el calendario de vencimiento de las especies que se utilizan en la operatoria de la entidad.
Una vez creada la especie en el caso de los títulos públicos que no sean zero coupon el usuario debe dar de alta la agenda de vencimientos de la especie.
En el caso de zero coupon si el usuario indica la condición en el alta de la especie la agenda se genera automáticamente.  

### Modo especies {: #ModEsp}

**Objetivo** {: #obj3}

Definir cómo se expresa cada moneda respecto a otra, si en forma directa o inversa. Se utiliza en todos los cálculos donde se consideran cotizaciones. 

![modo_especies1.png](/modo_especies1.png)

### Cotizaciones {: #Coti}
**Objetivo** {: #obj4}

Definir las cotizaciones de cada especie. En esta tabla se ingresan cotizaciones spot para monedas, títulos e índices. Las cotizaciones de futuros se ingresan en la tabla de Cotizaciones futuro y las tasas en la tablas Tasas Dia. La carga puede ser manual desde el ABM. También se reciben las cotizaciones de cierre del MAE. Cada cotización que se ingresa ya sea en forma manual automática actualiza la cotización de la tabla, quedando registrada la última ingresada.

**Campos** {: #cmp}

**Solapa General**

![cotizaciones_solapa_general.png](/cotizaciones_solapa_general.png)

**Fecha:** Fecha de la cotización

**Cod.especie:** Especie de la cotización

**Precio cierre:** Último precio de la especie

**Última:** Fecha de ingreso de la cotización

**Moneda:** Moneda en que está expresada la cotización 

El resto de los campos no se utilizan en esta instalación.

**Solapa Adicional**

![cotizaciones_solapa_adicional.png](/cotizaciones_solapa_adicional.png)

**P.Contable:** Cotización utilizada en la contabilidad. 
En el caso de monedas se ingresa manualmente el precio BNA.

### Tipos de Tasa {: #Tipotasa}

**Objetivo** {: #obj5}

Definir los tipos de tasa operados en el mercado y que se utilizan en el sistema.

![tipostasa_abm.png](/tipostasa_abm.png)

**Campos** {: #cmp2}

![tipostasamod_abm.png](/tipostasamod_abm.png)

**Código:** Código mnemotécnico del tipo tasa 

**Nombre:** Descripción del tipo tasa

**Especie válida:** Moneda a la que se aplica el tipo tasa. Puede ser blanco si aplica a todas. Ejemplo: Tasa fija

**Base:** Base de cálculo del interés

**Cod.Tasa Ext:** Código de tasa del sistema externo. Se utiliza para relacionar el tipo tasa con las tasas recibidas desde un sistema externo de información. Ejemplo:

![codigotiposdetasa.png](/codigotiposdetasa.png)

### Tasas dia {: #tasa}
**Objetivo** {: #obj6}

Definir las tasas diarias para cada tipo de tasa. 

![tasasdia_abm.png](/tasasdia_abm.png)

**Campos** {: #cmp3}

**Solapa General**
![tasasdiasolapageneral.png](/tasasdiasolapageneral.png)

**Fecha:** Fecha de la tasa

**Especie:** Moneda a la que se aplica la tasa.

**Tipo Tasa:** Tipo de tasa a la que se aplica la tasa.

**Plazo desde:** Plazo mínimo al  que se aplica la tasa.

**Plazo hasta:** Plazo máximo al  que se aplica la tasa.

**Solapa Valores**
![tasasdiasolapavalores.png](/tasasdiasolapavalores.png)

**Valor 1:**  Tasa expresada en porcentaje

El resto de los campos no tiene uso.

**Actualización de tasas** {: #Actasas}

Las tasas se pueden ingresar en forma manual o automáticamente tomando como fuente un archivo excel.


**Evento de Importación de tasas**
![importaciondetasas.png](/importaciondetasas.png)

Este evento agrega las tasas inexistentes en la tabla Tasas Dia y actualiza las existentes.

### Cotizaciones Futuro {: #Cotfuturo}

**Objetivo** {: #obj7}

Definir las cotizaciones de futuros en los distintos mercados. 

**Campos**

**Solapa General**

![cotfuturo_abm.png](/cotfuturo_abm.png)

**Fecha Cotización:** Fecha de la cotización

**Cod.especie:** Especie de la cotización

**Moneda:** Moneda en que está expresada la cotización 

**Fecha Cotización:** futuro (identificado por su fecha de vencimiento) al que corresponde la cotización

**Mercado:** Mercado al que corresponde la cotización 

**Close:** Precio del futuro 

El resto de los campos no se utilizan en esta instalación

### Plazos Mercado {: #Plamer}

**Objetivo** {: #obj8}

Definir los plazos de futuros de cada mercado.  Los plazos se generan en forma automática en función a la información recibida de los mercados regulados. también se pueden dar de alta en forma manual cuando los plazos no se reciben o se reciben incorrectamente. También se puede modificar la fecha de vencimiento de algún plazo existente cuando hay feriados imprevistos.

**Campos** {: #cmp4}

**Solapa General** {: #solgen}

![plazosmer_abm.png](/plazosmer_abm.png)

**Mercado:** mercado del plazo

**Fecha Vto:** fecha de vencimiento del futuro a la que corresponde el plazo configurado

**Especie:** Especie del futuro

**Nombre:** código con el que el mercado identifica a este futuro (definido por mercado, especies y fecha de vencimiento). Las operaciones y las cotizaciones futuro recibidas por el mercado se identifican  con el mismo.


El resto de los campos no se utilizan en esta instalación.





