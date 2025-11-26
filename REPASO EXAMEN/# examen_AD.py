# examen_AD.py
# Examen interactivo completo de 50 preguntas sobre Directorio Activo, Cuentas y Copias de Seguridad

import os

preguntas = [
    # TEMA 2
    {"pregunta": "¿Qué es un Directorio Activo?",
     "opciones": ["a) Un antivirus", "b) Una base de datos de objetos de red", "c) Una red LAN", "d) Un servidor web", "e) Un grupo de trabajo"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es un bosque?",
     "opciones": ["a) Un único dominio", "b) Varios dominios con un esquema común", "c) Varias OUs", "d) Varias subredes", "e) Un conjunto de perfiles"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es un dominio?",
     "opciones": ["a) Un conjunto de usuarios y recursos administrados", "b) Un firewall", "c) Un servidor DNS", "d) Una OU", "e) Un perfil obligatorio"],
     "respuesta": "a"},

    {"pregunta": "¿Qué es un sitio en AD?",
     "opciones": ["a) Un lugar físico", "b) Un conjunto de subredes que controlan replicación", "c) Un dominio", "d) Un GPO", "e) Un grupo global"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es una Unidad Organizativa?",
     "opciones": ["a) Un perfil móvil", "b) Un contenedor para organizar objetos", "c) Un dominio", "d) Un sitio", "e) Un grupo local"],
     "respuesta": "b"},

    {"pregunta": "Verdadero o Falso: dcpromo sigue siendo el método para promocionar un controlador de dominio.",
     "opciones": ["Verdadero", "Falso"],
     "respuesta": "Falso"},

    {"pregunta": "¿Qué herramienta usarías para administrar usuarios?",
     "opciones": ["a) Sitios y Servicios", "b) Usuarios y Equipos de Active Directory", "c) Visor de Eventos", "d) Monitor de Recursos", "e) Copias de Seguridad"],
     "respuesta": "b"},

    {"pregunta": "¿Qué herramienta gestiona la replicación entre sitios?",
     "opciones": ["a) Monitor de Rendimiento", "b) Sitios y Servicios de AD", "c) Usuarios y Equipos AD", "d) Copias de Seguridad", "e) DNS"],
     "respuesta": "b"},

    {"pregunta": "Verdadero o Falso: Dos bosques pueden tener relaciones de confianza.",
     "opciones": ["Verdadero", "Falso"],
     "respuesta": "Verdadero"},

    {"pregunta": "¿Qué es una relación de confianza?",
     "opciones": ["a) Un perfil móvil", "b) Un vínculo entre dominios", "c) Un GPO", "d) Un sitio", "e) Un registro DNS"],
     "respuesta": "b"},

    # TEMA 3
    {"pregunta": "¿Qué es una cuenta de usuario?",
     "opciones": ["a) Archivo temporal", "b) Identidad digital para iniciar sesión", "c) Un dominio", "d) Un sitio", "e) Un perfil obligatorio"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es una cuenta de equipo?",
     "opciones": ["a) Un perfil móvil", "b) Identidad del equipo en el dominio", "c) Un GPO", "d) Un sitio", "e) Un bosque"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es una cuenta de grupo?",
     "opciones": ["a) Una cuenta de un usuario", "b) Agrupa usuarios/equipos", "c) Un dominio", "d) Un DNS", "e) Un perfil móvil"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es un grupo de distribución?",
     "opciones": ["a) Grupo con permisos", "b) Grupo para correo", "c) Grupo de perfiles", "d) Dominio", "e) OU"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es un grupo de seguridad?",
     "opciones": ["a) Correo", "b) Permisos", "c) Perfil móvil", "d) GPO", "e) OU"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es un perfil móvil?",
     "opciones": ["a) Un perfil que se guarda en el servidor", "b) Solo local", "c) Obligatorio", "d) Temporal", "e) Super-obligatorio"],
     "respuesta": "a"},

    {"pregunta": "¿Qué es un perfil obligatorio?",
     "opciones": ["a) Se guardan cambios", "b) No se guardan cambios", "c) Perfil local", "d) Perfil de invitado", "e) GPO"],
     "respuesta": "b"},

    {"pregunta": "Verdadero o Falso: un perfil super-obligatorio impide cambios incluso temporales.",
     "opciones": ["Verdadero", "Falso"],
     "respuesta": "Verdadero"},

    {"pregunta": "¿Qué significa ser miembro de un grupo?",
     "opciones": ["a) Nada", "b) Hereda permisos", "c) Borra privilegios", "d) Crea perfiles", "e) Elimina usuarios"],
     "respuesta": "b"},

    {"pregunta": "¿Cómo se crea una OU?",
     "opciones": ["a) Panel de control", "b) Usuarios y Equipos AD → clic derecho → nueva OU", "c) DNS", "d) Monitor de Recursos", "e) Visor de Eventos"],
     "respuesta": "b"},

    # TEMA 4
    {"pregunta": "¿Qué es una copia incremental?",
     "opciones": ["a) Copia archivos específicos", "b) Copia solo cambios desde la última copia", "c) Copia completa", "d) Copia temporal", "e) Copia local"],
     "respuesta": "b"},

    {"pregunta": "¿Por qué se hace una copia de seguridad?",
     "opciones": ["a) Por diversión", "b) Recuperar datos ante fallos", "c) Crear OUs", "d) Crear perfiles", "e) Monitorear CPU"],
     "respuesta": "b"},

    {"pregunta": "¿Qué herramienta usas para copias de seguridad?",
     "opciones": ["a) DNS", "b) Copias de seguridad de Windows Server", "c) Usuarios y Equipos AD", "d) Visor de Eventos", "e) Sitios y Servicios"],
     "respuesta": "b"},

    {"pregunta": "¿Qué es el Programador de Tareas?",
     "opciones": ["a) Crear OUs", "b) Ejecutar tareas automáticamente", "c) Configurar DNS", "d) Instalar roles", "e) Copiar archivos"],
     "respuesta": "b"},

    {"pregunta": "Verdadero o Falso: El Monitor de Rendimiento permite configurar alertas.",
     "opciones": ["Verdadero", "Falso"],
     "respuesta": "Verdadero"},

    {"pregunta": "¿Qué es el Visor de Eventos?",
     "opciones": ["a) Editor de perfiles", "b) Registro de sucesos del sistema", "c) DNS", "d) Replicación", "e) Firewall"],
     "respuesta": "b"},

    {"pregunta": "¿Qué muestra el Visor de Eventos?",
     "opciones": ["a) Solo errores", "b) Errores, advertencias e información", "c) GPO", "d) Usuarios", "e) Grupos"],
     "respuesta": "b"},

    {"pregunta": "Verdadero o Falso: Los eventos reenviados permiten centralizar registros.",
     "opciones": ["Verdadero", "Falso"],
     "respuesta": "Verdadero"},
]

# ===========================================================
# LÓGICA DEL EXAMEN
# ===========================================================

def examen():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== EXAMEN INTERACTIVO DE DIRECTORIO ACTIVO ===")
    print("Responde con la letra correcta o 'Verdadero/Falso'\n")

    aciertos = 0

    for i, p in enumerate(preguntas, start=1):
        print(f"\nPregunta {i}: {p['pregunta']}")
        for opcion in p["opciones"]:
            print(opcion)

        resp = input("Tu respuesta: ").strip().lower()
        correcta = p["respuesta"].lower()

        if resp == correcta:
            print("✔️ Correcto")
            aciertos += 1
        else:
            print(f"❌ Incorrecto. Respuesta correcta: {p['respuesta']}")

    print("\n=== RESULTADO FINAL ===")
    print(f"Aciertos: {aciertos}/{len(preguntas)}")
    print(f"Nota: {round((aciertos / len(preguntas)) * 10, 2)} / 10")

if __name__ == "__main__":
    examen()
