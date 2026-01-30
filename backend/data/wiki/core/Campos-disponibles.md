---
title: Campos disponibles
description: 
published: true
date: 2021-11-16T15:11:02.902Z
tags: 
editor: markdown
dateCreated: 2019-11-27T18:37:32.922Z
---

# Campos defaults

## Eventos e Informes

### Lookups
| Nombre | Tabla | Clave | Campos visibles | Tamaño default |
| ------ | ------ | ------ | ------ | ------ |
| Especie[1-9] | Especies | Codigo | Codigo,Nombre,Extendido,ISIN,CUSIP |  |
| TipoOp[N-9] | TiposOperacion | Codigo | Codigo,Nombre |  |
| TipoTr[1-4] | TiposTransaccion2 | Codigo | Codigo,Nombre |  |
| TipoOrd[1-3] | TiposOrden | Codigo | Codigo,Nombre |  |
| Mercado[N-7] | Mercados | Codigo | Codigo,Descripcion |  |
| Cliente[1-5] | Clientes | Codigo | Codigo,RazonSocial,NrMAE,NrCuenta |  |
| Operador[N-2] | Usuarios | Codigo | Codigo,Nombre |  |
| ContraEspecie[N-7] | Especies | Codigo | Codigo,Nombre,Extendido,ISIN,CUSIP |  |
| TipoDocumento[1-2] | Documentos | Codigo | Codigo,Descripcion |  |
| NrOrden[N-4] | Ordenes | NrOrden | NrOrden,TipoOrden,Especie |  |
| NrTrans[1-20] | Transacciones2 | NrTrans | NrTrans,TipoTr2,Especie,Cliente1 |  |
| NrOperacion[N-9] | Operaciones | NrOperacion | NrOperacion,TipoOp,Especie,FechaOp,Cliente1 |  |
| NrOperacionRef[1-10] | Operaciones | NrOperacion | NrOperacion,TipoOp,Especie,FechaOp,Cliente1 |  |
| TablaFeriados[1-2] | Feriados | Codigo | Codigo,Descripcion |  |
| Vehiculo[1-4] | Vehiculos | Codigo | Codigo,Descripcion |  |
| Cartera[N-2] | Carteras | Codigo | Codigo,Descripcion |  |
| Cuenta[1-5] | Cuentas | Codigo | Codigo,Nombre,Numero |  |
| Pais[N-2] | Paises | Codigo | Codigo,Nombre |  |
| CuentaContable[1-2] | Contabilidad | Codigo | Codigo,Nombre,Tipo,Cliente |  |
| Book[1-2] | Books | Codigo | Codigo,Descripcion |  |
| Usuario[1-2] | Usuarios | Codigo | Codigo,Nombre |  |
| Corredor[N-2] | Corredores | Codigo | Codigo,Nombre |  |
| NrBOperacion[N-2] | BOperaciones | NrOperacion | NrOperacion,TipoOp,Especie,FechaOp,Cliente1 |  |
| NrBTrans[N-2] | BTransacciones2 | NrTrans | NrTrans,TipoTr2,Especie,Cliente1 |  |
| OpSIOPEL | OperadoresSIOPEL | CodOperador | CodOperador,NomOperador,AgenteMAE |  |
| Feriado[1-2] | Feriados | Codigo | Codigo,Descripcion |  |
| NrProducto[N-2] | Productos2 | NrProducto | NrProducto,TipoProducto,Especie,TotalAux1 |  |
| GrupoEspecie[N-2] | GruposEspecie | Codigo | Codigo,Descripcion |  |
| Perfil[1-2] | Perfiles2 | Codigo | Codigo,Nombre |  |
| Sucursal[N-2] | Sucursales | Codigo | Codigo,Nombre |  |
| NrUnicoAsiento[N-2] | ASIENTOSCON | NrUnicoAsiento | NrUnicoAsiento,NrAsiento,NrOperacion,FechaGeneracion |  |
| TipoAsiento[N-2] | TIPOSASIENTO | Codigo | Codigo,Descripcion |  |
| ModeloAsiento[1-10] | ModelosAsiento | Codigo | Codigo,Descripcion |  |
| ConceptoBCRA[1-2] | ConceptosBCRA | Codigo | Codigo,Descripcion |  |
| Informe[1-2] | Informes | Codigo | Codigo,Nombre |  |
| Evento[1-2] | Eventos | Codigo | Codigo,Nombre |  |
| Funcion[1-2] | Funciones | Codigo | Codigo,Descripcion |  |
| TipoNegocio[1-2] | TiposNegocio | Codigo | Codigo,Descripcion |  |
| RazonSocial | Clientes | RazonSocial | RazonSocial,Codigo | 200 |
| Responsable[1-2] | Responsables | Codigo | Codigo,Descripcion |  |
| TipoPosicion[1-5] | TiposPosicion | Codigo | Codigo,Descripcion |  |
| TipoLimite[1-5] | TiposLimite | Codigo | Codigo,Descripcion | 100 |

### Numericos

| Nombre | Mascara default |
| ------ | ------ |
| Cantidad[N-20] | ##,###,###,###,###.## |
| ENTERO[1-50] | ######### |
| Cotizacion[1-2] | #########.####### |
| Precio[1-30] | #########.##### |
| Cupon[1-2] | |

### Texto

| Nombre | Max input Length |
| ------ | ------ |
| Observac[1-7] |  |
| STRING[N-20] |  |

### Resto de los controles

| Nombre | Tipo |
| ------ | ------ |
| RADIO[1-20] | COMBO |
| FECHA[1-20] | DATE |
| CHECK[1-20] | CHECK |
| LABEL[1-20] | LABEL |
| LISTA[1-20] | LIST |
| LISTACLAVES[N-5] | LISTCLAVE |
| ListaTabla[1-4] | TABLE_LIST |
| Archivo[N-9] | FILEPATH |
| Directorio[N-9] | DIRECTORYPATH |

## Operaciones

### Lookups

| Nombre | Tabla | Clave | Campos visibles |
| ------ | ------ | ------ | ------ |
| Especie[N-5] | Especies | Codigo | Codigo,Nombre,Extendido,ISIN,CUSIP |
| TipoOp[N-2] | TiposOperacion | Codigo | Codigo,Nombre |
| NrOperacion[N-6] | Operaciones | NrOperacion | NrOperacion,TipoOp,Especie,FechaOp,Cliente1 |
| Mercado[N-4] | Mercados | Codigo | Codigo,Descripcion |
| Cliente[1-5] | Clientes | Codigo | Codigo,RazonSocial,NrMAE,NrCuenta |
| Operador[N-1] | Usuarios | Codigo | Codigo,Nombre |
| ContraEspecie[N-7] | Especies | Codigo | Codigo,Nombre,Extendido,ISIN,CUSIP |
| TipoDoc | Documentos | Codigo | Codigo,Descripcion |
| TipoTasa[N-3] | TiposTasa | Codigo | Codigo,Nombre |
| OperacionRef | Operaciones | NrOperacion | NrOperacion,TipoOp,Especie,FechaOp,Cliente1 |
| NrOrden[N-1] | Ordenes | NrOrden | NrOrden,TipoOrden,Especie |
| Corredor[N-2] | Corredores | Codigo | Codigo,Nombre |
| TablaFeriados[1-2] | Feriados | Codigo | Codigo,Descripcion |
| Vehiculo[1-2] | Vehiculos | Codigo | Codigo,Descripcion |
| ConceptoBCRA | ConceptosBCRA | Codigo | Codigo,Descripcion |
| Cuenta[1-5] | Cuentas | Codigo | Codigo,Nombre,Numero |
| PrecioRef[N-4] | PreciosRef | Codigo | Codigo,Descripcion |
| Sector[1-2] | Sectores | Codigo | Codigo,Descripcion |
| Centro[1-2] | CentrosCosto | Codigo | Codigo,Descripcion |
| Contrato | Contratos | Codigo | Codigo,Descripcion |
| Pais | Paises | Codigo | Codigo,Nombre |
| CuentaContable[1-2] | Contabilidad | Codigo | Codigo,Nombre,Tipo,Cliente |
| Indice | Indices | Codigo | Codigo,Descripcion |
| Book[1-2] | Books | Codigo | Codigo,Descripcion |
| OpSIOPEL | OperadoresSIOPEL | CodOperador | CodOperador,NomOperador,AgenteMAE |
| Cartera[1-2] | Carteras | Codigo | Codigo,Descripcion |
| NrProducto | Productos2 | NrProducto | NrProducto,TipoProducto,Especie,TotalAux1 |
| UDN[1-2] | UDNS | Codigo | Codigo,Descripcion |
| TipoLimite | TiposLimite | Codigo | Codigo,Descripcion |
| Sublimite | SubLimites | Codigo | Codigo,Descripcion |
| Responsable1 | Responsables | Codigo | Codigo,Descripcion |
| TipoPosicion | TiposPosicion | Codigo | Codigo,Descripcion |
| Sucursal | Sucursales | Codigo | Codigo,Nombre |
| NrTrans[1-5] | TRANSACCIONES2 | NrTrans | NrTrans,TipoTr2,Especie,Cliente1 |
| Indicador[1-4] | IndicadorIvaPer | Codigo | Codigo,Descripcion |

### Numericos

| Nombre | Mascara default |
| ------ | ------ |
| Cantidad[N-40] | |
| Precio[1-8] | |
| Spread | |
| InteresesCorr | |
| PrecioEj | |
| PrecioMer | |
| TasaPrecan | |
| Plazo[N-7] | |
| TipoCambio[N-3] | |
| Lotes | |
| TotalBrutoCli[1-3] | |
| TotalComisiones | |
| TotalGastos | |
| TotalDerechos | |
| TotalRetenciones | |
| TotalImpuestos | |
| TotalNetoCli[1-3] | |
| TotalIntereses | |
| Numerador | |
| biReales | |
| biStrings | |
| biFechas | |
| biIntegers | |
| biTotales | |
| GrupoOp | |
| Direccion | |
| LInstancia | |
| Cuotas[1-2] | |
| TotalAux[1-10] | |
| TasaBase | |
| Cotizacion[1-2] | |
| PlazoGracia | |
| TotalIVA | |
| TotalGanancias | |
| PorAforo | |
| CantImpresiones[1-3] | |
| IntDevengados[1-2] | |
| DeltaTasa | |
| PeriodoInts | |
| PlazoRenovPredeter | |
| TasaInteresesCupon | |
| Comision | |
| Color | |
| Cupon[1-2] | |
| PorComMer[1-2] | |
| PorComCor[1-2] | |
| ImpComMer[1-2] | |
| ImpComCor[1-2] | |
| ImpComMerEq[1-2] | |
| ImpComCorEq[1-2] | |
| TCComCor[1-2] | |
| TCComMer[1-2] | |
| ImpGastos[1-2] | |
| TasaImp1 | |
| ImporteImp | |
| Coeficiente | |
| CantidadOri | |
| ResultadoIndice | |
| TotalImpuesto1 | |
| VCAN[1-31] | |
| VPRE[1-21] | |
| VTEORICO[N-5] | |
| PorDerechoBolsa | |
| PorImpuesto | |
| PorImpuestoBolsa | |
| MinImpuestoBolsa | |
| MinDerechoBolsa | |
| MinDerechoMercado | |
| MinArancel | |
| TotalCaucion | |
| PorArancel[N-2] | |
| PorComision | |
| NrAltaCV | |
| PorCaucion | |
| PorDerechoMercado | |
| CanPosTrad | |
| CanPosInv[1-2] | |
| CanPosOSoc | |
| TotalIVAAD | | #########.####### |
| TotalIVAADI | | #########.####### |
| TotalIVAPER | | #########.####### |
| TotalBonificacion | | #########.####### |
| MinImpuesto | | #########.####### |
| TASA[1-2] | |
| Importe[1-4] | |


### Texto

| Nombre | Tipo | Max input length |
| ------ | ------ | ------ |
| Observac[2-5] | TEXT | 100 |
| ConceptoEmp | TEXT |
| Custodia | TEXT |
| EsMultioperacion | TEXT |
| DiasMes | TEXT |
| ObservacDoc | TEXT |
| MensajeChequeo | TEXT |
| UsrInput | TEXT |
| Impresa | TEXT |
| FechaCargaSys | DATE |
| CodComitente | TEXT |
| NrBoleto | TEXT |
| SistAmortizacion | TEXT |
| PlazoEnHoras | TEXT |
| RuedaContinua | TEXT |
| Plaza[1-2] | TEXT |
| TasaVar | TEXT |
| TasaEspecie | TEXT |
| OpPrecancelar | TEXT |
| OpRenovar | TEXT |
| ModoCotiza | TEXT |
| SectorRB | TEXT |
| Arbitraje | TEXT |
| Rojo | TEXT |
| Opcion | TEXT |
| UMedida | TEXT |
| ViaPago1 | TEXT |
| CategDepositante | TEXT | |
| NroBajaMae | TEXT | 20 |
| Externa | TEXT | 3 |
| NrSisExterno | TEXT |
| CodErrorMae | TEXT |
| CodSisExterno | TEXT |
| EnteCus[1-2] | TEXT |
| ObsErrorMae | TEXT |
| CodErrorCV | TEXT |
| NroAltaMae | TEXT |
| Observaciones | LARGE_TEXT | 255 |
| VTXT[1-51] | MEDIUM_TEXT | 100 |
 
### Otros controles

| Nombre | Tipo | 
| ------ | ------ |
| TipoOpcion | LABEL |
| DiasAnio | LABEL |
| RB[1-17] | LABEL |
| MB[1-6] | LABEL |
| TipoGracia | LABEL |
| FormaLiquidacion[1-4] | LABEL |
| ValorRB[1-2] | LABEL |
| MercadoRB | LABEL |
| VRB[1-21] | LABEL |
| LABEL[1-21] | LABEL |
| Cartera | LABEL |
| TipoTicket | LABEL |
| Convenio | LABEL |
| Puesto | CHECK |
| CB[1-17] | CHECK |
| PaseCB | CHECK |
| EsAforado | CHECK |
| FechaOp[N-2] | DATE |
| FechaVto[N-2] | DATE |
| FechaEj | DATE |
| FechaCarga | DATE |
| FechaPrecan | DATE |
| FechaPago | DATE |
| FechaUltCupon | DATE |
| FechaEx[1-4] | DATE |
| VFEC[1-21] | DATE |
| FechaAltaSisExterno | DATE |
| FechaAltaMae | DATE |
| Fecha[N-8] | DATE |
| FechaEnvioMae | DATE |
	
