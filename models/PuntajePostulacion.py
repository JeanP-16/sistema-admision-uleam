"""
Módulo: PuntajePostulacion
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripcion: Clase que calcula el puntaje final de postulacion segun SENESCYT
"""

from datetime import datetime
from typing import Optional


# ===== CLASE BASE CON DECORADORES =====
class PuntajePostulacion:
    """
    Calcula y gestiona el puntaje final de postulacion.
    Segun normativa SENESCYT: maximo 1000 puntos
    Incluye DECORADORES @property y @classmethod
    """
    
    _contador_puntajes = 0
    
    PESO_NOTA_GRADO = 0.30
    PESO_EVALUACION = 0.50
    PESO_MERITO = 0.20
    PUNTAJE_MAXIMO = 1000
    
    def _init_(self,
                 id_postulante: int,
                 nota_grado: float,
                 puntaje_evaluacion: float,
                 cedula_postulante: str,
                 puntaje_meritos: float = 0.0):
        PuntajePostulacion._contador_puntajes += 1
        
        self.id_puntaje = PuntajePostulacion._contador_puntajes
        self.id_postulante = id_postulante
        self.cedula_postulante = cedula_postulante
        
        self._nota_grado = self._validar_nota_grado(nota_grado)
        self._puntaje_evaluacion = self._validar_puntaje(puntaje_evaluacion, "evaluacion")
        self._puntaje_meritos = self._validar_puntaje(puntaje_meritos, "meritos")
        
        self.fecha_calculo = datetime.now()
        self._puntaje_final = self.calcularPuntajeTotal()
        self.observaciones = None
    
    def _validar_nota_grado(self, nota: float) -> float:
        if not 0 <= nota <= 10:
            raise ValueError("La nota de grado debe estar entre 0 y 10")
        return nota
    
    def _validar_puntaje(self, puntaje: float, tipo: str) -> float:
        if not 0 <= puntaje <= self.PUNTAJE_MAXIMO:
            raise ValueError(f"El puntaje de {tipo} debe estar entre 0 y {self.PUNTAJE_MAXIMO}")
        return puntaje
    
    # DECORADORES @property (ENCAPSULAMIENTO)
    @property
    def nota_grado(self) -> float:
        """Getter para nota de grado"""
        return self._nota_grado
    
    @property
    def puntaje_evaluacion(self) -> float:
        """Getter para puntaje de evaluacion"""
        return self._puntaje_evaluacion
    
    @property
    def puntaje_meritos(self) -> float:
        """Getter para puntaje de meritos"""
        return self._puntaje_meritos
    
    @property
    def puntaje_final(self) -> float:
        """Getter para puntaje final"""
        return self._puntaje_final
    
    # DECORADOR @property con setter
    @puntaje_meritos.setter
    def puntaje_meritos(self, valor: float):
        """Setter para actualizar meritos y recalcular"""
        self._puntaje_meritos = self._validar_puntaje(valor, "meritos")
        self._puntaje_final = self.calcularPuntajeTotal()
    
    def calcularPuntajeTotal(self) -> float:
        """Calcula el puntaje total segun la normativa SENESCYT"""
        puntaje_grado_normalizado = (self._nota_grado * 100)
        
        componente_grado = puntaje_grado_normalizado * self.PESO_NOTA_GRADO
        componente_evaluacion = self._puntaje_evaluacion * self.PESO_EVALUACION
        componente_meritos = self._puntaje_meritos * self.PESO_MERITO
        
        puntaje_total = componente_grado + componente_evaluacion + componente_meritos
        puntaje_total = min(puntaje_total, self.PUNTAJE_MAXIMO)
        
        return round(puntaje_total, 2)
    
    def mostrar_desglose(self) -> None:
        print("\n" + "=" * 60)
        print("DESGLOSE DE PUNTAJE")
        print("=" * 60)
        
        puntaje_grado_norm = (self._nota_grado * 100)
        comp_grado = puntaje_grado_norm * self.PESO_NOTA_GRADO
        comp_eval = self._puntaje_evaluacion * self.PESO_EVALUACION
        comp_meritos = self._puntaje_meritos * self.PESO_MERITO
        
        print(f"1. Nota de Grado (30%):")
        print(f"   Nota: {self._nota_grado}/10")
        print(f"   Normalizado: {puntaje_grado_norm}/1000")
        print(f"   Ponderado: {comp_grado:.2f} puntos")
        print()
        print(f"2. Evaluacion de Aptitudes (50%):")
        print(f"   Puntaje: {self._puntaje_evaluacion}/1000")
        print(f"   Ponderado: {comp_eval:.2f} puntos")
        print()
        print(f"3. Meritos Adicionales (20%):")
        print(f"   Puntaje: {self._puntaje_meritos}/1000")
        print(f"   Ponderado: {comp_meritos:.2f} puntos")
        print()
        print("=" * 60)
        print(f"PUNTAJE FINAL: {self._puntaje_final}/1000 puntos")
        print("=" * 60)
    
    def agregarObservaciones(self, texto: str) -> None:
        self.observaciones = texto
    
    def mostrar_info(self) -> None:
        print("\n" + "=" * 60)
        print(f"PUNTAJE POSTULACION ID: {self.id_puntaje}")
        print("=" * 60)
        print(f"Cedula Postulante: {self.cedula_postulante}")
        print(f"Postulante ID: {self.id_postulante}")
        print(f"Fecha calculo: {self.fecha_calculo.strftime('%d/%m/%Y %H:%M')}")
        print(f"\nCOMPONENTES:")
        print(f"  Nota de Grado: {self._nota_grado}/10")
        print(f"  Evaluacion: {self._puntaje_evaluacion}/1000")
        print(f"  Meritos: {self._puntaje_meritos}/1000")
        print(f"\nPUNTAJE FINAL: {self._puntaje_final}/1000")
        if self.observaciones:
            print(f"\nObservaciones: {self.observaciones}")
        print("=" * 60)
    
    def _str_(self) -> str:
        return f"PuntajePostulacion(ID:{self.id_puntaje}, Postulante:{self.id_postulante}, Puntaje:{self.puntaje_final})"