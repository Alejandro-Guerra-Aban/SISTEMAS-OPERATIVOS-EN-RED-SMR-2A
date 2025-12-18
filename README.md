# 🖥️ Administración de Windows Server y GNU/Linux — DASHBOARD DEFINITIVO ASIR/SMR

![Nivel](https://img.shields.io/badge/Nivel-ASIR/SMR-orange)
![Estado](https://img.shields.io/badge/Estado-Completo-brightgreen)
![License](https://img.shields.io/badge/Licencia-MIT-blue)

---

## 📌 ÍNDICE RÁPIDO (clickable)

<details>
<summary>Ver índice interactivo</summary>

* 🌳 [TEMA 2 — Active Directory](#tema-2---active-directory)
* 👥 [TEMA 3 — Usuarios, Grupos y Equipos](#tema-3---usuarios-grupos-y-equipos)
* 📊 [TEMA 4 — Copias y Monitorización](#tema-4---copias-y-monitorización)
* 🖥️ [TEMA 5 — Clientes del Dominio](#tema-5---clientes-del-dominio)
* 🐧 [TEMA 6 — Ubuntu](#tema-6---ubuntu)
* 🧬 [TEMA 7–8 — OpenLDAP](#tema-7–8---openldap)
* 💻 [Instalación Ubuntu Server](#instalación-ubuntu-server)
* 🛠️ [Prácticas Guiadas](#prácticas-guiadas)
* 📝 [Simulacro de Examen](#simulacro-de-examen)
* 💡 [Tips y Consejos de Examen](#tips-y-consejos-de-examen)

</details>

---

# 🌳 TEMA 2 — ACTIVE DIRECTORY

## 🧠 Conceptos Clave

```diff
+ AD: Servicio de directorio centralizado
+ Bosque (Forest): Nivel más alto
+ Dominio (Domain): Unidad lógica
+ OU (Organizational Unit): Organizar objetos + GPO
+ DC (Domain Controller): Controlador de dominio
+ Protocolos: LDAP, Kerberos, DNS
```

---

## 🌐 Estructura AD — Diagrama Interactivo

```ini
[BOSQUE]
   |
   |-- dominio.local
        |-- OU Usuarios
        |     |-- Usuario1
        |     |-- Usuario2
        |
        |-- OU Equipos
        |     |-- Equipo1
        |
        |-- Domain Controllers
```

---

## ⚙️ Instalación AD DS ✅

```diff
[✔] Configurar IP estática
[✔] Cambiar nombre del servidor
[✔] Instalar rol AD DS
[✔] Promocionar a Domain Controller
[✔] Configurar DNS y replicación
[✔] Verificar estado: dcdiag / repadmin / eventvwr
```

### ❌ Errores comunes

```diff
- No configurar IP fija
- Crear usuarios en contenedor Users
- Usar Administrator para todo
```

---

# 👥 TEMA 3 — USUARIOS, GRUPOS Y EQUIPOS

## Tipos de Grupo

```ini
[Distribución] → Correo
[Seguridad] → Permisos
```

**Ámbitos:**

* Global → Usuarios mismo dominio
* Local de dominio → Permisos locales
* Universal → Usuarios varios dominios

**Regla AGDLP**:

```ini
Accounts -> Global -> Domain Local -> Permissions
```

---

## 💼 Tipos de Perfiles

```diff
+ Obligatorio: no guarda cambios
+ Temporal: borrado al cerrar sesión
+ Móvil: sigue al usuario en cualquier PC
```

---

# 📊 TEMA 4 — COPIAS Y MONITORIZACIÓN

## Tipos de copia de seguridad

```ini
[Completa] → Todo el sistema (respaldo total)
[Incremental] → Cambios desde última copia
[Selectiva] → Archivos específicos
```

---

## Monitorización

```diff
+ Visor de eventos → errores y seguridad
+ Monitor de rendimiento → CPU, RAM, disco
+ Monitor de recursos → uso en tiempo real
```

---

# 🖥️ TEMA 5 — CLIENTES DEL DOMINIO

## 🔗 Unión al dominio Windows

```diff
[✔] Usuario creado en AD
[✔] Configurar IP y DNS
[✔] Cambiar nombre del equipo
[✔] Unir al dominio con credenciales
[✔] Reiniciar y iniciar sesión usuario dominio
```

## 🔐 Permisos, Derechos y Privilegios

```ini
Permiso    → Acceso a recursos
Derecho    → Inicio de sesión
Privilegio → Acciones especiales
```

---

# 🐧 TEMA 6 — UBUNTU

## Conceptos Clave

```diff
+ Linux: software libre
+ Ubuntu: Debian-based
+ LTS: soporte 5 años
+ Root → sudo
```

---

## ⚙️ Instalación Ubuntu Server

```diff
[✔] Descargar ISO oficial LTS
[✔] Crear USB booteable
[✔] Arrancar desde USB
[✔] Seleccionar idioma, teclado, zona horaria
[✔] Configurar red: IP, DNS, hostname
[✔] Crear usuario principal
[✔] Elegir disco y particiones: /, swap, /home
[✔] Instalar software adicional
[✔] Finalizar y reiniciar
```

---

# 🧬 TEMA 7–8 — OPENLDAP

## Objetos LDAP

```ldif
dn: uid=jlopez,ou=usuarios,dc=empresa,dc=local
objectClass: posixAccount
objectClass: inetOrgPerson
uid: jlopez
cn: Juan Lopez
sn: Lopez
mail: juan@empresa.local
```

## Comandos LDAP

```bash
ldapadd -x -D "cn=admin,dc=empresa,dc=local" -W -f archivo.ldif
ldapsearch -x -LLL -b "dc=empresa,dc=local"
ldapmodify -x -D "cn=admin,dc=empresa,dc=local" -W -f cambios.ldif
ldapdelete -x -D "cn=admin,dc=empresa,dc=local" -W "uid=jlopez,ou=usuarios,dc=empresa,dc=local"
slapcat
systemctl status slapd
```

---

# 🏋️‍♂️ PRÁCTICAS GUIADAS

<details>
<summary>Práctica 1: Bosque y Dominio AD</summary>

```diff
[✔] Instalar Windows Server
[✔] Configurar IP fija
[✔] Instalar AD DS
[✔] Promocionar a DC
[✔] Crear OU Usuarios y Equipos
[✔] Crear usuarios y grupos siguiendo AGDLP
[✔] Aplicar políticas básicas
```

</details>

<details>
<summary>Práctica 2: Ubuntu + OpenLDAP</summary>

```diff
[✔] Instalar Ubuntu Server LTS
[✔] Configurar red y hostname
[✔] Instalar OpenLDAP (sudo apt install slapd ldap-utils)
[✔] Configurar dominio LDAP
[✔] Crear usuarios con LDIF
[✔] Verificar con ldapsearch
```

</details>

---

# 📝 SIMULACRO DE EXAMEN

<details>
<summary>Parte A — Test (12 preguntas)</summary>

```ini
1. AD → B
2. Estructura AD → D
3. OU → B
4. Protocolo AD → C
5. Grupo → C
6. Ámbito → C
7. Copia → C
8. Herramienta → C
9. Unir al dominio → B
10. Permiso/Privilegio → D
11. Ubuntu → C
12. LDAP → B
```

</details>

<details>
<summary>Parte B — Desarrollo</summary>

```ini
1️⃣ Bosque/Dominio/OU
- Bosque: nivel más alto
- Dominio: unidad lógica
- OU: contenedor + GPO

2️⃣ Unión cliente Windows
- Crear usuario
- Configurar IP/DNS
- Cambiar nombre equipo
- Unir al dominio + credenciales
- Reiniciar + iniciar sesión

3️⃣ Tipos de copia
- Completa: todo
- Incremental: cambios desde última
- Selectiva: selección manual

4️⃣ OpenLDAP
- Implementación libre LDAP
- Gestión centralizada usuarios/grupos
```

</details>

---

# 💡 Tips y Consejos

```diff
+ Memoriza definiciones y diagramas
+ Practica AGDLP y perfiles
+ Privilegio > Permiso > Derecho
+ Domina todos los comandos
+ Realiza simulacros completos
+ Evita errores comunes: IP dinámica en DC, usar Administrator sin control
```

---

# 📄 LICENCIA

MIT — Uso educativo libre
