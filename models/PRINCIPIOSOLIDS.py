"""
Sistema de Admision ULEAM 
Autor: Equipo 3ro TI "C" - Jean Pierre, Braddy, Bismark
Fecha: Diciembre 2025

Este main usa las clases de los archivos de PRINCIPIOS SOLID (VERSIONES BUENAS):

 - S (SRP): RegistroNacional  -> models/RegistroNacional.py
 - O (OCP): Postulante        -> models/Postulante.py
 - L (LSP): SedeCampus        -> models/SedeCampus.py
 - I (ISP): Interfaces demo   -> models/PRINCIPIOSOLIDI4.py
 - D (DIP): Inscripcion (demo)-> models/PRINCIPIOSOLIDD5.py

Y además muestra CÓDIGOS MALOS para comparar:

 - OCP MALO:  models/PRINCIPIOSOLIDO.py        (Postulante malo)
 - LSP MALO:  models/PRINCIPIOSOLIDL3.py       (SedeCampus malo)
 - ISP BUENO: models/PRINCIPIOSOLIDI4.py       (OfertaCarrera con interfaces)
 - DIP BUENO: models/PRINCIPIOSOLIDD5.py       (Inscripcion con inyección)
"""

from datetime import datetime, timedelta

# ================== PRINCIPIOS SOLID (CLASES BUENAS) ==================
from models.RegistroNacional import RegistroNacional          # S (SRP)
from models.Postulante import Postulante                      # O (OCP)
from models.SedeCampus import SedeCampus                      # L (LSP)
import models.PRINCIPIOSOLIDI4 as PRINCIPIOSOLIDI4           # I (ISP) - demo bueno
import models.PRINCIPIOSOLIDD5 as PRINCIPIOSOLIDD5           # D (DIP) - demo bueno

# ================== DEMOS CÓDIGO MALO / COMPARACIÓN ==================
# Postulante MALO (VIOLA OCP)
from models.PRINCIPIOSOLIDO import Postulante as PostulanteMALO

# SedeCampus MALO (VIOLA varios principios, incluido LSP)
from models.PRINCIPIOSOLIDL3 import SedeCampus as SedeCampusMALO

# =============== MODELOS DEL SISTEMA REAL ===============
from models.ofertaCarrera import OfertaCarrera          # Clase real usada en el sistema
from models.Inscripcion import Inscripcion              # Inscripcion REAL del menú
from models.Evaluacion import Evaluacion
from models.Asignacion import Asignacion
from models.PuntajePostulacion import PuntajePostulacion


# ==================== ALMACENAMIENTO GLOBAL ====================
sedes_disponibles = []
ofertas_disponibles = []
registros_nacionales = []
postulantes_creados = []
inscripciones_creadas = []
evaluaciones_creadas = []
asignaciones_creadas = []
puntajes_creados = []


# ==================== INICIALIZACIÓN DE DATOS ====================
def inicializar_sistema():
    """Inicializa el sistema con datos reales de ULEAM"""
    global sedes_disponibles, ofertas_disponibles, registros_nacionales

    import sys
    import io

    # Redirigir stdout temporalmente por si las clases imprimen algo al crearse
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        # ----- SEDES (USA SedeCampus BUENA) -----
        # La clase SedeCampus BUENA solo recibe el ID de la sede.
        sede_matriz = SedeCampus(1)
        sede_chone = SedeCampus(2)
        sede_el_carmen = SedeCampus(3)
        sede_pedernales = SedeCampus(4)
        sede_bahia = SedeCampus(5)
        sede_tosagua = SedeCampus(6)
        sede_santo_domingo = SedeCampus(7)
        sede_flavio_alfaro = SedeCampus(8)
        sede_pichincha = SedeCampus(9)

        sedes_disponibles = [
            sede_matriz,
            sede_chone,
            sede_el_carmen,
            sede_pedernales,
            sede_bahia,
            sede_tosagua,
            sede_santo_domingo,
            sede_flavio_alfaro,
            sede_pichincha
        ]

        # ----- OFERTAS ACADEMICAS (USA OfertaCarrera REAL) -----
        oferta_ti_matriz = OfertaCarrera(
            carrera_id=101,
            nombre_carrera="Tecnologias de la Informacion",
            sede_id=sede_matriz.sede_id,
            nombre_sede=sede_matriz.nombre_sede,
            cupos_total=40,
            nivel="TERCER NIVEL",
            modalidad="PRESENCIAL",
            jornada="MATUTINA"
        )

        oferta_software_matriz = OfertaCarrera(
            carrera_id=102,
            nombre_carrera="Ingenieria en Software",
            sede_id=sede_matriz.sede_id,
            nombre_sede=sede_matriz.nombre_sede,
            cupos_total=35,
            nivel="TERCER NIVEL",
            modalidad="PRESENCIAL",
            jornada="VESPERTINA"
        )

        oferta_medicina_matriz = OfertaCarrera(
            carrera_id=103,
            nombre_carrera="Medicina",
            sede_id=sede_matriz.sede_id,
            nombre_sede=sede_matriz.nombre_sede,
            cupos_total=25,
            nivel="TERCER NIVEL",
            modalidad="PRESENCIAL",
            jornada="MATUTINA"
        )

        oferta_admin_chone = OfertaCarrera(
            carrera_id=104,
            nombre_carrera="Administracion de Empresas",
            sede_id=sede_chone.sede_id,
            nombre_sede=sede_chone.nombre_sede,
            cupos_total=30,
            nivel="TERCER NIVEL",
            modalidad="PRESENCIAL",
            jornada="NOCTURNA"
        )

        ofertas_disponibles = [
            oferta_ti_matriz,
            oferta_software_matriz,
            oferta_medicina_matriz,
            oferta_admin_chone
        ]

        # ----- REGISTROS NACIONALES (USA RegistroNacional BUENO - SRP) -----
        registro1 = RegistroNacional(
            identificacion="1316202082",
            nombres="JEAN PIERRE",
            apellidos="FLORES PILOSO"
        )
        registro1.completar_datos_personales("2007-05-15", "HOMBRE", "MESTIZO")
        registro1.completar_ubicacion("MANABI", "MANTA", "MANTA", "LOS ESTEROS", "AV. 24 DE MAYO")
        registro1.completar_contacto("0999999999", "florespilosojeanpierre@gmail.com")
        registro1.completar_datos_academicos("U.E. MANTA", "FISCAL", 9.5, "SI")
        registro1.validar_completitud()

        registro2 = RegistroNacional(
            identificacion="1350432058",
            nombres="BRADDY LONDRE",
            apellidos="VERA ANCHUNDIA"
        )
        registro2.completar_datos_personales("2007-03-20", "HOMBRE", "MONTUBIO")
        registro2.completar_ubicacion("MANABI", "CHONE", "CHONE", "CENTRO", "CALLE PRINCIPAL")
        registro2.completar_contacto("0988888888", "braddy.vera@uleam.edu.ec")
        registro2.completar_datos_academicos("U.E. CHONE", "FISCAL", 9.0, "NO")
        registro2.validar_completitud()

        registro3 = RegistroNacional(
            identificacion="1360234567",
            nombres="BISMARK GABRIEL",
            apellidos="CEVALLOS CEDEÑO"
        )
        registro3.completar_datos_personales("2007-07-10", "HOMBRE", "MESTIZO")
        registro3.completar_ubicacion("MANABI", "MANTA", "MANTA", "TARQUI", "CALLE 10")
        registro3.completar_contacto("0977777777", "bismark.cevallos@uleam.edu.ec")
        registro3.completar_datos_academicos("U.E. MANTA", "FISCAL", 9.2, "NO")
        registro3.validar_completitud()

        registros_nacionales = [registro1, registro2, registro3]

    finally:
        # restaurar stdout
        sys.stdout = old_stdout


# ==================== FUNCIONES PRINCIPALES (SISTEMA REAL) ====================

def ver_sedes():
    """Opcion 1: Ver sedes disponibles"""
    print("\n" + "=" * 60)
    print("SEDES ULEAM DISPONIBLES")
    print("=" * 60)

    for sede in sedes_disponibles:
        print(f"\nSede:   {sede.nombre_sede}")
        print(f"Codigo: {sede.sede_id}")

    print(f"\nTotal de sedes: {len(sedes_disponibles)}")


def ver_ofertas_carreras():
    """Opcion 2: Ver ofertas de carreras reales"""
    print("\n" + "=" * 60)
    print("OFERTAS ACADEMICAS ULEAM - PERIODO 2025-1")
    print("=" * 60)

    for i, oferta in enumerate(ofertas_disponibles, 1):
        print(f"\n[{i}] {oferta.nombre_carrera}")
        print(f"   Sede:     {oferta.nombre_sede}")
        print(f"   Cupos:    {oferta.cupos_total}")
        print(f"   Nivel:    {oferta.nivel}")
        print(f"   Jornada:  {oferta.jornada}")
        print(f"   Modalidad:{oferta.modalidad}")


def verificar_registro_nacional():
    """Opcion 3: Verificar registro nacional por cédula"""
    print("\n" + "=" * 60)
    print("VERIFICAR REGISTRO NACIONAL")
    print("=" * 60)

    cedula = input("\nIngrese numero de cedula: ").strip()

    registro = next((r for r in registros_nacionales
                     if r.identificacion == cedula), None)

    if registro:
        print("\nREGISTRO ENCONTRADO:")
        print(f"Cedula:           {registro.identificacion}")
        print(f"Nombres:          {registro.nombres} {registro.apellidos}")
        print(f"Estado:           {registro.estado}")
        print(f"Unidad Educativa: {registro.unidad_educativa}")
        print(f"Tipo Unidad:      {registro.tipo_unidad_educativa}")
        print(f"Calificacion:     {registro.calificacion}")
        print(f"Provincia:        {registro.provincia_reside}")
        print(f"Canton:           {registro.canton_reside}")
        print(f"Correo:           {registro.correo}")
        print(f"Celular:          {registro.celular}")
    else:
        print(f"\nNo se encontro registro con cedula: {cedula}")


def ver_todos_registros():
    """Opcion 4: Ver todos los registros nacionales cargados"""
    print("\n" + "=" * 60)
    print("LISTA DE REGISTROS NACIONALES CARGADOS")
    print("=" * 60)

    for i, registro in enumerate(registros_nacionales, 1):
        print(f"\n[{i}] Cedula: {registro.identificacion}")
        print(f"Nombre: {registro.nombres} {registro.apellidos}")
        print(f"Estado: {registro.estado}")
        print("-" * 60)

    print(f"\nTotal de registros: {len(registros_nacionales)}")


def crear_inscripcion():
    """Opcion 5: Crear inscripcion (GENERA EVALUACION AUTOMATICAMENTE)"""
    print("\n" + "=" * 60)
    print("CREAR INSCRIPCION")
    print("=" * 60)

    cedula = input("\nIngrese numero de cedula: ").strip()

    registro = next((r for r in registros_nacionales
                     if r.identificacion == cedula), None)

    if not registro:
        print(f"\nError: No existe registro nacional con cedula {cedula}")
        return

    if registro.estado != "COMPLETO":
        print(f"\nError: El registro debe estar COMPLETO. "
              f"Estado actual: {registro.estado}")
        return

    print(f"\nRegistro encontrado: {registro.nombres} {registro.apellidos}")

    nombre_completo = f"{registro.nombres} {registro.apellidos}"
    email = getattr(registro, "correo", "sin_correo@uleam.edu.ec")
    telefono = getattr(registro, "celular", "0000000000")

    # La edad y validaciones ya están en RegistroNacional; aquí solo usamos la fecha
    fecha_nac_str = "2000-01-01"  # valor por defecto por si no estuviera cargada

    # Postulante viene de Postulante.py (OCP BUENO)
    postulante = Postulante(
        cedula=registro.identificacion,
        nombre_completo=nombre_completo,
        email=email,
        telefono=telefono,
        fecha_nacimiento=fecha_nac_str
    )

    postulantes_creados.append(postulante)
    print(f"Postulante creado exitosamente (ID: {postulante.id_postulante})")

    print("\nCARRERAS DISPONIBLES:")
    for i, oferta in enumerate(ofertas_disponibles, 1):
        print(f"{i}. {oferta.nombre_carrera} - "
              f"{oferta.nombre_sede} ({oferta.jornada})")

    try:
        opcion_carrera = int(
            input("\nSeleccione carrera (1-{0}): "
                  .format(len(ofertas_disponibles)))
        )
        if opcion_carrera < 1 or opcion_carrera > len(ofertas_disponibles):
            print("Opcion invalida")
            return
    except ValueError:
        print("Entrada invalida")
        return

    oferta_seleccionada = ofertas_disponibles[opcion_carrera - 1]

    try:
        orden_pref = int(input("Ingrese orden de preferencia (1-3): "))
    except ValueError:
        print("Entrada invalida")
        return

    # Inscripcion REAL del sistema (models.Inscripcion)
    inscripcion = Inscripcion(
        id_postulante=postulante.id_postulante,
        carrera_id=oferta_seleccionada.carrera_id,
        orden_preferencia=orden_pref,
        sede_id=oferta_seleccionada.sede_id,
        jornada=oferta_seleccionada.jornada,
        cedula_postulante=cedula
    )

    inscripciones_creadas.append(inscripcion)

    evaluacion = inscripcion.obtenerEvaluacion()
    if evaluacion:
        evaluaciones_creadas.append(evaluacion)

    print("\n" + "=" * 60)
    print("INSCRIPCION CREADA EXITOSAMENTE")
    print("=" * 60)
    inscripcion.mostrar_info_completa()

    print("\nPROXIMOS PASOS:")
    print("1. Presente su documento de identidad el dia del examen")
    print("2. Llegue 30 minutos antes de la hora programada")
    print("3. Consulte su evaluacion con la opcion 6")


def consultar_evaluacion():
    """Opcion 6: Consultar evaluación por cedula"""
    print("\n" + "=" * 60)
    print("CONSULTAR EVALUACION")
    print("=" * 60)

    cedula = input("\nIngrese numero de cedula: ").strip()

    evaluacion = next((e for e in evaluaciones_creadas
                       if e.cedula_postulante == cedula), None)

    if evaluacion:
        evaluacion.mostrar_info()
    else:
        print("\nNo hay evaluacion asociada a esta inscripcion")


def consultar_asignacion():
    """Opcion 7: Consultar asignacion por cedula"""
    print("\n" + "=" * 60)
    print("CONSULTAR ASIGNACION")
    print("=" * 60)

    cedula = input("\nIngrese numero de cedula: ").strip()

    asignacion = next((a for a in asignaciones_creadas
                       if a.cedula_postulante == cedula), None)

    if asignacion:
        asignacion.mostrar_info()
    else:
        print(f"\nNo se encontro asignacion con cedula: {cedula}")
        print("\n📅 Su examen aún no se ha realizado o está pendiente de "
              "calificación.")
        print("   Espere hasta la fecha programada para conocer su resultado "
              "y asignación de cupo.")
        print("   Puede revisar su fecha de examen con la opcion 6 del menú.")


def consultar_puntaje():
    """Opcion 8: Consultar puntaje por cedula"""
    print("\n" + "=" * 60)
    print("CONSULTAR PUNTAJE DE POSTULACION")
    print("=" * 60)

    cedula = input("\nIngrese numero de cedula: ").strip()

    puntaje = next((p for p in puntajes_creados
                    if p.cedula_postulante == cedula), None)

    if puntaje:
        puntaje.mostrar_resumen()
    else:
        print(f"\nNo se encontro puntaje con cedula: {cedula}")


def simular_proceso_completo():
    """Opcion 9: Simular proceso completo de admision (DEMO)"""
    print("\n" + "=" * 60)
    print("SIMULACION COMPLETA DE PROCESO DE ADMISION")
    print("=" * 60)

    if not registros_nacionales:
        print("No hay registros cargados. Inicializando sistema...")
        inicializar_sistema()

    registro = registros_nacionales[0]
    cedula = registro.identificacion

    print(f"\nUsando registro de: {registro.nombres} {registro.apellidos} "
          f"(Cédula: {cedula})")

    nombre_completo = f"{registro.nombres} {registro.apellidos}"
    email = getattr(registro, "correo", "sin_correo@uleam.edu.ec")
    telefono = getattr(registro, "celular", "0000000000")

    fecha_nac_str = "2000-01-01"

    postulante = Postulante(
        cedula=registro.identificacion,
        nombre_completo=nombre_completo,
        email=email,
        telefono=telefono,
        fecha_nacimiento=fecha_nac_str
    )
    postulantes_creados.append(postulante)

    oferta = ofertas_disponibles[0]

    inscripcion = Inscripcion(
        id_postulante=postulante.id_postulante,
        carrera_id=oferta.carrera_id,
        orden_preferencia=1,
        sede_id=oferta.sede_id,
        jornada=oferta.jornada,
        cedula_postulante=cedula
    )
    inscripciones_creadas.append(inscripcion)

    evaluacion = inscripcion.obtenerEvaluacion()
    evaluaciones_creadas.append(evaluacion)

    print("\n1. Inscripcion y evaluacion generadas automaticamente")

    calificacion_evaluacion = 850.0
    evaluacion.registrarCalificacion(calificacion_evaluacion)
    print(f"\n2. Evaluacion calificada: {calificacion_evaluacion} puntos")

    puntaje = PuntajePostulacion(
        id_postulante=postulante.id_postulante,
        nota_grado=registro.calificacion,
        puntaje_evaluacion=calificacion_evaluacion,
        cedula_postulante=cedula,
        puntaje_meritos=100.0
    )
    puntajes_creados.append(puntaje)
    print(f"\n3. Puntaje calculado: {puntaje.puntaje_final}/1000")

    asignacion = Asignacion(
        id_postulante=postulante.id_postulante,
        carrera_id=oferta.carrera_id,
        sede_id=oferta.sede_id,
        puntaje_final=puntaje.puntaje_final,
        cedula_postulante=cedula
    )
    asignaciones_creadas.append(asignacion)
    print(f"\n4. Asignacion creada (ID: {asignacion.id_asignacion})")

    asignacion.confirmar()
    print(f"\n5. Asignacion confirmada")

    print("\n" + "=" * 60)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print("=" * 60)
    print(f"\nPuede consultar toda la informacion con la cedula: {cedula}")
    print("Use las opciones 6, 7 y 8 del menu")


# ==================== DEMOS SOLID (BUENOS Y MALOS) ====================

def demo_postulante_ocp_malo():
    """Opcion 10: Demostración de Postulante MALO (viola OCP)"""
    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN: PRINCIPIO O (OCP) - CÓDIGO MALO (PRINCIPIOSOLIDO)")
    print("=" * 80)

    # 1. POSTULANTE REGULAR
    print("\n1. POSTULANTE REGULAR:")
    p1 = PostulanteMALO("1234567890", "Juan Pérez", "juan@mail.com",
                        "0987654321", "1995-05-15", tipo='REGULAR')
    p1.validarIdentidad()
    print(f"   ¿Puede inscribirse? {p1.puede_inscribirse()}")

    # 2. POSTULANTE MENOR
    print("\n2. POSTULANTE MENOR:")
    p2 = PostulanteMALO("9876543210", "María López", "maria@mail.com",
                        "0912345678", "2008-03-20", tipo='MENOR')
    p2.validarIdentidad()  # Rechazado - falta tutor
    p2.registrar_tutor("Pedro López", "1111111111")
    p2.validarIdentidad()  # Verificado
    print(f"   ¿Puede inscribirse? {p2.puede_inscribirse()}")

    # 3. POSTULANTE EXTRANJERO
    print("\n3. POSTULANTE EXTRANJERO:")
    p3 = PostulanteMALO("PASS123456", "John Smith", "john@mail.com",
                        "0998877665", "1990-07-10", tipo='EXTRANJERO')
    p3.validarIdentidad()  # Rechazado - falta homologación
    p3.marcar_titulo_homologado()
    p3.validarIdentidad()  # Verificado
    print(f"   ¿Puede inscribirse? {p3.puede_inscribirse()}")

    print("\n" + "=" * 80)
    print("PROBLEMAS DE ESTE CÓDIGO (para explicar OCP):")
    print("- Usa if/elif por cada tipo de postulante.")
    print("- Para agregar un nuevo tipo → hay que MODIFICAR la clase.")
    print("- La clase tiene atributos de todos los tipos (REGULAR, MENOR, EXTRANJERO, CON_CUPO).")
    print("=" * 80)


def demo_sede_lsp_malo():
    """Opcion 11: Demostración de SedeCampus MALO (viola varios principios, LSP)"""
    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN: CÓDIGO MALO - SEDE CAMPUS (PRINCIPIOSOLIDL3)")
    print("=" * 80)

    # Crear sede principal
    print("\n1. SEDE PRINCIPAL:")
    sede1 = SedeCampusMALO("SEDE-001", "Campus Central Manta", tipo_sede='PRINCIPAL')
    sede1.establecer_ubicacion("MANABÍ", "MANTA", "Av. Principal 123")
    sede1.agregar_edificio("Edificio A")
    sede1.agregar_aula("A-101", 40)
    sede1.agregar_aula("A-102", 35)
    sede1.agregar_carrera("Ingeniería en Sistemas")
    sede1.agregar_carrera("Medicina")
    sede1.agregar_personal("Dr. Juan Pérez", "DIRECTOR")
    sede1.inscribir_estudiante("María López")
    sede1.validar_sede()

    # Crear sede extensión
    print("\n2. SEDE EXTENSIÓN:")
    sede2 = SedeCampusMALO("SEDE-002", "Extensión Pedernales", tipo_sede='EXTENSION')
    sede2.establecer_ubicacion("MANABÍ", "PEDERNALES", "Calle Principal")
    sede2.agregar_edificio("Edificio B")  # No debería poder
    sede2.agregar_carrera("Administración")  # Permitida
    sede2.agregar_carrera("Medicina")        # No permitida en extensión

    # Crear sede virtual
    print("\n3. SEDE VIRTUAL:")
    sede3 = SedeCampusMALO("SEDE-003", "Campus Virtual", tipo_sede='VIRTUAL')
    sede3.agregar_carrera("Marketing Digital")
    sede3.agregar_edificio("Edificio C")  # Virtual no tiene edificios

    # Generar reporte de la sede 1
    print("\n4. REPORTE COMPLETO SEDE PRINCIPAL:")
    sede1.generar_reporte_completo()

    print("\n" + "=" * 80)
    print("PROBLEMAS DE ESTE CÓDIGO (para explicar LSP / SRP / OCP / DIP):")
    print("- Una sola clase maneja carreras, infraestructura, personal, ubicación, estudiantes, BD, notificaciones.")
    print("- Usa muchos if/elif según tipo de sede (PRINCIPAL, EXTENSION, VIRTUAL).")
    print("- Depende directamente de MySQL, Email, etc. (viola DIP).")
    print("=" * 80)


def demo_isp_oferta_carrera():
    """Opcion 12: Demostración PRINCIPIO I (ISP) con carreras"""
    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN: PRINCIPIO I (ISP) - CÓDIGO BUENO (PRINCIPIOSOLIDI4)")
    print("=" * 80)

    CarreraBasica = PRINCIPIOSOLIDI4.CarreraBasica
    CarreraConCupos = PRINCIPIOSOLIDI4.CarreraConCupos
    CarreraConModalidades = PRINCIPIOSOLIDI4.CarreraConModalidades
    CarreraCompleta = PRINCIPIOSOLIDI4.CarreraCompleta

    # 1. Carrera básica
    print("\n1. CARRERA BÁSICA (solo interfaz básica):")
    carrera1 = CarreraBasica("001", "Filosofía")
    print(f"   {carrera1.obtener_informacion()}")
    print(f"   ¿Disponible? {carrera1.esta_disponible()}")

    # 2. Carrera con cupos
    print("\n2. CARRERA CON CUPOS:")
    carrera2 = CarreraConCupos("002", "Medicina", cupos_totales=50)
    print(f"   {carrera2.obtener_informacion()}")
    carrera2.verificar_cupos_disponibles()
    carrera2.asignar_cupo("Juan Pérez")
    carrera2.asignar_cupo("María López")
    carrera2.verificar_cupos_disponibles()

    # 3. Carrera con modalidades
    print("\n3. CARRERA CON MODALIDADES:")
    carrera3 = CarreraConModalidades("003", "Administración")
    carrera3.agregar_modalidad("PRESENCIAL")
    carrera3.agregar_modalidad("SEMIPRESENCIAL")
    carrera3.agregar_modalidad("EN LÍNEA")
    carrera3.listar_modalidades()

    # 4. Carrera completa
    print("\n4. CARRERA COMPLETA (todas las interfaces):")
    carrera4 = CarreraCompleta("004", "Ingeniería en Sistemas", cupos_totales=100)
    print(f"   {carrera4.obtener_informacion()}")
    carrera4.agregar_modalidad("PRESENCIAL")
    carrera4.agregar_horario("MATUTINO")
    carrera4.agregar_horario("VESPERTINO")
    print(f"   ¿Requiere nivelación? {carrera4.requiere_nivelacion()}")
    carrera4.asignar_nivel("Pedro García", "NIVEL 1")

    print("\n" + "=" * 80)
    print("VENTAJAS ISP:")
    print("- Cada clase implementa SOLO las interfaces que necesita.")
    print("- No obligamos a implementar métodos que no usan.")
    print("- Fácil agregar nuevas interfaces sin romper código existente.")
    print("=" * 80)


def demo_dip_inscripcion():
    """Opcion 13: Demostración PRINCIPIO D (DIP) con Inscripcion"""
    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN: PRINCIPIO D (DIP) - CÓDIGO BUENO (PRINCIPIOSOLIDD5)")
    print("=" * 80)

    # Configuración 1: MySQL + Gmail
    print("\n1. CONFIGURACIÓN: MySQL + Gmail")
    bd_mysql = PRINCIPIOSOLIDD5.BaseDatosMySQL()
    email_gmail = PRINCIPIOSOLIDD5.ServicioGmail()

    inscripcion1 = PRINCIPIOSOLIDD5.Inscripcion(
        postulante="Juan Pérez",
        carrera="Ingeniería en Sistemas",
        periodo="2025-1",
        base_datos=bd_mysql,
        servicio_email=email_gmail
    )
    inscripcion1.procesar_inscripcion()

    # Configuración 2: PostgreSQL + Outlook
    print("\n2. CONFIGURACIÓN: PostgreSQL + Outlook")
    bd_postgres = PRINCIPIOSOLIDD5.BaseDatosPostgreSQL()
    email_outlook = PRINCIPIOSOLIDD5.ServicioOutlook()

    inscripcion2 = PRINCIPIOSOLIDD5.Inscripcion(
        postulante="María López",
        carrera="Medicina",
        periodo="2025-1",
        base_datos=bd_postgres,
        servicio_email=email_outlook
    )
    inscripcion2.procesar_inscripcion()

    print("\n" + "=" * 80)
    print("VENTAJAS DIP:")
    print("- Inscripcion depende de ABSTRACCIONES (InterfazBaseDatos, InterfazEmail).")
    print("- Podemos cambiar MySQL ↔ PostgreSQL, Gmail ↔ Outlook sin tocar la clase Inscripcion.")
    print("- Fácil de testear con mocks (inyección de dependencias).")
    print("=" * 80)


# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu():
    """Muestra el menu principal"""
    print("\n" + "=" * 60)
    print("MENU PRINCIPAL - SISTEMA ULEAM (CON PRINCIPIOS SOLID)")
    print("=" * 60)
    print("1. Ver Sedes Disponibles")
    print("2. Ver Ofertas de Carreras Reales")
    print("3. Verificar Registro Nacional por Cédula")
    print("4. Ver Todos los Registros Nacionales")
    print("5. Crear Inscripcion")
    print("6. Consultar Evaluacion por Cedula")
    print("7. Consultar Asignacion por Cedula")
    print("8. Consultar Puntaje por Cedula")
    print("9. Simular Proceso Completo (DEMO)")
    print("-" * 60)
    print("10. DEMO OCP - Postulante (codigo MALO)")
    print("11. DEMO LSP - SedeCampus (codigo MALO)")
    print("12. DEMO ISP - OfertaCarrera (codigo BUENO)")
    print("13. DEMO DIP - Inscripcion (codigo BUENO)")
    print("0. Salir")
    print("=" * 60)


def main():
    inicializar_sistema()

    while True:
        try:
            mostrar_menu()
            opcion = input("\nSeleccione una opcion: ").strip()

            if opcion == '1':
                ver_sedes()
            elif opcion == '2':
                ver_ofertas_carreras()
            elif opcion == '3':
                verificar_registro_nacional()
            elif opcion == '4':
                ver_todos_registros()
            elif opcion == '5':
                crear_inscripcion()
            elif opcion == '6':
                consultar_evaluacion()
            elif opcion == '7':
                consultar_asignacion()
            elif opcion == '8':
                consultar_puntaje()
            elif opcion == '9':
                simular_proceso_completo()
            elif opcion == '10':
                demo_postulante_ocp_malo()
            elif opcion == '11':
                demo_sede_lsp_malo()
            elif opcion == '12':
                demo_isp_oferta_carrera()
            elif opcion == '13':
                demo_dip_inscripcion()
            elif opcion == '0':
                print("\nGracias por usar el Sistema de Admision ULEAM")
                print("\nPrincipios SOLID aplicados (version BUENA en el sistema):")
                print(" - S (SRP): RegistroNacional  -> models/RegistroNacional.py")
                print(" - O (OCP): Postulante        -> models/Postulante.py")
                print(" - L (LSP): SedeCampus        -> models/SedeCampus.py")
                print(" - I (ISP): Interfaces demo   -> models/PRINCIPIOSOLIDI4.py")
                print(" - D (DIP): Inscripcion (demo)-> models/PRINCIPIOSOLIDD5.py")
                print("\nY se mostraron códigos MALOS para comparación en opciones 10–13.")
                break
            else:
                print("\nOpcion invalida. Intente nuevamente.")

        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Por favor, revise los imports y que la carpeta 'models' exista.")


if __name__ == "__main__":
    main()
