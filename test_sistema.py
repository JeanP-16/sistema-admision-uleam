"""
Test Sistema Completo
Prueba de integración de todos los módulos
Autor: Jean Pierre Flores Piloso
Fecha: Octubre 2025
"""

import sys
from datetime import datetime, timedelta

# Importar módulos
from models.Postulante import Postulante
from models.SedeCampus import SedeCampus
from models.ofertaCarrera import OfertaCarrera
from models.RegistroNacional import RegistroNacional
from models.Inscripcion import Inscripcion
from models.Evaluacion import Evaluacion
from models.Asignacion import Asignacion
from models.PuntajePostulacion import PuntajePostulacion

def test_completo():
    """Ejecuta prueba completa del sistema"""
    
    print("=" * 70)
    print("TEST COMPLETO - SISTEMA DE ADMISION ULEAM")
    print("=" * 70)
    
    # 1. CREAR SEDES
    print("\n1️⃣ CREANDO SEDES...")
    sede_manta = SedeCampus(1)
    sede_chone = SedeCampus(2)
    print("✅ Sedes creadas")
    
    # 2. CREAR OFERTAS
    print("\n2️⃣ CREANDO OFERTAS...")
    oferta_ti = OfertaCarrera(
        carrera_id=101,
        nombre_carrera="Tecnologias de la Informacion",
        sede_id=sede_manta.sede_id,
        nombre_sede=sede_manta.nombre_sede,
        cupos_total=40,
        nivel="TERCER NIVEL",
        modalidad="PRESENCIAL",
        jornada="MATUTINA"
    )
    print("✅ Ofertas creadas")
    
    # 3. CREAR REGISTRO NACIONAL
    print("\n3️⃣ CREANDO REGISTRO NACIONAL...")
    registro = RegistroNacional(
        identificacion="1316202082",
        nombres="Jean Pierre",
        apellidos="Flores Piloso"
    )
    registro.fecha_nacimiento = datetime(2002, 5, 15)
    registro.correo = "jean.flores@uleam.edu.ec"
    registro.celular = "0987654321"
    registro.provincia_reside = "Manabi"
    registro.canton_reside = "Manta"
    registro.estado = "COMPLETO"
    registro.calificacion = 9.5
    print("✅ Registro Nacional creado")
    
    # 4. CREAR POSTULANTE
    print("\n4️⃣ CREANDO POSTULANTE...")
    postulante = Postulante(
        cedula="1316202082",
        nombre_completo="Jean Pierre Flores Piloso",
        email="jean.flores@uleam.edu.ec",
        telefono="0987654321",
        fecha_nacimiento="2002-05-15"
    )
    print("✅ Postulante creado")
    
    # 5. CREAR INSCRIPCION (crea evaluacion automatica)
    print("\n5️⃣ CREANDO INSCRIPCION...")
    inscripcion = Inscripcion(
        id_postulante=postulante.id_postulante,
        carrera_id=oferta_ti.carrera_id,
        orden_preferencia=1,
        sede_id=sede_manta.sede_id,
        jornada="MATUTINA",
        cedula_postulante="1316202082"
    )
    print("✅ Inscripcion creada")
    
    # 6. OBTENER Y CALIFICAR EVALUACION
    print("\n6️⃣ CALIFICANDO EVALUACION...")
    evaluacion = inscripcion.obtenerEvaluacion()
    evaluacion.registrarCalificacion(850.0)
    print("✅ Evaluacion calificada: 850/1000")
    
    # 7. CALCULAR PUNTAJE
    print("\n7️⃣ CALCULANDO PUNTAJE...")
    puntaje = PuntajePostulacion(
        id_postulante=postulante.id_postulante,
        nota_grado=registro.calificacion,
        puntaje_evaluacion=850.0,
        cedula_postulante="1316202082",
        puntaje_meritos=50.0
    )
    print(f"✅ Puntaje calculado: {puntaje.puntaje_final}/1000")
    
    # 8. CREAR ASIGNACION
    print("\n8️⃣ CREANDO ASIGNACION...")
    asignacion = Asignacion(
        id_postulante=postulante.id_postulante,
        carrera_id=oferta_ti.carrera_id,
        sede_id=sede_manta.sede_id,
        puntaje_final=puntaje.puntaje_final,
        cedula_postulante="1316202082"
    )
    asignacion.confirmar()
    print("✅ Asignacion confirmada")
    
    # RESUMEN FINAL
    print("\n" + "=" * 70)
    print("✅ TEST COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print(f"Postulante: {postulante.nombre_completo}")
    print(f"Carrera: Tecnologias de la Informacion")
    print(f"Puntaje: {puntaje.puntaje_final}/1000")
    print(f"Estado: {asignacion.estado}")
    print("=" * 70)

if __name__ == "__main__":
    try:
        test_completo()
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()