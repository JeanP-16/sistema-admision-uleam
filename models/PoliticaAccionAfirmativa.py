"""
Módulo: PoliticaAccionAfirmativa (PAA)
Autor: Jean Pierre Flores Piloso - Equipo 3ro TI "C"
Fecha: Octubre 2025
Descripción: Gestiona las Políticas de Acción Afirmativa según SENESCYT
Basado en: cgtic-ddpti-2025-m-002 (Servicio Web PAA y Orden de Asignación)
"""

from typing import Optional


class PoliticaAccionAfirmativa:
    """
    Gestiona las Políticas de Acción Afirmativa (PAA) y Orden de Asignación.
    
    Según SENESCYT 2025:
    - Marcaciones de Estado (ME)
    - Políticas de Acción Afirmativa (PAA)
    - Orden de Asignación (OA)
    
    Attributes:
        Marcaciones de Estado
        Políticas de Acción Afirmativa
        Orden de Asignación
        Segmento asignado
    """
    
    # Contador
    _contador = 0
    
    # === ORDEN OBLIGATORIO DE SEGMENTOS (Art. SENESCYT) ===
    ORDEN_SEGMENTOS = [
        'CUOTAS',                      # 1. Política de cuotas (5-10%)
        'VULNERABILIDAD',              # 2. Mayor vulnerabilidad socioeconómica
        'MERITO_ACADEMICO',            # 3. Mérito académico (abanderados/escoltas)
        'RECONOCIMIENTOS',             # 4. Otros reconocimientos
        'PUEBLOS_NACIONALIDADES',      # 5. Pueblos y nacionalidades
        'BACHILLERES',                 # 6. Bachilleres último régimen
        'GENERAL'                      # 7. Población general
    ]
    
    def __init__(self, id_postulante: int, identificacion: str):
        """
        Inicializa las políticas para un postulante.
        
        Args:
            id_postulante: ID del postulante
            identificacion: Cédula del postulante
        """
        PoliticaAccionAfirmativa._contador += 1
        
        self.id_postulante = id_postulante
        self.identificacion = identificacion
        
        # === MARCACIONES DE ESTADO (ME) ===
        self.cupo_aceptado_historico_pc = 'NO'
        self.anulacion_matricula_niv_carr = 'NO'
        self.periodo_sancion = None
        self.cupo_historico_activo = 'NO'
        self.numero_cupos_activos = 0
        self.cupo_pendiente_registro = 'NO'
        self.aspirante_focalizado = 'NO'
        self.tiene_puntaje_eval_4_periodos = 'NO'
        self.puntaje_mayor_eval = 0
        self.bachiller_artes = 'NO'
        
        # === POLÍTICAS DE ACCIÓN AFIRMATIVA (PAA) ===
        self.condicion_socioeconomica = 'NO'         # Pobreza (Registro Social)
        self.ruralidad = 'NO'                        # Estudió en zona rural
        self.territorialidad = 'NO'                  # Parroquia con índice de pobreza
        self.discapacidad = 'NO'                     # Discapacidad >= 30%
        self.bono_jgl = 'NO'                         # Bono Joaquín Gallegos Lara
        self.victima_violencia = 'NO'                # Víctima violencia sexual/género
        self.migrantes_retornados = 'NO'             # Migrante/retornado
        self.femicidio = 'NO'                        # Víctima femicidio
        self.enfermedades_catastroficas = 'NO'       # Enfermedades catastróficas
        self.casa_acogida = 'NO'                     # Ex casa de acogida
        self.pueblos_nacionalidades = 'NO'           # Pueblos y nacionalidades
        
        # === ORDEN DE ASIGNACIÓN (OA) ===
        self.vulnerabilidad_socioeconomica = 'NO'    # Pobreza extrema
        self.merito_academico = 'NO'                 # Abanderado/escolta
        self.bachiller_pueblos_nacionalidad = 'NO'   # Bachiller de pueblos
        self.bachiller_periodo_academico = 'NO'      # Bachiller último año
        self.poblacion_general = 'SI'                # Todos califican aquí
        
        # === SEGMENTO ASIGNADO ===
        self.segmento_asignado = None
        self.prioridad_segmento = 99  # Menor número = mayor prioridad
        
        print(f"✅ PAA creada para postulante ID: {id_postulante}")
    
    def marcar_cupo_historico(self, tiene_cupo: bool, activo: bool = False):
        """Marca si tiene cupo aceptado histórico."""
        self.cupo_aceptado_historico_pc = 'SI' if tiene_cupo else 'NO'
        self.cupo_historico_activo = 'SI' if activo else 'NO'
        if activo:
            self.numero_cupos_activos += 1
        print(f"📋 Cupo histórico: {self.cupo_aceptado_historico_pc}")
    
    def aplicar_condicion_socioeconomica(self, quintil: int):
        """
        Aplica condición socioeconómica según Registro Social.
        
        Args:
            quintil: Quintil del Registro Social (1-5)
        """
        if quintil <= 2:  # Quintil 1 o 2 = pobreza
            self.condicion_socioeconomica = 'SI'
            
            if quintil == 1:  # Quintil 1 = pobreza extrema
                self.vulnerabilidad_socioeconomica = 'SI'
                print(f"🏚️ Vulnerabilidad socioeconómica detectada (Quintil {quintil})")
        
        print(f"💰 Condición socioeconómica: Quintil {quintil}")
    
    def aplicar_ruralidad(self, tipo_institucion: str, zona: str):
        """Aplica si estudió en zona rural."""
        if tipo_institucion == 'FISCAL' and zona.upper() == 'RURAL':
            self.ruralidad = 'SI'
            print(f"🌾 Ruralidad aplicada")
    
    def aplicar_discapacidad(self, porcentaje: int, tiene_carnet: bool):
        """Aplica si tiene discapacidad >= 30%."""
        if tiene_carnet and porcentaje >= 30:
            self.discapacidad = 'SI'
            print(f"♿ Discapacidad aplicada: {porcentaje}%")
    
    def aplicar_pueblos_nacionalidades(self, autoidentificacion: str):
        """Aplica si pertenece a pueblos y nacionalidades."""
        PUEBLOS = ['INDIGENA', 'AFROECUATORIANO', 'MONTUBIO', 'AFRODESCENDIENTE']
        if autoidentificacion.upper() in PUEBLOS:
            self.pueblos_nacionalidades = 'SI'
            print(f"🌍 Pueblos y nacionalidades: {autoidentificacion}")
    
    def aplicar_merito_academico(self, cuadro_honor: str, distincion: str = None):
        """Aplica si fue abanderado o escolta."""
        if cuadro_honor == 'SI':
            DISTINCIONES_MERITO = [
                'ABANDERADO PABELLON NACIONAL',
                'PORTA ESTANDARTE CIUDAD',
                'PORTA ESTANDARTE PLANTEL',
                '1er. ESCOLTA PABELLON NACIONAL',
                '2do. ESCOLTA PABELLON NACIONAL'
            ]
            if distincion and distincion in DISTINCIONES_MERITO:
                self.merito_academico = 'SI'
                print(f"🏆 Mérito académico: {distincion}")
    
    def aplicar_bachiller_ultimo_anio(self, es_bachiller: bool, 
                                     pertenece_pueblos: bool = False):
        """Aplica si está cursando último año de bachillerato."""
        if es_bachiller:
            self.bachiller_periodo_academico = 'SI'
            
            if pertenece_pueblos:
                self.bachiller_pueblos_nacionalidad = 'SI'
                print(f"🎓 Bachiller de pueblos y nacionalidades")
            else:
                print(f"🎓 Bachiller último año")
    
    def calcular_segmento(self) -> str:
        """
        Calcula el segmento de asignación según orden obligatorio.
        
        Returns:
            str: Segmento asignado
        """
        # Verificar cada segmento en orden de prioridad
        
        # 1. CUOTAS (si tiene cupo histórico aceptado, NO puede ser cuotas)
        if self.cupo_aceptado_historico_pc == 'NO':
            # Cuotas aplica si tiene al menos una PAA
            tiene_paa = any([
                self.condicion_socioeconomica == 'SI',
                self.ruralidad == 'SI',
                self.discapacidad == 'SI',
                self.pueblos_nacionalidades == 'SI',
                self.victima_violencia == 'SI',
                self.migrantes_retornados == 'SI'
            ])
            
            if tiene_paa:
                self.segmento_asignado = 'CUOTAS'
                self.prioridad_segmento = 1
                print(f"🎯 Segmento: CUOTAS (Prioridad 1)")
                return self.segmento_asignado
        
        # 2. VULNERABILIDAD SOCIOECONÓMICA
        if self.vulnerabilidad_socioeconomica == 'SI':
            self.segmento_asignado = 'VULNERABILIDAD'
            self.prioridad_segmento = 2
            print(f"🎯 Segmento: VULNERABILIDAD (Prioridad 2)")
            return self.segmento_asignado
        
        # 3. MÉRITO ACADÉMICO
        if self.merito_academico == 'SI':
            self.segmento_asignado = 'MERITO_ACADEMICO'
            self.prioridad_segmento = 3
            print(f"🎯 Segmento: MÉRITO ACADÉMICO (Prioridad 3)")
            return self.segmento_asignado
        
        # 5. PUEBLOS Y NACIONALIDADES (bachilleres)
        if self.bachiller_pueblos_nacionalidad == 'SI':
            self.segmento_asignado = 'PUEBLOS_NACIONALIDADES'
            self.prioridad_segmento = 5
            print(f"🎯 Segmento: PUEBLOS Y NACIONALIDADES (Prioridad 5)")
            return self.segmento_asignado
        
        # 6. BACHILLERES ÚLTIMO AÑO
        if self.bachiller_periodo_academico == 'SI':
            self.segmento_asignado = 'BACHILLERES'
            self.prioridad_segmento = 6
            print(f"🎯 Segmento: BACHILLERES (Prioridad 6)")
            return self.segmento_asignado
        
        # 7. POBLACIÓN GENERAL
        self.segmento_asignado = 'GENERAL'
        self.prioridad_segmento = 7
        print(f"🎯 Segmento: POBLACIÓN GENERAL (Prioridad 7)")
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
            'ruralidad': self.ruralidad,
            'cupo_historico': self.cupo_aceptado_historico_pc
        }
    
    def __str__(self) -> str:
        """Representación en string."""
        return (f"PAA(Postulante: {self.id_postulante}, "
                f"Segmento: {self.segmento_asignado}, "
                f"Prioridad: {self.prioridad_segmento})")
    
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
    print("\n🏆 CASO 1: Estudiante con mérito académico")
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
    print("\n\n🏚️ CASO 2: Estudiante con vulnerabilidad socioeconómica")
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
    
    print(f"\n📊 Total PAA creadas: {PoliticaAccionAfirmativa.obtener_total()}")
    print("\n" + "=" * 70)