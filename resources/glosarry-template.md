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

- JSON: JSON es un formato de texto sencillo para el intercambio de datos. Es usado a la hora de hacer peticiones por medio de las apis para devolver una respuesta, en este caso los datos solicitados.
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
  - 200: OK. La solicitud ha tenido éxito. El significado de un éxito varía dependiendo del método HTTP:
  - 201: CREATED. La solicitud ha tenido éxito y se ha creado un nuevo recurso como resultado de ello. Ésta es típicamente la respuesta enviada después de una petición PUT.
  - 203: NON AUTHORITATIVE INFORMATION. La petición se ha completado con éxito, pero su contenido no se ha obtenido de la fuente originalmente solicitada, sino que se recoge de una copia local o de un tercero. Excepto esta condición, se debe preferir una respuesta de 200 OK en lugar de esta respuesta.
  - 204: NO CONTENT. La petición se ha completado con éxito pero su respuesta no tiene ningún contenido, aunque los encabezados pueden ser útiles. El agente de usuario puede actualizar sus encabezados en caché para este recurso con los nuevos valores.
  - 400: BAD REQUEST. Esta respuesta significa que el servidor no pudo interpretar la solicitud dada una sintaxis inválida.
  - 401: UNAUTHORIZED. Es necesario autenticar para obtener la respuesta solicitada. Esta es similar a 403, pero en este caso, la autenticación es posible.
  - 403: FORBIDDEN. El cliente no posee los permisos necesarios para cierto contenido, por lo que el servidor está rechazando otorgar una respuesta apropiada.
  - 404: NOT FOUND. El servidor no pudo encontrar el contenido solicitado. Este código de respuesta es uno de los más famosos dada su alta ocurrencia en la web.
  - 500: INTERNAL SERVER ERROR. El servidor ha encontrado una situación que no sabe cómo manejarla.
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
