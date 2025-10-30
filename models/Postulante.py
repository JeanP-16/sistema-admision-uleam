"""
Módulo: Postulante
Autor: Jean Pierre Flores Piloso
Fecha: Octubre 2025
Descripción: Clase que representa a un postulante en el sistema de admisión ULEAM
"""

from datetime import datetime
from typing import Optional, List
import re


class Postulante:
    """
    Representa a una persona que se postula al sistema de admisión.
    
    Attributes:
        id_postulante       (int):      Identificador único del postulante
        cedula              (str):      Número de cédula (10 dígitos)
        nombre_completo     (str):      Nombre completo del postulante
        email               (str):      Correo electrónico
        telefono            (str):      Número de teléfono
        fecha_nacimiento    (str):      Fecha de nacimiento (formato: YYYY-MM-DD)
        estado_registro     (str):      Estado del registro nacional
        fecha_registro      (datetime): Fecha de registro en el sistema
    """
    
    # Atributo de clase - contador de postulantes
    _contador_postulantes = 0
    
    # Estados válidos
    ESTADOS_VALIDOS = ['VERIFICADO', 'PENDIENTE', 'RECHAZADO']
    
    def __init__(self, cedula: str, nombre_completo: str, email: str, 
                 telefono: str, fecha_nacimiento: str):
        """
        Inicializa un nuevo postulante.
        
        Args:
            cedula:                 Número de cédula de identidad
            nombre_completo:        Nombre completo del postulante
            email:                  Correo electrónico
            telefono:               Número de teléfono
            fecha_nacimiento:       Fecha de nacimiento (YYYY-MM-DD)
        Raises:
            ValueError: Si los datos no son válidos
        """
        # Incrementar contador y asignar ID
        Postulante._contador_postulantes += 1
        self.id_postulante = Postulante._contador_postulantes
        
        # Validar y asignar atributos
        self.cedula = self._validar_cedula(cedula)
        self.nombre_completo = nombre_completo.strip()
        self.email = self._validar_email(email)
        self.telefono = telefono.strip()
        self.fecha_nacimiento = fecha_nacimiento
        self.estado_registro = 'PENDIENTE'
        self.fecha_registro = datetime.now()
        
        # Listas relacionadas (inicialmente vacías)
        self._inscripciones = []
        self._puntajes = []
        self._asignacion = None
        
        print(f"✅ Postulante creado: {self.nombre_completo} (ID: {self.id_postulante})")
    
    def _validar_cedula(self, cedula: str) -> str:
        """
        Valida el formato de la cédula ecuatoriana.
        Args:
            cedula: Número de cédula a validar  
        Returns:
            str: Cédula validada 
        Raises:
            ValueError: Si la cédula no es válida
        """
        cedula = cedula.strip()
        
        # Verificar que tenga 10 dígitos
        if not cedula.isdigit() or len(cedula) != 10:
            raise ValueError(f"❌ Cédula inválida: debe tener 10 dígitos numéricos")
        
        # Verificar que los dos primeros dígitos sean válidos (01-24)
        provincia = int(cedula[:2])
        if provincia < 1 or provincia > 24:
            raise ValueError(f"❌ Código de provincia inválido: {provincia}")
        
        return cedula
    
    def _validar_email(self, email: str) -> str:
        """
        Valida el formato del email.
        
        Args:
            email: Correo electrónico a validar
            
        Returns:
            str: Email validado
            
        Raises:
            ValueError: Si el email no es válido
        """
        email = email.strip().lower()
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(patron, email):
            raise ValueError(f"❌ Email inválido: {email}")
        
        return email
    
    def validarIdentidad(self) -> bool:
        """
        Verifica la identidad del postulante con el registro nacional.
        
        En producción, esto consultaría DIGERCIC.
        Por ahora, solo valida el formato.
        
        Returns:
            bool: True si la identidad es válida
        """
        # Aquí iría la integración con DIGERCIC
        # Por ahora, solo validamos formato
        es_valido = len(self.cedula) == 10 and self.cedula.isdigit()
        
        if es_valido:
            self.estado_registro = 'VERIFICADO'
            print(f"✅ Identidad verificada: {self.nombre_completo}")
        else:
            self.estado_registro = 'RECHAZADO'
            print(f"❌ Identidad rechazada: {self.nombre_completo}")
        
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
            print(f"📧 Email actualizado: {self.email}")
        
        if telefono:
            self.telefono = telefono.strip()
            print(f"📱 Teléfono actualizado: {self.telefono}")
    
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
        print(f"📝 Inscripción agregada para {self.nombre_completo}")
    
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
        """
        Calcula la edad del postulante.
        
        Returns:
            int: Edad en años
        """
        fecha_nac = datetime.strptime(self.fecha_nacimiento, '%Y-%m-%d')
        hoy = datetime.now()
        edad = hoy.year - fecha_nac.year
        
        # Ajustar si no ha cumplido años este año
        if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
            edad -= 1
        
        return edad
    
    def __str__(self) -> str:
        """Representación en string del postulante."""
        return (f"Postulante(ID: {self.id_postulante}, "
                f"Nombre: {self.nombre_completo}, "
                f"Cédula: {self.cedula}, "
                f"Estado: {self.estado_registro})")
    
    def __repr__(self) -> str:
        """Representación técnica del postulante."""
        return self.__str__()
    
    @classmethod
    def obtener_total_postulantes(cls) -> int:
        """
        Obtiene el total de postulantes registrados.
        
        Returns:
            int: Número total de postulantes
        """
        return cls._contador_postulantes


# ========== EJEMPLO DE USO ==========
if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBA DEL MÓDULO POSTULANTE")
    print("=" * 60)
    
    try:
        # Crear postulante 1
        postulante1 = Postulante(
            cedula="1316202082",
            nombre_completo="Jean Pierre Flores Piloso",
            email="florespilosojeanpierre@gmail.com",
            telefono="0979421538",
            fecha_nacimiento="2007-03-01"
        )
        
        # Validar identidad
        postulante1.validarIdentidad()
        
        # Mostrar información
        print(f"\n{postulante1}")
        print(f"Edad: {postulante1.calcularEdad()} años")
        
        # Actualizar datos
        postulante1.actualizarDatos(telefono="0979421538")
        
        print(f"\n📊 Total de postulantes: {Postulante.obtener_total_postulantes()}")
        
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)