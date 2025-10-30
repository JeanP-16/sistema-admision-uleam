"""
Módulo: PoliticaAccionAfirmativa (PAA)
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripción:
    Gestiona las Políticas de Acción Afirmativa (PAA) según SENESCYT 2025.
    Incluye herencia múltiple, abstracción y polimorfismo.
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict


# ==============================
# CLASES BASE ABSTRACTAS
# ==============================

class EvaluacionSocial(ABC):
    """Clase abstracta base para representar condiciones sociales de los postulantes."""

    @abstractmethod
    def aplicar_condicion_socioeconomica(self, quintil: int):
        pass

    @abstractmethod
    def aplicar_ruralidad(self, tipo_institucion: str, zona: str):
        pass

    @abstractmethod
    def aplicar_discapacidad(self, porcentaje: int, tiene_carnet: bool):
        pass


class SegmentacionAsignacion(ABC):
    """Clase abstracta base que define el cálculo de segmento y priorización."""

    @abstractmethod
    def calcular_segmento(self) -> str:
        pass

    @abstractmethod
    def obtener_resumen(self) -> Dict:
        pass


# ==============================
# CLASE PRINCIPAL CON HERENCIA MÚLTIPLE
# ==============================

class PoliticaAccionAfirmativa(EvaluacionSocial, SegmentacionAsignacion):
    """
    Clase principal que combina EvaluacionSocial + SegmentacionAsignacion.
    Gestiona las Políticas de Acción Afirmativa (PAA) con base en la normativa SENESCYT 2025.
    """

    _contador = 0

    ORDEN_SEGMENTOS = [
        'CUOTAS',
        'VULNERABILIDAD',
        'MERITO_ACADEMICO',
        'RECONOCIMIENTOS',
        'PUEBLOS_NACIONALIDADES',
        'BACHILLERES',
        'GENERAL'
    ]

    def __init__(self, id_postulante: int, identificacion: str):
        PoliticaAccionAfirmativa._contador += 1
        self.id_postulante = id_postulante
        self.identificacion = identificacion

        # Marcaciones iniciales
        self.cupo_aceptado_historico_pc = 'NO'
        self.cupo_historico_activo = 'NO'
        self.numero_cupos_activos = 0

        # Condiciones sociales
        self.condicion_socioeconomica = 'NO'
        self.ruralidad = 'NO'
        self.discapacidad = 'NO'
        self.pueblos_nacionalidades = 'NO'
        self.victima_violencia = 'NO'
        self.migrantes_retornados = 'NO'
        self.merito_academico = 'NO'
        self.vulnerabilidad_socioeconomica = 'NO'
        self.bachiller_pueblos_nacionalidad = 'NO'
        self.bachiller_periodo_academico = 'NO'
        self.poblacion_general = 'SI'

        # Segmento asignado
        self.segmento_asignado = None
        self.prioridad_segmento = 99  # Menor número = mayor prioridad
        
        print(f" PAA creada para postulante ID: {id_postulante}")
    
    def marcar_cupo_historico(self, tiene_cupo: bool, activo: bool = False):
        """Marca si tiene cupo aceptado histórico."""
        self.cupo_aceptado_historico_pc = 'SI' if tiene_cupo else 'NO'
        self.cupo_historico_activo = 'SI' if activo else 'NO'
        if activo:
            self.numero_cupos_activos += 1
        print(f" Cupo histórico: {self.cupo_aceptado_historico_pc}")
    
    def aplicar_condicion_socioeconomica(self, quintil: int):
        """Aplica condición socioeconómica según Registro Social."""
        if quintil <= 2:
            self.condicion_socioeconomica = 'SI'
            if quintil == 1:
                self.vulnerabilidad_socioeconomica = 'SI'
                print(f" Vulnerabilidad socioeconómica detectada (Quintil {quintil})")
        
        print(f" Condición socioeconómica: Quintil {quintil}")
    
    def aplicar_ruralidad(self, tipo_institucion: str, zona: str):
        """Aplica si estudió en zona rural."""
        if tipo_institucion.upper() == 'FISCAL' and zona.upper() == 'RURAL':
            self.ruralidad = 'SI'
            print(f" Ruralidad aplicada")
    
    def aplicar_discapacidad(self, porcentaje: int, tiene_carnet: bool):
        """Aplica si tiene discapacidad ≥ 30%."""
        if tiene_carnet and porcentaje >= 30:
            self.discapacidad = 'SI'
            print(f" Discapacidad aplicada: {porcentaje}%")
    
    def aplicar_pueblos_nacionalidades(self, autoidentificacion: str):
        """Aplica si pertenece a pueblos o nacionalidades reconocidos."""
        grupos = ['INDIGENA', 'AFROECUATORIANO', 'MONTUBIO']
        if autoidentificacion.upper() in grupos:
            self.pueblos_nacionalidades = 'SI'
            print(f" Pueblos y nacionalidades: {autoidentificacion}")
    
    def aplicar_merito_academico(self, cuadro_honor: str, distincion: str = None):
        """Aplica si fue abanderado o escolta."""
        if cuadro_honor == 'SI':
            DISTINCIONES_MERITO = [
                'ABANDERADO PABELLON NACIONAL',
                'PORTA ESTANDARTE PLANTEL',
                '1er. ESCOLTA PABELLON NACIONAL'
            ]
            if distincion and distincion in distincion:
                self.merito_academico = 'SI'
                print(f" Mérito académico: {distincion}")
    
    def aplicar_bachiller_ultimo_anio(self, es_bachiller: bool, 
                                     pertenece_pueblos: bool = False):
        """Aplica si está cursando último año de bachillerato."""
        if es_bachiller:
            self.bachiller_periodo_academico = 'SI'
            if pertenece_pueblos:
                self.bachiller_pueblos_nacionalidad = 'SI'
                print(f" Bachiller de pueblos y nacionalidades")
            else:
                print(f" Bachiller último año")
    
    def calcular_segmento(self) -> str:
        """Determina el segmento de asignación según orden SENESCYT."""
        # 1. CUOTAS
        if any([self.condicion_socioeconomica == 'SI',
                self.ruralidad == 'SI',
                self.discapacidad == 'SI',
                self.pueblos_nacionalidades == 'SI',
                self.victima_violencia == 'SI',
                self.migrantes_retornados == 'SI'
            ]):
            
            self.segmento_asignado = 'CUOTAS'
            self.prioridad_segmento = 1
            print(f" Segmento: CUOTAS (Prioridad 1)")
            return self.segmento_asignado
        
        # 2. VULNERABILIDAD SOCIOECONÓMICA
        if self.vulnerabilidad_socioeconomica == 'SI':
            self.segmento_asignado = 'VULNERABILIDAD'
            self.prioridad_segmento = 2
            print(f" Segmento: VULNERABILIDAD (Prioridad 2)")
            return self.segmento_asignado
        
        # 3. MÉRITO ACADÉMICO
        if self.merito_academico == 'SI':
            self.segmento_asignado = 'MERITO_ACADEMICO'
            self.prioridad_segmento = 3
            print(f" Segmento: MÉRITO ACADÉMICO (Prioridad 3)")
            return self.segmento_asignado
        
        # 5. PUEBLOS Y NACIONALIDADES (bachilleres)
        if self.bachiller_pueblos_nacionalidad == 'SI':
            self.segmento_asignado = 'PUEBLOS_NACIONALIDADES'
            self.prioridad_segmento = 5
            print(f" Segmento: PUEBLOS Y NACIONALIDADES (Prioridad 5)")
            return self.segmento_asignado
        
        # 6. BACHILLERES ÚLTIMO AÑO
        if self.bachiller_periodo_academico == 'SI':
            self.segmento_asignado = 'BACHILLERES'
            self.prioridad_segmento = 6
            print(f" Segmento: BACHILLERES (Prioridad 6)")
            return self.segmento_asignado
        
        # 7. POBLACIÓN GENERAL
        self.segmento_asignado = 'GENERAL'
        self.prioridad_segmento = 7
        print(f" Segmento: POBLACIÓN GENERAL (Prioridad 7)")
        return self.segmento_asignado
    
    def obtener_resumen(self) -> dict:
        """Obtiene resumen de PAA y segmento."""
        return {
            'id_postulante': self.id_postulante,
            'segmento': self.segmento_asignado,
            'prioridad': self.prioridad_segmento,
            'vulnerabilidad': self.vulnerabilidad_socioeconomica,
            'merito': self.merito_academico,
            'pueblos': self.pueblos_nacionalidades,
            'discapacidad': self.discapacidad,
            'ruralidad': self.ruralidad
        }

    def __str__(self) -> str:
        """Representación legible de la PAA."""
        return f"PAA(Postulante:{self.id_postulante}, Segmento:{self.segmento_asignado}, Prioridad:{self.prioridad_segmento})"

    @classmethod
    def obtener_total(cls) -> int:
        """Total de PAA creadas."""
        return cls._contador


# ========== EJEMPLO DE USO ==========
if __name__ == "__main__":
    print("=" * 70)
    print("PRUEBA: POLÍTICA DE ACCIÓN AFIRMATIVA - SISTEMA ULEAM")
    print("=" * 70)
    
    # CASO 1: Estudiante con mérito académico
    print("\n CASO 1: Estudiante con mérito académico")
    print("-" * 70)
    
    paa1 = PoliticaAccionAfirmativa(
        id_postulante=1,
        identificacion="1316202082"
    )
    
    paa1.aplicar_merito_academico(
        cuadro_honor='SI',
        distincion='ABANDERADO PABELLON NACIONAL'
    )
    
    paa1.calcular_segmento()
    print(f"\nResumen: {paa1.obtener_resumen()}")
    
    # CASO 2: Estudiante con vulnerabilidad
    print("\n\n CASO 2: Estudiante con vulnerabilidad socioeconómica")
    print("-" * 70)
    
    paa2 = PoliticaAccionAfirmativa(
        id_postulante=2,
        identificacion="1350123456"
    )
    
    paa2.aplicar_condicion_socioeconomica(quintil=1)  # Pobreza extrema
    paa2.aplicar_ruralidad(tipo_institucion='FISCAL', zona='RURAL')
    paa2.aplicar_pueblos_nacionalidades('MONTUBIO')
    
    paa2.calcular_segmento()
    print(f"\nResumen: {paa2.obtener_resumen()}")
    
    # CASO 3: Población general
    print("\n\n👥 CASO 3: Población general")
    print("-" * 70)
    
    paa3 = PoliticaAccionAfirmativa(
        id_postulante=3,
        identificacion="1360234567"
    )
    
    paa3.calcular_segmento()
    print(f"\nResumen: {paa3.obtener_resumen()}")
    
    print(f"\n Total PAA creadas: {PoliticaAccionAfirmativa.obtener_total()}")
    print("\n" + "=" * 70)
