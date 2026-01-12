# **TEMA 9 - Administración Linux Server**



### **9.1 Monitorización**



En la imagen se puede ver el esquema de un protocolo típico de reacción ante incidentes:



###### **1. Detección:**



En un primer momento, los esfuerzos se centrarán en detectar con precisión qué es lo que ha sucedido.



###### **2. Resolución:**



Lógicamente, cuando se ha identificado el problema, el siguiente paso será resolverlo. Este proceso se divide en tres fases:



\- Diagnóstico: Se buscará establecer los motivos del problema y la estrategia para solucionarlo.



\- Reparación: Se realizan las operaciones necesarias para garantizar que todo vuelve a la normalidad.



\- Recuperación: Se restaura el sistema al estado en el que estaba antes de que ocurriera el incidente. Esta etapa suele implicar la recuperación de copias de seguridad de los datos.



###### **3. Sistema activo:**

En esta fase, el sistema realiza sus funciones con normalidad.



Como puede suponerse, los esfuerzos de un administrador de sistemas deben centrarse en dos aspectos principales:



• Establecer las estrategias necesarias para que el sistema esté inactivo el menor tiempo posible, acortando al máximo los tiempos de detección y resolución de incidentes.



• Tratar de prolongar el tiempo en el que el sistema se encuentra activo. Para lograrlo, deberán conocer lo que ocurre en el sistema e identificar situaciones que puedan originar problemas, antes de que éstos se manifiesten.



###### **9.2 Programas o herramientas de monitorización**



Los programas de monitorización permiten observar el funcionamiento del sistema en tiempo real, detectar problemas de rendimiento y entender cómo se usan los recursos.



El primer paso para administrar un servidor Linux es comprender cómo funciona el sistema, qué usuarios existen, cuáles son sus permisos y cómo se gestionan los servicios y demonios que proporcionan funcionalidades al servidor.



• **id** → muestra el UID, GID y grupos a los que pertenece un usuario.

• **whoami** → indica el nombre del usuario actual.

• **groups** → lista todos los grupos del usuario.

• **chmod** → cambia los permisos de un archivo o carpeta.

• **chown** → cambia el propietario del archivo.

• **chgrp** → cambia el grupo propietario.



Los **demonios** son programas que se ejecutan en segundo plano y ofrecen servicios como SSH, web o bases de datos. En los servidores modernos se gestionan mediante **systemd**, que se encargará de poner en marcha los diferentes componentes que deben cargarse después del núcleo y controlar su funcionamiento mientras el sistema esté en marcha. Para controlar los servicios administrados por Systemd, disponemos del comando **systemctl**.



Algunos comandos fundamentales para gestionar servicios son:



• **systemctl status servicio** → permite comprobar si un servicio está activo.

• **systemctl start/stop/restart servicio** → iniciar, parar o reiniciar un servicio.

• **systemctl enable/disable servicio** → habilitar o deshabilitar el inicio automático de un servicio al arrancar el sistema.

• **systemctl list-units --type=servicio** → servicios activos y su estado.

• **systemctl status servicio** → estado detallado de un servicio.



Los logs son registros que almacenan la actividad del sistema, los servicios y los errores que se producen. En servidores modernos se gestionan con **systemd**, mediante el **journal**:



• **journalctl** → consulta el registro completo.

• **journalctl -f** → sigue los logs en tiempo real, útil para depurar problemas.

• **journalctl -k** → muestra solo los mensajes del kernel.

• **journalctl -u servicio** → filtra los logs de un servicio concreto.



En ocasiones, observamos que nuestro ordenador no rinde como esperamos. En estos casos, será muy interesante conocer diferentes aspectos que pueden influir en su productividad, como la cantidad de memoria usada o el porcentaje de tiempo que está trabajando el procesador.



También nos interesará saber si se está ejecutando algún proceso que consuma una cantidad excesiva de memoria o que ocupe el procesador más tiempo del razonable. Incluso podemos estar interesados en conocer la cuenta de usuario desde la que se está ejecutando dicho proceso.



Algunas de las herramientas que se pueden usar son:



1. **top**: ofrece información sobre el grado de ocupación de la CPU, de la memoria RAM, de la memoria de intercambio (swap) y los procesos que se están ejecutando. (top)



 	Para salir pulsamos q. Para finalizar la ejecución de cualquier proceso pulsando 	la tecla k y escribiendo el PID del proceso. Para ver información solo sobre un 	usuario: u y el nombre del usuario (o directamente top -u usuario)



2\. **htop**: es más flexible y fácil de usar, ya que podemos interactuar con él por medio del ratón (htop → sudo apt install htop).



Tiene una cabecera con el uso del procesador, memoria ram, memoria de intercambio, nº tareas en ejecución y tiempo de uso. El cuerpo donde viene la lista de procesos ordenada en función del porcentaje de uso del procesador. Y el pie con el menú de acciones de htop.



3\. **IOTOP**:  muestra la actividad de lectura/escritura de discos. Un proceso con %IO alto puede ralentizar el sistema. Es útil para detectar cuellos de botella en disco. (iotop → sudo apt install iotop)



4\. **vmstat 2 5**: estadísticas de memoria, CPU y procesos cada 2 segundos, 5 veces.  Su uso típico es ver problemas de CPU o disco a nivel global, no por proceso individual.



###### **9.3 Gestión y rendimiento del almacenamiento**



Uno de los problemas más inmediatos para un administrador de red, con muchos usuarios, es el uso racional del almacenamiento.



Sin límites, los usuarios tienden a almacenar mucha información, a menudo no relacionada con su trabajo. Esto desborda la previsión de necesidades de la red, especialmente cuando se usa almacenamiento centralizado.



Por otra parte, un usuario malintencionado podría impedir el uso normal del sistema informático simplemente saturando la capacidad de su almacenamiento de red.



En este contexto, cualquier administrador tendrá dos inquietudes: poder consultar el espacio ocupado por los usuarios de forma individual y poder establecer límites a la capacidad máxima de almacenamiento que puedan utilizar los usuarios.



Las cuotas se establecen para cada volumen (que habitualmente se corresponde con una partición) de forma independiente, y pueden fijarse tanto para usuarios individuales como para grupos.



El propietario y el grupo al que éste pertenece, se almacenan en los metadatos de cada archivo del sistema, lo que hace que dicha información sea fácilmente accesible para el sistema de cuotas.



Además, existen dos enfoques diferentes en el momento de establecer cuotas:



• Limitar el número de bloques de disco, con lo que se restringe el tamaño máximo que se puede ocupar.



• Limitar el número de i-nodos, que restringe el número máximo de archivos que pueden crearse. Un i-nodo guarda las características de un objeto del sistema de archivos (un archivo, un directorio, etc,). Por lo tanto, limitando su número limitamos la cantidad máxima de objetos.



Además, cuando un administrador establece cuotas, puede fijar dos tipos de límites:



• Rígido (hard): El sistema operativo impedirá que el límite sea sobrepasado.

• Flexible (soft): El sistema operativo avisará cuando el límite sea sobrepasado.



Los pasos que deberemos seguir para hacer uso de las cuotas de disco son:



• Instalar los paquetes necesarios.

• Activar las cuotas en el sistema de archivos y volver a montarlo.

• Crear los archivos de cuota y la tabla de uso de espacio compartido.

• Configurar cuotas para usuarios y grupos.

• Establecer un valor para el periodo de gracia.



Herramientas interesantes que se pueden emplear:



**1. Espacio y uso de disco**



• df -h → muestra el espacio usado y disponible en cada disco.

• du -sh /ruta → calcula el tamaño de carpetas específicas.



**2. Rendimiento de discos**

 

• iostat -x 1 5 → proporciona información detallada sobre la actividad de los discos, IOPS y utilización.



• vmstat 1 5 → muestra estadísticas de CPU, memoria y swap en intervalos de tiempo.



**3. Estado de discos y detección de fallos**



• dmesg | grep -i error → permite detectar errores de hardware o fallos de dispositivos.



###### **9.4 Mantenimiento y actualización del software**



Realizar tareas de mantenimiento asegura que el sistema funcione correctamente y esté protegido frente a vulnerabilidades.



**Tareas básicas en Ubuntu:**



• Actualizar la lista de paquetes: sudo apt update

• Actualizar paquetes instalados: sudo apt upgrade

• Eliminar paquetes innecesarios: sudo apt autoremove

• Limpiar archivos temporales: sudo apt clean sudo apt autoclean

• Listar paquetes instalados: dpkg -l



###### **9.5 Automatización de tareas**



Es muy habitual que ciertas tareas administrativas, como la exportación de datos, copias de seguridad, instalación de actualizaciones, sincronizar el reloj del sistema con un servidor de tiempo, etc., se vayan repitiendo a lo largo del tiempo con una determinada frecuencia.



Muchas veces, habremos conseguido automatizarlas a través de un script y otras consistirá, simplemente, en ejecutar un programa particular con unos argumentos específicos. En cualquier caso, para el administrador será de gran ayuda poder iniciar la ejecución de esos programas o scripts de forma automatizada sin tener que estar pendiente de hacerlo a mano en el momento oportuno. Pues bien, en eso consisten las tareas programadas.



Linux ofrece dos servicios (cron y anacron) y dos comandos (crontab y at) para ejecutar tareas en momentos específicos.



###### **9.5.1 Ejecutar tareas a intervalos regulares (cron)**



El servicio cron ejecuta tareas a intervalos regulares. Está compuesto por el demonio crond y tablas que definen los trabajos y su frecuencia. Normalmente, crond se inicia con el sistema y se activa cada minuto para revisar las tablas y comprobar si hay acciones pendientes de ejecutar.



Tanto el administrador como los propios usuarios gestionan las tablas con los trabajos pendientes mediante el comando crontab.



Básicamente, la idea es que cada línea en el archivo de crontab tiene seis datos:



• Minuto: Un valor entero entre 0 y 59.

• Hora: Un valor entero entre 0 y 23.

• Día del mes: Un valor entero entre 1 y 31.

• Mes del año: Un valor entero entre 1 y 12.



• Día de la semana: Se puede expresar de dos formas:



 	o Como un valor entero entre 0 y 7, donde 0 ó 7 = domingo, 1 = lunes, 2 = martes, 	etc.

 	o Como un texto con los valores sun, mon, tue, wed, thu, fri y sat.



• Orden que será ejecutada por la Shell. crontab no analiza su contenido, sólo envía a la Shell cualquier cosa que haya después del día de la semana y hasta el final de la línea.



Los primeros cinco datos pueden expresarse como valores individuales, como rangos de valores (expresados como dos valores separados por un guión), como una lista de valores individuales o rangos (separados por comas) o con un asterisco (\*) que representa todos los valores posibles para ese dato.



**Ejemplos sencillos:**



• Escribir en un fichero Hola Mundo cada minuto de cada hora de cada mes.



 	\* \* \* \* \* echo "Hola mundo" >> /home/usuario/prueba\_cron.txt



• Hacer un backup a las 2:00 de todos los días de todos los meses.



 	0 2 \* \* \* /home/usuario/backup.sh



• Apagado automático de lunes a viernes a las 15:30:



 	30 15 \* \* 1-5 /sbin/poweroff



**Comandos útiles:**



• sudo apt update \&\& sudo apt install cron → Instalar cron

• crontab -l → consultar que tareas hay programas

• crontab -e → edita el crontab

• sudo crontab -u usuario -e → para asignar la tarea al usuario

• sudo crontab -u usuario -l → consultar las tareas de cualquier usuario

• sudo crontab -u usuario -r → eliminar tareas del usuario



• sudo nano /etc/cron.allow → escribir los nombres de aquellos usuarios que puedan crear tareas programadas. también se puede escribir directamente como:



 	sudo echo usuario >> /etc/cron.allow



• sudo nano /etc/cron.deny → escribir los nombres de aquellos usuarios que NO puedan crear tareas programadas



Por defecto en Ubuntu, todos los usuarios pueden crear tareas programadas a excepción de que se rellenen cron.allow o cron.deny y diga lo contrario.



Las tareas programadas por los usuarios se guardan en /var/spool/cron/crontabs/ y solo se puede acceder a la ruta con privilegios administrativos. Para acceder a las tareas generales del sistema también se necesitan priviledios administrativos y se puede consultar el archivo en /etc/crontabs.



Llegados a este punto, es importante hacer tres observaciones:



1\. Se recomienda incluir siempre la ruta completa de los comandos o scripts que incluyamos dentro de una tarea programada. Si no lo hacemos, probablemente el comando se ejecute correctamente, pero dependemos de que su ruta sea encontrada dentro de la variable $PATH y de que ésta haya sido correctamente definida en el momento de ejecutar la tarea programada.



2\. La tarea programada se ejecutará con los privilegios de la cuenta en la que se ha creado. Si no hubiésemos utilizado el comando sudo, cuando llegara el momento de ejecutar la tarea, lo haría como si el usuario hubiese escrito la orden en ese preciso momento.



3\. Si el ordenador está apagado cuando se cumple un plazo, la tarea no queda aplazada para cuando el equipo esté disponible. En otras palabras, la tarea correspondiente al plazo que se haya perdido no se recuperará.



###### **9.5.2 Como gestiona el sistema las tareas programadas**



El algoritmo concreto usado por cron en cada sistema puede variar ligeramente, pero en general, el mecanismo es el siguiente:



1\. Durante el proceso de arranque del sistema, se busca en el directorio /var/spool/cron/crontabs los archivos con las tareas programadas de cada cuenta de usuario.



2\. Para cada archivo encontrado, se establece el momento en el que habrá que ejecutar cada una de sus tareas y se sitúan en una lista ordenada por tiempo.



3\. Se inicia un proceso repetitivo donde:



a) Se analiza la primera tarea de la lista anterior y se averigua si es el momento de ejecutarla.



b) En caso afirmativo, la ejecuta en segundo plano usando los privilegios de su cuenta propietaria. Después, se establece el siguiente momento de ejecución de la tarea y se sitúa en la posición adecuada de la lista. Cuando termine, se vuelve al paso a).



c) El demonio se suspende hasta el siguiente minuto (normalmente usando la función sleep). Por este motivo no se discriminan periodos de tiempo inferiores a 1 minuto.



d) Al despertar, comprueba si se han producido cambios en la programación de tareas. Si es necesario se rehace la lista de tareas.



###### **9.5.2 Ejecutar tareas asíncronas**



El servicio cron es útil para servidores y equipos que funcionan continuamente. Sin embargo, en equipos que se apagan intermitentemente (escritorio, portátiles), cron puede ser ineficaz porque, si el equipo está apagado al vencer un plazo, la tarea no se recuperará.



En estos casos, puede resultar muy útil el servicio anacron (el nombre proviene del inglés anachronistic cron). A diferencia de cron, si programamos una tarea para una hora en particular y, en ese momento, el ordenador está apagado, la tarea se retomará en cuanto sea posible. Esto nos permitirá atender tareas críticas que no puedan dejar de atenderse.



A diferencia de cron, anacron es ejecutado por los scripts de inicio del sistema o por alguna tarea programada y, cuando acaba su trabajo, deja de ejecutarse. Durante su funcionamiento comprueba si ha vencido el plazo de alguna tarea prevista.



Como veremos más adelante, anacron también atiende las tareas asignadas a cron con un periodo diario (daily), semanal (weekly) o mensual (monthly). Sin embargo, no atiende trabajos que cron deba atender cada hora (hourly).



Para llevar a cabo su trabajo, anacron mantiene archivos con marcas de tiempo en la carpeta /var/spool/anacron, que le permiten saber en qué momento se han ejecutado por última vez las tareas



En cuanto a las tareas que deben ejecutarse, se encuentran definidas en el archivo /etc/anacrontab. Cada vez que se ejecuta, anacron recorre la lista y, para cada tarea, comprueba si ha pasado el número adecuado de días desde su última ejecución. Si es necesario, la ejecuta.



Lo primero que se ve dentro de anacrontab (sudo nano /etc/anacrontab) son tres variables de entorno con algunos valores predeterminados:



• SHELL: El intérprete de comandos que se usará para la ejecución de las tareas.

• HOME: La ruta que actuará como directorio predeterminado.

• LOGNAME: El nombre de la cuenta de usuario bajo la que se ejecutarán las tareas.



Debajo, cada línea definirá una tarea diferente e incluirá los siguientes valores:



• El periodo de ejecución. Indica la frecuencia con la que debe ejecutarse la tarea. Puede contener parámetros como @daily, @weekly o @monthly o valores numéricos, como 1 (diario), 7 (semanal) o un número diferente, para otros periodos.



• Un retraso en minutos. Indica el número de minutos que debe esperar el sistema para ejecutar la tarea después de ejecutar anacron. Su objetivo es evitar una avalancha de tareas ejecutándose a la vez cuando arrancamos el sistema.



• El nombre de la tarea. Puede ser cualquier conjunto de caracteres, excepto la barra (/), pero debe ser único, porque será el nombre que utilice anacron para crear el archivo en /var/spool/anacron, donde guarda la fecha de la última vez que la ha ejecutado.



• La tarea a realizar.



##### **9.6 Copias de seguridad**



Una copia de seguridad (backup) es una copia de los datos importantes de un sistema que se guarda en otro lugar, para poder recuperarlos en caso de pérdida.



Las copias de seguridad protegen frente a: borrados accidentales, fallos de hardware (discos duros), errores del sistema, Ataques (virus, ransomware) y fallos humanos.



Es muy importante recordar que no se deben guardar las copias de seguridad en el mismo disco de la información que copiamos.



###### **9.6.1 Tipos de copias de seguridad**



• Copia completa (Full backup): copia todos los archivos seleccionados. Es la más sencilla, pero ocupa más espacio y tarda más. Es necesaria la primera vez y a lo mejor de manera mensual o anual.



• Copia incremental: copia solo los archivos que han cambiado desde la última copia. Es más rápida y ocupa menos espacio, pero para restaurarla se necesita la copia completa más todas las incrementales. Muy usada en servidores.



• Copia diferencial: copia los archivos modificados desde la última copia completa. Ocupa más que la incremental, pero es más fácil de restaurar.



###### **9.6.2 Automatización copias de seguridad**

###### 

Las copias deben hacerse automáticamente, de forma periódica y sin intervención del usuario. Por ello se usan scripts y tareas programadas. Normalmente en Linux se suelen hacer copias diarias de /home y copias semanales de /etc.



Una vez que se automatiza una copia se tiene que comprobar que el archivo se ha creado, revisar los logs y probar alguna restauración para ver que todo funciona correctamente. también es muy importante no guardar todas las copias eternamente, sino que hay que definir que copias se conservar y durante cuánto tiempo.





**Comandos útiles:**



• tar czvf backup.tar.gz /ruta/a/copiar → comprimir lo que se quiere copiar

 

• tar -xzvf backup\_home.tar.gz -C / → restaurar la copia



• rsync -av /origen /destino → copias incrementales



• rsync -av /backup/home /home → restaurar la copia

