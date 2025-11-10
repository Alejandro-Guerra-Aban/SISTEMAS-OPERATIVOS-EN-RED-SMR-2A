# **TEMA 2 – Servicio de Directorio Activo**

### 📘 ¿Qué es un Directorio Activo?

El **Directorio Activo (Active Directory)** es un servicio de directorio desarrollado por **Microsoft** que permite administrar y organizar recursos en una red (usuarios, equipos, impresoras, etc.) de forma centralizada.

### 🌳 Conceptos clave

* **Bosque:** Conjunto de uno o varios dominios que comparten una estructura lógica común y una configuración de seguridad.
* **Dominio:** Unidad principal de organización dentro del Directorio Activo; agrupa usuarios, equipos y otros objetos bajo una misma política.

### 🧰 Herramientas del Directorio Activo

Algunas herramientas más utilizadas son:

* **Usuarios y equipos de Active Directory**
* **Dominios y confianzas de Active Directory**
* **Sitios y servicios de Active Directory**
* **Centro de administración de Active Directory**

### 🔗 Relaciones de confianza

Las **relaciones de confianza** permiten que los usuarios de un dominio puedan acceder a recursos de otro dominio o bosque.

> 💡 Si existen **dos bosques distintos**, es necesario **crear una relación de confianza** entre ellos para compartir recursos.

### ⚙️ Consola personalizada

Puedes **crear una consola MMC personalizada** que incluya las herramientas más utilizadas del Directorio Activo para facilitar la administración diaria.

---

# **TEMA 3 – Cuentas de Usuario**

### 👤 Usuarios, Equipos y Grupos

En el Directorio Activo, los **usuarios** representan personas, los **equipos** representan dispositivos y los **grupos** permiten gestionar permisos de forma colectiva.

### 🌐 Ámbitos de grupos

* **Local:** Solo tiene efecto dentro del dominio o equipo donde se crea.
* **Global:** Permite agregar miembros de un mismo dominio y asignar permisos en cualquier dominio del bosque.

### ➕ Creación de usuarios

**¿Cómo se crea un usuario?**
Se puede crear desde la consola **Usuarios y equipos de Active Directory**, seleccionando la unidad organizativa y eligiendo **Nuevo → Usuario**.

### 🏢 Unidades Organizativas (UO)

* Una **Unidad Organizativa (UO)** es un contenedor que permite organizar objetos del Directorio Activo.
* **¿Cómo se crea una UO?**
  Desde la misma consola: **Clic derecho → Nuevo → Unidad organizativa**.

---

# **TEMA 4 – Copias de Seguridad y Monitorización**

### 💾 Copias de Seguridad

Tipos principales:

* **Completa:** Copia todos los archivos seleccionados.
* **Incremental:** Copia solo los archivos modificados desde la última copia.
* **Diferencial:** Copia los archivos modificados desde la última copia completa.

#### 🧱 Operaciones básicas

* **¿Cómo hacer una copia de seguridad?**
  Usar la herramienta **Copia de seguridad de Windows Server** o software especializado.
* **Recuperar una copia de seguridad**
  Selecciona el punto de restauración y los elementos a recuperar.
* **Programar una copia de seguridad**
  Configura la tarea en el **Programador de tareas** para realizar copias automáticas.

### ⏰ Programador de Tareas

* **¿Qué es?**
  Permite **automatizar procesos** en el sistema operativo.
* **¿Cómo se crea una tarea programada?**
  Abre el **Programador de tareas → Crear tarea → Configura los disparadores y acciones**.

### 🧩 Visor de Eventos

* **¿Qué es?**
  Herramienta que muestra los **registros del sistema**, advertencias y errores.
* **¿Qué podemos ver?**
  Eventos de **seguridad, sistema, aplicaciones** y **servicios**.

### 📈 Monitorización

* **Monitor de rendimiento:** Permite analizar el uso de recursos (CPU, memoria, disco, red).
* **Monitor de recursos:** Muestra información en tiempo real sobre los procesos y el rendimiento del sistema.

---

## ⚖️ Licencia

Este curso usa la licencia [**CC-BY-NC-ND**](https://github.com/Alejandro-Guerra-Aban/SMR-2A-SEGURIDAD-INFORMATICA/blob/main/LICENSE), que permite:

* ✅ Compartir el material
* ✅ Usar el contenido para fines personales
* ❌ Uso comercial prohibido
* ❌ Modificación del material prohibida
* ⚠️ Requiere atribución al autor

---

## 👨‍💻 Autor

[**@Alejandro Guerra Abán**](https://www.github.com/Alejandro-Guerra-Aban)

---

⭐ **¡Gracias por visitar el repositorio!**
