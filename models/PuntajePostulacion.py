"""
Módulo: PuntajePostulacion
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripción: Clase que calcula el puntaje final de postulación según SENESCYT
"""

from datetime import datetime
from typing import Optional

class PuntajePostulacion:
    """
    Calcula y gestiona el puntaje final de postulación.
    Según normativa SENESCYT: máximo 1000 puntos
    """
    
    _contador_puntajes = 0
    
    # Ponderaciones según SENESCYT
    PESO_NOTA_GRADO = 0.30      # 30% - Nota de grado (bachillerato)
    PESO_EVALUACION = 0.50      # 50% - Evaluación de aptitudes
    PESO_MERITO = 0.20          # 20% - Méritos adicionales
    
    PUNTAJE_MAXIMO = 1000
    
    def __init__(self,
                 id_postulante: int,
                 nota_grado: float,
                 puntaje_evaluacion: float,
                 cedula_postulante: str,
                 puntaje_meritos: float = 0.0):
        """
        Inicializa el cálculo de puntaje de postulación.
        
        Args:
            id_postulante: ID del postulante
            nota_grado: Nota de grado del bachillerato (sobre 10)
            puntaje_evaluacion: Puntaje de evaluación (sobre 1000)
            cedula_postulante: Cédula del postulante
            puntaje_meritos: Puntaje por méritos adicionales (sobre 1000)
        """
        PuntajePostulacion._contador_puntajes += 1
        
        self.id_puntaje = PuntajePostulacion._contador_puntajes
        self.id_postulante = id_postulante
        self.cedula_postulante = cedula_postulante
        
        # Validar y normalizar datos
        self.nota_grado = self._validar_nota_grado(nota_grado)
        self.puntaje_evaluacion = self._validar_puntaje(puntaje_evaluacion, "evaluacion")
        self.puntaje_meritos = self._validar_puntaje(puntaje_meritos, "meritos")
        
        self.fecha_calculo = datetime.now()
        
        # Calcular puntaje final automáticamente
        self.puntaje_final = self.calcularPuntajeTotal()
        
        self.observaciones = None
    
    def _validar_nota_grado(self, nota: float) -> float:
        """Valida que la nota de grado esté en escala 0-10."""
        if not 0 <= nota <= 10:
            raise ValueError("La nota de grado debe estar entre 0 y 10")
        return nota
    
    def _validar_puntaje(self, puntaje: float, tipo: str) -> float:
        """Valida que el puntaje esté entre 0 y 1000."""
        if not 0 <= puntaje <= self.PUNTAJE_MAXIMO:
            raise ValueError(f"El puntaje de {tipo} debe estar entre 0 y {self.PUNTAJE_MAXIMO}")
        return puntaje
    
    def calcularPuntajeTotal(self) -> float:
        """
        Calcula el puntaje total según la normativa SENESCYT.
        
        Fórmula:
        Puntaje Total = (Nota Grado * 100 * 0.30) + (Eval * 0.50) + (Meritos * 0.20)
        
        Returns:
            float: Puntaje total (máximo 1000 puntos)
        """
        # Convertir nota de grado (0-10) a escala de 1000
        puntaje_grado_normalizado = (self.nota_grado * 100)
        
        # Aplicar ponderaciones
        componente_grado = puntaje_grado_normalizado * self.PESO_NOTA_GRADO
        componente_evaluacion = self.puntaje_evaluacion * self.PESO_EVALUACION
        componente_meritos = self.puntaje_meritos * self.PESO_MERITO
        
        # Sumar componentes
        puntaje_total = componente_grado + componente_evaluacion + componente_meritos
        
        # Asegurar que no exceda el máximo
        puntaje_total = min(puntaje_total, self.PUNTAJE_MAXIMO)
        
        return round(puntaje_total, 2)
    
    def mostrar_desglose(self) -> None:
        """Muestra el desglose detallado del puntaje."""
        print("\n" + "=" * 60)
        print("DESGLOSE DE PUNTAJE")
        print("=" * 60)
        
        # Calcular componentes
        puntaje_grado_norm = (self.nota_grado * 100)
        comp_grado = puntaje_grado_norm * self.PESO_NOTA_GRADO
        comp_eval = self.puntaje_evaluacion * self.PESO_EVALUACION
        comp_meritos = self.puntaje_meritos * self.PESO_MERITO
        
        print(f"1. Nota de Grado (30%):")
        print(f"   Nota: {self.nota_grado}/10")
        print(f"   Normalizado: {puntaje_grado_norm}/1000")
        print(f"   Ponderado: {comp_grado:.2f} puntos")
        print()
        print(f"2. Evaluacion de Aptitudes (50%):")
        print(f"   Puntaje: {self.puntaje_evaluacion}/1000")
        print(f"   Ponderado: {comp_eval:.2f} puntos")
        print()
        print(f"3. Meritos Adicionales (20%):")
        print(f"   Puntaje: {self.puntaje_meritos}/1000")
        print(f"   Ponderado: {comp_meritos:.2f} puntos")
        print()
        print("=" * 60)
        print(f"PUNTAJE FINAL: {self.puntaje_final}/1000 puntos")
        print("=" * 60)
    
    def agregarObservaciones(self, texto: str) -> None:
        """Agrega observaciones al puntaje."""
        self.observaciones = texto
    
    def mostrar_info(self) -> None:
        """Muestra la información completa del puntaje."""
        print("\n" + "=" * 60)
        print(f"PUNTAJE POSTULACION ID: {self.id_puntaje}")
        print("=" * 60)
        print(f"Cedula Postulante: {self.cedula_postulante}")
        print(f"Postulante ID: {self.id_postulante}")
        print(f"Fecha calculo: {self.fecha_calculo.strftime('%d/%m/%Y %H:%M')}")
        print(f"\nCOMPONENTES:")
        print(f"  Nota de Grado: {self.nota_grado}/10")
        print(f"  Evaluacion: {self.puntaje_evaluacion}/1000")
        print(f"  Meritos: {self.puntaje_meritos}/1000")
        print(f"\nPUNTAJE FINAL: {self.puntaje_final}/1000")
        if self.observaciones:
            print(f"\nObservaciones: {self.observaciones}")
        print("=" * 60)
    
    def __str__(self) -> str:
        return f"PuntajePostulacion(ID:{self.id_puntaje}, Postulante:{self.id_postulante}, Puntaje:{self.puntaje_final})"
