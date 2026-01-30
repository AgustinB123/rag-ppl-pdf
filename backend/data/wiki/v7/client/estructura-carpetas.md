---
title: Estructura carpetas
description: Breve descripción de que se puede encontrar en cada carpeta de V7
published: true
date: 2023-08-01T12:00:29.853Z
tags: 
editor: markdown
dateCreated: 2023-08-01T12:00:29.853Z
---

# ESTRUCTURA CARPETAS

### Una breve descripcion de que se encuentra en cada carpeta



**assets:** imagenes, fonts o materiales para el diseño



**components**: componentes de react que van surgiendo para resolver los problemas de la aplicacion
  - **dialogTabs** : un componente que todavia no se esta usando. pero es para usar cuando esten los tabs de los 											dialogos.

  - **FormComponents**: Son los componentes de los dialogos de ppl. Texto,Check,LookUp entre otros. (Tal vez su 		nombre no se actualizo y necesita ser actualizado a algo como: DialogComponents| DialogFormComponents). 				Estos componentes son usados en CustomFieldFactory al momento de generar todo el dialogo. 

- **pplScript**: Son los componentes que se utilizan para armar el flujo de ejecución de un script (dialogo,grilla). Tiene varios "containers" que se utilizan para inicializar los contextos (sin los containers los componentes no podrian acceder a los contextos)

- props: esta carpeta quedo inutilizada. Pero era para poner todas las props repetidas o props de componentes.

- search: Son los componentes de busqueda. Por ahora hay uno solo que esta en construccion. El objetivo es 								hacerlo lo mas generico posible.




**config**: carpeta para los archivos de configuracion




**context**: aca estan todos los contextos definidos hasta ahora. 
- **GllobaContext** : Va a almacenar estado "global" de la aplicación. Por ejemplo: scripts disponibles, fechasys, etc.
- **PPLContext** :  Es el estado de la ejecución de un script PPL. Por ejemplo: cual es la sección que esta ejecutando actualmente, el dialog definition, los valores completados en el dialogo.
- **DialogContext** : Es el estado de un dialogo. Dialog definiton, temp values, estado de recalculos.



**helpers**: funciones que se repiten en varios componentes y solucionan algo particular. actualmente hay helpers de listas y de objetos.




**hooks**: nuestros hooks propios de react. Actualmente solo esta useApi. este se encarga de tener todas las funciones para relacionarse con pages/api y pedir la informacion mockeada. useApi deberia ser utilizado por los contextos y no por los componentes.




**layouts**: esquemas de diseño de la pagina (navbar,sidebar,footbar,etc)
-sideBar:  contiene los scripts disponbiles. actualmente por cada vez que abrimos el menu estos se van a buscar para no cargarse todos al mismo tiempo. Cuando le hacen click a un scriPt, este redirIge a el componente: pages/ppl/webview/[scriptId]

asi lo fui pensando: https://docs.google.com/document/d/1tLQOIUDwtM5I9bozYM5JCLBg6WcLe39AtaEcGi50yzU/edit
  
  
  
  
**mocks**: archivos simulan algun dato que deberiamos tener y no tenemos.



 **pages** :  En esta carpeta se encuentra la simulacion de la api y tambien las paginas de la aplicacion.

**api**: Next.js permite tener una api interna en el proyecto y simularla para que nos devuelva lo que nosotros necesitamos en algun componente. Todos los llamados a esta api estan en el hook UseAPI.

- __mock__: carpeta que contienen mocks que fueron surgiendo por la api. Tal vez necesita ser unificada con la otra carpeta de mocks

- **globals**: datos globales que se piden al momento de abrir la aplicacion (fecha sistema,etc)

- **lookUp/[lookUpId]:** en proceso: es para intentar mejorar el mockeo de la informacion que usa el lookUp.

- **ppl**: esta carpeta dentro de api tiene la simulacion de empezar la ejecucion de un script y de pedir la siguiente seccion del script(start y next)

- ademas contiene dos archivos.ts , uno para pedir los tipos de scripts disponibles y otro para pedir todos los scripts disponibles


**paginas de la aplicacion**:
encontramos ppl. esta pagina se encarga de admnistrar los llamados de las secciones de un script. utiliza dialogos, containers que se encuentran en la carpeta components. Esta pagina solamente se activa cuando le hacen click a un script en el sidebar

---

**pplui**: No se para que se utilizaba esta carpeta , Me parece que era para la interfaz de ppl. Tiene un par de tipos de typescript que utilizamos.




**routes**:  rutas que acepta la aplicacion. por ahora solo esta definida  y funcional "/" el resto estarian deprecadas.



**styles**: estilos globales para los componetnes,textos,etc. es el CSS




**types**: tipos de datos de la aplicacion. por ahora tiene una carpeta "api"  en donde fuimos poniendo la forma que tienen los Response de la api. entre ellos(GlobalsReponse,PplScriptTypesResponse, pplSectionResponse,etc)




