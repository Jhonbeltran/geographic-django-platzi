##Analicemos la estructura de carpetas y archivos que se generaron:

###Dentro de la "App Central"

* init.py --> Le dice a Python que es un paquete
* settings.py --> Configuraciones del proyecto
* urls.py --> URL’s del proyecto
* wsgl.py --> Es un archivo que mas adelante nos va a permitir desplegar el proyecto

### Dentro de nuevas App
* init.py --> Le dice a Python que es un paquete
* admin.py --> Administrador de contenidos para la aplicacion actual
* apps.py --> Configuración de nuestra aplicación dentro de los settings
* models.py --> Comunicacion con la base de datos
* migrations/ (carpeta) --> Cambios en la estructura de la base de datos
* test.py --> Pruebas Unitarias
* views.py --> Componente encargado de enlazar modelos con templates y ejecutar operaciones lógicas



### Herramienta de utilidades

* manage.py --> Poner el proyecto dentro del path de Django, Contiene un listado de posibilidades utilidades que nos van a servir para la gestión del proyecto.

### Base de datos por defecto

* db.sqlite3 --> Base de Datos por Defecto Sqlite 3

> Recuerda que cada aplicación de Django se compone de diferentes aplicaciones, de forma que tenemos mini-apps dentro de las aplicaciones más grandes, esto nos sirve para mantener el código organizado y reusar dichas aplicaciones en otros proyectos.

> Cada App de Django es una librería en si misma