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

# How-to use it
## First steps
1. populate data:
    - _data/documents/ (parties manifestos)
    - _data/categorization/statuses.yaml and topics.yaml
    - _data/tracks/ (promises tracks)
1. populate images
    - assets/images/parties/ and 
    - assets/images/teasers/
1. create/edit content:
    - _pages/ files according to your needs
    - _posts/ files according to your needs
1. configure comments system:
    - setup a server anywhere else
    - edit staticman.yml accordingly


## Execution instructions
1. First of all you need to instal [Jekyll](https://jekyllrb.com/docs/installation/) and [Python](https://wiki.python.org/moin/BeginnersGuide) on your machine.
1. go to /scripts folder and execute "python3 update_files.py" to automatically generate _tracks/, _statements/ and _docs/ files. Make sure you've got imported modules installed as well.
1. execute "bundle exec jekyll serve"
1. DONE now you can check the resulting website on http://127.0.0.1:4000

## Parallel useful repositories 
1. [manifestos-converter](https://github.com/seguimiento-politico/manifestos-converter) -> Helps you convert any manifesto (PDF file) into an yaml file in the format needed by this app in _data/documents/. The yaml resulting file will contain a basic structure and all content. Then you will need to manually join/merge some paragraphs, add page number and turn some statements into chapters. Althought is not a fully automated process it helps you to speed-up and simplify it greatly.
1. [congreso-scrapper](https://github.com/seguimiento-politico/congreso-scrapper) -> Web scrapper of [Congreso de los Diputados de España](http://congreso.es). The data extracted using this script will be used by this project as functionalities grow. 

# TO-DOs
## Prototype Dev TO-DOs
1. Comments feature [DONE]. Staticman is used but for the time being is deactivated
1. Python web scrapper ~~to automatically populate YAML files~~ from congress activity [DONE]
1. Python web scrapper ~~to automatically populate YAML files~~ of politicians [DONE]
1. Python PDFs scrapper to automatically add new manifestos [PARTIALLY-DONE] (semi-automatic for the time being)

## Full APP Dev TO-DOs
1. migrate this static web jekyll based prototype to a more suited technology/framework (PHP/CodeIgniter-Phalcon, JS/Node.js, Python/Django, Rust, ...)
1. Add "likes" feature. Each user may be able to like/dont-like every statement and be able to see an overview of their selections. Show which ideologies and parties are more alligened (selected).
1. Add global statistics based on all ausers likes/dont-likes
1. Show related statements based on topics and differentiating by position and effect. Filtering by date, topics, party...
1. show conflicting promises
1. show parties incoherences
1. show show parties ideology evolution in time
1. create script to translate YAML manifestos to MD/DOC/PDF format (including templates usage; as a means to promote the use of YAML as main format for creating new manisfestos)
1. add means to open creating and editing data in a more convenient way
1. Add graphics and statics from elections
1. Multilingual website
1. add view feature to analize "megathreats"
1. add view feature to merge different promises (from same or differente parties) into a single and equivalent one (megapromise)
1. add view feature to sintetize a manifesto content based on topics, arguments and promises (megapromises).

## Content TO-DOs
1. Migrate YAML documents (manifestos) to new v3 custom format
1. Start to analyze YAML documents (defects, fallacies, consequences, comments)
1. Create a simple manual on how to add new manifestos (from PDF to YAML)
1. Create a manual on how to analyze manifestos
1. Continue scrapping congress activity

## Analysis TO-DOs
1. Think how to do: for every voting should be catched the reasons why so that we can contrast them with the manifestos arguments
1. Continue progress on ways to classify, analyze and compare ideologies from different parties
1. Apart from manifestos the are other sources of statements (Congress/Senate activity, Public activity/media recorded). think how to include statements from both. 

## Social TO-DOs
1. Share the project in the dev community (developers to join or feedback)
1. share with small group of non-dev-people for feedback
1. Recruit power users such as journalists, students and college professors, professional politics, political analysts, etc. willing to contribute by creating and editing data.
1. Share the project to the general public (so it starts to be useful)




