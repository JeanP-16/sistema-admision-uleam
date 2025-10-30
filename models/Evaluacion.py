"""
Módulo: Evaluacion
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripción: Clase que representa una evaluación académica con programación automática
"""

from datetime import datetime, timedelta
from typing import Optional

class Evaluacion:
    """
    Representa una sesión de evaluación (examen) para un postulante.
    Se crea automáticamente cuando se genera una inscripción.
    """
    
    _contador_evaluaciones = 0
    
    # Horarios por jornada
    HORARIOS_JORNADA = {
        'matutina': ('08:00', '10:00'),
        'vespertina': ('14:00', '16:00'),
        'nocturna': ('18:00', '20:00')
    }
    
    # Laboratorios por sede
    LABORATORIOS_SEDE = {
        1: [101, 102, 103],  # Manta
        2: [201, 202],       # Chone
        3: [301],            # Bahía
    }
    
    def __init__(self, 
                 id_inscripcion: int,
                 tipo: str,
                 sede_id: int,
                 jornada: str = 'matutina',
                 laboratorio_id: Optional[int] = None,
                 auto_programar: bool = True):
        """
        Inicializa una evaluación.
        
        Args:
            id_inscripcion: ID de la inscripción asociada
            tipo: Tipo de evaluación ('escrito', 'practico', 'oral')
            sede_id: ID de la sede
            jornada: Jornada ('matutina', 'vespertina', 'nocturna')
            laboratorio_id: ID del laboratorio (se asigna automáticamente si es None)
            auto_programar: Si True, programa automáticamente fecha y hora
        """
        Evaluacion._contador_evaluaciones += 1
        
        self.id_evaluacion = Evaluacion._contador_evaluaciones
        self.id_inscripcion = id_inscripcion
        self.tipo = tipo.lower()
        self.sede_id = sede_id
        self.jornada = jornada.lower()
        
        # Asignar laboratorio automáticamente si no se especifica
        if laboratorio_id is None:
            self.laboratorio_id = self._asignar_laboratorio_automatico()
        else:
            self.laboratorio_id = laboratorio_id
        
        # Programación automática
        if auto_programar:
            self._programar_automaticamente()
        else:
            self.fecha_programada = None
            self.hora_inicio = None
            self.hora_fin = None
        
        self.calificacion = None
        self.estado = 'PROGRAMADA'
        self.observaciones = None
        
    def _asignar_laboratorio_automatico(self) -> int:
        """Asigna automáticamente un laboratorio según la sede."""
        laboratorios = self.LABORATORIOS_SEDE.get(self.sede_id, [101])
        # Asignar el primer laboratorio disponible
        return laboratorios[0]
    
    def _programar_automaticamente(self) -> None:
        """Programa automáticamente la fecha y hora de la evaluación."""
        # Programar para 15 días después de hoy
        hoy = datetime.now()
        self.fecha_programada = hoy + timedelta(days=15)
        
        # Asignar horario según jornada
        horario = self.HORARIOS_JORNADA.get(self.jornada, ('08:00', '10:00'))
        self.hora_inicio = horario[0]
        self.hora_fin = horario[1]
    
    def registrarCalificacion(self, calificacion: float) -> None:
        """Registra la calificación obtenida."""
        if not 0 <= calificacion <= 1000:
            raise ValueError("La calificación debe estar entre 0 y 1000 puntos")
        
        self.calificacion = calificacion
        self.estado = 'COMPLETADA'
        print(f"Calificación registrada: {calificacion} puntos")
    
    def reprogramar(self, nueva_fecha: datetime, nueva_hora_inicio: str) -> None:
        """Reprograma la evaluación."""
        if nueva_fecha < datetime.now():
            raise ValueError("No se puede programar en el pasado")
        
        self.fecha_programada = nueva_fecha
        self.hora_inicio = nueva_hora_inicio
        self.estado = 'REPROGRAMADA'
        print(f"Evaluación reprogramada para {nueva_fecha.strftime('%d/%m/%Y')} a las {nueva_hora_inicio}")
    
    def cancelar(self) -> None:
        """Cancela la evaluación."""
        self.estado = 'CANCELADA'
        print(f"Evaluación {self.id_evaluacion} cancelada")
    
    def agregarObservaciones(self, texto: str) -> None:
        """Agrega observaciones a la evaluación."""
        self.observaciones = texto
    
    def mostrar_info(self) -> None:
        """Muestra la información completa de la evaluación."""
        print("\n" + "=" * 60)
        print(f"EVALUACION ID: {self.id_evaluacion}")
        print("=" * 60)
        print(f"Inscripcion ID: {self.id_inscripcion}")
        print(f"Tipo: {self.tipo.upper()}")
        print(f"Sede ID: {self.sede_id}")
        print(f"Laboratorio: {self.laboratorio_id}")
        print(f"Fecha programada: {self.fecha_programada.strftime('%d/%m/%Y')}")
        print(f"Hora: {self.hora_inicio} - {self.hora_fin}")
        print(f"Jornada: {self.jornada.upper()}")
        print(f"Estado: {self.estado}")
        if self.calificacion is not None:
            print(f"Calificacion: {self.calificacion} puntos")
        if self.observaciones:
            print(f"Observaciones: {self.observaciones}")
        print("=" * 60)
    
    def __str__(self) -> str:
        return f"Evaluacion(ID:{self.id_evaluacion}, Tipo:{self.tipo}, Estado:{self.estado})"
