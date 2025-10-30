"""
Módulo: SedeCampus
Autor: Jean Pierre Flores Piloso - Equipo 3ro TI "C"
Fecha: Octubre 2025
Descripción: Gestiona las sedes y campus de ULEAM
Basado en: 102_ULEAM_OFERTASEGMENTADA_IIPA-2025.pdf
"""


class SedeCampus:
    """
    Representa una sede o campus de ULEAM.
    
    Sedes oficiales ULEAM según SENESCYT:
    - Matriz - Manta
    - Chone
    - El Carmen
    - Pedernales
    - Bahía de Caráquez (Sucre)
    - Tosagua
    - Santo Domingo de los Colorados
    - Flavio Alfaro
    - Pichincha
    
    Attributes:
        sede_id: ID único de la sede
        nombre_sede: Nombre oficial
        canton: Cantón donde se ubica
        provincia: Provincia
        activa: Si está activa
    """
    
    # Contador
    _contador = 0
    
    # Sedes oficiales ULEAM
    SEDES_ULEAM = {
        1: {'nombre': 'Matriz - Manta', 'canton': 'MANTA', 'provincia': 'MANABÍ'},
        2: {'nombre': 'Chone', 'canton': 'CHONE', 'provincia': 'MANABÍ'},
        3: {'nombre': 'El Carmen', 'canton': 'EL CARMEN', 'provincia': 'MANABÍ'},
        4: {'nombre': 'Pedernales', 'canton': 'PEDERNALES', 'provincia': 'MANABÍ'},
        5: {'nombre': 'Bahía de Caráquez', 'canton': 'SUCRE', 'provincia': 'MANABÍ'},
        6: {'nombre': 'Tosagua', 'canton': 'TOSAGUA', 'provincia': 'MANABÍ'},
        7: {'nombre': 'Santo Domingo', 'canton': 'SANTO DOMINGO', 'provincia': 'SANTO DOMINGO DE LOS TSÁCHILAS'},
        8: {'nombre': 'Flavio Alfaro', 'canton': 'FLAVIO ALFARO', 'provincia': 'MANABÍ'},
        9: {'nombre': 'Pichincha', 'canton': 'PICHINCHA', 'provincia': 'MANABÍ'}
    }
    
    def __init__(self, sede_id: int):
        """
        Inicializa una sede.
        
        Args:
            sede_id: ID de la sede (1-9)
            
        Raises:
            ValueError: Si el ID no existe
        """
        if sede_id not in self.SEDES_ULEAM:
            raise ValueError(f"Sede ID {sede_id} no existe en ULEAM")
        
        SedeCampus._contador += 1
        
        datos = self.SEDES_ULEAM[sede_id]
        self.sede_id = sede_id
        self.nombre_sede = datos['nombre']
        self.canton = datos['canton']
        self.provincia = datos['provincia']
        self.activa = True
        
        # Contadores
        self.total_carreras = 0
        self.total_cupos = 0
        self.total_laboratorios = 0
        
        print(f"Sede creada: {self.nombre_sede} ({self.canton})")
    
    def agregar_carrera(self, nombre_carrera: str, cupos: int):
        """Registra una carrera en la sede."""
        self.total_carreras += 1
        self.total_cupos += cupos
        print(f"Carrera agregada: {nombre_carrera} ({cupos} cupos)")
    
    def obtener_info(self) -> dict:
        """Obtiene información de la sede."""
        return {
            'sede_id': self.sede_id,
            'nombre': self.nombre_sede,
            'canton': self.canton,
            'provincia': self.provincia,
            'carreras': self.total_carreras,
            'cupos_totales': self.total_cupos,
            'activa': self.activa
        }
    
    def __str__(self) -> str:
        """Representación en string."""
        return f"Sede({self.nombre_sede}, {self.provincia})"
    
    @classmethod
    def listar_todas_sedes(cls):
        """Lista todas las sedes disponibles."""
        print("\n" + "="*60)
        print("           SEDES UNIVERSIDAD ULEAM 2025")
        print("="*60)
        for id_sede, datos in cls.SEDES_ULEAM.items():
            print(f" {id_sede}. {datos['nombre']:<30} | {datos['canton']:<16}")
        print("="*60 + "\n")
    
    @classmethod
    def obtener_sede_por_canton(cls, canton: str):
        """Busca sede por cantón."""
        canton = canton.upper()
        for id_sede, datos in cls.SEDES_ULEAM.items():
            if datos['canton'] == canton:
                return id_sede
        return None
    
    @classmethod
    def obtener_total_sedes(cls) -> int:
        """Total de sedes creadas."""
        return cls._contador