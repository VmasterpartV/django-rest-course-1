# Glosario

## Django

- Model: Un modelo de Django es una descripción de los datos en la base de datos, representada como código de Python.
- Migration: Las migraciones son cómo almacena Django cambios a sus modelos (y por tanto el esquema de base de datos) - son simplemente los archivos en el disco. Puedes leer la migración para su nuevo modelo si se quiere; que es el archivo polls/migrations/0001_initial.py.
- ORM: Un ORM es un modelo de programación que permite mapear las estructuras de una base de datos relacional (SQL Server, Oracle, MySQL, etc.), en adelante RDBMS (Relational Database Management System), sobre una estructura lógica de entidades con el objeto de simplificar y acelerar el desarrollo de nuestras aplicaciones.
- QuerySet:Un QuerySet es, en esencia, una lista de objetos de un modelo determinado. Un QuerySet te permite leer los datos de la base de datos, filtrarlos y ordenarlos.

## Django REST Framework

- Serializers: Los serializers son clases que nos permiten transformar datos de formatos más propios de Django como objetos que extienden de Model o querysets, en formatos más propios del entorno web como puedan ser JSON y XML, y nos permiten hacerlo en ambas direcciones.
- Viewsets: Django REST Framework incorpora una abstracción para trabajar con ViewSets, que nos permite concentrarnos en modelar el estado y las interacciones de la API, y dejar que la construcción de URLS se gestione automáticamente, en base a unas convenciones comunes.
Los ViewSet son clases similares a las clases View, con la diferencia de que en lugar de proporcionar métodos de gestión como get y put, proporciona operaciones de read y update.
- Mixins: Un mixin no es nada más que una clase que no está concebida para tener entidad por sí misma, sino por extender la funcionalidad a otras clases usando la herencia múltiple de Python. Un mixin, por lo tanto, añade funcionalidad a las clases.

## RESTful

- JSON:
- Headers:
  - Content-Type:
  - Authorization:
  - Cookie:
  - Accept:
  - Content-Length:
  - Attachment:
- Parsers
- Renders
- Status codes
  - 200:
  - 201:
  - 400:
  - 401:
  - 404:
  - 500:
    ...
- HTTP Methods:
  - GET
  - POST
  - PUT
  - PATCH
  - DELETE
  - HEAD
  - OPTIONS

## Otros conceptos

- CRUD:
- JWT
  - Definition:
  - HS254:
- OpenAPI:
