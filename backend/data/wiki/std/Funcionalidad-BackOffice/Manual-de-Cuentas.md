---
title: Manual De Cuentas
description: 
published: true
date: 2024-09-10T14:38:04.161Z
tags: 
editor: markdown
dateCreated: 2024-09-10T14:08:26.992Z
---

# Manual Del Usuario	

## Manual de cuentas

### Indice 

[Objetivo](#Obj)
[Selección de cuentas	](#Selec)

[MAE-CPC1](#CPC1)
[Cuenta Moneda vehículo](#CtaMon1)
[Cuenta Título Vehículo](#CtaTitul1)

[BYMA - SDIB](#SDIB)
[Cuenta Moneda vehículo](#CtaMon2)
[Cuenta Título vehículo](#CtaTitul2)

[MAE-TRD](#TRD)
[Cuenta Moneda vehículo](#CtaMon3)
[Cuenta título vehículo](#CtaTitul3)

[BYMA-SENEBI](#SENEBI)
[Cuenta Moneda vehículo](#CtaMon4)
[Cuenta título vehículo](#CtaTitul4)

### Objetivo {: #Obj}

Definir las cuentas vehículo al momento de liquidar operaciones concertadas en los  mercados MAE/BYMA.  (CPC1-SDIB-TRD-SENEBI-SISTACO).


### Selección de Cuentas {: #Selec}

Se deberán dar de alta 3 cuentas por mercado/moneda en concepto de monto de la operación, comisiones y derechos.

Las cuentas de liquidación del vehículo no se seleccionan desde el alta de la orden/operación, se toman por default en el evento “Neteo-Preliquidación”. 
Cuando el sistema asigna por default una cuenta VEHÍCULO en los eventos de liquidación sigue los siguientes criterios:

Busca entre las cuentas que cumplen con los parámetros de cada caso: Cliente, Alias 1 ,Mercado de Negociación, Mercado de liquidación, Especie, Tipo y que esté habilitada.
El orden de selección es el siguiente:
1) Dentro de las cuentas que cumplan todos los parámetros seleccionará primero entre las cuentas que tengan el campo “Cta. Default” en “SI” 
2) Si más de una cuenta tiene la marca, toma la primera ordenada por código en forma ascendente.
3) Si no existe ninguna con la marca de “Cta. Default” selecciona la primera dentro de todas las que no tengan la marca, ordenadas por código en forma ascendente
Para más detalle de cómo seleccionar una cuenta por default consultar manual “Generales - Tablas del sistema”. 


### MAE - CPC1 {: #CPC1}

**Cuenta Moneda Vehículo**  {: #CtaMon1} 

![maecpc01.png](/maecpc01.png)

**Campos Obligatorios**
**Código:** Mnemotécnico definido por el usuario, se visualiza en las operaciones y   transacciones.
**Cliente:** Debe ser el vehículo. 
**Merc. / Cle. :** “BCRA”	
Especie: Ingresar especie moneda para la cual se quiere asignar la cuenta. 
**Alias 1:** “TER”, “COM” o “DER” según corresponda. Para capital “TER” , “Comisión” COM y derechos “DER”. 
**M. Negociación:** “MAE” 
**M.Liquidación :** “BCRA”
**Tipo:**  “C.A” , “Cta. Cte”. 

**Cuenta Título Vehículo** {: #CtaTitul1}

![maecpc02.png](/maecpc02.png)

**Campos Obligatorios**
**Código:** Mnemotécnico definido por el usuario, se visualiza en las operaciones y   transacciones.
**Cliente:** Debe ser el vehículo. 
**“Merc- /Cle.” :** “MC”
**Alias 1:** “TER” .  Si es necesario utilizar la misma cuenta para CPC1 y TRD(MC)  también se debe ingresar “CP” . Ejemplo :  “TER|CP”
**M. Negociación:** “MAE”
**Especie:** Ingresar especie para la cual se quiere asignar la cuenta. 
**Tipo:**  “Custodia”.

### BYMA - SDIB {: #SDIB}

**Cuenta Moneda Vehículo** {: #CtaMon2}

![bymasdib01.png](/bymasdib01.png)

**Campos Obligatorios**
**Código:** Mnemotécnico definido por el usuario, se visualiza en las operaciones y   transacciones.
**Cliente: Debe ser el vehículo. 
**“Merc- /Cle.” :** “BCRA”
**Alias 1:** “TER”, “COM” o “DER” según corresponda. Para capital  “TER” , “Comisión” COM y derechos “DER”. 
**M. Negociación:** “BYMA”	
**M.liquidación :** “BCRA” 		 
**Especie:** Ingresar especie moneda para la cual se quiere asignar la cuenta. 
**Tipo:**  “C.A” , “Cta. Cte”. 

**Cuenta Título Vehículo** {: #CtaTitul2}

![bymasdib02.png](/bymasdib02.png)

**Campos Obligatorios**
**Código:** Mnemotécnico definido por el usuario, se visualiza en las operaciones y   transacciones.
Cliente: Debe ser el vehículo. 
**“Merc- /Cle.” :** “MV”
**Alias 1:** “TER” 
**M. Negociación:** “BYMA”
**M.Liquidación:** “CV” .
**Especie:** Ingresar especie para la cual se quiere asignar la cuenta. 
**Tipo:**  “Custodia”. 

### MAE - TRD {: #TRD}

En el alta de operaciones con mercados de liquidación  MC-MC se asignan las mismas cuentas tanto para el cliente como para el vehículo. Sin embargo, al momento de realizar la liquidación, las cuentas del vehículo se ajustarán a las correspondientes cuentas propias. Esto asegura que la tenencia de la contraparte no se vea afectada, mientras que se actualizan correctamente las propia.

**Cuenta Moneda Vehículo** {: #CtaMon3}

![maetrd01.png](/maetrd01.png)

**Campos Obligatorios**
**Código:** Mnemotécnico definido por el usuario, se visualiza en las operaciones y   transacciones.
**Cliente:**  MAECLEAR. 
**“Merc- /Cle.” :** BCRA
**Alias 1:** “CP” 
**M. Negociación:** “MAE”
**M.Liquidación:** “MC” .
**Especie:** Ingresar especie moneda para la cual se quiere asignar la cuenta. 
**Tipo:**  “C.A” o ”C.CTE”. 

**Cuenta Título Vehículo** {: #CtaTitul3}

![maetrd02.png](/maetrd02.png)

**Campos Obligatorios**
**Código:** Mnemotécnico definido por el usuario, se visualiza en las operaciones y   transacciones.
**Cliente:**  VEHÍCULO. 
**“Merc- /Cle.” :** “MC”
**Depositante:** “MAECLEAR”
**Alias 1:** “CP” 
**Especie:** Ingresar especie moneda para la cual se quiere asignar la cuenta. 
**Tipo:**  “C.A” o ”C.CTE”. 

### BYMA - SENEBI {: #SENEBI}

En el alta de operaciones con mercados de liquidación  MV-MV se asignan las mismas cuentas tanto para el cliente como para el vehículo. Sin embargo, al momento de realizar la liquidación, las cuentas del vehículo se ajustarán a las correspondientes cuentas propias. Esto asegura que la tenencia de la contraparte no se vea afectada, mientras que se actualiza correctamente la propia.

**Cuenta Moneda Vehículo** {: #CtaMon4}

![bymasenebi01.png](/bymasenebi01.png)

**Campos Obligatorios**
**Código:** Mnemotécnico definido por el usuario, se visualiza en las operaciones y   transacciones.
**Cliente:**  MVAL. 
**“Merc- /Cle.” :** BCRA
**Alias 1:** “CP” 
**M.Liquidación:** “MV” .
**Especie:** Ingresar especie moneda para la cual se quiere asignar la cuenta. 
**Tipo:**  “C.A” o ”C.CTE”. 

**Cuenta Título Vehículo** {: #CtaTitul4}

![bymasenebi02.png](/bymasenebi02.png)

**Campos Obligatorios**
**Código:** Mnemotécnico definido por el usuario, se visualiza en las operaciones y   transacciones.
**Cliente:** Debe ser el vehículo. 
**“Merc- /Cle.” :** “MV”
**Alias 1:** “TER” 
**M. Negociación:** “BYMA”
**M.Liquidación:** “CV” .
**Especie:** Ingresar especie para la cual se quiere asignar la cuenta. 
**Tipo:**  “Custodia”. 