<<<<<<< HEAD
"""
Módulo: Evaluacion
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos.
Fecha: Octubre 2025
Descripcion: Clase que representa una evaluacion academica con programacion automatica
"""

from datetime import datetime, timedelta
from typing import Optional
from abc import ABC, abstractmethod


# ===== CLASE ABSTRACTA BASE =====
class Examen(ABC):
    """Clase abstracta base para examenes"""
    
    def __init__(self, id_referencia: int, tipo: str):
        self.id_referencia = id_referencia
        self.tipo = tipo
        self.calificacion = None
        self.estado = 'PROGRAMADA'
    
    @abstractmethod
    def registrarCalificacion(self, calificacion: float) -> None:
        """Metodo abstracto para registrar calificacion"""
        pass
    
    @abstractmethod
    def mostrar_info(self) -> None:
        """Metodo abstracto para mostrar informacion"""
        pass


# ===== HERENCIA SIMPLE: Evaluacion hereda de Examen =====
class Evaluacion(Examen):
    """
    Representa una sesion de evaluacion (examen) para un postulante.
    HEREDA de la clase abstracta Examen
    """
    
    _contador_evaluaciones = 0
    
    HORARIOS_JORNADA = {
        'matutina': ('08:00', '10:00'),
        'vespertina': ('14:00', '16:00'),
        'nocturna': ('18:00', '20:00')
    }
    
    LABORATORIOS_SEDE = {
        1: [101, 102, 103],
        2: [201, 202],
        3: [301],
    }
    
    def __init__(self, 
                 id_inscripcion: int,
                 tipo: str,
                 sede_id: int,
                 jornada: str = 'matutina',
                 laboratorio_id: Optional[int] = None,
                 auto_programar: bool = True):
        # Llamar al constructor de la clase padre
        super().__init__(id_inscripcion, tipo.lower())
        
        Evaluacion._contador_evaluaciones += 1
        
        self.id_evaluacion = Evaluacion._contador_evaluaciones
        self.id_inscripcion = id_inscripcion
        self.sede_id = sede_id
        self.jornada = jornada.lower()
        
        if laboratorio_id is None:
            self.laboratorio_id = self._asignar_laboratorio_automatico()
        else:
            self.laboratorio_id = laboratorio_id
        
        if auto_programar:
            self._programar_automaticamente()
        else:
            self.fecha_programada = None
            self.hora_inicio = None
            self.hora_fin = None
        
        self.observaciones = None
    
    def _asignar_laboratorio_automatico(self) -> int:
        laboratorios = self.LABORATORIOS_SEDE.get(self.sede_id, [101])
        return laboratorios[0]
    
    def _programar_automaticamente(self) -> None:
        hoy = datetime.now()
        self.fecha_programada = hoy + timedelta(days=15)
        
        horario = self.HORARIOS_JORNADA.get(self.jornada, ('08:00', '10:00'))
        self.hora_inicio = horario[0]
        self.hora_fin = horario[1]
    
    # IMPLEMENTACION del metodo abstracto (POLIMORFISMO)
    def registrarCalificacion(self, calificacion: float) -> None:
        """Sobrescribe el metodo abstracto de Examen"""
        if not 0 <= calificacion <= 1000:
            raise ValueError("La calificacion debe estar entre 0 y 1000 puntos")
        
        self.calificacion = calificacion
        self.estado = 'COMPLETADA'
        print(f"Calificacion registrada: {calificacion} puntos")
    
    def reprogramar(self, nueva_fecha: datetime, nueva_hora_inicio: str) -> None:
        if nueva_fecha < datetime.now():
            raise ValueError("No se puede programar en el pasado")
        
        self.fecha_programada = nueva_fecha
        self.hora_inicio = nueva_hora_inicio
        self.estado = 'REPROGRAMADA'
        print(f"Evaluacion reprogramada para {nueva_fecha.strftime('%d/%m/%Y')} a las {nueva_hora_inicio}")
    
    def cancelar(self) -> None:
        self.estado = 'CANCELADA'
        print(f"Evaluacion {self.id_evaluacion} cancelada")
    
    def agregarObservaciones(self, texto: str) -> None:
        self.observaciones = texto
    
    # IMPLEMENTACION del metodo abstracto (POLIMORFISMO)
    def mostrar_info(self) -> None:
        """Sobrescribe el metodo abstracto de Examen"""
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
    
    # DECORADOR @property
    @property
    def esta_completada(self) -> bool:
        """Property para verificar si esta completada"""
        return self.estado == 'COMPLETADA'
    
    def __str__(self) -> str:
        return f"Evaluacion(ID:{self.id_evaluacion}, Tipo:{self.tipo}, Estado:{self.estado})"
=======
"""
Módulo: Evaluacion
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos.
Fecha: Octubre 2025
Descripcion: Clase que representa una evaluacion academica con programacion automatica
"""

from datetime import datetime, timedelta
from typing import Optional
from abc import ABC, abstractmethod


# ===== CLASE ABSTRACTA BASE =====
class Examen(ABC):
    """Clase abstracta base para examenes"""
    
    def __init__(self, id_referencia: int, tipo: str):
        self.id_referencia = id_referencia
        self.tipo = tipo
        self.calificacion = None
        self.estado = 'PROGRAMADA'
    
    @abstractmethod
    def registrarCalificacion(self, calificacion: float) -> None:
        """Metodo abstracto para registrar calificacion"""
        pass
    
    @abstractmethod
    def mostrar_info(self) -> None:
        """Metodo abstracto para mostrar informacion"""
        pass


# ===== HERENCIA SIMPLE: Evaluacion hereda de Examen =====
class Evaluacion(Examen):
    """
    Representa una sesion de evaluacion (examen) para un postulante.
    HEREDA de la clase abstracta Examen
    """
    
    _contador_evaluaciones = 0
    
    HORARIOS_JORNADA = {
        'matutina': ('08:00', '10:00'),
        'vespertina': ('14:00', '16:00'),
        'nocturna': ('18:00', '20:00')
    }
    
    LABORATORIOS_SEDE = {
        1: [101, 102, 103],
        2: [201, 202],
        3: [301],
    }
    
    def __init__(self, 
                 id_inscripcion: int,
                 tipo: str,
                 sede_id: int,
                 jornada: str = 'matutina',
                 laboratorio_id: Optional[int] = None,
                 auto_programar: bool = True):
        # Llamar al constructor de la clase padre
        super().__init__(id_inscripcion, tipo.lower())
        
        Evaluacion._contador_evaluaciones += 1
        
        self.id_evaluacion = Evaluacion._contador_evaluaciones
        self.id_inscripcion = id_inscripcion
        self.sede_id = sede_id
        self.jornada = jornada.lower()
        
        if laboratorio_id is None:
            self.laboratorio_id = self._asignar_laboratorio_automatico()
        else:
            self.laboratorio_id = laboratorio_id
        
        if auto_programar:
            self._programar_automaticamente()
        else:
            self.fecha_programada = None
            self.hora_inicio = None
            self.hora_fin = None
        
        self.observaciones = None
    
    def _asignar_laboratorio_automatico(self) -> int:
        laboratorios = self.LABORATORIOS_SEDE.get(self.sede_id, [101])
        return laboratorios[0]
    
    def _programar_automaticamente(self) -> None:
        hoy = datetime.now()
        self.fecha_programada = hoy + timedelta(days=15)
        
        horario = self.HORARIOS_JORNADA.get(self.jornada, ('08:00', '10:00'))
        self.hora_inicio = horario[0]
        self.hora_fin = horario[1]
    
    # IMPLEMENTACION del metodo abstracto (POLIMORFISMO)
    def registrarCalificacion(self, calificacion: float) -> None:
        """Sobrescribe el metodo abstracto de Examen"""
        if not 0 <= calificacion <= 1000:
            raise ValueError("La calificacion debe estar entre 0 y 1000 puntos")
        
        self.calificacion = calificacion
        self.estado = 'COMPLETADA'
        print(f"Calificacion registrada: {calificacion} puntos")
    
    def reprogramar(self, nueva_fecha: datetime, nueva_hora_inicio: str) -> None:
        if nueva_fecha < datetime.now():
            raise ValueError("No se puede programar en el pasado")
        
        self.fecha_programada = nueva_fecha
        self.hora_inicio = nueva_hora_inicio
        self.estado = 'REPROGRAMADA'
        print(f"Evaluacion reprogramada para {nueva_fecha.strftime('%d/%m/%Y')} a las {nueva_hora_inicio}")
    
    def cancelar(self) -> None:
        self.estado = 'CANCELADA'
        print(f"Evaluacion {self.id_evaluacion} cancelada")
    
    def agregarObservaciones(self, texto: str) -> None:
        self.observaciones = texto
    
    # IMPLEMENTACION del metodo abstracto (POLIMORFISMO)
    def mostrar_info(self) -> None:
        """Sobrescribe el metodo abstracto de Examen"""
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
    
    # DECORADOR @property
    @property
    def esta_completada(self) -> bool:
        """Property para verificar si esta completada"""
        return self.estado == 'COMPLETADA'
    
    def __str__(self) -> str:
        return f"Evaluacion(ID:{self.id_evaluacion}, Tipo:{self.tipo}, Estado:{self.estado})"
>>>>>>> d4f7eac51555ebae2693ce93b24af2bc4943b607
