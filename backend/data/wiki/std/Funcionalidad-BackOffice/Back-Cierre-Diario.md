---
title:  Cierre Diario
description: 
published: true
date: 2020-11-03T18:11:26.004Z
tags: 
editor: markdown
dateCreated: 2020-10-16T12:47:06.800Z
---

# Manual del Usuario	

## Back Cierre Diario 

### Indice 

[Introducción](#Intro)	
[Parámetros de la corrida](#Par1) 	
[Procesos automáticos](#Proc1) 	
[Controles](#Contr1)	
[Ejemplo de corrida fallida](#Ej1)	
[Ejemplo de corrida exitosa](#Ej2)	
[Glosario](#Glosa)	

### Introducción {: #Intro}

Diariamente al cierre de la operatoria habitual, el usuario de Back Office ejecuta el cierre. El cierre diario es un proceso que reúne los controles necesarios para que se genere la contabilidad y otros procesos relevantes para finalizar la operatoria del día.

Cuando éste termina, emite un listado de los procesos que fueron exitosos o fallaron.

### Parámetros de la corrida {: #Par1}

![cierre_diario.png](/cierre_diario.png)

**Diálogo**

**Fecha:** Fecha a la que se quiere ejecutar el cierre
Default: Fecha del día 
Validación: Que sea válida, menor o igual a la fecha del día. 
Modificable: Si

**Controles:** Indica si se quieren realizar los controles antes de ejecutar los procesos del cierre. En caso de que se destilde no se hacen los controles y se ejecutan todos los procesos.
Default: Tildado (se hacen los controles)
Modificable: Si. 

**Sólo se usa para casos de contingencia consensuados con FPA ya que al no realizarse los controles se puede generar la contabilidad con datos incorrectos o faltantes.**

### Procesos Automaticos {: #Proc1}

1) Se desconecta Siopel

2) Se eliminan operaciones de la instancia de Anulación que puedan encontrarse aún en la instancia de 30 - Anulación Manual

3) Cálculo diario de intereses ICL

### Controles {: #Contr1}

Se informan:
1) Precio contable del Dólar: Se alerta si no se encuentra

2) Precio contable de aquellos títulos que tengan Saldo o Posición: Se alerta si no se encuentra indicando la especie

3) Operaciones pendientes de liquidación

4) Operaciones pendientes de confirmación

5) Movs No operativos en Instancias Intermedias

6) Falta de cálculo de  MTM de futuros de moneda (Eventos MTM futuros y MTM futuros NDF)

7) Falta de cálculo del Fixing de futuros de moneda (Evento MTM futuros)

8) Operaciones con modificaciones pendientes de autorizar

9) Operaciones en instancias incorrectas: operaciones con problemas sobre las que falta tomar decisiones sobre la interfase con el sistema externo. Ejemplo especie no encontrada o sancionada, cliente incorrecto
 
10) Préstamos ICL - se alerta sobre:
* existencia de CONUs vigentes con saldo negativo
* Préstamos ICL con vencimiento posterior a las CONU
* Tasas faltantes
* Índices faltantes
 
11) Límites de Perfilamiento: Para cada cliente se visualiza el estado del límite, asignado, consumido y exceso. No es invalidante

Si todos los controles están OK:

1) Se envían las operaciones que puedan haber quedado en instancias intermedias de Siopel a la instancia 69 - Compliance

2) Se realiza el corte de posición de las especies que están en el período que va desde la actualización hasta el corte de cupón y que hayan operado con el cupón anterior. 

3) Se genera la contabilidad - Ver Manual Back Proceso Contable

4) Se emite un informe de asientos desbalanceados

5) Se actualiza el Status de las especies de PME

6) Se realiza el cálculo diario de intereses ICL

7) Se emiten los copiativos Libro de cartera, Libro de Caja, Copiativo de Boletos MAE - ROFEX

8) Se generan los Logs de cierre en un repositorio

9) Se informa el Status final del cierre indicando si este fue exitoso o no

### Ejemplo de corrida fallida {: #Ej1}

![informe_precierre.png](/informe_precierre.png)

![informe_precierre2.png](/informe_precierre2.png)

### Ejemplo de corrida exitosa {: #Ej2}

![informe_precierre_exitoso.png](/informe_precierre_exitoso.png)

![informe_precierre_exitoso2.png](/informe_precierre_exitoso2.png)

### Glosario {: #Glosa}

A continuación se detallan las abreviaturas utilizadas en el presente Manual del Usuario:

![glosario_cierre_diario.png](/glosario_cierre_diario.png)






