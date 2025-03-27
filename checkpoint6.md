# ***¿Para qué usamos Clases en Python?***

Usamos las Clases en Python para estructurar y organizar nuestro código
en componentes reutilizables.
Las Clases proveen una forma de empaquetar datos y funcionalidad
juntos.
Facilitan la reutilización, modularidad y facilidad de mantenimiento del
código al ‘encapsular’ datos y funcionalidades dentro de los objetos.
Una clase es como un constructor de objetos.
Para crear una Clase utilizamos la palabra clave ` class `.

## Sintaxis
```python
class __init__(self):
```


# ***¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?***

El método `__init__` se ejecuta automáticamente al crear una instancia
de una Clase.
Esta función se llama automáticamente cada vez que se utiliza la clase
para crear un objeto nuevo.
Se utiliza como constructor para inicializar los atributos de una instancia
recién creada de una clase. 
> Con instancia nos referimos a un objeto creado a partir de una clase.

## Sintaxis
```python
def __init__(self, name , age):
```

El parámetro `self` es obligatorio, hace referencia a la instancia actual del
objeto. Se utiliza para acceder a los atributos y métodos de esa instancia.

### Ejemplo
```python
class MyName:
    def __init__(self, name, last_name):
        self.name = name #Inicializa el atributo 'name' con el valor 'name'
        self.last_name = last_name #Inicializa el atributo 'last_name' con el valor 'last_name'

    def greeting(self):
        print(f'Hola me llamo {self.name} {self.last_name}.')

greet = MyName( "Janire", "Martinez") #Creamos la instancia de la clase MyName
greet.greeting() #Llamamos al método greeting
```

# ***¿Cuáles son los tres verbos de API?***
- **GET** <br> 
Este método se utiliza para **recuperar datos del servidor**. Se puede
acceder a todos los recursos de un tipo determinado o bien a un recurso
especifico.

### Ejemplo
```python
GET /books --> estos devolvería todos los libros
GET/books/4 --> devolvería el libro con el ID 4
```

- **POST** <br>
Este método es utiliza para **crear recursos nuevos**.

### Ejemplo
Tenemos una librería y nos llega un libro nuevo llamado "Nacidos de la
bruma" y queremos añadirlo a nuestra base de datos.
```python
POST /books
{“name”: “Nacidos de la bruma”,
“tapa”: “dura”,
“ISBN” : 9788419260451
“price” : 28.40
}
```

- **PUT** <br>
Este método se utiliza para **reemplazar un recurso existente** con una
versión actualizada. <br>
Es necesario incluir todos los datos ya que, si no lo hacemos, se borrarán.

### Ejemplo
El libro que añadimos en el ejemplo anterior, ahora vale 25.9.
```python
POST /books/5
{“name”: “Nacidos de la bruma”,
“tapa”: “dura”,
“ISBN” : 9788419260451
“price” : 25.90
}
```
Si no añadimos los datos de ‘name’, ‘tapa’ e ‘ISBN’ se borrarán, aunque
estos datos no hayan cambiado.<br>

Aparte de estos 3 verbos tenemos otros 2, PATCH y DELETE

- **PATCH** <br>
Este método es similar a `PUT` con la diferencia de que este no
sobreescribe recursos existentes, es decir, nos permite cambiar el precio
del libro sin la necesidad de insertar el resto de datos.

### Ejemplo
```python
PATCH /books/5
{
“price” : 25.90
}
```

- **DELETE** <br>
Este método se utiliza para eliminar datos de una base de datos. Ciertas
APIs utilizan mecanismos de autorización para que solo los clientes con
permisos adecuados puedan eliminar recursos.

### Ejemplo
```python
DELETE /books/5
```
Esto eliminaría permanentemente el libro con ID 5 de la base de datos.

# ***¿Es MongoDB una base de datos SQL o NoSQL?***

MongoDB es una base de datos *NoSQL* orientada a documentos y de
código abierto, considerada una base de datos no relacional.
A diferencia de una base de datos SQL, la cual almacena datos
relacionados en tablas separadas, MongoDB almacena datos en un
documento flexible en formato parecido a JSON llamado *BSON*.
En MongoDB en lugar de tablas, se llaman colecciones, las cuales pueden
mantener todos los datos relacionados juntos.

![MongoDB](https://kockpit.in/blogs-community/assets/uploads/16bcd0116efe156e2efba32903f17d05.webp)


# ***¿Qué es una API?***

**A**: Application<br>
**P**: Programming<br>
**I**: Interface<br>
En castellano sería Interfaz de Programación de Aplicaciones.
Son un conjunto de funciones y procedimientos que permite integrar
sistemas, permitiendo que sus funcionalidades puedan ser reutilizadas
por otras aplicaciones o software.
Hay 3 categorias:
- **API Web**. Es una interfaz de programación de aplicaciones para
la Web.
- **API de navegador**. Amplía la funcionalidad de un navegador
web.
- **API de servidor**. Amplía la funcionalidad de un servidor web.
  
Hay 4 tipos:
- **APIs públicas o abiertas**. Estas `APIs` están **disponibles** para que otros usuarios y/o desarrolladores las empleen con **mínimas restricciones**. Hay casos en las que son totalmente accesibles. <br>
Por ejemplo la API de Twitter.
- **APIs privadas o internas**. Estas `APIs` están **ocultas** de los usuarios externos, únicamente se exponen para los sistemas internos de una organización. Se emplean **para desarrollo interno** de la empresa.<br>
Por ejemplo la API interna de una empresa de ventas.
- **APIs de aliados comerciales**. Estas `APIs` se exponen entre aliados comerciales. Solo están disponibles si dispones de una **autorización**.<br>
Por ejemplo la API de PayPal
- **APIs compuestas**. Estas ``APIs`` utilizan diversas APIs de servicio y
permiten a los desarrolladores acceder a varios terminales.<br>
Por ejemplo la API de Vueling.<br>
La `API` actúa como **puente de comunicación** entre los servicios backend (base de datos, servidores…) y el cliente (la aplicación).

[API](https://www.sydle.com/es/blog/api-6214f68876950e47761c40e7) <br>
![Funcionamiento API](<https://outviocmsassets.s3.eu-central-1.amazonaws.com/cl2t0lc4l000w7b7t0yli356j.jpg>)


# ***¿Qué es Postman?***

Es una **herramienta que se utiliza para probar APIs**. <br>
- Permite a los desarrolladores interactuar y probar el funcionamiento de servicios web en aplicaciones proporcionando una interfaz gráfica intuitiva y fácil de usar para enviar solicitudes a servidores web y recibir las respuesta correspondiente.
- Permite gestionar diferentes entornos de desarrollo, organizar las solicitudes en colecciones y realizar pruebas automatizadas para verificar el comportamiento los sistemas.

## Caracteristicas y funcionalidades
- **ENVIO DE SOLICITUDES**<br>
Permite enviar diferentes tipos de solicitudes HTTP, como:<br>
`GET`: para obtener datos de un servidor.<br>
`PUT`: para reemplazar un recurso existente en el servidor.<br>
`POST`: para crear un uevo recurso en el servidor.<br>
`DELETE`: para eliminar un recurso del servidor.<br>

- **GESTION DE ENTORNOS**<br>
Facilita la configuración para distintos entornos y el cambio sencillo
entre ellos.

- **COLECCIONES DE SOLICITUDES**<br>
Agrupa las solicitudes relacionadas en colecciones. Esto facilita la
organización y ejecución de pruebas automatizadas.

- **PRUEBAS AUTOMATIZADAS**<br>
Permite crear pruebas que se ejecutan automáticamente para validar
que la API cumple con su comportamiento esperado. Esto facilita la
detección de fallos y contribuye a mejorar la confiabilidad del
software.

- **DOCUMENTACION DE API**<br>
Genera documentación detallada de la API, de forma automatizada, a
partir de las solicitudes y respuestas realizadas. Esto facilita su
comprensión y uso por parte de otros desarrolladores.
##VENTAJAS

- **FACILIDAD A LA HORA DE TRABAJAR**<br>
Dispone de una interfaz gráfica de usuario intuitiva, sencilla y
personalizable.

- **AMPLIA COMPATIBILIDAD CON NUMEROSAS TECNOLOGIAS Y PROTOCOLOS WEB**<br>
Es compatible con varios protocolos como HTTP, REST, SOAP,
HTTPS…

- **APLIA GAMA DEFUNCIONALIDADES PARA DISEÑAR, PROBAR Y DOCUMENTAR APIS**<br>
Postman se considera una de las soluciones mas completas
disponibles para gestionar todo el proceso de desarrollo de APIs.

- **FOMENTA Y FACILITA LA COLABORACION**<br>
Facilita la colaboracion entre los miembros del equipo de
desarrollo.

- **AMPLIA COMUNIDAD EN CONSTANTE CRECIMIENTO**<br>
Postman tiene una gran comunidad aportando una gran cantidad
de recursos.

- **SCRIPTS PERSONALIZADOS**
Permite agregar scripts personalizados utilizando JavaScript para
realizar validaciones avanzadas o automatizar procesos dentro de
las solicitudes.

- **SE INTEGRA CON HERRAMIENTAS POPULARES**<br>
Se integra perfectamente con herramientas utilizadas en desarrollo
de software como GitHub, Swagger, Jenkins… para facilitar el flujo
de trabajo.

- **PERMITE ORGANIZAR Y AGRUPAR SOLICITUDES RELACIONADAS**<br>
Las colecciones son una característica de Postman las cuales
permiten organizar y agrupar solicitudes relacionadas,
simplificando la administración de API complejas y facilitando la
reutilización de solicitudes y flujos de trabajos en diversos
proyectos.

# ***¿Qué es el polimorfismo?***

# ***¿Qué es un método dunder?***
Un método `dunder` es aquel cuyo nombre empieza con doble guion
bajo '__'. El nombre `dunder` es la abreviatura de double underscore.

Los métodos más comunes son:
- `__init__` : para inicializar una nueva instancia de una clase.
- `__str__`: devuelve una string de un objeto, legible para el usuario.
- `__repr__`:devuelve una string de un objeto, informativa y útil para
el desarrollador.
- `__len__`:devuelve la longitud de un objeto.
- `__getitem__`: para acceder a elementos mediante índices.
- `__setitem__`: para asignar valores a elementos mediante índices.
- `__delitem__`:para eliminar elementos mediante índices.
- `__iter__`: devuelve un iterador para el objeto.
- `__next__`: devuelve el siguiente elemento del iterador.
  
## Sintaxis
```python
def __init__(self):
def __str__(self):
def __repr__(self):
def __len__(self):
def __getitem__(self):
def __setitem__(self):
def __delitem__(self):
def __iter__(self):
def __next__(self):
```