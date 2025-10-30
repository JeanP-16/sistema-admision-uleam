"""
Módulo: Asignacion
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos.
Fecha: Octubre 2025
Descripción: Clase que gestiona la asignación de cupos a postulantes
"""

from datetime import datetime
from typing import Optional

class Asignacion:
    """
    Representa la asignación definitiva de un cupo a un postulante.
    Se crea después de que el postulante complete su evaluación.
    """
    
    _contador_asignaciones = 0
    
    ESTADOS_VALIDOS = ['PENDIENTE', 'CONFIRMADA', 'RECHAZADA', 'EXPIRADA']
    
    def __init__(self,
                 id_postulante: int,
                 carrera_id: int,
                 sede_id: int,
                 puntaje_final: float,
                 cedula_postulante: str):
        """
        Inicializa una asignación de cupo.
        
        Args:
            id_postulante: ID del postulante
            carrera_id: ID de la carrera asignada
            sede_id: ID de la sede
            puntaje_final: Puntaje final obtenido
            cedula_postulante: Cédula del postulante
        """
        Asignacion._contador_asignaciones += 1
        
        self.id_asignacion = Asignacion._contador_asignaciones
        self.id_postulante = id_postulante
        self.carrera_id = carrera_id
        self.sede_id = sede_id
        self.puntaje_final = puntaje_final
        self.cedula_postulante = cedula_postulante
        self.fecha_asignacion = datetime.now()
        self.estado = 'PENDIENTE'
        self.fecha_confirmacion = None
        self.observaciones = None
    
    def confirmar(self) -> None:
        """Confirma la asignación del cupo."""
        if self.estado == 'CONFIRMADA':
            print("La asignacion ya esta confirmada")
            return
        
        self.estado = 'CONFIRMADA'
        self.fecha_confirmacion = datetime.now()
        print(f"Asignacion {self.id_asignacion} confirmada exitosamente")
        self._notificar_confirmacion()
    
    def rechazar(self, motivo: Optional[str] = None) -> None:
        """Rechaza la asignación del cupo."""
        self.estado = 'RECHAZADA'
        if motivo:
            self.observaciones = f"Rechazada: {motivo}"
        print(f"Asignacion {self.id_asignacion} rechazada")
    
    def expirar(self) -> None:
        """Marca la asignación como expirada por falta de confirmación."""
        self.estado = 'EXPIRADA'
        print(f"Asignacion {self.id_asignacion} expirada")
    
    def _notificar_confirmacion(self) -> None:
        """Notifica al postulante sobre la confirmación."""
        print(f"Notificacion enviada a postulante {self.id_postulante}")
        print(f"Cupo confirmado en carrera {self.carrera_id}")
    
    def agregarObservaciones(self, texto: str) -> None:
        """Agrega observaciones a la asignación."""
        self.observaciones = texto
    
    def mostrar_info(self) -> None:
        """Muestra la información completa de la asignación."""
        print("\n" + "=" * 60)
        print(f"ASIGNACION ID: {self.id_asignacion}")
        print("=" * 60)
        print(f"Cedula Postulante: {self.cedula_postulante}")
        print(f"Postulante ID: {self.id_postulante}")
        print(f"Carrera ID: {self.carrera_id}")
        print(f"Sede ID: {self.sede_id}")
        print(f"Puntaje Final: {self.puntaje_final} puntos")
        print(f"Fecha asignacion: {self.fecha_asignacion.strftime('%d/%m/%Y %H:%M')}")
        print(f"Estado: {self.estado}")
        if self.fecha_confirmacion:
            print(f"Fecha confirmacion: {self.fecha_confirmacion.strftime('%d/%m/%Y %H:%M')}")
        if self.observaciones:
            print(f"Observaciones: {self.observaciones}")
        print("=" * 60)
    
    def __str__(self) -> str:
        return f"Asignacion(ID:{self.id_asignacion}, Postulante:{self.id_postulante}, Estado:{self.estado})"
