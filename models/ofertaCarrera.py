"""
Módulo: OfertaCarrera (ACTUALIZADO CON DATOS REALES ULEAM)
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripción: Gestiona ofertas de carreras con datos reales de ULEAM
Basado en: 102_ULEAM_OFERTASEGMENTADA_IIPA-2025.pdf
"""

from typing import Optional, List


class OfertaCarrera:
    """
    Representa la oferta de una carrera en una sede con sus cupos.
    ACTUALIZADO con datos reales de ULEAM según SENESCYT 2025.
    
    Datos del PDF:
    - IES_ID: 102 (ULEAM)
    - Sedes: Manta, Chone, El Carmen, etc.
    - Cupos segmentados por tipo
    - Modalidades y jornadas oficiales
    
    Attributes:
        carrera_id:             ID único de la carrera
        ofa_id:                 ID de oferta SENESCYT
        cus_id:                 ID de cupo SENESCYT
        nombre_carrera:         Nombre oficial
        sede_id:                ID de la sede
        nombre_sede:            Nombre de la sede
        nivel:                  TERCER NIVEL / TECNOLÓGICO SUPERIOR
        modalidad:              PRESENCIAL / HIBRIDA / SEMI-PRESENCIAL
        jornada:                MATUTINA / VESPERTINA / NOCTURNA
        cupos_total:            Total de cupos disponibles
        cupos_nivelacion:       Cupos para nivelación
        cupos_primer_semestre:  Cupos primer semestre
        cupos_pc:               Cupos política de cuotas
        tipo_cupo:              CUPOS_NIVELACION / CUPOS_PRIMER_SEMESTRE
        focalizada:             Si es carrera focalizada
    """
    
    # Contador
    _contador_ofertas = 0
    
    # Constantes SENESCYT
    PORCENTAJE_MINIMO_CUOTAS = 0.05  # 5%
    PORCENTAJE_MAXIMO_CUOTAS = 0.10  # 10%
    
    # Niveles oficiales
    NIVELES = ['TERCER NIVEL', 'TERCER NIVEL TECNOLÓGICO SUPERIOR']
    
    # Modalidades oficiales
    MODALIDADES = ['PRESENCIAL', 'HIBRIDA', 'SEMI-PRESENCIAL', 'DISTANCIA']
    
    # Jornadas oficiales
    JORNADAS = ['MATUTINA', 'VESPERTINA', 'NOCTURNA', 'NO APLICA JORNADA']
    
    def __init__(self, carrera_id: int, nombre_carrera: str, sede_id: int,
                 nombre_sede: str, cupos_total: int, nivel: str, 
                 modalidad: str, jornada: str, ofa_id: int = None, 
                 cus_id: int = None):
        """
        Inicializa una oferta de carrera.
        
        Args:
            carrera_id:             ID de la carrera
            nombre_carrera:         Nombre de la carrera
            sede_id:                ID de la sede
            nombre_sede:            Nombre de la sede
            cupos_total:            Total de cupos
            nivel:                  Nivel académico
            modalidad:              Modalidad de estudio
            jornada:                Jornada académica
            ofa_id:                 ID oferta SENESCYT (opcional)
            cus_id:                 ID cupo SENESCYT (opcional)
        """
        OfertaCarrera._contador_ofertas += 1
        
        # IDs y datos básicos
        self.carrera_id = carrera_id
        self.ofa_id = ofa_id or (244900 + OfertaCarrera._contador_ofertas)
        self.cus_id = cus_id or (349000 + OfertaCarrera._contador_ofertas)
        self.nombre_carrera = nombre_carrera.upper()
        self.sede_id = sede_id
        self.nombre_sede = nombre_sede
        
        # Características académicas
        self.nivel = nivel.upper()
        self.modalidad = modalidad.upper()
        self.jornada = jornada.upper()
        
        # Cupos (según PDF ULEAM)
        self.cupos_total = cupos_total
        self.cupos_nivelacion = 0
        self.cupos_primer_semestre = 0
        self.cupos_pc = 0  # Política de cuotas
        self.tipo_cupo = 'CUPOS_NIVELACION'  # Por defecto
        self.focalizada = 'N'  # N = No focalizada
        
        # Distribución de cupos por segmento
        self._calcular_distribucion_cupos()
        
        # Control de cupos asignados por segmento
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
        """Calcula la distribución de cupos según normativa."""
        # Política de cuotas: 5-10% obligatorio
        self.cupos_pc = max(int(self.cupos_total * 0.05), 1)
        
        # Por defecto, el resto va a nivelación
        self.cupos_nivelacion = self.cupos_total - self.cupos_pc
        
        # Distribuir por segmentos (ejemplo básico)
        cupos_restantes = self.cupos_total - self.cupos_pc
        
        self.cupos_vulnerabilidad = int(cupos_restantes * 0.20)  # 20%
        self.cupos_merito = int(cupos_restantes * 0.30)  # 30%
        self.cupos_general = cupos_restantes - self.cupos_vulnerabilidad - self.cupos_merito
    
    def configurar_desde_pdf(self, cupos_nivelacion: int = 0,
                            cupos_primer_semestre: int = 0,
                            cupos_pc: int = 0,
                            tipo_cupo: str = 'CUPOS_NIVELACION',
                            focalizada: str = 'N'):
        """
        Configura cupos según datos del PDF oficial.
        
        Args:
            cupos_nivelacion: CUS_CUPOS_NIVELACION
            cupos_primer_semestre: CUS_CUPOS_PRIMER_SEMESTRE
            cupos_pc: CUS_CUPOS_PC (política de cuotas)
            tipo_cupo: DESCRIPCION_TIPO_CUPO
            focalizada: FOCALIZADA (S/N)
        """
        self.cupos_nivelacion = cupos_nivelacion
        self.cupos_primer_semestre = cupos_primer_semestre
        self.cupos_pc = cupos_pc
        self.tipo_cupo = tipo_cupo
        self.focalizada = focalizada
        
        # Recalcular total
        self.cupos_total = cupos_nivelacion + cupos_primer_semestre + cupos_pc
        
        print(f"  Configuración desde PDF aplicada")
        print(f"   Nivelación: {cupos_nivelacion} | Primer Semestre: {cupos_primer_semestre} | PC: {cupos_pc}")
    
    def calcularCuposDisponibles(self, segmento: Optional[str] = None) -> int:
        """
        Calcula los cupos disponibles.
        
        Args:
            segmento: Segmento específico (opcional)
            
        Returns:
            int: Cupos disponibles
        """
        if segmento is None:
            # Cupos totales disponibles
            total_asignados = sum(self.cupos_asignados.values())
            return self.cupos_total - total_asignados
        
        # Cupos disponibles por segmento
        segmento = segmento.upper()
        
        if segmento == 'CUOTAS':
            return self.cupos_pc - self.cupos_asignados['CUOTAS']
        elif segmento == 'VULNERABILIDAD':
            return self.cupos_vulnerabilidad - self.cupos_asignados['VULNERABILIDAD']
        elif segmento == 'MERITO_ACADEMICO':
            return self.cupos_merito - self.cupos_asignados['MERITO_ACADEMICO']
        elif segmento == 'GENERAL':
            return self.cupos_general - self.cupos_asignados['GENERAL']
        else:
            # Otros segmentos usan cupos generales
            cupos_otros = (self.cupos_asignados['RECONOCIMIENTOS'] + 
                          self.cupos_asignados['PUEBLOS_NACIONALIDADES'] + 
                          self.cupos_asignados['BACHILLERES'])
            return self.cupos_general - cupos_otros - self.cupos_asignados['GENERAL']
    
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
        
        # Verificar disponibilidad
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
        porcentaje_ocupacion = (total_asignados / self.cupos_total) * 100 if self.cupos_total > 0 else 0
        
        return {
            'ofa_id': self.ofa_id,
            'cus_id': self.cus_id,
            'carrera': self.nombre_carrera,
            'sede': self.nombre_sede,
            'nivel': self.nivel,
            'modalidad': self.modalidad,
            'jornada': self.jornada,
            'cupos_total': self.cupos_total,
            'cupos_asignados': total_asignados,
            'cupos_disponibles': total_disponibles,
            'porcentaje_ocupacion': round(porcentaje_ocupacion, 2),
            'por_segmento': self.cupos_asignados.copy(),
            'focalizada': self.focalizada
        }
    
    def mostrar_resumen(self) -> None:
        """Muestra un resumen visual de la oferta."""
        stats = self.obtener_estadisticas()
        
        print(f"\n╔═══════════════════════════════════════════════════════════╗")
        print(f"║  OFERTA: {self.nombre_carrera[:48]:<48} ║")
        print(f"╠═══════════════════════════════════════════════════════════╣")
        print(f"║ Sede: {self.nombre_sede:<52} ║")
        print(f"║ Nivel: {self.nivel:<51} ║")
        print(f"║ Modalidad: {self.modalidad:<47} ║")
        print(f"║ Jornada: {self.jornada:<49} ║")
        print(f"║ OFA_ID: {self.ofa_id:<50} ║")
        print(f"║ CUS_ID: {self.cus_id:<50} ║")
        print(f"╠═══════════════════════════════════════════════════════════╣")
        print(f"║ Total Cupos: {self.cupos_total:<45} ║")
        print(f"║ Asignados: {stats['cupos_asignados']:<47} ║")
        print(f"║ Disponibles: {stats['cupos_disponibles']:<45} ║")
        print(f"║ Ocupación: {stats['porcentaje_ocupacion']:.1f}%{' '*45} ║")
        print(f"╠═══════════════════════════════════════════════════════════╣")
        print(f"║ Por Segmento:                                             ║")
        for seg, cant in stats['por_segmento'].items():
            print(f"║   {seg:<26} {cant:<29} ║")
        print(f"╚═══════════════════════════════════════════════════════════╝\n")
    
    def __str__(self) -> str:
        """Representación en string."""
        return (f"OfertaCarrera(ID: {self.carrera_id}, "
                f"{self.nombre_carrera}, {self.nombre_sede}, "
                f"Cupos: {self.cupos_total})")
    
    @classmethod
    def crear_desde_pdf_uleam(cls, datos_pdf: dict):
        """
        Crea una oferta desde los datos del PDF oficial de ULEAM.
        
        Args:
            datos_pdf: Diccionario con los datos del PDF
                - CAR_NOMBRE_CARRERA
                - PRQ_NOMBRE (sede)
                - NIVEL
                - MODALIDAD
                - JORNADA
                - CUS_TOTAL_CUPOS
                - CUS_CUPOS_NIVELACION
                - CUS_CUPOS_PRIMER_SEMESTRE
                - CUS_CUPOS_PC
                - OFA_ID
                - CUS_ID
                - FOCALIZADA
        
        Returns:
            OfertaCarrera: Instancia creada
        """
        oferta = cls(
            carrera_id=datos_pdf.get('carrera_id', 0),
            nombre_carrera=datos_pdf['CAR_NOMBRE_CARRERA'],
            sede_id=datos_pdf.get('sede_id', 1),
            nombre_sede=datos_pdf['PRQ_NOMBRE'],
            cupos_total=datos_pdf['CUS_TOTAL_CUPOS'],
            nivel=datos_pdf['NIVEL'],
            modalidad=datos_pdf['MODALIDAD'],
            jornada=datos_pdf['JORNADA'],
            ofa_id=datos_pdf.get('OFA_ID'),
            cus_id=datos_pdf.get('CUS_ID')
        )
        
        # Configurar cupos específicos
        oferta.configurar_desde_pdf(
            cupos_nivelacion=datos_pdf.get('CUS_CUPOS_NIVELACION', 0),
            cupos_primer_semestre=datos_pdf.get('CUS_CUPOS_PRIMER_SEMESTRE', 0),
            cupos_pc=datos_pdf.get('CUS_CUPOS_PC', 0),
            tipo_cupo=datos_pdf.get('DESCRIPCION_TIPO_CUPO', 'CUPOS_NIVELACION'),
            focalizada=datos_pdf.get('FOCALIZADA', 'N')
        )
        
        return oferta
    
    @classmethod
    def obtener_total_ofertas(cls) -> int:
        """Obtiene el total de ofertas creadas."""
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
