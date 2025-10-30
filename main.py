"""
Sistema de Admision ULEAM - COMPLETO Y AUTOMATIZADO
Autor: Equipo 3ro TI "C" - Jean Pierre, Braddy, Bismark
Fecha: Octubre 2025
"""

from datetime import datetime, timedelta

# Importar TODAS las clases desde carpeta models
from models.Postulante import Postulante
from models.SedeCampus import SedeCampus
from models.ofertaCarrera import OfertaCarrera
from models.RegistroNacional import RegistroNacional
from models.Inscripcion import Inscripcion
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
    
    # SEDES REALES (crear sin imprimir)
    import sys
    import io
    
    # Redirigir stdout temporalmente para silenciar prints
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        # CREAR TODAS LAS 9 SEDES DE ULEAM
        sede1 = SedeCampus(1)   # Matriz - Manta
        sede2 = SedeCampus(2)   # Chone
        sede3 = SedeCampus(3)   # El Carmen
        sede4 = SedeCampus(4)   # Pedernales
        sede5 = SedeCampus(5)   # Bahía de Caráquez
        sede6 = SedeCampus(6)   # Tosagua
        sede7 = SedeCampus(7)   # Santo Domingo
        sede8 = SedeCampus(8)   # Flavio Alfaro
        sede9 = SedeCampus(9)   # Pichincha
        
        sedes_disponibles = [sede1, sede2, sede3, sede4, sede5, sede6, sede7, sede8, sede9]
        
        # OFERTAS ACADÉMICAS (usar Manta y Chone como antes)
        oferta_ti_manta = OfertaCarrera(
            carrera_id=101,
            nombre_carrera="Tecnologias de la Informacion",
            sede_id=sede1.sede_id,
            nombre_sede=sede1.nombre_sede,
            cupos_total=40,
            nivel="TERCER NIVEL",
            modalidad="PRESENCIAL",
            jornada="MATUTINA"
        )
        
        oferta_software_manta = OfertaCarrera(
            carrera_id=102,
            nombre_carrera="Ingenieria en Software",
            sede_id=sede1.sede_id,
            nombre_sede=sede1.nombre_sede,
            cupos_total=35,
            nivel="TERCER NIVEL",
            modalidad="PRESENCIAL",
            jornada="VESPERTINA"
        )
        
        oferta_medicina_manta = OfertaCarrera(
            carrera_id=103,
            nombre_carrera="Medicina",
            sede_id=sede1.sede_id,
            nombre_sede=sede1.nombre_sede,
            cupos_total=25,
            nivel="TERCER NIVEL",
            modalidad="PRESENCIAL",
            jornada="MATUTINA"
        )
        
        oferta_admin_chone = OfertaCarrera(
            carrera_id=104,
            nombre_carrera="Administracion de Empresas",
            sede_id=sede2.sede_id,
            nombre_sede=sede2.nombre_sede,
            cupos_total=30,
            nivel="TERCER NIVEL",
            modalidad="PRESENCIAL",
            jornada="NOCTURNA"
        )
        
        ofertas_disponibles = [oferta_ti_manta, oferta_software_manta, oferta_medicina_manta, oferta_admin_chone]
        
        # REGISTROS NACIONALES
        registro1 = RegistroNacional(
            identificacion="1316202082",
            nombres="Jean Pierre",
            apellidos="Flores Piloso"
        )
        registro1.fecha_nacimiento = datetime(2002, 5, 15)
        registro1.correo = "jean.flores@example.com"
        registro1.celular = "0987654321"
        registro1.provincia_reside = "Manabi"
        registro1.canton_reside = "Manta"
        registro1.estado = "COMPLETO"
        registro1.unidad_educativa = "Colegio Nacional Manta"
        registro1.tipo_unidad_educativa = "FISCAL"
        registro1.calificacion = 9.5
        
        registro2 = RegistroNacional(
            identificacion="1350432058",
            nombres="Braddy",
            apellidos="Londre Vera"
        )
        registro2.fecha_nacimiento = datetime(2003, 8, 20)
        registro2.correo = "braddy.londre@example.com"
        registro2.celular = "0998765432"
        registro2.provincia_reside = "Manabi"
        registro2.canton_reside = "Chone"
        registro2.estado = "COMPLETO"
        registro2.unidad_educativa = "Colegio Tecnico Chone"
        registro2.tipo_unidad_educativa = "FISCAL"
        registro2.calificacion = 8.8
        
        registro3 = RegistroNacional(
            identificacion="1360234567",
            nombres="Bismark Gabriel",
            apellidos="Cevallos"
        )
        registro3.fecha_nacimiento = datetime(2002, 11, 10)
        registro3.correo = "bismark.cevallos@example.com"
        registro3.celular = "0976543210"
        registro3.provincia_reside = "Manabi"
        registro3.canton_reside = "Portoviejo"
        registro3.estado = "COMPLETO"
        registro3.unidad_educativa = "Colegio Olmedo"
        registro3.tipo_unidad_educativa = "FISCAL"
        registro3.calificacion = 9.2
        
        registros_nacionales = [registro1, registro2, registro3]
        
    finally:
        # Restaurar stdout
        sys.stdout = old_stdout

# ==================== FUNCIONES PRINCIPALES ====================

def ver_sedes():
    """Opcion 1: Ver sedes disponibles"""
    print("\n" + "="*60)
    print("SEDES ULEAM DISPONIBLES")
    print("="*60)
    
    for sede in sedes_disponibles:
        info = sede.obtener_info()
        print(f"\nSede: {info['nombre']}")
        print(f"Canton: {info['canton']}")
        print(f"Provincia: {info['provincia']}")
        print(f"Estado: {'ACTIVA' if info['activa'] else 'INACTIVA'}")
    
    print(f"\nTotal de sedes: {len(sedes_disponibles)}")

def ver_ofertas_carreras():
    """Opcion 2: Ver ofertas de carreras"""
    print("\n" + "="*60)
    print("OFERTAS ACADEMICAS - PERIODO 2025-1")
    print("="*60)
    
    for i, oferta in enumerate(ofertas_disponibles, 1):
        sede = next((s for s in sedes_disponibles if s.sede_id == oferta.sede_id), None)
        
        print(f"\n{i}. {oferta.nombre_carrera}")
        print(f"   Sede: {oferta.nombre_sede}")
        print(f"   Cupos: {oferta.cupos_total}")
        print(f"   Jornada: {oferta.jornada}")
        print(f"   Modalidad: {oferta.modalidad}")

def verificar_registro_nacional():
    """Opcion 3: Verificar registro nacional por cedula"""
    print("\n" + "="*60)
    print("VERIFICAR REGISTRO NACIONAL")
    print("="*60)
    
    cedula = input("\nIngrese numero de cedula: ").strip()
    
    registro = next((r for r in registros_nacionales if r.identificacion == cedula), None)
    
    if registro:
        print("\nREGISTRO ENCONTRADO:")
        print(f"Cedula: {registro.identificacion}")
        print(f"Nombres: {registro.nombres} {registro.apellidos}")
        print(f"Estado: {registro.estado}")
        if registro.correo:
            print(f"Email: {registro.correo}")
        if registro.celular:
            print(f"Telefono: {registro.celular}")
    else:
        print(f"\nNo se encontro registro con cedula: {cedula}")

def ver_todos_registros():
    """Opcion 4: Ver todos los registros nacionales"""
    print("\n" + "="*60)
    print("REGISTROS NACIONALES")
    print("="*60)
    
    for registro in registros_nacionales:
        print(f"\nCedula: {registro.identificacion}")
        print(f"Nombre: {registro.nombres} {registro.apellidos}")
        print(f"Estado: {registro.estado}")
        print("-" * 60)

def crear_inscripcion():
    """Opcion 5: Crear inscripcion (GENERA EVALUACION AUTOMATICAMENTE)"""
    print("\n" + "="*60)
    print("CREAR INSCRIPCION")
    print("="*60)
    
    # Solicitar cedula
    cedula = input("\nIngrese numero de cedula: ").strip()
    
    # Buscar registro
    registro = next((r for r in registros_nacionales if r.identificacion == cedula), None)
    
    if not registro:
        print(f"\nError: No existe registro nacional con cedula {cedula}")
        return
    
    if registro.estado != "COMPLETO":
        print(f"\nError: El registro debe estar COMPLETO. Estado actual: {registro.estado}")
        return
    
    print(f"\nRegistro encontrado: {registro.nombres} {registro.apellidos}")
    
    # Crear postulante con los parámetros correctos
    nombre_completo = f"{registro.nombres} {registro.apellidos}"
    
    # Buscar atributos de contacto
    email = registro.correo or "sin_correo@uleam.edu.ec"
    telefono = registro.celular or "0000000000"
    
    # Convertir fecha de nacimiento a string formato YYYY-MM-DD
    if isinstance(registro.fecha_nacimiento, datetime):
        fecha_nac_str = registro.fecha_nacimiento.strftime('%Y-%m-%d')
    else:
        fecha_nac_str = str(registro.fecha_nacimiento)
    
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
        print(f"{i}. {oferta.nombre_carrera} - {oferta.nombre_sede} ({oferta.jornada})")
    
    # Seleccionar carrera
    try:
        opcion_carrera = int(input("\nSeleccione carrera (1-4): "))
        if opcion_carrera < 1 or opcion_carrera > len(ofertas_disponibles):
            print("Opcion invalida")
            return
    except ValueError:
        print("Entrada invalida")
        return
    
    oferta_seleccionada = ofertas_disponibles[opcion_carrera - 1]
    
    # Seleccionar orden de preferencia
    try:
        orden_pref = int(input("Ingrese orden de preferencia (1-3): "))
    except ValueError:
        print("Entrada invalida")
        return
    
    # CREAR INSCRIPCION (GENERA EVALUACION AUTOMATICAMENTE)
    inscripcion = Inscripcion(
        id_postulante=postulante.id_postulante,
        carrera_id=oferta_seleccionada.carrera_id,
        orden_preferencia=orden_pref,
        sede_id=oferta_seleccionada.sede_id,
        jornada=oferta_seleccionada.jornada,
        cedula_postulante=cedula
    )
    
    inscripciones_creadas.append(inscripcion)
    
    # Guardar evaluacion creada automaticamente
    evaluacion = inscripcion.obtenerEvaluacion()
    if evaluacion:
        evaluaciones_creadas.append(evaluacion)
    
    print("\n" + "="*60)
    print("INSCRIPCION CREADA EXITOSAMENTE")
    print("="*60)
    inscripcion.mostrar_info_completa()
    
    print("\nPROXIMOS PASOS:")
    print("1. Presente su documento de identidad el dia del examen")
    print("2. Llegue 30 minutos antes de la hora programada")
    print("3. Consulte su evaluacion con la opcion 6")

def consultar_evaluacion():
    """Opcion 6: Consultar evaluacion por cedula"""
    print("\n" + "="*60)
    print("CONSULTAR EVALUACION")
    print("="*60)
    
    cedula = input("\nIngrese numero de cedula: ").strip()
    
    # Buscar inscripcion
    inscripcion = next((i for i in inscripciones_creadas if i.cedula_postulante == cedula), None)
    
    if not inscripcion:
        print(f"\nNo se encontro inscripcion con cedula: {cedula}")
        return
    
    evaluacion = inscripcion.obtenerEvaluacion()
    
    if evaluacion:
        evaluacion.mostrar_info()
    else:
        print("\nNo hay evaluacion asociada a esta inscripcion")

def consultar_asignacion():
    """Opcion 7: Consultar asignacion por cedula"""
    print("\n" + "="*60)
    print("CONSULTAR ASIGNACION")
    print("="*60)
    
    cedula = input("\nIngrese numero de cedula: ").strip()
    
    asignacion = next((a for a in asignaciones_creadas if a.cedula_postulante == cedula), None)
    
    if asignacion:
        asignacion.mostrar_info()
    else:
        print(f"\nNo se encontro asignacion con cedula: {cedula}")
        print("\n📅 Su examen aún no se ha realizado o está pendiente de calificación.")
        print("   Espere hasta la fecha programada para conocer su resultado y asignación de cupo.")
        print("   Puede revisar su fecha de examen con la opción 6 del menú.")



def consultar_puntaje():
    """Opcion 8: Consultar puntaje por cedula"""
    print("\n" + "="*60)
    print("CONSULTAR PUNTAJE DE POSTULACION")
    print("="*60)
    
    cedula = input("\nIngrese numero de cedula: ").strip()
    
    puntaje = next((p for p in puntajes_creados if p.cedula_postulante == cedula), None)
    
    if puntaje:
        puntaje.mostrar_info()
        print("\nDesea ver el desglose detallado? (s/n): ", end="")
        if input().lower() == 's':
            puntaje.mostrar_desglose()
    else:
        print(f"\nNo se encontro puntaje con cedula: {cedula}")
        print("\n📅 Su examen aún no se ha realizado o está pendiente de calificación.")
        print("   Espere hasta la fecha programada para poder consultar su puntaje final.")
        print("   Puede revisar su fecha de examen con la opción 6 del menú.")


def simular_proceso_completo():
    """Opcion 9: Simular proceso completo para demo"""
    print("\n" + "="*60)
    print("SIMULACION DE PROCESO COMPLETO")
    print("="*60)
    
    # Usar el primer registro de prueba
    registro = registros_nacionales[0]
    cedula = registro.identificacion
    
    print(f"\nSimulando proceso para: {registro.nombres} {registro.apellidos}")
    print(f"Cedula: {cedula}")
    
    # 1. Crear postulante
    nombre_completo = f"{registro.nombres} {registro.apellidos}"
    
    if isinstance(registro.fecha_nacimiento, datetime):
        fecha_nac_str = registro.fecha_nacimiento.strftime('%Y-%m-%d')
    else:
        fecha_nac_str = str(registro.fecha_nacimiento)
    
    postulante = Postulante(
        cedula=registro.identificacion,
        nombre_completo=nombre_completo,
        email=registro.correo,
        telefono=registro.celular,
        fecha_nacimiento=fecha_nac_str
    )
    postulantes_creados.append(postulante)
    print(f"\n1. Postulante creado (ID: {postulante.id_postulante})")
    
    # 2. Crear inscripcion (genera evaluacion automaticamente)
    oferta = ofertas_disponibles[0]  # Primera carrera
    inscripcion = Inscripcion(
        id_postulante=postulante.id_postulante,
        carrera_id=oferta.carrera_id,
        orden_preferencia=1,
        sede_id=oferta.sede_id,
        jornada=oferta.jornada,
        cedula_postulante=cedula
    )
    inscripciones_creadas.append(inscripcion)
    print(f"\n2. Inscripcion creada (ID: {inscripcion.id_inscripcion})")
    
    # 3. Obtener evaluacion creada automaticamente
    evaluacion = inscripcion.obtenerEvaluacion()
    evaluaciones_creadas.append(evaluacion)
    print(f"\n3. Evaluacion creada automaticamente (ID: {evaluacion.id_evaluacion})")
    
    # 4. Simular calificacion de evaluacion
    calificacion_evaluacion = 850.0  # 850/1000
    evaluacion.registrarCalificacion(calificacion_evaluacion)
    print(f"\n4. Evaluacion calificada: {calificacion_evaluacion} puntos")
    
    # 5. Calcular puntaje final
    puntaje = PuntajePostulacion(
        id_postulante=postulante.id_postulante,
        nota_grado=registro.calificacion,
        puntaje_evaluacion=calificacion_evaluacion,
        cedula_postulante=cedula,
        puntaje_meritos=100.0  # Bonus por meritos
    )
    puntajes_creados.append(puntaje)
    print(f"\n5. Puntaje calculado: {puntaje.puntaje_final}/1000")
    
    # 6. Crear asignacion
    asignacion = Asignacion(
        id_postulante=postulante.id_postulante,
        carrera_id=oferta.carrera_id,
        sede_id=oferta.sede_id,
        puntaje_final=puntaje.puntaje_final,
        cedula_postulante=cedula
    )
    asignaciones_creadas.append(asignacion)
    print(f"\n6. Asignacion creada (ID: {asignacion.id_asignacion})")
    
    # 7. Confirmar asignacion
    asignacion.confirmar()
    print(f"\n7. Asignacion confirmada")
    
    print("\n" + "="*60)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print("="*60)
    print(f"\nPuede consultar toda la informacion con la cedula: {cedula}")
    print("Use las opciones 6, 7 y 8 del menu")

# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu():
    """Muestra el menu principal"""
    print("\n" + "="*60)
    print("MENU PRINCIPAL - SISTEMA ULEAM")
    print("="*60)
    print("  1. Ver Sedes Disponibles")
    print("  2. Ver Ofertas de Carreras Reales")
    print("  3. Verificar Registro Nacional por Cedula")
    print("  4. Ver Todos los Registros Nacionales")
    print("  5. Crear Inscripcion (Genera Evaluacion Automatica)")
    print("  6. Consultar Evaluacion por Cedula")
    print("  7. Consultar Asignacion por Cedula")
    print("  8. Consultar Puntaje por Cedula")
    print("  9. Simular Proceso Completo (DEMO)")
    print("  0. Salir")
    print("="*60)

def main():
    """Funcion principal del sistema"""
    inicializar_sistema()
    
    while True:
        mostrar_menu()
        
        try:
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

            # ================================
            # OPCIONES EN MODO DEMO (NO ACTIVAS)
            # ================================
            elif opcion in ['6', '7', '8', '9']:
                print("\n⚙️  MODO DEMO ACTIVADO")
                print("   Esta opción está deshabilitada temporalmente para la versión de demostración.")
                print("   Próximamente podrá consultar evaluaciones, asignaciones y puntajes reales.")
                print("   Gracias por probar el Sistema de Admisión ULEAM 2025.")

            # ================================
            # SALIR Y MOSTRAR RESUMEN FINAL
            # ================================
            elif opcion == '0':
                print("\nGracias por usar el Sistema de Admision ULEAM")
                print("Hasta pronto!")

                print("\n" + "=" * 80)
                print("RESUMEN DE HERENCIA Y POLIMORFISMO - MODELOS ULEAM")
                print("=" * 80)

                try:
                    # Importar todos los módulos principales
                    from models.Asignacion import Asignacion, ProcesoAdmision
                    from models.Inscripcion import Inscripcion, ProcesoBase
                    from models.ofertaCarrera import OfertaCarrera, GestionCupos, InformacionSede
                    from models.PoliticaAccionAfirmativa import PoliticaAccionAfirmativa, EvaluacionSocial, SegmentacionAsignacion
                    from models.SedeCampus import SedeCampus, EntidadUniversitaria
                    from models.Evaluacion import Evaluacion
                    from models.Postulante import Postulante, Persona
                    from models.PuntajePostulacion import PuntajePostulacion
                    from models.RegistroNacional import RegistroNacional, DatosPersonales, Validable

                    # 1. CLASES ABSTRACTAS Y SUBCLASES
                    print("\n[1] CLASES ABSTRACTAS Y SUS SUBCLASES:")
                    print(" - ProcesoAdmision →", ProcesoAdmision.__subclasses__())
                    print(" - ProcesoBase →", ProcesoBase.__subclasses__())
                    print(" - GestionCupos →", GestionCupos.__subclasses__())
                    print(" - InformacionSede →", InformacionSede.__subclasses__())
                    print(" - EvaluacionSocial →", EvaluacionSocial.__subclasses__())
                    print(" - SegmentacionAsignacion →", SegmentacionAsignacion.__subclasses__())
                    print(" - EntidadUniversitaria →", EntidadUniversitaria.__subclasses__())
                    print(" - Persona →", Persona.__subclasses__())
                    print(" - Validable →", Validable.__subclasses__())

                    # 2. HERENCIA MÚLTIPLE
                    print("\n[2] CLASES CON HERENCIA MÚLTIPLE:")
                    print(" - OfertaCarrera →", OfertaCarrera.__bases__)
                    print(" - PoliticaAccionAfirmativa →", PoliticaAccionAfirmativa.__bases__)
                    print(" - RegistroNacional →", RegistroNacional.__bases__)

                    # 3. HERENCIA SIMPLE
                    print("\n[3] CLASES CON HERENCIA SIMPLE:")
                    print(" - Asignacion →", Asignacion.__bases__)
                    print(" - Inscripcion →", Inscripcion.__bases__)
                    print(" - Postulante →", Postulante.__bases__)
                    print(" - SedeCampus →", SedeCampus.__bases__)
                    print(" - PuntajePostulacion →", PuntajePostulacion.__bases__)
                    print(" - Evaluacion →", Evaluacion.__bases__)

                    # 4. POLIMORFISMO DETECTADO
                    print("\n[4] POLIMORFISMO DEMOSTRADO EN:")
                    print(" - confirmar() y mostrar_info() en Asignacion")
                    print(" - completar() y mostrar_info_completa() en Inscripcion")
                    print(" - mostrar_resumen() en OfertaCarrera")
                    print(" - calcular_segmento() en PoliticaAccionAfirmativa")
                    print(" - mostrar_info() en SedeCampus")
                    print(" - validarIdentidad() y calcularEdad() en Postulante")
                    print(" - validar_completitud() en RegistroNacional")
                    print(" - mostrar_desglose() en PuntajePostulacion")

                    # 5. TOTAL DE SUBCLASES
                    total = (
                        len(ProcesoAdmision.__subclasses__()) +
                        len(ProcesoBase.__subclasses__()) +
                        len(GestionCupos.__subclasses__()) +
                        len(InformacionSede.__subclasses__()) +
                        len(EvaluacionSocial.__subclasses__()) +
                        len(SegmentacionAsignacion.__subclasses__()) +
                        len(EntidadUniversitaria.__subclasses__()) +
                        len(Persona.__subclasses__()) +
                        len(Validable.__subclasses__())
                    )
                    print("\n[5] TOTAL DE SUBCLASES CARGADAS:")
                    print(f" → Total: {total} clases concretas detectadas")

                    print("\n" + "=" * 80)
                    print("FIN DEL RESUMEN - SISTEMA DE ADMISION ULEAM 2025")
                    print("=" * 80)

                except Exception as e:
                    print(f"\n[Error] No se pudo generar el resumen: {e}")
                break

            else:
                print("\nOpcion invalida. Intente nuevamente.")
        
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Por favor, intente nuevamente")


if __name__ == "__main__":
    main()