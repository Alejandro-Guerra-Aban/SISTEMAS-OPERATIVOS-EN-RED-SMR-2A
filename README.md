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
