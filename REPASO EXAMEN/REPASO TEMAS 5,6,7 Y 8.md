# **CAPITULO 9 - CLIENTES DEL DOMINIO EN WINDOWS SERVER \[TEMA 5]**



##### **ESTRUCTURA:**



│Consultas guardadas

│Dominio.local

&nbsp;├─ Builtin

&nbsp;├─ Computers

&nbsp;├─ Domain Controllers

&nbsp;├─ ForeignSecurityPrincipals

&nbsp;├─ Keys

&nbsp;├─ LostAndFond

&nbsp;├─ Managed Service Accounts

&nbsp;├─ Program Data

&nbsp;├─ System

&nbsp;├─ Users

&nbsp;├─ Usuarios y grupos propios

&nbsp;├─ NTDS Quotas

&nbsp;├─ TPM Devices



***Existen varias formas de añadir estos privilegios desde el Administrador de usuarios y grupos del directorio o desde el Administrador de directivas de grupos (GPO)***



##### **9.2 Unir un cliente al dominio**



├─ Crear el usuario

├─ Establecer las características de red para que coincidida con las necesidades del dominio

├─ Ajustar nombre de equipo y cliente

├─ Unir el equipo al dominio



Los cambios ene l ordenador cliente deberá realizarlos un administrador o persona con permisos del mismo dominio



##### **9.3 Creas carpetas personales para los clientes**



Un lugar donde el usuario va a poder subir cosas, que no se puede confundir con la carpeta del perfil móvil que es una carpeta para que se le cargue el perfil.



###### **¿Cómo se crea estas carpetas?**



1. Se crea una carpeta normal

2\. Propiedades

3\. Configuración avanzada

4\. Compartir Avanzado

5\. Añadimos permisos

6\. Volvemos a los usuarios del directorio activo

7\. Propiedades del usuario

8\. Ventana Perfil

9\. Marcar carpeta particular

10\. Seleccionar opción conectar

11\. Seleccionar una letra y añadir la ruta con el nombre (nombre del servidor / la carpeta en cuestión / %username% \[Variable de entorno para que cada usuario tenga la carpeta con su nombre de usuario.])



##### **9.4 Crear carpetas compartidas por un grupo de usuarios**



1. Seleccionamos la carpeta

2\. Compartir a usuario / grupo especifico

3\. Añadimos a los usuarios / grupos a los que queremos agregar



##### **9.5 - Asignación de derechos  a usuarios y grupos**



Los derechos permiten a los usuarios realizar acciones especificas en el sistema, con toda la estructura montada la pregunta es ¿Cómo gestiono el propio directorio?



**Permisos -->** Control del acceso a un recurso / equipo

**Derechos -->** La forma en la que yo accedo al sistema (inicio de sesión local, todo lo que tenga que ver con la conexión)

**Privilegios -->** Cosas especiales que hacemos en el sistema (Copias de seguridad).



El **privilegio** (sistemas) prevalece ante el **permiso** (recursos)



##### **9.6 Compartir una impresora del controlador de dominio con Windows Server 2022**



1. Configurar la impresora para que funcione con el servidor

2\. Creamos un grupo especifico para la impresora virtual (O usar grupo de impresión)

3\. Instalamos el rol de ***Servicios de impresión y documentos***

4\. Una vez tenemos el rol instalado, abriremos el Administrador de impresión

5\. Seleccionamos impresoras --> Seleccionamos la impresora

6\. Hacemos click en propiedades --> Compartir esta impresora

7\. Añadimos los grupos / usuarios que puedan usar dichas impresora

8\. **Panel de Control** --> **Hardware y Sonido** --> **Dispositivos e Impresoras** --> **Agregar dispositivos**

9\. Nos pedirá instalar los controladores y una ve todo este bien agregado y configurado podremos imprimir una página de prueba



### **CAPITULO 8 - INSTALACION DE UBUNTU \[TEMA 6]**



Distribuciones que existen de Linux

Que es software libre

Ventajas y Desventajas

Que es Ubuntu

Cuando se actualiza

Que es una versión LTS

Proceso de instalación

Que es una partición

Que es un sistema transaccional

La cuenta root y como funciona

Que es try or install Ubuntu | Ubuntu (safe grafics) | Test Memory

Configuración de fecha y hora

Cambiar el nombre del equipo

Configuración de IP



# **CAPITULO 12 - INSTALAR Y CONFIGURAR OpenLDAP en Ubuntu \[TEMA 7 Y TEMA 8]**



##### **LDAP**



**LDAP --> Es el protocolo que usa Active Directory para funcionar, por lo que este protocolo que ofrece el acceso a un servicio de directorio de entorno de red.**



**Usuario --> Ordenador --> PAM --> LDAP -->NNS --> /etc/passwd /etc/shadow /etc/group**



**NSS --> Name Service Switch**



**PAM --> Interfaz entre los programas de usuarios y distintos métodos de autentificación, gestiona procesos de autentificación**



**OpenLDAP --> Herramienta de Ubuntu para usar LDAP**



**Atributo --> Cualidad o Característica**



En base a la clase de objeto tiene asociados unos atributos u otros



##### **ESTRUCUTRA**



uid --> Identificador del usuario

objectClass --> Indica el tipo de objeto al que pertenece la entrada

cn --> Nombre de la persona

givenname --> Nombre de pila

sn --> Apellido de la persona

o --> Entidad a la que pertenece la persona

u --> El departamento en el que trabaja la persona

mail --> Dirección de correo electrónico de la persona



##### **INSTALACION DE OPENLDAP**



Agregamos las IP al servidor

Actualizamos el servidor e instalamos slapd



##### **LDIF**



**LDIF -->** Son unos ficheros en lo que podemos añadir la información, lo primero que se tiene que poner es la ruta | Se crean para escribir dentro la información de los objetos, se especifican los atributos de esos objetos, ruta, nombre, apellidos...



**Ejemplo -->** dn: cn=grupo,ou=unidad,dc=somebooks,dc=local

 	    objectClass: top

 	    objectClass: posixGroup

 	    gidNumber: 10000 (**grupos** empiezan por 10.000 \[Todos los **usuarios** automáticos empezarían a partir de 1000])

 	    cn: grupo



Una vez creado el documento y modificado para añadirlos al LDAP usamos el comando **ldapadd** para añadirlos y para luego comprobarlo y confirmarlo podemos usar el comando **slapcat**.



Para añadir más contenido crearemos otro .ldif donde pondremos nuestras sentencias nuevas



##### **TIPOS DE OBJETOS PARA LOS DIFERENTES TIPOS DE OBJETOS**

##### 

organizationalUnit | posixGroup | person | top | inetOrgPerson | posixAccount



**Para usuarios / personas** --> top | posixAccount | inetOrgPerson | person

**Para grupos** --> top | posixGroup



##### **ESTRUCTURA**



dn: cn=grupo,ou=unidad,dc=somebooks,dc=local

objectClass: top

objectclass: posixGroup

gidNumber: 10000

cn: grupo



dn: uid=jlopez, ou=medio, dc=somebooks, dc=es

objectClass: person

cn: Juan Lopez

givenname: Juan

sn: Lopez

o: somebooks

u: medio

mail: juanlopez@somebooks.es



##### **COMANDOS**



ldapadd --> Añadir los registros del archivo .ldif dentro de nuestro ldap (Directorio Activo) \[sudo ldapadd -x -D cn=admin,dc=somebooks,dc=local -W -f ou.ldif]

ldapsearch --> Buscar registro dentro de nuestro directorio LDAP

ldapmodify --> Permite cambiar el contenido de cualquier atribut, añadir nuevos atributos, modificarlos, eliminarlos....

ldapdelete --> Permite eliminar entradas del directorio

slapcat --> Muestra el contenido de nuestro LDAP

