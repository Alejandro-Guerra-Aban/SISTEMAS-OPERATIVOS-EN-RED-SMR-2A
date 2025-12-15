# 🖥️ **Administración de Windows Server — Apuntes Completos**

Este documento recopila los contenidos esenciales relacionados con **Active Directory**, **cuentas de usuario**, **grupos**, **copias de seguridad**, **monitorización** y más.

Incluye explicaciones claras, secciones prácticas y un examen final por tema para que puedas evaluarte.

---

# 📘 **TEMA 2 — Servicio de Directorio Activo**

## 🏢 **¿Qué es Active Directory?**

Active Directory (AD) es un **servicio de directorio** de Microsoft que organiza y administra usuarios, equipos, grupos, permisos y recursos en redes basadas en Windows Server.

> [!NOTE]
> 
> AD funciona como una base de datos distribuida que permite el control centralizado de la red.

---

## 🌳 **Estructuras principales de Active Directory**

### 🔹 **Bosque**

El **bosque (forest)** es la estructura de mayor rango en Active Directory.
Contiene uno o varios dominios que comparten:

* Esquema
* Catálogo global
* Relaciones de confianza implícitas

### 🔹 **Dominio**

Un **dominio** es una unidad lógica dentro del bosque en la que se gestionan:

* Usuarios
* Equipos
* Políticas
* Recursos

### 🔹 **Sitio**

Un **sitio** representa la **estructura física** de la red, generalmente asociada a una ubicación geográfica.

### 🔹 **Estructura**

La **estructura de AD** incluye bosques, árboles, dominios y unidades organizativas, todas ellas organizadas jerárquicamente.

### 🔹 **Unidad Organizativa (OU)**

Una OU es un contenedor donde se guardan objetos de AD como:

* Usuarios
* Grupos
* Equipos

Permite aplicar **GPOs** y delegar administración.

> [!TIP]
> 
> Usa OUs para separar departamentos, sedes o áreas administrativas.

---

## ⚙️ **Instalación y Gestión del Dominio**

### 🛠️ **Cómo instalar un dominio**

1. Instalar el rol **Servicios de dominio de Active Directory (AD DS)**.
2. Configurar IP estática.
3. Preparar nombre del servidor.
4. Ejecutar el asistente de configuración (Promocionar).

### 🚀 **Promocionar un dominio**

Convertir un servidor en **Controlador de Dominio (DC)**.

Pasos principales:

* Crear un nuevo bosque o añadir un dominio.
* Configurar contraseña de modo seguro.
* Reiniciar y validar.

### 🧹 **Degradar un dominio**

Proceso inverso:

* Retirar el rol AD DS.
* Eliminar metadatos del dominio si es necesario.

---

## 🧰 **Herramientas del Administrador**

Incluye herramientas esenciales como:

* **Copias de seguridad de Windows Server**
* **Sitios y servicios de Active Directory**
* **Usuarios y equipos de Active Directory**
* **Monitor de rendimiento**
* **Monitor de recursos**
* **Visor de eventos**

> [!IMPORTANT]
> 
> Estas herramientas permiten diagnosticar, analizar, gestionar y restaurar el entorno de AD.

---

## 🔐 **Relaciones de confianza**

Permiten que un dominio **confíe** en otro para compartir recursos.

Tipos:

* Unidireccional
* Bidireccional
* Transitivas
* No transitivas

### 🔗 **Relaciones entre bosques**

Cuando dos bosques requieren comunicarse, se debe crear una relación de confianza **forest trust**.

---

## 📝 **Consola personalizada**

Puedes crear una **MMC** con las herramientas más usadas:

1. Ejecuta `mmc`
2. Agrega complementos
3. Guarda como consola personalizada

---

---

# 📗 **TEMA 3 — Cuentas de Usuario, Equipos y Grupos**

## 👥 **Cuentas de usuario**

Son objetos que permiten a una persona autenticarse en el dominio.

Tipos:

* Administrador
* Invitado
* Usuarios estándar

### 👤 **Cuentas integradas**

* **Administrator**
* **Guest (invitado)** — deshabilitada por seguridad

---

## 🖥️ **Cuentas de equipo**

Cada equipo unido al dominio tiene una cuenta que permite su autenticación en el controlador de dominio.

---

## 👨‍👩‍👧‍👦 **Grupos en Active Directory**

### 🔸 **Grupos de distribución**

Usados para correo electrónico.
No tienen permisos de acceso.

### 🔸 **Grupos de seguridad**

Usados para asignar permisos en el dominio.

---

## 🌐 **Ámbitos de grupo**

* **Local de dominio**: Recursos dentro del dominio.
* **Global**: Usuarios dentro del mismo dominio.
* **Universal**: Usuarios y grupos de múltiples dominios.

> [!TIP]
> 
> Regla AGDLP: **Cuentas → Grupos Globales → Grupos Locales → Permisos**

---

## 💼 **Perfiles de usuario**

* **Perfil obligatorio**
* **Perfil temporal**
* **Perfil super-obligatorio**
* **Perfil móvil** (roaming profile)

### 📂 **¿Qué es un perfil móvil?**

Un perfil que se almacena en un recurso compartido y sigue al usuario en cualquier equipo del dominio.

---

## 🏗️ **Crear objetos en Active Directory**

### Crear un usuario

1. Abrir *Usuarios y equipos de Active Directory*
2. Seleccionar OU
3. Clic derecho → Nuevo → Usuario

### Crear una OU

1. Clic derecho en el dominio
2. Nuevo → Unidad organizativa

---

---

# 📙 **TEMA 4 — Copias de Seguridad y Monitorización**

## 🔐 **Tipos de copias**

* **Completa**
* **Incremental**
* **Individual (selectiva)**

> [!IMPORTANT]
> 
> La copia completa es la única que marca archivos como respaldados.

---

## 💾 **¿Por qué se hacen copias de seguridad?**

Para proteger los datos ante:

* Fallos del sistema
* Corrupción
* Eliminación accidental
* Ataques de malware

---

## ➕ **Agregar un disco al servidor**

1. Panel de control → Administración de discos
2. Inicializar disco
3. Crear volumen
4. Formatear

---

## 📀 **Hacer una copia de seguridad**

1. Abrir *Copia de seguridad de Windows Server*
2. Acción → Nueva copia
3. Seleccionar tipo y destino

### 🔄 **Recuperar una copia**

Usando el asistente de recuperación.

### ⏰ **Programar una copia**

Se hace desde el planificador de copias del sistema o desde **Programador de tareas**.

---

## ⏳ **Programador de tareas**

Permite ejecutar tareas automáticamente en un horario especificado.

* Tareas básicas
* Tareas avanzadas

---

## 📊 **Visor de eventos**

Permite ver registros del sistema:

* Errores
* Advertencias
* Eventos informativos
* Eventos de seguridad

### Monitor de rendimiento

Analiza el rendimiento del sistema mediante contadores.

### Monitor de recursos

Visualiza CPU, RAM, disco y red en tiempo real.

### Eventos reenviados

Permite recibir eventos de otros equipos mediante suscripciones.

---

---

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

---

---

# 📝 **EXAMEN FINAL — TEMA 2**

1. Define "bosque" en Active Directory.
2. ¿Para qué sirven las Unidades Organizativas?
3. Explica qué son las relaciones de confianza.
4. ¿Qué herramientas se utilizan para administrar AD?
5. ¿Qué ocurre al promocionar un servidor?
6. ¿Cuál es la diferencia entre un sitio y un dominio?

---

# 📝 **EXAMEN FINAL — TEMA 3**

1. ¿Qué diferencia hay entre un grupo de seguridad y uno de distribución?
2. Define los tres ámbitos de grupo.
3. Explica qué es un perfil móvil.
4. ¿Cómo se crea un usuario en AD?
5. ¿Qué es una cuenta de equipo?
6. ¿Qué significa que un usuario sea miembro de un grupo?

---

# 📝 **EXAMEN FINAL — TEMA 4**

1. Explica los tres tipos de copia de seguridad.
2. ¿Por qué es importante programar copias?
3. ¿Qué información se puede ver en el visor de eventos?
4. ¿Qué es el monitor de rendimiento?
5. ¿Cómo se agrega un disco al servidor?
6. Explica el uso del programador de tareas.

---

# 📝 **EXAMEN TIPO TEST — TEMA 2 (Active Directory)**

### **1. ¿Qué es un bosque en Active Directory?**

**A.** `Un grupo de unidades organizativas`
**B.** `Una agrupación lógica de sitios`
**C.** `La estructura más alta que contiene uno o varios dominios`
**D.** `Un dominio principal con un nombre DNS`

---

### **2. ¿Qué es un dominio?**

**A.** `Un conjunto de sitios que comparten subred`
**B.** `Un conjunto de objetos que comparten base de datos y políticas`
**C.** `Un contenedor donde se almacenan perfiles móviles`
**D.** `Un nodo físico dentro de la red`

---

### **3. ¿Qué herramienta se utiliza para administrar usuarios y grupos?**

**A.** `Monitor de rendimiento`
**B.** `Sitios y servicios de Active Directory`
**C.** `Usuarios y equipos de Active Directory`
**D.** `Visor de eventos`

---

### **4. La promoción de un servidor a controlador de dominio implica…**

**A.** `Instalar el rol DHCP`
**B.** `Instalar AD DS y configurar un dominio`
**C.** `Cambiar de red física`
**D.** `Crear un sitio nuevo`

---

### **5. ¿Qué tipo de relación permite comunicación bidireccional entre dos bosques?**

**A.** `Trust unidireccional`
**B.** `Trust de ámbito local`
**C.** `Forest trust`
**D.** `Trust transitorio`

---

### **6. Una Unidad Organizativa sirve para…**

**A.** `Crear políticas de red física`
**B.** `Organizar objetos y delegar administración`
**C.** `Administrar registros DNS`
**D.** `Crear bosques automáticamente`

---

---

# 📝 **EXAMEN TIPO TEST — TEMA 3 (Usuarios, Equipos y Grupos)**

### **1. Un grupo de distribución se usa para…**

**A.** `Conceder permisos`
**B.** `Crear GPOs`
**C.** `Listas de correo`
**D.** `Controlar perfiles móviles`

---

### **2. ¿Qué ámbito de grupo permite incluir usuarios de cualquier dominio dentro del bosque?**

**A.** `Grupo local`
**B.** `Grupo global`
**C.** `Grupo universal`
**D.** `Grupo de distribución`

---

### **3. ¿Qué es un perfil móvil?**

**A.** `Un perfil temporal que se borra al cerrar sesión`
**B.** `Un perfil almacenado en el servidor que sigue al usuario`
**C.** `Un perfil que no se puede modificar`
**D.** `Un perfil que solo existe localmente`

---

### **4. ¿Qué cuenta es integrada en Windows Server?**

**A.** `Invitado`
**B.** `Técnico`
**C.** `Estándar`
**D.** `Usuario local del dominio`

---

### **5. Una cuenta de equipo sirve para…**

**A.** `Ejecutar programas sin permisos`
**B.** `Permitir que un PC se autentique en el dominio`
**C.** `Crear políticas del sistema`
**D.** `Conectar el equipo a Internet`

---

### **6. ¿Cómo se crea una OU?**

**A.** `Desde el Visor de Eventos`
**B.** `Desde Usuarios y equipos de Active Directory`
**C.** `Desde Servicios`
**D.** `Desde Panel de control`

---

---

# 📝 **EXAMEN TIPO TEST — TEMA 4 (Copias de Seguridad y Monitorización)**

### **1. ¿Qué tipo de copia marca todos los archivos como respaldados?**

**A.** `Incremental`
**B.** `Completa`
**C.** `Diferencial`
**D.** `Selectiva`

---

### **2. ¿Para qué sirve el programador de tareas?**

**A.** `Para restaurar el sistema`
**B.** `Para ejecutar acciones en momentos programados`
**C.** `Para administrar memoria RAM`
**D.** `Para gestionar DNS`

---

### **3. El Visor de eventos permite ver…**

**A.** `Sólo errores críticos`
**B.** `Eventos del sistema, seguridad y aplicaciones`
**C.** `El historial de copia de seguridad`
**D.** `Gráficas de rendimiento`

---

### **4. ¿Qué se usa para medir rendimiento mediante contadores?**

**A.** `Monitor de recursos`
**B.** `Monitor de rendimiento`
**C.** `Programador de tareas`
**D.** `Administrador de discos`

---

### **5. ¿Qué tipo de copia guarda solo los archivos cambiados desde la última copia completa?**

**A.** `Diferencial`
**B.** `Incremental`
**C.** `Individual`
**D.** `Clonada`

---

### **6. Para agregar un disco nuevo se debe…**

**A.** `Formatearlo sin inicializar`
**B.** `Inicializarlo en Administración de discos`
**C.** `Crear un dominio nuevo`
**D.** `Ejecutar tareas avanzadas`

---
