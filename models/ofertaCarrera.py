"""
Módulo: OfertaCarrera (ACTUALIZADO CON DATOS REALES ULEAM)
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripción:
    Gestiona las ofertas académicas de carreras con integración de herencia múltiple
    y polimorfismo aplicado a la administración de cupos y sedes ULEAM.
"""

from typing import Optional, Dict
from abc import ABC, abstractmethod


# ==============================
# CLASES BASE ABSTRACTAS
# ==============================

class GestionCupos(ABC):
    """Clase abstracta que define métodos generales para gestión de cupos."""

    @abstractmethod
    def calcularCuposDisponibles(self, segmento: Optional[str] = None) -> int:
        pass

    @abstractmethod
    def reservarCupo(self, segmento: str) -> bool:
        pass

    @abstractmethod
    def liberarCupo(self, segmento: str) -> None:
        pass


class InformacionSede(ABC):
    """Clase abstracta que modela datos básicos de una sede universitaria."""

    @abstractmethod
    def mostrar_info_sede(self) -> None:
        pass


# ==============================
# CLASE PRINCIPAL CON HERENCIA MÚLTIPLE
# ==============================

class OfertaCarrera(GestionCupos, InformacionSede):
    """
    Representa la oferta de una carrera en una sede con sus cupos.
    Aplica herencia múltiple entre la gestión de cupos y la información de sede.
    """

    _contador_ofertas = 0
    PORCENTAJE_MINIMO_CUOTAS = 0.05
    PORCENTAJE_MAXIMO_CUOTAS = 0.10

    NIVELES = ['TERCER NIVEL', 'TERCER NIVEL TECNOLÓGICO SUPERIOR']
    MODALIDADES = ['PRESENCIAL', 'HIBRIDA', 'SEMI-PRESENCIAL', 'DISTANCIA']
    JORNADAS = ['MATUTINA', 'VESPERTINA', 'NOCTURNA', 'NO APLICA JORNADA']

    def __init__(self, carrera_id: int, nombre_carrera: str, sede_id: int,
                 nombre_sede: str, cupos_total: int, nivel: str,
                 modalidad: str, jornada: str, ofa_id: int = None,
                 cus_id: int = None):
        """
        Inicializa una oferta de carrera (SENESCYT ULEAM 2025).
        """
        OfertaCarrera._contador_ofertas += 1

        self.carrera_id = carrera_id
        self.ofa_id = ofa_id or (244900 + OfertaCarrera._contador_ofertas)
        self.cus_id = cus_id or (349000 + OfertaCarrera._contador_ofertas)
        self.nombre_carrera = nombre_carrera.upper()
        self.sede_id = sede_id
        self.nombre_sede = nombre_sede

        self.nivel = nivel.upper()
        self.modalidad = modalidad.upper()
        self.jornada = jornada.upper()

        self.cupos_total = cupos_total
        self.cupos_nivelacion = 0
        self.cupos_primer_semestre = 0
        self.cupos_pc = 0
        self.tipo_cupo = 'CUPOS_NIVELACION'
        self.focalizada = 'N'

        # Segmentación de cupos
        self._calcular_distribucion_cupos()

        # Registro de cupos asignados
        self.cupos_asignados = {
            'CUOTAS': 0,
            'VULNERABILIDAD': 0,
            'MERITO_ACADEMICO': 0,
            'RECONOCIMIENTOS': 0,
            'PUEBLOS_NACIONALIDADES': 0,
            'BACHILLERES': 0,
            'GENERAL': 0
        }
        
        print(f"  Oferta creada: {nombre_carrera[:40]} ({nombre_sede})")
        print(f"   Cupos: {cupos_total} | {nivel} | {modalidad} | {jornada}")
    
    def _calcular_distribucion_cupos(self):
        """Calcula la distribución inicial de cupos."""
        self.cupos_pc = max(int(self.cupos_total * self.PORCENTAJE_MINIMO_CUOTAS), 1)
        self.cupos_nivelacion = self.cupos_total - self.cupos_pc
        
        # Distribuir por segmentos (ejemplo básico)
        cupos_restantes = self.cupos_total - self.cupos_pc
        
        self.cupos_vulnerabilidad = int(cupos_restantes * 0.20)  # 20%
        self.cupos_merito = int(cupos_restantes * 0.30)  # 30%
        self.cupos_general = cupos_restantes - self.cupos_vulnerabilidad - self.cupos_merito
    
    def mostrar_info_sede(self) -> None:
        """Implementación del método abstracto de InformacionSede."""
        print("\n--- Información de la Sede ---")
        print(f"Sede ID: {self.sede_id}")
        print(f"Nombre Sede: {self.nombre_sede}")
        print(f"Carrera: {self.nombre_carrera}")
        print(f"Nivel: {self.nivel}")
        print(f"Modalidad: {self.modalidad}")
        print(f"Jornada: {self.jornada}")
        print("-" * 40)

    def configurar_desde_pdf(self, cupos_nivelacion: int = 0,
                            cupos_primer_semestre: int = 0,
                            cupos_pc: int = 0,
                            tipo_cupo: str = 'CUPOS_NIVELACION',
                            focalizada: str = 'N'):
        """
        Configura los cupos según los datos extraídos del PDF oficial ULEAM.

        Args:
            cupos_nivelacion (int): CUS_CUPOS_NIVELACION
            cupos_primer_semestre (int): CUS_CUPOS_PRIMER_SEMESTRE
            cupos_pc (int): CUS_CUPOS_PC (política de cuotas)
            tipo_cupo (str): DESCRIPCION_TIPO_CUPO
            focalizada (str): FOCALIZADA (S/N)
        """
        self.cupos_nivelacion = cupos_nivelacion
        self.cupos_primer_semestre = cupos_primer_semestre
        self.cupos_pc = cupos_pc
        self.tipo_cupo = tipo_cupo
        self.focalizada = focalizada

        # Recalcular el total general
        self.cupos_total = cupos_nivelacion + cupos_primer_semestre + cupos_pc

        print("  Configuración desde PDF aplicada")
        print(f"   Nivelación: {cupos_nivelacion} | Primer Semestre: {cupos_primer_semestre} | PC: {cupos_pc}")


    def obtener_total_ofertas(cls) -> int:
            """Devuelve el total de ofertas registradas."""
            return cls._contador_ofertas

    @classmethod
    def crear_desde_pdf_uleam(cls, datos: dict):
            """Crea una oferta a partir de los datos del PDF ULEAM."""
            oferta = cls(
                carrera_id=datos.get('carrera_id', 0),
                nombre_carrera=datos.get('CAR_NOMBRE_CARRERA', 'SIN NOMBRE'),
                sede_id=datos.get('sede_id', 0),
                nombre_sede=datos.get('PRQ_NOMBRE', 'NO DEFINIDA'),
                cupos_total=datos.get('CUS_TOTAL_CUPOS', 0),
                nivel=datos.get('NIVEL', 'TERCER NIVEL'),
                modalidad=datos.get('MODALIDAD', 'PRESENCIAL'),
                jornada=datos.get('JORNADA', 'MATUTINA'),
                ofa_id=datos.get('OFA_ID'),
                cus_id=datos.get('CUS_ID')
            )

            oferta.configurar_desde_pdf(
                cupos_nivelacion=datos.get('CUS_CUPOS_NIVELACION', 0),
                cupos_primer_semestre=datos.get('CUS_CUPOS_PRIMER_SEMESTRE', 0),
                cupos_pc=datos.get('CUS_CUPOS_PC', 0),
                tipo_cupo=datos.get('DESCRIPCION_TIPO_CUPO', 'CUPOS_NIVELACION'),
                focalizada=datos.get('FOCALIZADA', 'N')
            )

            return oferta
    
    def calcularCuposDisponibles(self, segmento: Optional[str] = None) -> int:
        """Polimorfismo: calcula disponibilidad general o segmentada."""
        if segmento is None:
            total_asignados = sum(self.cupos_asignados.values())
            return self.cupos_total - total_asignados

        seg = segmento.upper()
        if seg not in self.cupos_asignados:
            return 0

        limites = {
            'CUOTAS': self.cupos_pc,
            'VULNERABILIDAD': self.cupos_vulnerabilidad,
            'MERITO_ACADEMICO': self.cupos_merito,
            'GENERAL': self.cupos_general
        }

        limite = limites.get(seg, self.cupos_general)
        return max(limite - self.cupos_asignados[seg], 0)

    def reservarCupo(self, segmento: str) -> bool:
        """
        Reserva un cupo en el segmento especificado.
        
        Args:
            segmento: Segmento donde reservar
            
        Returns:
            bool: True si se reservó exitosamente
        """
        segmento = segmento.upper()
        
        if segmento not in self.cupos_asignados:
            print(f" Segmento inválido: {segmento}")
            return False

        disponibles = self.calcularCuposDisponibles(segmento)
        if disponibles <= 0:
            print(f" No hay cupos disponibles en {segmento}")
            return False
        
        # Reservar cupo
        self.cupos_asignados[segmento] += 1
        
        print(f"  Cupo reservado en {segmento}")
        print(f"   Asignados: {self.cupos_asignados[segmento]} | Disponibles: {disponibles - 1}")
        
        return True

    def liberarCupo(self, segmento: str) -> None:
        """Libera un cupo previamente asignado."""
        segmento = segmento.upper()
        
        if segmento not in self.cupos_asignados:
            print(f" Segmento inválido: {segmento}")
            return
        
        if self.cupos_asignados[segmento] > 0:
            self.cupos_asignados[segmento] -= 1
            disponibles = self.calcularCuposDisponibles(segmento)
            
            print(f" Cupo liberado en {segmento}")
            print(f"   Disponibles ahora: {disponibles}")
        else:
            print(f" No hay cupos asignados en {segmento} para liberar")
    
    def obtener_estadisticas(self) -> dict:
        """Obtiene estadísticas completas de la oferta."""
        total_asignados = sum(self.cupos_asignados.values())
        total_disponibles = self.cupos_total - total_asignados
        porcentaje_ocupacion = (total_asignados / self.cupos_total * 100) if self.cupos_total > 0 else 0

        return {
            'carrera': self.nombre_carrera,
            'sede': self.nombre_sede,
            'total_cupos': self.cupos_total,
            'asignados': total_asignados,
            'disponibles': total_disponibles,
            'ocupacion_%': round(porcentaje_ocupacion, 2),
            'segmentos': self.cupos_asignados.copy()
        }

    def mostrar_resumen(self) -> None:
        """Polimorfismo aplicado: muestra resumen según estado de ocupación."""
        info = self.obtener_estadisticas()
        print("\n" + "=" * 60)
        print(f"OFERTA: {info['carrera']} - {info['sede']}")
        print("=" * 60)
        print(f"Cupos Totales: {info['total_cupos']}")
        print(f"Cupos Asignados: {info['asignados']}")
        print(f"Cupos Disponibles: {info['disponibles']}")
        print(f"Ocupación: {info['ocupacion_%']}%")
        print("-" * 60)
        for s, c in info['segmentos'].items():
            print(f"{s:<25}: {c}")
        print("=" * 60)

    def __str__(self) -> str:
        """Representación legible de la oferta."""
        return f"OfertaCarrera({self.nombre_carrera}, {self.nombre_sede}, Cupos={self.cupos_total})"

    @classmethod
    def obtener_total_ofertas(cls) -> int:
        """Devuelve el total de ofertas registradas."""
        return cls._contador_ofertas


# ========== EJEMPLO DE USO CON DATOS REALES ULEAM ==========
if __name__ == "__main__":
    print("=" * 70)
    print("PRUEBA: OFERTAS REALES - UNIVERSIDAD ULEAM 2025")
    print("=" * 70)
    
    # Ejemplo 1: Tecnologías de la Información (datos reales del PDF)
    print("\n OFERTA 1: Tecnologías de la Información - Manta")
    print("-" * 70)
    
    datos_ti = {
        'carrera_id': 101,
        'CAR_NOMBRE_CARRERA': 'TECNOLOGIAS DE LA INFORMACION',
        'PRQ_NOMBRE': 'MANTA',
        'sede_id': 1,
        'NIVEL': 'TERCER NIVEL',
        'MODALIDAD': 'PRESENCIAL',
        'JORNADA': 'MATUTINA',
        'CUS_TOTAL_CUPOS': 40,
        'CUS_CUPOS_NIVELACION': 38,
        'CUS_CUPOS_PRIMER_SEMESTRE': 0,
        'CUS_CUPOS_PC': 2,
        'OFA_ID': 245912,
        'CUS_ID': 350708,
        'FOCALIZADA': 'N',
        'DESCRIPCION_TIPO_CUPO': 'CUPOS_NIVELACIÓN'
    }
    
    oferta_ti = OfertaCarrera.crear_desde_pdf_uleam(datos_ti)
    oferta_ti.mostrar_resumen()
    
    # Simular asignaciones
    print(" Simulando asignaciones...")
    oferta_ti.reservarCupo("MERITO_ACADEMICO")
    oferta_ti.reservarCupo("VULNERABILIDAD")
    oferta_ti.reservarCupo("GENERAL")
    
    oferta_ti.mostrar_resumen()
    
    # Ejemplo 2: Medicina (datos reales)
    print("\n OFERTA 2: Medicina - Manta")
    print("-" * 70)
    
    datos_medicina = {
        'carrera_id': 102,
        'CAR_NOMBRE_CARRERA': 'MEDICINA',
        'PRQ_NOMBRE': 'MANTA',
        'sede_id': 1,
        'NIVEL': 'TERCER NIVEL',
        'MODALIDAD': 'PRESENCIAL',
        'JORNADA': 'MATUTINA',
        'CUS_TOTAL_CUPOS': 70,
        'CUS_CUPOS_NIVELACION': 63,
        'CUS_CUPOS_PRIMER_SEMESTRE': 0,
        'CUS_CUPOS_PC': 7,
        'OFA_ID': 249494,
        'CUS_ID': 349824,
        'FOCALIZADA': 'N'
    }
    
    oferta_medicina = OfertaCarrera.crear_desde_pdf_uleam(datos_medicina)
    print(f"\n{oferta_medicina}")
    
    print(f"\n Total ofertas creadas: {OfertaCarrera.obtener_total_ofertas()}")
    print("\n" + "=" * 70)
