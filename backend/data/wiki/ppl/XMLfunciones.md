---
title: Funciones para manipular XML en PPL
description: 
published: true
date: 2025-08-07T19:09:27.083Z
tags: xml ppl
editor: markdown
dateCreated: 2025-06-02T12:47:10.717Z
---

# Introducción
**XML** (eXtensible Markup Language, en español Lenguaje de Marcado Extensible) es un formato de archivo que permite estructurar y representar datos de manera jerárquica y legible tanto para humanos como para máquinas. Similar al HTML, utiliza etiquetas para describir la estructura y los elementos de los datos

## Descripción detallada

### Estructura jerárquica
XML se basa en una estructura de árbol donde los elementos se pueden anidar unos dentro de otros, creando una jerarquía de datos. 
### Etiquetas
Las etiquetas, similares a las de HTML, definen los elementos y atributos de los datos. Las etiquetas pueden ser personalizadas, lo que hace a XML más flexible que HTML. 
### Legibilidad
XML es un formato de texto simple, lo que lo hace legible para humanos y fácil de procesar por computadoras. 
### Intercambio de datos
XML es ideal para intercambiar datos entre diferentes sistemas, aplicaciones o plataformas, ya que es compatible con muchos lenguajes de programación. 
### Aplicaciones
XML se utiliza en diversas aplicaciones, incluyendo la creación de archivos de configuración, la transmisión de datos en servicios web, el almacenamiento de datos en bases de datos XML, y mucho más. 
### Esquemas XML (XSD)
Para definir la estructura y las restricciones de un documento XML, se utilizan los esquemas XML (XSD), que establecen reglas sobre los elementos, atributos y tipos de datos. 

# Integración con PPL
## Metodos
Proporcionamos los siguientes métodos para interactuar con XML.

|#|Método|Descripción|Parámetro|Devuelve
|-|------|-----------|---------|---------|
|1|XML.Iniciar| Crea el componente vacio sin datos | (sin parametros)|void
|2|XML.CargarSQL(sqlquery)|Carga en el componente un xml extraido de un campo de una tabla|Query valido cuya primera fila del resultado es una string xml|void
|3|XML.CargarArchivo(AarchivoXml)| Crea el componente vacio sin datos | Ruta completa con un archvo xml valido|void
|4|XML.Seleccionar(Pathquery)| Elecuta query filtro sobre el xml cargado, reduce el resultado. Hace el RunXPathQuery del componente|pathquery|void
|5|XML.BuscarCampo(string)| hace GetField del componente|nombre del campo|void
|6|XML.SetearNameSpace(namespace)|setea namespace en el componente|NameSpace del XML|void
|7|XML.FBN[nombrecampo]| devuelve el campo llamado nombrecampo en la recorrida que se esta haciendo|NombreCampo|valor del campo en el archivo xml
|8|XML.String |trae el nodo actual completo con tags y valores, para parsear a mano.| sin |string|

## Sentencias 
Sentencias para recorrer resultados

|#|Método|Descripción|Parámetro|
|-|------|-----------|---------|
|1|RecorrerXML(nodo)| Itera en un conjunto de filas que dependen de un nodo en particular| Nodo a partir del cual se iteran las filas|void


# Ejemplos
- A continuación un evento que recorre un xml .


```
ModoReproceso(ConDialogo)
CrearDialogo
  Radio1 : 'Origen|Archivo|Tabla' ; ; ; ;NO;  ;;;;0
  Fecha1 : 'Fecha'        ;2;1; ;Dialogo.Radio1=1;Dialogo.Radio1=0;;;;;FSys
  String1: 'Ruta'         ;2;1; ;Dialogo.Radio1=0;Dialogo.Radio1=0;;;;VAR('PATHIEXP')
  String2: 'Archivo'      ;3;1; ;Dialogo.Radio1=0;Dialogo.Radio1=0;;;;VAR('ARCHBOFA')
  Check1 : 'Procesa'      ;5;1; ;NO;SI;;;;0
  Check2 : 'Ver pantalla' ;5;2; ;Dialogo.Check1=1;SI;;;;1;iif(Dialogo.Check1=0,1,Dialogo.Check2)
FinDialogo
if Not OK
  Cancelar
endif

CrearFont(1,'Arial,8,')
CrearFont(2,'Arial,8,B')
CrearFont(3,'Arial,10,B')

if Dialogo.Check2=1
  HojaVisible(SI)
endif

ACT(x:1, Dialogo.String1~'\'~Dialogo.String2)

if Dialogo.Radio1=0
  if ExisteArchivo(Val(x:1))
    XML.Iniciar
    XML.CargarArchivo(Val(x:1))
    if OK
      ACN(y:1, 1)
    endif
  else
    MessageBox('No existe el archivo '~Val(x:1))
  endif
else
  if Dialogo.Check1=0
    SQL.ADD("Select * from "~DBO~".INTERFAZ_FPA where Trunc(FechaInput) = '"~IdxDate(Dialogo.Fecha1)~"' ")
  else
    SQL.ADD("Select * from "~DBO~".INTERFAZ_FPA where Trunc(FechaInput) = '"~IdxDate(Dialogo.Fecha1)~"' and (Estado is Null or Estado <> 'IMP') ")
  endif
  recorrer SQL
    DFA
    ACN(x:2, 1)
    ACT(y:2, fbn('INTERFAZFPAID'))
  proximo
  if Val(x:2)=1
    XML.Iniciar
    XML.CargarSQL("Select Datos from "~DBO~".INTERFAZ_FPA where Trunc(FechaInput) = '"~IdxDate(Dialogo.Fecha1)~"' ")
*    MessageBox('cargo de tabla')
    if OK   
      ACN(y:1, 1)
    endif
  else
    if Val(x:2)=0
      MessageBox('No existe extracto en la tabla para la fecha solicitada')
    else
      MessageBox('Existen '~PYC(Val(x:2),1,0)~' extractos en la tabla para la fecha solicitada')
    endif
  endif
endif

SetFilaActual(1)
ACT(a:FAC, 'Importacion extracto ')
ACT(a:FAC+1, 'Fecha: '~Dialogo.Fecha1)
ACT(a:FAC+2, 'Origen: '~iif(Dialogo.Radio1=0,'Archivo '~Val(x:1),'Tabla INTERFAZ_BOFA_FPA'))

SetFont(a:FAC, 3)
SetFont(a:FAC+1..a:FAC+2, 2)

SetFilaActual(FAC+4)
ACT(a:FAC, 'F. Creacion')
ACT(a:FAC+1, 'F. Movs')
ACT(a:FAC+2, 'Cuenta')
ACT(a:FAC+3, 'Moneda')
ACT(a:FAC+4, 'Nombre')


ACT(a:FAC+6, 'Total Entradas')
ACT(a:FAC+7, 'Total Movs')
ACT(a:FAC+8, 'Diario')
ACT(a:FAC+9, 'Tipo')
ACT(a:FAC+10, 'Neto Diario')
ACT(a:FAC+12, 'Cant Cred')
ACT(a:FAC+13, 'Total Cred')
ACT(a:FAC+14, 'Cant Deb')
ACT(a:FAC+15, 'Total Deb')

SetFont(a:FAC..a:FAC+15, 2)

if Val(y:1)=1
  RecorrerXML("//Stmt")
    DFA
    SCN(s:1, 1)
    ACT(t:Val(s:1), XML.FBN['Id'])
    SetFont(t:Val(s:1), 1)
  proximo

  if Val(s:1)>0
  
    RecorrerXML("//Stmt[Acct/Id/Othr/Id='1901517079']")
      DFA

      ACT(b:FAC, XML.FBN['CreDtTm'])
      ACD(c:FAC, Fecha(Copy(Val(b:FAC),9,2)~'/'~Copy(Val(b:FAC),6,2)~'/'~Copy(Val(b:FAC),1,4)))
      ACT(b:FAC+1, XML.FBN['FrToDt/ToDtTm'])
      ACD(c:FAC+1, Fecha(Copy(Val(b:FAC+1),9,2)~'/'~Copy(Val(b:FAC+1),6,2)~'/'~Copy(Val(b:FAC+1),1,4)))
      ACT(b:FAC+2, XML.FBN['Acct/Id/Othr/Id'])
*      ACT(o:2, Val(b:FAC+1))
      ACT(b:FAC+3, XML.FBN['Acct/Ccy'])
      ACT(b:FAC+4, XML.FBN['Acct/Nm'])

      ACN(b:FAC+6, Num(XML.FBN['TxsSummry/TtlNtries/NbOfNtries']))
      ACN(b:FAC+7, Num(XML.FBN['TxsSummry/TtlNtries/Sum']))
      ACN(b:FAC+8, Num(XML.FBN['TxsSummry/TtlNtries/TtlNetNtryAmt']))
      ACT(b:FAC+9, XML.FBN['TxsSummry/TtlNtries/CdtDbtInd'])
      if EqStr(Val(b:FAC+9),'CRDT')
        ACN(b:FAC+10, Val(b:FAC+8))
      else
        ACN(b:FAC+10, -Val(b:FAC+8))
      endif

      ACN(b:FAC+12, Num(XML.FBN['TxsSummry/TtlCdtNtries/NbOfNtries']))
      ACN(b:FAC+13, Num(XML.FBN['TxsSummry/TtlCdtNtries/Sum']))

      ACN(b:FAC+14, Num(XML.FBN['TxsSummry/TtlDbtNtries/NbOfNtries']))
      ACN(b:FAC+15, Num(XML.FBN['TxsSummry/TtlDbtNtries/Sum']))

      ACN(c:FAC+6, Val(b:FAC+12)+Val(b:FAC+14))
      ACN(c:FAC+7, Val(b:FAC+13)+Val(b:FAC+15))
      ACN(c:FAC+10, Val(b:FAC+13)-Val(b:FAC+15))

      SetFont(b:FAC..c:FAC+15, 1)

      ACN(x:3, Val(b:FAC+6))
      ACN(x:4, FAC)
      SetFilaActual(FAC+17)
      ACT(a:FAC, 'Movimientos')
      SetFont(a:FAC, 2)

      SetFilaActual(FAC+2)

      ACT(a:FAC, 'ID')
      ACT(b:FAC, 'Monto')
      ACT(c:FAC, 'Tipo')
      ACT(d:FAC, 'Ref')
      ACT(e:FAC, 'Fecha')
      ACT(f:FAC, 'Accion')
      ACT(g:FAC, 'Nr.Mov.')

      ACT(i:FAC, 'ORG')
      ACT(j:FAC, 'SND')
      ACT(k:FAC, 'BNF')
      ACT(l:FAC, 'INF')
      ACT(m:FAC, 'CDT')
      ACT(n:FAC, 'Descripcion')
      ACT(o:FAC, 'Estado')

      ACT(ab:FAC, 'Long')

      ACT(ac:FAC, 'ORG')
      ACT(ad:FAC, 'Ini')
      ACT(ae:FAC, 'Fin')
      ACT(af:FAC, 'Larg')

      ACT(ag:FAC, 'SND')
      ACT(ah:FAC, 'Ini')
      ACT(ai:FAC, 'Fin')
      ACT(aj:FAC, 'Larg')

      ACT(ak:FAC, 'BNF')
      ACT(al:FAC, 'Ini')
      ACT(am:FAC, 'Fin')
      ACT(an:FAC, 'Larg')

      ACT(ao:FAC, 'INF')
      ACT(ap:FAC, 'Ini')
      ACT(aq:FAC, 'Fin')
      ACT(ar:FAC, 'Larg')

      ACT(as:FAC, 'CDT')
      ACT(at:FAC, 'Ini')
      ACT(au:FAC, 'Fin')
      ACT(av:FAC, 'Larg')

      ACT(aw:FAC, 'Otros')
      ACT(ax:FAC, 'Ini')
      ACT(ay:FAC, 'Fin')
      ACT(az:FAC, 'Larg')

      ACT(ca:FAC, 'FechaVal')
      SetFont(a:FAC..cz:FAC, 2)
      ACN(w:1, FAC+1)

      if Val(x:3)>0
        RecorrerXML("//Stmt[Acct/Id/Othr/Id='1901517079']/Ntry")
          SCN(w:2, 1)
          ACT(a:FAC, XML.FBN['NtryRef'])
          ACN(b:FAC, Num(XML.FBN['Amt']))
          ACT(c:FAC, XML.FBN['CdtDbtInd'])
          ACT(d:FAC, XML.FBN['NtryDtls/TxDtls/Refs/AcctSvcrRef'])
          ACT(ca:FAC, XML.FBN['ValDt/DtTm'])
          RecorrerXML("//Stmt[Acct/Id/Othr/Id='1901517079']/Ntry[NtryRef='"~Val(a:FAC)~"']/NtryDtls/TxDtls/RmtInf")
            DFA
            SCN(z:FAC, 1)
            ACT(aa:FAC, XML.FBN['Ustrd[0]'])
            ACT(aa:FAC, Val(aa:FAC)~XML.FBN['Ustrd[1]'])
            ACT(aa:FAC, Val(aa:FAC)~XML.FBN['Ustrd[2]'])
            ACT(aa:FAC, Val(aa:FAC)~XML.FBN['Ustrd[3]'])
          proximo
          ACN(ab:FAC, Longitud(Val(aa:FAC)))
          ACD(e:FAC, Fecha(Copy(Val(ca:FAC),9,2)~'/'~Copy(Val(ca:FAC),6,2)~'/'~Copy(Val(ca:FAC),1,4)))
          ACT(o:FAC, 'PEN')

          if EqStr(Val(c:FAC),'CRDT')
            if Buscar('ORG',Val(aa:FAC))
              ACN(ac:FAC, 1)
              ACN(ad:FAC, Posicion('ORG',Val(aa:FAC), 0)+4)
            endif
            if Buscar('SND',Val(aa:FAC))
              ACN(ag:FAC, 1)
              ACN(ah:FAC, Posicion('SND',Val(aa:FAC), 0)+4)
              ACN(ae:FAC, Posicion('SND',Val(aa:FAC), 0))
            endif
            if Buscar('BNF',Val(aa:FAC))
              ACN(ak:FAC, 1)
              ACN(al:FAC, Posicion('BNF',Val(aa:FAC), 0)+4)
              ACN(ai:FAC, Posicion('BNF',Val(aa:FAC), 0))
            endif
            if Buscar('INF',Val(aa:FAC))
              ACN(ao:FAC, 1)
              ACN(ap:FAC, Posicion('INF',Val(aa:FAC), 0)+4)
              ACN(am:FAC, Posicion('INF',Val(aa:FAC), 0))
              ACN(aq:FAC, Val(ab:FAC))
            else
              if Val(ak:FAC)=1
                ACN(am:FAC, Val(ab:FAC))
              endif
            endif
            if Val(ac:FAC)=0
              if Buscar('REG RECR',Val(aa:FAC))
                ACT(o:FAC, 'AUT')
                ACN(aw:FAC, 1)
                ACN(ax:FAC, Posicion('REG RECR',Val(aa:FAC), 0))
                ACN(ay:FAC, Val(ab:FAC))
                ACN(az:FAC, Val(ay:FAC)-Val(ax:FAC)+1)
              endif
            endif

            if Val(ac:FAC)=1
              * ORG
              ACN(af:FAC, Val(ae:FAC)-Val(ad:FAC))
              ACT(i:FAC, Copy(Val(aa:FAC),Val(ad:FAC),Val(af:FAC)))
            endif
            if Val(ag:FAC)=1
              * SND
              ACN(aj:FAC, Val(ai:FAC)-Val(ah:FAC))
              ACT(j:FAC, Copy(Val(aa:FAC),Val(ah:FAC),Val(aj:FAC)))
            endif
            if Val(ak:FAC)=1
              * BNF
              ACN(an:FAC, Val(am:FAC)-Val(al:FAC))
              ACT(k:FAC, Copy(Val(aa:FAC),Val(al:FAC),Val(an:FAC)))
            endif
            if Val(ao:FAC)=1
              * INF
              ACN(ar:FAC, Val(aq:FAC)-Val(ap:FAC)+1)
              ACT(l:FAC, Copy(Val(aa:FAC),Val(ap:FAC),Val(ar:FAC)))
            endif
            if Val(ac:FAC)=1
              ACT(n:FAC, Copy(Val(aa:FAC),Val(ad:FAC)-4,Val(ab:FAC)-Val(ad:FAC)+5))
            else
              if Val(aw:FAC)=1
                ACT(n:FAC, Copy(Val(aa:FAC),Val(ax:FAC),Val(az:FAC)))
              else
                ACT(n:FAC, Copy(Val(aa:FAC),1,200))
              endif
            endif
          endif

          if EqStr(Val(c:FAC),'DBIT')
            if Buscar('BNF',Val(aa:FAC))
              ACN(ak:FAC, 1)
              ACN(al:FAC, Posicion('BNF',Val(aa:FAC), 0)+4)
            endif
            if Buscar('ORG',Val(aa:FAC))
              ACN(ac:FAC, 1)
              ACN(ad:FAC, Posicion('ORG',Val(aa:FAC), 0)+4)
              ACN(am:FAC, Posicion('ORG',Val(aa:FAC), 0))
            endif
            if Buscar('CDT',Val(aa:FAC))
              ACN(as:FAC, 1)
              ACN(at:FAC, Posicion('CDT',Val(aa:FAC), 0)+4)
              ACN(ae:FAC, Posicion('CDT',Val(aa:FAC), 0))
              ACN(au:FAC, Val(ab:FAC))
            endif
            if Buscar('INF',Val(aa:FAC))
              ACN(ao:FAC, 1)
              ACN(ap:FAC, Posicion('INF',Val(aa:FAC), 0)+4)
              ACN(au:FAC, Posicion('INF',Val(aa:FAC), 0))
              ACN(aq:FAC, Val(ab:FAC))
            endif
            if Val(ak:FAC)=0
              if Buscar('REG INV',Val(aa:FAC))
                ACT(o:FAC, 'AUT')
                ACN(aw:FAC, 1)
                ACN(ax:FAC, Posicion('REG INV',Val(aa:FAC), 0))
                ACN(ay:FAC, Val(ab:FAC)+1)
                ACN(az:FAC, Val(ay:FAC)-Val(ax:FAC)+1)
              endif
              if Val(aw:FAC)=0
                ACN(aw:FAC, 1)
                ACN(ax:FAC, Posicion('ENTRY',Val(aa:FAC), 0)+13)
                ACN(ay:FAC, Val(ab:FAC))
                ACN(az:FAC, Val(ay:FAC)-Val(ax:FAC)+1)
              endif
            endif

            if Val(ak:FAC)=1
              * BNF
              ACN(an:FAC, Val(am:FAC)-Val(al:FAC))
              ACT(k:FAC, Copy(Val(aa:FAC),Val(al:FAC),Val(an:FAC)))
            endif
            if Val(ac:FAC)=1
              * ORG
              ACN(af:FAC, Val(ae:FAC)-Val(ad:FAC))
              ACT(i:FAC, Copy(Val(aa:FAC),Val(ad:FAC),Val(af:FAC)))
            endif
            if Val(as:FAC)=1
              * CDT
              ACN(av:FAC, Val(au:FAC)-Val(at:FAC)+1)
              ACT(m:FAC, Copy(Val(aa:FAC),Val(at:FAC),Val(av:FAC)))
            endif
            if Val(ao:FAC)=1
              * INF
              ACN(av:FAC, Val(au:FAC)-Val(at:FAC))
              ACT(m:FAC, Copy(Val(aa:FAC),Val(at:FAC),Val(av:FAC)))
              ACN(ar:FAC, Val(aq:FAC)-Val(ap:FAC)+1)
              ACT(l:FAC, Copy(Val(aa:FAC),Val(ap:FAC),Val(ar:FAC)))
            endif
            if Val(ak:FAC)=1
              ACT(n:FAC, Copy(Val(aa:FAC),Val(al:FAC)-4,Val(ab:FAC)-Val(al:FAC)+5))
            else
              if Val(aw:FAC)=1
                ACT(n:FAC, Copy(Val(aa:FAC),Val(ax:FAC),Val(az:FAC)))
              else
                ACT(n:FAC, Copy(Val(aa:FAC),1,200))
              endif
            endif
          endif

          ACN(w:3, FAC)
          SetFont(a:FAC..ca:FAC, 1)
        proximo
      endif
    proximo

    recorrer&i Val(w:1),Val(w:3)
      if Val(y:FAC)=0
        ACT(f:&i, 'Insert')
        if Dialogo.Check1=1
          ACT(g:&i, GetNumerador(201))
          *- Insertar registro
          SQL.ADD("INSERT INTO "~DBO~".INTMOVBANCARIOS ( ")
          SQL.ADD("   NrMov, Fecha, Banco, Cuenta, ")
          SQL.ADD("   Referencia, Moneda, MonedaFPA, Importe, ")
          SQL.ADD("   TipoMov, Descripcion, FechaCarga, UsrCarga, ")
          SQL.ADD("   TipoCarga, Estado, Cliente, AdressBook ")
          SQL.ADD("   ) VALUES (")
          * NrMov
          SQL.ADD("   '"~Val(g:&i)~"', ")
          SQL.ADD("   '"~IdxDate(Val(e:&i))~"', ")
          SQL.ADD("   'MIA', ")
          SQL.ADD("   '1901517079', ")
          * Referencia
          SQL.ADD("   '"~Val(d:&i)~"', ")
          SQL.ADD("   'USD', ")
          SQL.ADD("   'DOL', ")
          SQL.ADD("   "~FStr(Val(b:&i),1,2)~", ")
          * TipoMov
          SQL.ADD("   '"~Val(c:&i)~"', ")
          SQL.ADD("   '"~Copy(Val(n:&i),1,190)~"', ")
          SQL.ADD("   '"~IdxDate(Fecha(Ahora))~"', ")
          SQL.ADD("   '"~UsuarioActivo~"', ")
          * TipoCarga
          if Dialogo.Radio1=0
            SQL.ADD("   'ARC', ")
          else
            SQL.ADD("   'TAB', ")
          endif
          SQL.ADD("   '"~Val(o:&i)~"', ")
          SQL.ADD("   NULL, ")
          SQL.ADD("   NULL ")
          SQL.ADD("   )")
          SQL.NEW
          SQL.EXEC
        Endif
      endif
    proximo
    if Dialogo.Radio1=1
      SQL.ADD("Update "~DBO~".INTERFAZ_FPA ")
      SQL.ADD("   Set Estado   = 'IMP', ")
      SQL.ADD("       FechaFPA = '"~IdxDate(FSys)~"' ")
      SQL.ADD(" where InterfazBofaFpaId = '"~Val(y:2)~"' ")
      SQL.NEW
      SQL.EXEC
    Endif
    SetFont(a:Val(w:1)..ca:Val(w:3), 1)
  else
    MessageBox('Error en XML leido')
  endif
else
  MessageBox('Error al leer XML')
endif

SetFont(v:1..z:6, 1)

ACO(1,12)
ACO(2,12)
ACO(3,10)
ACO(4,10)
ACO(5,10)
ACO(6,8)
ACO(7,8)

ACO(9,40)
ACO(10,40)
ACO(11,40)
ACO(12,40)
ACO(13,40)
ACO(14,40)

ACO(20,20)

*LimitesVision(g:FAC)

```