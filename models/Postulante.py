"""
Módulo: Postulante
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripcion: Clase que representa a un postulante en el sistema de admision ULEAM
"""

from datetime import datetime
from typing import Optional, List
import re
from abc import ABC, abstractmethod


# ===== CLASE ABSTRACTA (ABC) =====
class Persona(ABC):
    """Clase abstracta base para personas en el sistema"""
    
    def __init__(self, cedula: str, nombre_completo: str):
        self.cedula = cedula
        self.nombre_completo = nombre_completo
    
    @abstractmethod
    def validarIdentidad(self) -> bool:
        """Metodo abstracto que debe ser implementado"""
        pass
    
    @abstractmethod
    def calcularEdad(self) -> int:
        """Metodo abstracto para calcular edad"""
        pass


# ===== HERENCIA SIMPLE: Postulante hereda de Persona =====
class Postulante(Persona):
    """
    Representa a una persona que se postula al sistema de admision.
    HEREDA de la clase abstracta Persona
    """
    
    _contador_postulantes = 0
    ESTADOS_VALIDOS = ['VERIFICADO', 'PENDIENTE', 'RECHAZADO']
    
    def __init__(self, cedula: str, nombre_completo: str, email: str, 
                 telefono: str, fecha_nacimiento: str):
        # Llamar al constructor de la clase padre (Persona)
        super().__init__(cedula, nombre_completo)
        
        Postulante._contador_postulantes += 1
        self.id_postulante = Postulante._contador_postulantes
        
        self.cedula = self._validar_cedula(cedula)
        self.email = self._validar_email(email)
        self.telefono = telefono.strip()
        self.fecha_nacimiento = fecha_nacimiento
        self.estado_registro = 'PENDIENTE'
        self.fecha_registro = datetime.now()
        
        self._inscripciones = []
        self._puntajes = []
        self._asignacion = None
        
        print(f" Postulante creado: {self.nombre_completo} (ID: {self.id_postulante})")
    
    def _validar_cedula(self, cedula: str) -> str:
        cedula = cedula.strip()
        if not cedula.isdigit() or len(cedula) != 10:
            raise ValueError(f" Cédula inválida: debe tener 10 dígitos numéricos")
        
        # Verificar que los dos primeros dígitos sean válidos (01-24)
        provincia = int(cedula[:2])
        if provincia < 1 or provincia > 24:
            raise ValueError(f" Código de provincia inválido: {provincia}")
        
        return cedula
    
    def _validar_email(self, email: str) -> str:
        email = email.strip().lower()
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, email):
            raise ValueError(f" Email inválido: {email}")
        
        return email
    
    # IMPLEMENTACION de metodo abstracto (POLIMORFISMO)
    def validarIdentidad(self) -> bool:
        """Implementa el metodo abstracto de Persona"""
        es_valido = len(self.cedula) == 10 and self.cedula.isdigit()
        
        if es_valido:
            self.estado_registro = 'VERIFICADO'
            print(f" Identidad verificada: {self.nombre_completo}")
        else:
            self.estado_registro = 'RECHAZADO'
            print(f" Identidad rechazada: {self.nombre_completo}")
        
        return es_valido
    
    def actualizarDatos(self, email: Optional[str] = None, 
                       telefono: Optional[str] = None) -> None:
        """
        Actualiza los datos de contacto del postulante.
        
        Args:
            email: Nuevo email (opcional)
            telefono: Nuevo teléfono (opcional)
        """
        if email:
            self.email = self._validar_email(email)
            print(f" Email actualizado: {self.email}")
        
        if telefono:
            self.telefono = telefono.strip()
            print(f" Teléfono actualizado: {self.telefono}")
    
    def obtenerInscripciones(self) -> List:
        """
        Obtiene todas las inscripciones del postulante.
        
        Returns:
            List: Lista de inscripciones
        """
        return self._inscripciones.copy()
    
    def agregarInscripcion(self, inscripcion) -> None:
        """
        Agrega una inscripción al postulante.
        
        Args:
            inscripcion: Objeto Inscripcion
        """
        self._inscripciones.append(inscripcion)
        print(f" Inscripción agregada para {self.nombre_completo}")
    
    def obtenerPuntajes(self) -> List:
        """
        Obtiene todos los puntajes del postulante.
        
        Returns:
            List: Lista de puntajes
        """
        return self._puntajes.copy()
    
    def tieneAsignacionActiva(self) -> bool:
        """
        Verifica si el postulante tiene una asignación activa.
        
        Returns:
            bool: True si tiene asignación activa
        """
        return self._asignacion is not None
    
    def calcularEdad(self) -> int:
        """Implementa el metodo abstracto de Persona"""
        fecha_nac = datetime.strptime(self.fecha_nacimiento, '%Y-%m-%d')
        hoy = datetime.now()
        edad = hoy.year - fecha_nac.year
        
        if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
            edad -= 1
        
        return edad
    
    # DECORADOR @property
    @property
    def nombre_apellidos(self):
        """Property para obtener nombre completo"""
        return self.nombre_completo
    
    def actualizarDatos(self, email: Optional[str] = None, 
                       telefono: Optional[str] = None) -> None:
        if email:
            self.email = self._validar_email(email)
            print(f"Email actualizado: {self.email}")
        
        if telefono:
            self.telefono = telefono.strip()
            print(f"Telefono actualizado: {self.telefono}")
    
    def obtenerInscripciones(self) -> List:
        return self._inscripciones.copy()
    
    def agregarInscripcion(self, inscripcion) -> None:
        self._inscripciones.append(inscripcion)
        print(f"Inscripcion agregada para {self.nombre_completo}")
    
    def obtenerPuntajes(self) -> List:
        return self._puntajes.copy()
    
    def tieneAsignacionActiva(self) -> bool:
        return self._asignacion is not None
    
    def __str__(self) -> str:
        return (f"Postulante(ID: {self.id_postulante}, "
                f"Nombre: {self.nombre_completo}, "
                f"Cedula: {self.cedula}, "
                f"Estado: {self.estado_registro})")
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @classmethod
    def obtener_total_postulantes(cls) -> int:
        return cls._contador_postulantes


if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBA DEL MODULO POSTULANTE CON HERENCIA")
    print("=" * 60)
    
    try:
        postulante1 = Postulante(
            cedula="1316202082",
            nombre_completo="Jean Pierre Flores Piloso",
            email="florespilosojeanpierre@gmail.com",
            telefono="0979421538",
            fecha_nacimiento="2007-03-01"
        )
        
        postulante1.validarIdentidad()
        print(f"\n{postulante1}")
        print(f"Edad: {postulante1.calcularEdad()} años")
        print(f"Nombre (property): {postulante1.nombre_apellidos}")
        
        postulante1.actualizarDatos(telefono="0979421538")
        
        print(f"\n Total de postulantes: {Postulante.obtener_total_postulantes()}")
        
    except ValueError as e:
        print(f" Error: {e}")
    
    print("\n" + "=" * 60)
