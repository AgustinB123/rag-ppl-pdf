---
title: CARGILL - Pedidos que suelen hacer
description: 
published: true
date: 2021-03-03T18:33:06.201Z
tags: 
editor: markdown
dateCreated: 2021-02-17T22:28:20.325Z
---

[CARGILL - Integrity](/cargill/integrity)

# Pedidos que suelen hacer

## 1. Asignar una factura a una operación CCX solo por los intereses

Información que nos dan:

Operación CCX = 12343556
Intereses = 25406.25
NrFactura = 0122-00006706
PEmbarque = 20052EC01007144E

Lo que hay que pedir son los siguientes queries:

```
Select * from PM.INTDETCOBRANZAS 
where NrFactura = '0122-00006706'
and PEmbarque = '20052EC01007144E'

Select * from PM.MAESTROEXPO 
where NrFactura = '0122-00006706'
and PEmbarque = '20052EC01007144E'
```

Con el resultado del primer query se obtienen los campos: NrCobranza, MaestroId, NrDetIMB, NrMovBancario y NrIdenMovBan.
Con el segundo query viendo el TotalFactura y SaldoFactura, podemos determinar si la factura queda en estado "Liquidado".

#### Join entre tablas:

**INTDETCOBRANZAS C -> INTDETIDENMOVBAN DC**
C.NrDetIMB = DC.NrDetIdenMB

**INTDETCOBRANZAS C -> INTIDENMOVBAN IM**
C.NrIdenMovBan = IM.NrMov

**INTDETCOBRANZAS C -> INTMOVBANCARIOS M**
C.NrMovBancario = M.NrMov

Con todo este análisis se debe simular la asignación de la operación CCX (evento IASCCX) pero solo para los intereses (ya que el evento de Asignación de Operaciones no permite asignar solo los intereses).
Para esto, se utiliza el evento "IPRO02 - Ajustes Implementacion Integrity", para armar todos los updates e inserts que sean necesarios para la asignación de la operación.
Se envía en un pmi este evento para su testeo en QA, y con su OK, impactarlo en Producción.

## Evento IPRO02 a enviar

```
SQL.ADD(" Update "~DBO~".MAESTROEXPO Set ")
SQL.ADD("   LiquidadoFactura = LiquidadoFactura + 25406.25, ")
SQL.ADD("   SaldoFactura = SaldoFactura - 25406.25, ")
SQL.ADD("   LiquidadoEmbarque = LiquidadoEmbarque + 25406.25, ")
SQL.ADD("   SaldoEmbarque = SaldoEmbarque - 25406.25, ")
SQL.ADD("   Estado = 'LIQ'  ")
SQL.ADD(" Where MaestroId='00019753' ")
SQL.NEW
SQL.EXEC

SQL.ADD("Update "~DBO~".INTDETCOBRANZAS Set ")
SQL.ADD("   Liquidado  = NVL(Liquidado,0) + 25406.25, ")
SQL.ADD("   Estado = 'LIQ'  ")
SQL.ADD(" Where NrCobranza = '00001891' ")
SQL.NEW
SQL.EXEC

SQL.ADD(" Update "~DBO~".INTIDENMOVBAN Set ")
SQL.ADD("   Liquidado = NVL(Liquidado,0) + 25406.25, ")
SQL.ADD("   Estado = 'LIQ' ")
SQL.ADD(" Where NrMov = '00009905' ")
SQL.NEW
SQL.ADD(" Update "~DBO~".INTDETIDENMOVBAN Set ")
SQL.ADD("   Liquidado = NVL(Liquidado,0) + 25406.25, ")
SQL.ADD("   Estado = 'LIQ' ")
SQL.ADD(" Where NrDetIdenMB = '00010987' ")
SQL.NEW
SQL.ADD(" Update "~DBO~".INTMOVBANCARIOS Set ")
SQL.ADD("   Liquidado = NVL(Liquidado,0) + 25406.25 ")
SQL.ADD(" Where NrMov = '00018461' ")
SQL.NEW
SQL.EXEC

If SQL("Select Count(*) From "~DBO~".MOVEJECUTADOS Where NrOperacion='12343556' and EnteCustodia='00019753' ")>0
   SQL.ADD("Delete From "~DBO~".MOVEJECUTADOS ")
   SQL.ADD(" Where NrOperacion='12343556' and EnteCustodia='00019753' ")
   SQL.NEW
   SQL.EXEC
EndIf

SQL.ADD(" Insert Into "~DBO~".MOVEJECUTADOS ")
SQL.ADD(" (NrOperacion,  Cliente, Cantidad,     Especie, Leyenda, NrInstan, ")
SQL.ADD("  NrSaldo,      NrMov,   EnteCustodia, NrGrupo, Cuenta,  FechaMov, ")
SQL.ADD("  FechaEje,     Status,  Bits ") 
SQL.ADD(" ) Values ( ")
* NrOperacion
SQL.ADD("  '12343556', ")
* Cliente
SQL.ADD("  'GRAINOIL',   ")
* Cantidad
SQL.ADD("  25406.25, ")
* Especie
SQL.ADD("  'DOL', ")
* Leyenda
SQL.ADD("  'Liquidacion de cobranza', ")
* NrInstan
SQL.ADD("  0,  ")
* NrSaldo
SQL.ADD("  335, ")
* NrMov
SQL.ADD("  704, ")
* EnteCustodia (maestroID)
SQL.ADD("  '00019753', ")
* NrGrupo (#Orden) - Campo Orden de la tabla INTDETCOBRANZAS 
SQL.ADD("  11, ")
* Cuenta (NrCobranza/Conciliacion) - Campo NrCobranza de la tabla INTDETCOBRANZAS 
SQL.ADD("  '00001891', ")
* FechaMov - Fecha del diálogo del evento
SQL.ADD("  '"~IdxDate(Fecha('28/08/2020'))~"', ") ç
* FechaEje
SQL.ADD("  '"~IdxDate(FSYS)~"', ")
* Status
SQL.ADD("  'AUTOM', ")
* Bits
SQL.ADD("  '00010987' ")
SQL.ADD(" ) ")
SQL.NEW
SQL.EXEC

// En TotalAux4 va Cantidad + Intereses
SQL.ADD(" Update "~DBO~".OPERACIONES Set ")
SQL.ADD("   TotalAux4 = NVL(TotalAux4,0) + 30025406.25, ")
SQL.ADD("   MercadoRB = '2' ")
SQL.ADD(" where NrOperacion = '12343556' ")
SQL.NEW
SQL.EXEC

SQL.ADD(" Update "~DBO~".COMISIONES2 Set ")
SQL.ADD("   Importe3 = Importe1 + Importe4 - Importe2, ")
SQL.ADD("   Tasa3 = Importe4 - Tasa2, ")
SQL.ADD("   RB1 = '1' ")
SQL.ADD(" where NrOperacion = '12343556' ")
SQL.NEW
SQL.EXEC

EjecutarEvento('IDACCX',NrOperacion1='12343556',Check1=1)
```
