# ***¿Para qué usamos Clases en Python?***

Las clases en `Python` son una estructura de programación que permite definir un conjunto de métodos y atributos los cuales describen un objeto.<br>
Una clase es como un constructor de objetos.
Cuando creamos una clase nueva, creamos un nuevo tipo de objeto, el cual nos permite crear una instancia de ese tipo.<br>

## Motivos para usar las ``clases``
- Permite reutilizar el código.<br>
Las ``clases`` permiten crear una plantilla para objetos, por lo tanto, puedes crear múltiples instancias de una clase sin la necesidad de escribir el mismo código una y otra vez.
- Modularidad. <br>
Las ``clases`` permiten dividir el código en unidades mas pequeñas, haciendo que el código sea más **fácil de manejar, probar**...
- Encapsulación.<br>
Las ``clases`` permiten agrupar datos y funcionalidades en un único objeto, haciendo que el código sea más limpio y tenga menos errores.
- Herencia.<br>
Las ``clases`` permiten crear jerarquías mediante herencia. 
- Polimorfismo.<br>
Gracias al ``polimorfismo`` se puede utilizar el mismo nombre de método en diferentes clases obteniendo un comportamiento diferente dependiendo del tipo de objeto.

## Sintaxis para crear una clase
Para crear una Clase utilizamos la palabra clave ` class `.<br>
```python
class EjemploClase:
```

## Sintaxis para crear un objeto
```python
class EjemploClase:

obj = EjemploClase() 
```

### Ejemplo
```python
class MyName: #Aqui hemos creado la clase
    def greeting(self):
        return f'Hello everybody.'

greet = MyName() #Aqui hemos creado el objeto
print (greet.greeting())
```


# ***¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?***

El método `__init__` se ejecuta automáticamente al crear una instancia de una Clase. Esta función se llama automáticamente cada vez que se utiliza la clase para crear un objeto nuevo.<br>
Se utiliza como constructor para inicializar los atributos de una instancia recién creada de una clase, el método ``__init__`` no tiene un valor de retorno, si escribimos un ``return`` dentro de ese método, Python lo ignorara.<br>
> Con instancia nos referimos a un objeto creado a partir de una clase.

![Instancia](https://kinsta.com/wp-content/uploads/2021/06/Kinsta-Instances.png)

## Sintaxis
```python
def __init__(self, name , age):
```

El parámetro `self` es obligatorio, hace referencia a la instancia actual del objeto. Se utiliza para acceder a los atributos y métodos de esa instancia.

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
Tenemos una librería y nos llega un libro nuevo llamado "Nacidos de la bruma" y queremos añadirlo a nuestra base de datos.
```python
POST /books
{“name”: “Nacidos de la bruma”,
“tapa”: “dura”,
“ISBN” : 9788419260451
“price” : 28.40
}
```

- **PUT** <br>
Este método se utiliza para **reemplazar un recurso existente** con una versión actualizada. <br>
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
Si no añadimos los datos de ‘name’, ‘tapa’ e ‘ISBN’ se borrarán, aunque estos datos no hayan cambiado.<br>

Aparte de estos 3 verbos tenemos otros 2, PATCH y DELETE

- **PATCH** <br>
Este método es similar a `PUT` con la diferencia de que este no sobreescribe recursos existentes, es decir, nos permite cambiar el precio del libro sin la necesidad de insertar el resto de datos.

### Ejemplo
```python
PATCH /books/5
{
“price” : 25.90
}
```

- **DELETE** <br>
Este método se utiliza para eliminar datos de una base de datos. Ciertas APIs utilizan mecanismos de autorización para que solo los clientes con permisos adecuados puedan eliminar recursos.

### Ejemplo
```python
DELETE /books/5
```
Esto eliminaría permanentemente el libro con ID 5 de la base de datos.

# ***¿Es MongoDB una base de datos SQL o NoSQL?***

MongoDB es una base de datos *NoSQL* orientada a documentos y de código abierto, considerada una base de datos no relacional. <br>
A diferencia de una base de datos SQL, la cual almacena datos relacionados en tablas separadas, MongoDB almacena datos en un documento flexible en formato parecido a JSON llamado *BSON*.<br>
En MongoDB en lugar de tablas, se llaman colecciones, las cuales pueden mantener todos los datos relacionados juntos.

## Caracteristicas
- Consultas ad hoc.<br>
Se pueden realizar búsquedas por campos, consultas de rangos y expresiones regulares. Estas consultas pueden devolver un campo especifico del documento o puede ser una funcion JS definida por el usuario.
- Indexacion<br>
Cualquier campo documentado puede ser indexado y añadir multiples índices secundarios.
- Replicacion.<br>
La replicaión es un proceso en el que se crean copias de los datos para garantizar disponibilidad y seguridad. En ``MongoDB`` se usa el modelo de replicacio primario-secundario. Quere decir que hay un servidor primario con todas las operaciones de escritura y lectura y un servidor secundario que solo permite la lectura 
Los servidores secundarios actuan como respaldo. Son como una **copia de seguridad**.
- Balanceo de carga.<br>
Puede ejecutarse de manera simultanea en diversos servidores ofreciendo distribución de trabajo de manera equitativa para evitar la sobrecarga de un único servidor, lo que hace que, el rendimiento y disponibilidad del servidor sea mayor.
- Almacenamiento de archivos.<br>
Se puede utilizar como sistema de almacenamiento debido a la funcionalidad ``GridFS``. ``GridFS`` permite manipular contenido y archivos grandes , tales como, imágenes y videos.
- Ejecucion de JavaScript del lado del servidor.<br>
``MongoDB`` puede realizar consultas utilizando JS, enviándolas directamente a la base de datos para ser ejecutadas. Facilita la manipulación de datos y y realización de consultas sin la necesidad de enviar esos datos a una aplicación externa para su procesamiento.

![MongoDB](https://www.nisum.com/hubfs/Sql%20vs%20NoSQL.svg)


# ***¿Qué es una API?***

**A**: Application<br>
**P**: Programming<br>
**I**: Interface<br>
En castellano sería Interfaz de Programación de Aplicaciones.
Son un conjunto de funciones y procedimientos que permite integrar sistemas, permitiendo que sus funcionalidades puedan ser reutilizadas por otras aplicaciones o software. Una `API` actúa como **puente de comunicación** entre los servicios backend (base de datos, servidores…) y el cliente (la aplicación).<br>
Hay 3 categorias:
- **API Web**. Es una interfaz de programación de aplicaciones para
la Web.
- **API de navegador**. Amplía la funcionalidad de un navegador
web.
- **API de servidor**. Amplía la funcionalidad de un servidor web.
  
Hay 4 tipos:
- **APIs públicas o abiertas**.<br>
Estas `APIs` están **disponibles** para que otros usuarios y/o desarrolladores las empleen con **mínimas restricciones**. Hay casos en las que son totalmente accesibles. <br>
Por ejemplo la API de Twitter.
- **APIs privadas o internas**.<br>
Estas `APIs` están **ocultas** de los usuarios externos, únicamente se exponen para los sistemas internos de una organización. Se emplean **para desarrollo interno** de la empresa.<br>
Por ejemplo la API interna de una empresa de ventas.
- **APIs de aliados comerciales**.<br>
Estas `APIs` se exponen entre aliados comerciales. Solo están disponibles si dispones de una **autorización**.<br>
Por ejemplo la API de PayPal
- **APIs compuestas**.<br>
Estas ``APIs`` utilizan diversas APIs de servicio y
permiten a los desarrolladores acceder a varios terminales.<br>
Por ejemplo la API de Vueling.<br>


[API](https://www.sydle.com/es/blog/api-6214f68876950e47761c40e7) <br>
![Funcionamiento API](https://apiaddicts-web.s3.eu-west-1.amazonaws.com/wp-content/uploads/2022/08/12150313/1_7yAihbfGrMCzjUzIF2UitA-768x377.png)


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
Facilita la configuración para distintos entornos y el cambio sencillo entre ellos.

- **COLECCIONES DE SOLICITUDES**<br>
Agrupa las solicitudes relacionadas en colecciones. Esto facilita la organización y ejecución de pruebas automatizadas.

- **PRUEBAS AUTOMATIZADAS**<br>
Permite crear pruebas que se ejecutan automáticamente para validar que la API cumple con su comportamiento esperado. Esto facilita la detección de fallos y contribuye a mejorar la confiabilidad del software.

- **DOCUMENTACION DE API**<br>
Genera documentación detallada de la API, de forma automatizada, a partir de las solicitudes y respuestas realizadas. Esto facilita su comprensión y uso por parte de otros desarrolladores.

## Ventajas

- **FACILIDAD A LA HORA DE TRABAJAR**<br>
Dispone de una interfaz gráfica de usuario intuitiva, sencilla y personalizable.

- **AMPLIA COMPATIBILIDAD CON NUMEROSAS TECNOLOGIAS Y PROTOCOLOS WEB**<br>
Es compatible con varios protocolos como HTTP, REST, SOAP, HTTPS…

- **APLIA GAMA DEFUNCIONALIDADES PARA DISEÑAR, PROBAR Y DOCUMENTAR APIS**<br>
Postman se considera una de las soluciones mas completas disponibles para gestionar todo el proceso de desarrollo de APIs.

- **FOMENTA Y FACILITA LA COLABORACION**<br>
Facilita la colaboracion entre los miembros del equipo de desarrollo.

- **AMPLIA COMUNIDAD EN CONSTANTE CRECIMIENTO**<br>
Postman tiene una gran comunidad aportando una gran cantidad de recursos.

- **SCRIPTS PERSONALIZADOS**
Permite agregar scripts personalizados utilizando JavaScript para realizar validaciones avanzadas o automatizar procesos dentro de las solicitudes.

- **SE INTEGRA CON HERRAMIENTAS POPULARES**<br>
Se integra perfectamente con herramientas utilizadas en desarrollo de software como GitHub, Swagger, Jenkins… para facilitar el flujo de trabajo.

- **PERMITE ORGANIZAR Y AGRUPAR SOLICITUDES RELACIONADAS**<br>
Las colecciones son una característica de Postman las cuales permiten organizar y agrupar solicitudes relacionadas, simplificando la administración de API complejas y facilitando la reutilización de solicitudes y flujos de trabajos en diversos proyectos.

# ***¿Qué es el polimorfismo?***

Es la capacidad de utilizar una interfaz única para diferentes tipos de datos o clases.
La palabra `polimorfismo` significa **muchas formas**. En programación esto se refiere a métodos/funciones/operadores con el mismo nombre que pueden ejecutarse en muchos objetos o clases.

## Polimorfismo de clases
Se usa en en métodos de clase, pudiendo tener varias clases con el mismo nombre.

### Ejemplo
Tenemos 3 clases distintas (AlumnOne, AlumnTwo y AlumnThree) y las 3 tienen el mismo método greet( ):
```python
class AlumnOne:
    def __init__ (self, name, last_name):
        self.name = name
        self.last_name = last_name

    def greet(self):
        print(f'My name is {self.name} {self.last_name}.')

class AlumnTwo:
    def __init__ (self, name, last_name):
        self.name = name
        self.last_name = last_name

    def greet(self):
        print(f'My name is {self.name} {self.last_name}.')

class AlumnThree:
    def __init__ (self, name, last_name):
        self.name = name
        self.last_name = last_name

    def greet(self):
      print(f'My name is {self.name} {self.last_name}.')

Alumn1= AlumnOne('Janire', 'Martinez') #Creamos el objeto AlumnOne
Alumn2= AlumnTwo('Maria', 'Gonzalez') #Creamos el objeto AlumnTwo
Alumn3= AlumnThree('Laura', 'Fernandez') #Creamos el objeto AlumnThree

for alumn in (Alumn1, Alumn2, Alumn3):
  alumn.greet()
```
### Polimorfismo de clase herencia
Tambien podemos crear una **clase padre** llamada Alumns y hacer las clases AlumnOne AlumnTwo y AlumnThree hijas de Alumns. Estas heredarían los métodos de la clase padre Alumns.

### Ejemplo
```python
class Alumns:
  def __init__ (self, name, last_name, city):
    self.name = name
    self.last_name = last_name
    self.city = city

  def greet(self):
    print(f"Me llamo {self.name} {self.last_name} y soy de {self.city}")

class AlumnOne(Alumns):
  pass #`pass`significa que no se agrega ningún tipo de funcionalidad extra, heredan directamente el comportamiento de la clase padre alumns

class AlumnTwo(Alumns):
  pass #`pass` significa que no se agrega ningún tipo de funcionalidad extra, heredan directamente el comportamiento de la clase padre alumns

class AlumnThree(Alumns):
  def greet(self):
    print(f"O meu nome é {self.name} {self.last_name} e sou de Portugal.") #Sobreescribe el método greet()

Alumn1= AlumnOne('Janire', 'Martinez', 'España') 
Alumn2= AlumnTwo('Maria', 'Gonzalez', 'España') 
Alumn3= AlumnThree('Laura', 'Fernandez', 'Portugal') 

for alumn in (Alumn1, Alumn2, Alumn3):
  alumn.greet()
```

[Polimorfismo](https://www.w3schools.com/python/python_polymorphism.asp)

# ***¿Qué es un método dunder?***
Un método `dunder` es aquel cuyo nombre empieza y acaba con doble guion
bajo '__'. El nombre `dunder` es la abreviatura de double underscore.<br>
Estos métodos no son llamados por el usuario, son invocados automaticamente por el intérprete de ``Python`` en momento específicos para permitir que objetos y clases se comporten de maneras especiales.<br>
Los métodos ``dunder`` permiten **personalizar el comportamiento** de los objetos.

Los métodos más comunes son:
- `__init__` : para inicializar una nueva instancia de una clase.
- `__str__`: devuelve una string de un objeto, legible para el usuario. ```print(objeto)```
- `__repr__`:devuelve una string de un objeto, informativa y útil para
el desarrollador. ``eval()``
- `__len__`:devuelve la longitud de un objeto. ``(len(objeto))``
- `__getitem__`: permite acceder a elementos mediante índices. ``(objeto[index])``
- `__setitem__`: permite modificar elementos mediante índices.``(objeto[index] = valor)``
- `__delitem__`:permite eliminar elementos mediante índices. ``(del objeto[index])``
- `__iter__`: convierte un objeto en un iterable.
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
[Dunder](https://www.luisllamas.es/metodos-dunder-python/)

# ***¿Qué es un decorador de python?***

Un ``decorador de Python`` es una función que permite modificar o extender el comportamiento de otra función, clase o método sin cambiar su código original. Es muy útil cuando queremos añadir funcionalidades adicionales a una función o método de manera flexible y reutilizable.<br>

## Cómo funciona un decorador
Un ``decorador`` **envuelve** la función original en una nueva función. Dentro de esa función se pueden agregar comportamientos adicionales antes o después de llamar a la funcion original. El ``decorador`` devuelve la función modificada, reemplazando la original.

## Sintaxis
Para aplicar un decorador en una función usamos el símbolo ``@``.
```python
@decorador(func)
```

### Ejemplo
```python
def greeting(func):
    def greet():
        print("Good morning")
        func()#Llamamos a la funcion original decorada
    return greet

@greeting #Usamos el decorador
def MyGreet():
    print("Good morning, my name is Janire.")

MyGreet()#Llamamos a la funcion decorada
```
![Decorator](https://www.ionos.es/digitalguide/fileadmin/DigitalGuide/Schaubilder/representacion-grafica-del-patron-decorator.png)