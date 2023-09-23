---
title: Describiendo nuestra metodología
date: 2023-09-20
description: En este artículo explicamos de manera muy general en que consiste la metodología que seguimos para desarrollar Seguimiento Político
category: Metodología
lastmod: 2023-09-23T14:44:48.808Z
---

Seguimiento político no pretende ser otra cosa que una plataforma colaborativa en la que cualquier persona, independientemente de sus ideas políticas, pueda informarse sobre los "hechos" o la "realidad" política en España. Decimos que es "colaborativa" porque la información recogida es el resultado del trabajo de cualquiera que quiera aportar su granito de arena. 

Esperamos que esta web sirva para que las personas más interesadas en la política, aquellas que se esfuerzan en mayor medida a la hora de informarse y que además quieren compartir su esfuerzo puedan hacer precisamente eso, compartir su conocimiento.

El principal beneficio que encontramos a esto, es que si aquellos que se informan sobre una cuestión concreta comparten la información y conclusiones obtenidas, ayudarán a las demás personas a invertir menos tiempo para llevar a cabo la misma tarea. El tiempo extra generado puede redundar en más capacidad para informarse sobre otras cuestiones. Buscamos que se cree un ciclo virtuoso basado en las aportaciones de toda la comunidad que beneficie a todos por igual.

Hoy queremos explicar de manera muy general en que consiste la metodología que estamos empleando, la base de dicha plataforma colaborativa. No describimos aún como  pueden colaborar, solo queremos mostrar los fundamentos para que comprendan mejor como funciona {SP} en sus entrañas. Más adelante explicaremos en una "guía práctica, paso a paso", como pueden colaborar de manera sencilla.

## Metodología
Los pasos estándar del Análisis de datos, que son los que se muestran a continuación, describen perfectamente la labor que intentamos realizar en {SP}.
1. Recopilación de datos: es la fase inicial en la que se obtienen los datos necesarios para el análisis
1. Limpieza de datos: se eliminan o corrigen datos incorrectos, incompletos o irrelevantes. En {SP} únicamente nos preocupamos de nuestros propios errores. Por motivos de confiabilidad, ni en esta, ni ninguna otra etapa modificamos los datos originales, salvo los errores tipográficos o gramaticales.
1. Integración de datos: dónde se combinan y unifican las diferentes fuentes de datos a un formato homogéneo en una misma base de datos
1. Transformación de datos: dónde se convierten los datos a un formato adecuado para el análisis
1. Análisis: Es la última etapa y más importante, dónde se examinan los datos y se genera información útil para alcanzar conclusiones y tomar decisiones informadas.

Centrándonos en la cuestión de las __promesas electorales__, nuestra metodología consiste en las siguientes tareas secuenciales:
1. **Identificar las fuentes**, es decir, los programas electorales. Quizás en el futuro incluyamos las declaraciones por parte de los dirigentes políticos recogidas por los medios de comunicación y que, por tanto, puedan ser contrastables (salvando la incertidumbre que crea la posible manipulación a través de «Deep-fakes» mediante Inteligencia Artificial).
1. **Transformación de cada programa electoral en un "Documento".** Esto básicamente consiste en crear un archivo vinculado a un determinado Partido y un contexto electoral concreto. Entre otras, permite la visualización más interactiva del contenido del programa que si se hiciera a través del PDF original.
1. **Recopilación de cada propuesta electoral.** Se genera una "Promesa" creando un archivo único, vinculado al "Documento" (es decir, al partido y a las elecciones concretas), que recoge el contenido literal de cada propuesta. En esta etapa se realiza una labor inicial de integración de datos porque tanto los "Documentos" como las "Promesas" tienen un formato predefinido (que unifica y homogeiniza los datos) quedando automáticamente integrados en nuestra base de datos.
1. **Transformación de datos**. Esta etapa puede llevarse a cabo a la misma vez que la anterior o *a posteriori*. Tendemos a pensar, que una vez creado un sistema de clasificación de promesas adecuado, lo ideal es realizaro a la misma vez que la recopilación de datos. Por una simple cuestión de optimización de recursos y evitar trabajar dos veces sobre una misma promesa.
1. **Análisis**. El último paso, es a la vez el más importante y complicado. Tiene dos variantes:
    - Análisis individual: Se trata de una análisis cualitativo, en el que nos centramos en evaluar la propia medida *per se* en relación a su *forma de comunicación* (evaluando parámetros como claridad/ambigüedad, determinismo o "medibilidad" de sus metas/objetivos), *grado de cumplimiento* (en caso de existir iniciativas legislativas relacionadas, analizando si lo prometido se alinea con los hechos consumados en el congreso), *realismo* (si lo propuesto es realizable). Además, en caso de haberse cumplido la promesa se evalúan los resultados obtenidos comparados con los esperables.

    - Análisis comparativo: Se trata de analizar en que cuestiones difiere una medida concreta con respecto a otras relacionadas. Se compara por un lado la *coherencia* con respecto a otras propuestas actuales y previas del mismo partido. Por el otro lado, se compara con propuestas de otros partidos en cuanto a *alineamiento* (es decir, si unas propuestas se alinean con otras de distintos partidos) y *diferenciación* (es decir, en que medida se proponen lineas de actuación distintas, independientemente de si existe alineación o no).

Hay que destacar que en cierto modo, los pasos (3) "recopilación, (4) "transformación" y (5) "análisis" no son completamente independientes. Por un lado, la fase de transformación de datos (que se puede llevar a cabo durante la fase de recopilación) puede requerir de cierta capacidad de análisis por parte de la persona que se encargue (aún no es una etapa automatizada). Ahí se realiza un "análisis de contenido" inicial, en el que se clasifica el texto.

La última etapa, la de Análisis está enfocada a dos cuestiones primordiales:
- Qué se promete (análisis de contenido)
- Qué se cumple

Para responder a la segunda cuestión, primero se ha de completar el análisis de la primera. Por eso, tras una codificación inicial, ya en la etapa de Análisis se retoma dicho "análisis de contenido" inicial para completarlo. Al fin y al cabo, el contenido de una propuesta suele ser muy limitado, pero se encuentra enmarcado en un programa electoral que vincula la propuesta concreta con otras propuestas y declaraciones que se realizan en el documento así como en el capítulo al que pertenece la propuesta de forma más particular. Es decir, a la hora de analizar una promesa se **debe** completar la transformación añadiendo datos provenientes del programa electoral, expuestos de manera genérica (no en una propuesta concreta) y de la que se pueden deducir motivaciones, objetivos, resultados esperables, etc... 

Es un proceso complejo, pero que dada su sistematización permite verificar las conclusiones si no son respaldadas por los datos y, en su caso, detectar con relativa facilidad los errores. La sistematización también ayuda a la presentación homogénea de los resultados, independientemente de la persona que haya realizado el análisis.

La gran dificultad de esta tarea de sistematización radica en tratar de alcanzar una metodología rigurosa y, a la vez, suficientemente flexible.

Los análisis son el producto final de Seguimiento Político, o mejor dicho, de las personas que quieran colaborar en la plataforma. Por mucho que se trate de objetivar los datos y sistematizar el proceso, el resultado no puede dejar de ser subjetivo. Por eso, y aunque todas las etapas descritas previamente son en realidad tareas colaborativas que pueden realizar varias personas conjuntamente, creemos que los análisis tienen un carácter especial. Cada programa electoral y propuesta sólo se registran y transforman una vez. Sin embargo, hay mucho margen de diferencia en su interpretación y análisis. Por eso, y para evitar que se genere un único "mega-análisis" elaborado y modificado por distintas personas con, posiblemente, diferentes visiones y, por tanto, con argumentos y conclusiones potencialmente contradictorios e incoherentes (como a veces ocurre en la Wikipedia) hemos desarrollado {SP} de modo que que puedan generar tantos análisis de una misma propuesta como se desee. 