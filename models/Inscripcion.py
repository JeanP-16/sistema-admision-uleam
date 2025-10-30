"""
Módulo: Inscripcion
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripción: Clase que representa la inscripción de un postulante a una carrera.
              Crea automáticamente la evaluación al inscribirse.
"""

from datetime import datetime
from typing import Optional, List

class Inscripcion:
    """
    Representa la solicitud de inscripción de un postulante a una carrera.
    Al crear una inscripción, automáticamente se genera su evaluación.
    """
    
    _contador_inscripciones = 0
    
    JORNADAS_VALIDAS = ['matutina', 'vespertina', 'nocturna']
    ESTADOS_VALIDOS = ['ACTIVA', 'CANCELADA', 'COMPLETADA']
    MAX_PREFERENCIAS = 3
    
    def __init__(self,
                 id_postulante: int,
                 carrera_id: int,
                 orden_preferencia: int,
                 sede_id: int,
                 jornada: str,
                 cedula_postulante: str,
                 laboratorio_id: Optional[int] = None):
        """
        Inicializa una nueva inscripción y crea automáticamente su evaluación.
        
        Args:
            id_postulante: ID del postulante
            carrera_id: ID de la carrera
            orden_preferencia: Orden de preferencia (1-3)
            sede_id: ID de la sede
            jornada: Jornada académica
            cedula_postulante: Cédula del postulante (para búsqueda)
            laboratorio_id: ID del laboratorio (opcional)
        """
        Inscripcion._contador_inscripciones += 1
        
        self.id_inscripcion = Inscripcion._contador_inscripciones
        self.id_postulante = id_postulante
        self.carrera_id = carrera_id
        self.orden_preferencia = self._validar_orden_preferencia(orden_preferencia)
        self.sede_id = sede_id
        self.jornada = self._validar_jornada(jornada)
        self.laboratorio_id = laboratorio_id
        self.cedula_postulante = cedula_postulante
        self.fecha_inscripcion = datetime.now()
        self.comprobante_pdf_url = f"COMP-{self.id_inscripcion}-{self.cedula_postulante}.pdf"
        self.estado = 'ACTIVA'
        self._evaluacion = None
        
        # CREAR EVALUACIÓN AUTOMÁTICAMENTE
        self._crear_evaluacion_automatica()
    
    def _crear_evaluacion_automatica(self) -> None:
        """Crea automáticamente la evaluación para esta inscripción."""
        try:
            from models.Evaluacion import Evaluacion
            
            # Determinar tipo de evaluación según carrera
            tipo_evaluacion = self._determinar_tipo_evaluacion(self.carrera_id)
            
            # Crear evaluación con programación automática
            self._evaluacion = Evaluacion(
                id_inscripcion=self.id_inscripcion,
                tipo=tipo_evaluacion,
                sede_id=self.sede_id,
                jornada=self.jornada,
                laboratorio_id=self.laboratorio_id,
                auto_programar=True
            )
            
            print(f"\n>>> EVALUACION CREADA AUTOMATICAMENTE <<<")
            print(f"ID Evaluacion: {self._evaluacion.id_evaluacion}")
            print(f"Tipo: {self._evaluacion.tipo}")
            print(f"Fecha: {self._evaluacion.fecha_programada.strftime('%d/%m/%Y')}")
            print(f"Hora: {self._evaluacion.hora_inicio} - {self._evaluacion.hora_fin}")
            print(f"Laboratorio: {self._evaluacion.laboratorio_id}")
            
        except ImportError:
            print("ADVERTENCIA: No se pudo importar el modulo Evaluacion")
    
    def _determinar_tipo_evaluacion(self, carrera_id: int) -> str:
        """Determina el tipo de evaluación según la carrera."""
        # Carreras técnicas/prácticas
        if carrera_id in [101, 102]:  # TI, Software
            return "practico"
        # Carreras teóricas
        elif carrera_id in [103, 104]:  # Medicina, Administración
            return "escrito"
        else:
            return "escrito"
    
    def _validar_orden_preferencia(self, orden: int) -> int:
        """Valida el orden de preferencia."""
        if not isinstance(orden, int) or orden < 1 or orden > self.MAX_PREFERENCIAS:
            raise ValueError(f"Orden debe estar entre 1 y {self.MAX_PREFERENCIAS}")
        return orden
    
    def _validar_jornada(self, jornada: str) -> str:
        """Valida la jornada."""
        jornada = jornada.lower().strip()
        if jornada not in self.JORNADAS_VALIDAS:
            raise ValueError(f"Jornada invalida. Debe ser: {', '.join(self.JORNADAS_VALIDAS)}")
        return jornada
    
    def obtenerEvaluacion(self):
        """Obtiene la evaluación asociada a esta inscripción."""
        return self._evaluacion
    
    def validarRequisitos(self) -> bool:
        """Valida que la inscripción cumpla con los requisitos."""
        cumple_requisitos = True
        
        if not self.comprobante_pdf_url:
            print("Advertencia: Falta comprobante")
            cumple_requisitos = False
        
        if self.estado == 'CANCELADA':
            print("Inscripcion cancelada")
            return False
        
        if cumple_requisitos:
            print(f"Requisitos validados para inscripcion {self.id_inscripcion}")
        
        return cumple_requisitos
    
    def cancelar(self) -> None:
        """Cancela la inscripción."""
        self.estado = 'CANCELADA'
        if self._evaluacion:
            self._evaluacion.cancelar()
        print(f"Inscripcion {self.id_inscripcion} cancelada")
    
    def completar(self) -> None:
        """Completa la inscripción."""
        self.estado = 'COMPLETADA'
        print(f"Inscripcion {self.id_inscripcion} completada")
    
    def mostrar_info_completa(self) -> None:
        """Muestra toda la información de la inscripción incluyendo evaluación."""
        print("\n" + "=" * 60)
        print(f"INSCRIPCION ID: {self.id_inscripcion}")
        print("=" * 60)
        print(f"Cedula Postulante: {self.cedula_postulante}")
        print(f"Postulante ID: {self.id_postulante}")
        print(f"Carrera ID: {self.carrera_id}")
        print(f"Orden preferencia: {self.orden_preferencia}")
        print(f"Sede ID: {self.sede_id}")
        print(f"Jornada: {self.jornada}")
        print(f"Laboratorio ID: {self.laboratorio_id}")
        print(f"Fecha inscripcion: {self.fecha_inscripcion.strftime('%d/%m/%Y %H:%M')}")
        print(f"Comprobante: {self.comprobante_pdf_url}")
        print(f"Estado: {self.estado}")
        print("=" * 60)
        
        # Mostrar evaluación asociada
        if self._evaluacion:
            print("\nEVALUACION ASOCIADA:")
            self._evaluacion.mostrar_info()
    
    def __str__(self) -> str:
        return f"Inscripcion(ID:{self.id_inscripcion}, Postulante:{self.id_postulante}, Estado:{self.estado})"
