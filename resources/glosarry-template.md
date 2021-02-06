# Glosario

## Django

- Model: Un modelo de Django es una descripción de los datos en la base de datos, representada como código de Python.
- Migration: Las migraciones son cómo almacena Django cambios a sus modelos (y por tanto el esquema de base de datos) - son simplemente los archivos en el disco. Puedes leer la migración para su nuevo modelo si se quiere; que es el archivo polls/migrations/0001_initial.py.
- ORM: Un ORM es un modelo de programación que permite mapear las estructuras de una base de datos relacional (SQL Server, Oracle, MySQL, etc.), en adelante RDBMS (Relational Database Management System), sobre una estructura lógica de entidades con el objeto de simplificar y acelerar el desarrollo de nuestras aplicaciones.
- QuerySet: Un QuerySet es, en esencia, una lista de objetos de un modelo determinado. Un QuerySet te permite leer los datos de la base de datos, filtrarlos y ordenarlos.

## Django REST Framework

- Serializers: Los serializers son clases que nos permiten transformar datos de formatos más propios de Django como objetos que extienden de Model o querysets, en formatos más propios del entorno web como puedan ser JSON y XML, y nos permiten hacerlo en ambas direcciones.
- Viewsets: Django REST Framework incorpora una abstracción para trabajar con ViewSets, que nos permite concentrarnos en modelar el estado y las interacciones de la API, y dejar que la construcción de URLS se gestione automáticamente, en base a unas convenciones comunes.
Los ViewSet son clases similares a las clases View, con la diferencia de que en lugar de proporcionar métodos de gestión como get y put, proporciona operaciones de read y update.
- Mixins: Un mixin no es nada más que una clase que no está concebida para tener entidad por sí misma, sino por extender la funcionalidad a otras clases usando la herencia múltiple de Python. Un mixin, por lo tanto, añade funcionalidad a las clases.

## RESTful

- JSON: JSON es un formato de texto sencillo para el intercambio de datos. Es usado a la hora de hacer peticiones por medio de las apis para devolver una respuesta, en este caso los datos solicitados.
- Headers:
  - Content-Type: Indica el tipo de medio del recurso.
  - Authorization: Contiene las credenciales para autenticar a un usuario con un servidor.
  - Cookie: Contiene HTTP cookies enviadas previamente por el servidor con la cabecera Set-Cookie.
  - Accept: Informa al servidor sobre los diferentes tipos de datos que pueden enviarse de vuelta. Es de tipo MIME.
  - Content-Length: Indica el tamaño del cuerpo del recurso, expresado en números decimales de octetos, que ha sido enviado al recipiente.
  - Attachment: Indica que debe descargarse.
- Parsers: Es un analizador de mensajes HTTP escritos en C. Analiza tanto las solicitudes como las respuestas. El analizador está diseñado para utilizarse en aplicaciones HTTP de rendimiento. No realiza ninguna llamada al sistema ni asignaciones, no almacena datos en el búfer, se puede interrumpir en cualquier momento. Dependiendo de su arquitectura, solo requiere alrededor de 40 bytes de datos por flujo de mensajes (en un servidor web que es por conexión). 
- Renders: Es un anglicismo para representación gráfica, usado en la jerga informática para referirse al proceso de generar imagen fotorrealista, o no, a partir de un modelo 2D o 3D (o en lo que colectivamente podría llamarse un archivo de escena) por medio de programas informáticos.
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
  - GET: El método GET solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos.
  - POST: El método POST se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor.
  - PUT: El modo PUT reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición.
  - PATCH: El método PATCH es utilizado para aplicar modificaciones parciales a un recurso.
  - DELETE: El método DELETE borra un recurso en específico.
  - HEAD: El método HEAD pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.
  - OPTIONS: El método OPTIONS es utilizado para describir las opciones de comunicación para el recurso de destino.

## Otros conceptos

- CRUD: Hace referencia a un acrónimo en el que se reúnen las primeras letras de las cuatro operaciones fundamentales de aplicaciones persistentes en sistemas de bases de datos:
  - Create (Crear registros)
  - Read bzw. Retrieve (Leer registros)
  - Update (Actualizar registros)
  - Delete bzw. Destroy (Borrar registros)
En pocas palabras, CRUD resume las funciones requeridas por un usuario para crear y gestionar datos.
- JWT
  - Definition: Es un estándar abierto basado en JSON propuesto por IETF (RFC 7519) para la creación de tokens de acceso que permiten la propagación de identidad y privilegios o claims en inglés.
  - HS254: Es un algoritmo de encriptación que da lugar a un fichero cifrado.
- OpenAPI: Es un estándar para definir contratos de Api. Los cuales describen la interfaz de una serie de servicios que vamos a poder consumir por medio de una signatura. Por ejemplo, saber que vamos a tener una operación de sumar que va a recibir dos números y que estos son del tipo “entero”.
