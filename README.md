# Introducción (Español)
Este es un proyecto piloto de seguimiento y análisis político.

Su objetivo es simplemente determinar los datos necesarios, su estructura más adecuada y recibir comentarios de mejora.

Se ha usado Jekyll y github-pages por conveniencia. El siguiente paso sería el de desarrollar una aplicación equivalente empleado otras tecnologías como PHP o Javascript y bases de datos que aporten más flexibilidad y potencial.

Las principales funciones/utilidades de esta aplicación pretenden ser:
- Consulta rápida y veraz de los programas electorales de los distintos partidos políticos en un único lugar. Mejorando la navegabilidad frente a las limitaciones de un documento PDF, y la detección de puntos clave (temáticas, propuestas, ideologías) que ayuden a tomar decisiones informadas de manera más ágil y simple.
- Comparativa de ideologías y propuestas sobre temas concretos
- Seguimiento del cumplimiento de dichas propuestas a partir de la actividad parlamentaria en el congreso de los diputados.

Este proyecto se basó inicialmente en el proyecto [Trump tracker](https://github.com/TrumpTracker/trumptracker.github.io) aunque ha evolucionado de manera que ya poco tiene que ver.

Cualquier ayuda es bienvenida!

# Introduction (English)
Here is a pilot project for political tracking and analysis.

Its aim is simply to determine the necessary data, its most appropriate structure, and receive improvement feedback.

Jekyll and GitHub Pages have been used for convenience. The next step would be to develop an equivalent application using other technologies such as PHP or JavaScript and databases that offer more flexibility and potential.

The main functions/utilities of this application aim to be:
- Quick and reliable consultation of the electoral programs (manifestos) of the different political parties in one place. This improves navigation compared to the limitations of a PDF document and helps detect every statement key points (such as topics, proposals, ideology) to make informed decisions more quickly and simply.
- Comparison of ideologies and proposals on specific topics
- Monitoring the fulfillment of these proposals based on parliamentary activity in the Congress.

This project was initially based on (forked from) [Trump tracker](https://github.com/TrumpTracker/trumptracker.github.io) project, although it has evolved to the point where it now has little in common with it.

We welcome any help!

# First steps
1. populate _data/documents/ (parties manifestos)
1. populate _data/categorization/statuses.yaml and topics.yaml
1. populate _data/tracks/ (promises tracks)
1. populate assets/images/parties/ and assets/images/teasers/
1. edit _data/pages/ files according to your needs

# Execution instructions
1. First of all you need to instal [Jekyll](https://jekyllrb.com/docs/installation/) and [Python](https://wiki.python.org/moin/BeginnersGuide) on your machine.
1. go to /scripts folder and execute "python3 update_files.py" to automatically generate _tracks/, _statements/ and _docs/ files. Make sure you've got imported modules installed as well.
1. execute "bundle exec jekyll serve"
1. DONE now you can check the resulting website on http://127.0.0.1:4000

# Parallel useful repositories 
1. [manifestos-converter](https://github.com/seguimiento-politico/manifestos-converter) -> Helps you convert any manifesto (PDF file) into an yaml file in the format needed by this app in _data/documents/. The yaml resulting file will contain a basic structure and all content. You will need to manually join some paragraphs, add page number and categories and topics. Althought is not a fully automated process it helps you to simplify it greatly.
1. [congreso-scrapper](https://github.com/seguimiento-politico/congreso-scrapper) -> Web scrapper of [Congreso de los Diputados de España](http://congreso.es). The data extracted using this script will be used by this project as functionalities grow. 

# TO-DOs
1. Comments feature [DONE]. Staticman is used but for the time being is deactivated
1. Python web scrapper ~~to automatically populate YAML files~~ from congress activity [DONE]
1. Python web scrapper ~~to automatically populate YAML files~~ of politicians [DONE]
1. Python PDFs scrapper to automatically create new promises [PARTIALLY-DONE] (semi-automatic for the time being)
1. Continue progress on tracking congress activity
1. Continue progress on ways to compare ideologies from different parties
1. Continue progress on ways to detect incongruity and contradictions in the same party
1. Share the project in the dev community (developers to join or feedback)
1. Share the project to the public (so that the projects starts to be useful)
1. add forms so that creating and editing data is more convenient and non-developers friendly
1. Recruit power users such as journalists, students and college professors, professional politics, political analysts, etc. willing to contribute by creating and editing data.
1. Add graphics and statics from elections
1. Show related statements (promises and statements) based on topics and differentiating by position and effect (ideology)
1. Multilingual website


