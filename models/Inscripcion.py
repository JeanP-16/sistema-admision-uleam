"""
Módulo: Inscripcion
<<<<<<< HEAD
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
=======
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Gabriel Cevallos
>>>>>>> 029f97d (Actualización definitiva: modelos y main.py con herencia y polimorfismo)
Fecha: Octubre 2025
Descripción: Clase que representa la inscripción de un postulante a una carrera.
              Implementa herencia, abstracción y polimorfismo básico.
"""

from datetime import datetime
from abc import ABC, abstractmethod
from typing import Optional


class ProcesoBase(ABC):
    """
    Clase base abstracta para procesos administrativos del sistema.
    Define métodos abstractos comunes a todas las operaciones.
    """

    @abstractmethod
    def validarRequisitos(self) -> bool:
        """Valida los requisitos del proceso."""
        pass

    @abstractmethod
    def cancelar(self) -> None:
        """Cancela el proceso."""
        pass

    @abstractmethod
    def completar(self) -> None:
        """Completa el proceso."""
        pass

    @abstractmethod
    def mostrar_info_completa(self) -> None:
        """Muestra toda la información detallada del proceso."""
        pass


class Inscripcion(ProcesoBase):
    """
    Representa la solicitud de inscripción de un postulante a una carrera.
    Hereda de ProcesoBase y aplica polimorfismo en métodos clave.
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

        self._crear_evaluacion_automatica()

    # ==============================
    # MÉTODOS HEREDADOS (POLIMÓRFICOS)
    # ==============================

    def validarRequisitos(self) -> bool:
        """Valida que la inscripción cumpla con los requisitos."""
        cumple = True

        if not self.comprobante_pdf_url:
            print("Advertencia: Falta comprobante de inscripción.")
            cumple = False

        if self.estado == 'CANCELADA':
            print("No se puede validar una inscripción cancelada.")
            return False

        if cumple:
            print(f"Requisitos validados correctamente para inscripción {self.id_inscripcion}.")
        return cumple

    def cancelar(self) -> None:
        """Cancela la inscripción."""
        self.estado = 'CANCELADA'
        if self._evaluacion:
            self._evaluacion.cancelar()
        print(f"Inscripción {self.id_inscripcion} cancelada correctamente.")

    def completar(self) -> None:
        """Completa la inscripción."""
        self.estado = 'COMPLETADA'
        print(f"Inscripción {self.id_inscripcion} completada exitosamente.")

    def mostrar_info_completa(self) -> None:
        """Muestra toda la información de la inscripción, incluyendo evaluación."""
        print("\n" + "=" * 60)
        print(f"INSCRIPCIÓN ID: {self.id_inscripcion}")
        print("=" * 60)
        print(f"Cédula Postulante: {self.cedula_postulante}")
        print(f"Postulante ID: {self.id_postulante}")
        print(f"Carrera ID: {self.carrera_id}")
        print(f"Orden preferencia: {self.orden_preferencia}")
        print(f"Sede ID: {self.sede_id}")
        print(f"Jornada: {self.jornada}")
        print(f"Laboratorio ID: {self.laboratorio_id}")
        print(f"Fecha inscripción: {self.fecha_inscripcion.strftime('%d/%m/%Y %H:%M')}")
        print(f"Comprobante: {self.comprobante_pdf_url}")
        print(f"Estado: {self.estado}")
        print("=" * 60)
        if self._evaluacion:
            print("\nEVALUACIÓN ASOCIADA:")
            self._evaluacion.mostrar_info()

    # ==============================
    # MÉTODOS INTERNOS Y DE APOYO
    # ==============================

    def _crear_evaluacion_automatica(self) -> None:
        """Crea automáticamente la evaluación para esta inscripción."""
        try:
            from models.Evaluacion import Evaluacion
            tipo_eval = self._determinar_tipo_evaluacion(self.carrera_id)

            self._evaluacion = Evaluacion(
                id_inscripcion=self.id_inscripcion,
                tipo=tipo_eval,
                sede_id=self.sede_id,
                jornada=self.jornada,
                laboratorio_id=self.laboratorio_id,
                auto_programar=True
            )

            print(f"\nEvaluación creada automáticamente:")
            print(f"ID: {self._evaluacion.id_evaluacion}")
            print(f"Tipo: {self._evaluacion.tipo}")
            print(f"Fecha: {self._evaluacion.fecha_programada.strftime('%d/%m/%Y')}")
            print(f"Laboratorio: {self._evaluacion.laboratorio_id}")

        except ImportError:
            print("No se pudo importar el módulo Evaluacion. Verifique la estructura del proyecto.")

    def _determinar_tipo_evaluacion(self, carrera_id: int) -> str:
        """Determina el tipo de evaluación según la carrera."""
        if carrera_id in [101, 102]:
            return "practico"
        elif carrera_id in [103, 104]:
            return "escrito"
        else:
            return "escrito"

    def _validar_orden_preferencia(self, orden: int) -> int:
        """Valida el orden de preferencia."""
        if not isinstance(orden, int) or orden < 1 or orden > self.MAX_PREFERENCIAS:
            raise ValueError(f"Orden debe estar entre 1 y {self.MAX_PREFERENCIAS}.")
        return orden

    def _validar_jornada(self, jornada: str) -> str:
        """Valida la jornada ingresada."""
        jornada = jornada.lower().strip()
        if jornada not in self.JORNADAS_VALIDAS:
            raise ValueError(f"Jornada inválida. Debe ser: {', '.join(self.JORNADAS_VALIDAS)}.")
        return jornada

    def obtenerEvaluacion(self):
        """Devuelve la evaluación asociada."""
        return self._evaluacion

    def __str__(self) -> str:
        return f"Inscripcion(ID:{self.id_inscripcion}, Postulante:{self.id_postulante}, Estado:{self.estado})"
