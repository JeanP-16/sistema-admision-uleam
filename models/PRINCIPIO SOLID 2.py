"""
2 OCP

Se muestra un ejemplo de uso de CÓDIGO MALO - VIOLANDO PRINCIPIO O (ABIERTO/CERRADO)

PROBLEMA: No usa herencia ni polimorfismo
Maneja diferentes tipos de postulantes con if/elif

VIOLACIÓN OCP:
- Para agregar un nuevo tipo de postulante → hay que MODIFICAR esta clase
- Usa string 'tipo' en lugar de herencia
- Código cerrado para extensión

Autores: Jean Pierre Flores Piloso, 
         Braddy Londre Vera, 
         Bismark Grabriel Cevallos
Fecha: Noviembre 2025
"""
#2. Open/Closed Principle (OCP) - Principio de Abierto/Cerrado
#"Las entidades de software (clases, módulos, funciones, etc.) 
# deben estar abiertas para su extensión, pero cerradas para su modificación".

#En otras palabras, debes diseñar tus clases o módulos de manera que se puedan agregar nuevas 
#funcionalidades sin modificar el código existente. Esto se logra mediante
#  el uso de interfaces, herencia o composición.

from datetime import datetime
import re


class Postulante:
    """CLASE PROBLEMÁTICA - NO USA ABSTRACCIÓN NI HERENCIA"""
    
    _contador_postulantes = 0
    ESTADOS_VALIDOS = ['VERIFICADO', 'PENDIENTE', 'RECHAZADO']
    
    def __init__(self, cedula, nombre_completo, email, telefono, fecha_nacimiento, 
                 tipo='REGULAR'):
        
        Postulante._contador_postulantes += 1
        self.id_postulante = Postulante._contador_postulantes
        
        # Datos basicos
        self.cedula = cedula
        self.nombre_completo = nombre_completo
        self.email = email
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        
        self.tipo = tipo  # 'REGULAR', 'MENOR', 'EXTRANJERO', 'CON_CUPO'
        
        # Estado
        self.estado_registro = 'PENDIENTE'
        
        self.tutor_legal = None  # Para menores
        self.titulo_homologado = False  # Para extranjeros
        self.cupo_anterior = None  # Para con cupo
    
    def validarIdentidad(self):
        """VIOLA OCP: Usa if/elif para manejar diferentes tipos"""
        
        # BRANCH 1: REGULAR
        if self.tipo == 'REGULAR':
            if len(self.cedula) == 10 and self.cedula.isdigit():
                self.estado_registro = 'VERIFICADO'
                print(f" {self.nombre_completo} - Identidad verificada (REGULAR)")
                return True
            else:
                self.estado_registro = 'RECHAZADO'
                print(f" {self.nombre_completo} - Cédula inválida")
                return False
        
        #  BRANCH 2: MENOR
        elif self.tipo == 'MENOR':
            if not self.tutor_legal:
                print(f" {self.nombre_completo} es menor y necesita tutor legal")
                self.estado_registro = 'RECHAZADO'
                return False
            
            if len(self.cedula) == 10 and self.cedula.isdigit():
                self.estado_registro = 'VERIFICADO'
                print(f" {self.nombre_completo} - Menor verificado con tutor")
                return True
            return False
        
        #  BRANCH 3: EXTRANJERO
        elif self.tipo == 'EXTRANJERO':
            if not self.titulo_homologado:
                print(f" {self.nombre_completo} necesita título homologado")
                self.estado_registro = 'RECHAZADO'
                return False
            
            self.estado_registro = 'VERIFICADO'
            print(f" {self.nombre_completo} - Extranjero verificado")
            return True
        
        #  BRANCH 4: CON_CUPO
        elif self.tipo == 'CON_CUPO':
            if self.cupo_anterior:
                print(f" {self.nombre_completo} tiene cupo anterior")
                self.estado_registro = 'VERIFICADO'
                return True
            return False
        
        #  Para agregar nuevo tipo → modificar AQUÍ
        else:
            return False
    
    def calcularEdad(self):
        """ VIOLA OCP: Más lógica con if/elif"""
        fecha_nac = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.now()
        edad = hoy.year - fecha_nac.year
        
        if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
            edad -= 1
        
        #  BRANCH: Comportamiento especial para MENOR
        if self.tipo == 'MENOR':
            if edad >= 18:
                print(f" {self.nombre_completo} ya no es menor de edad")
                self.tipo = 'REGULAR'  #  Cambia tipo en runtime!
        
        return edad
    
    def puede_inscribirse(self):
        """ VIOLA OCP: OTRO método con if/elif"""
        
        # BRANCH: REGULAR
        if self.tipo == 'REGULAR':
            return self.estado_registro == 'VERIFICADO'
        
        #  BRANCH: MENOR
        elif self.tipo == 'MENOR':
            return self.estado_registro == 'VERIFICADO' and self.tutor_legal is not None
        
        #  BRANCH: EXTRANJERO
        elif self.tipo == 'EXTRANJERO':
            return self.estado_registro == 'VERIFICADO' and self.titulo_homologado
        
        #  BRANCH: CON_CUPO
        elif self.tipo == 'CON_CUPO':
            return False  # No puede inscribirse directamente
        
        #  Para agregar nuevo tipo → modificar AQUÍ TAMBIÉN
        else:
            return False
    
    def registrar_tutor(self, nombre_tutor, cedula_tutor):
        """Método solo para menores"""
        if self.tipo == 'MENOR':
            self.tutor_legal = {
                'nombre': nombre_tutor,
                'cedula': cedula_tutor
            }
            print(f" Tutor registrado para {self.nombre_completo}")
        else:
            print(f" Solo menores necesitan tutor")
    
    def marcar_titulo_homologado(self):
        """Método solo para extranjeros"""
        if self.tipo == 'EXTRANJERO':
            self.titulo_homologado = True
            print(f" Título homologado para {self.nombre_completo}")
        else:
            print(f" Solo extranjeros necesitan homologar título")
    
    def __str__(self):
        return f"Postulante[{self.tipo}]: {self.nombre_completo} - {self.estado_registro}"


# ==================== EJEMPLO DE USO ====================
if __name__ == "__main__":
    print("=" * 80)
    print("DEMOSTRACIÓN: PRINCIPIO O (OCP) - CÓDIGO MALO")
    print("=" * 80)
    
    # Crear postulante regular
    print("\n1. POSTULANTE REGULAR:")
    p1 = Postulante("1234567890", "Juan Pérez", "juan@mail.com", 
                    "0987654321", "1995-05-15", tipo='REGULAR')
    p1.validarIdentidad()
    print(f"   ¿Puede inscribirse? {p1.puede_inscribirse()}")
    
    # Crear postulante menor
    print("\n2. POSTULANTE MENOR:")
    p2 = Postulante("9876543210", "María López", "maria@mail.com",
                    "0912345678", "2008-03-20", tipo='MENOR')
    p2.validarIdentidad()  #  Rechazado - falta tutor
    p2.registrar_tutor("Pedro López", "1111111111")
    p2.validarIdentidad()  #  Verificado
    print(f"   ¿Puede inscribirse? {p2.puede_inscribirse()}")
    
    # Crear postulante extranjero
    print("\n3. POSTULANTE EXTRANJERO:")
    p3 = Postulante("PASS123456", "John Smith", "john@mail.com",
                    "0998877665", "1990-07-10", tipo='EXTRANJERO')
    p3.validarIdentidad()  #  Rechazado - falta homologación
    p3.marcar_titulo_homologado()
    p3.validarIdentidad()  #  Verificado
    print(f"   ¿Puede inscribirse? {p3.puede_inscribirse()}")
    
    print("\n" + "=" * 80)
    print(" PROBLEMAS DE ESTE CÓDIGO:")
    print("=" * 80)
    print("1. Para agregar tipo DISCAPACITADO necesitas modificar:")
    print("   - validarIdentidad() (agregar elif)")
    print("   - puede_inscribirse() (agregar elif)")
    print("   - Constructor (agregar atributos)")
    print("   - calcularEdad() (si aplica)")
    print("")
    print("2. Todos los postulantes tienen atributos de todos los tipos:")
    print("   - PostulanteRegular tiene 'tutor_legal' (no lo usa)")
    print("   - PostulanteExtranjero tiene 'cupo_anterior' (no lo usa)")
    print("")
    print("3. Código cerrado para extensión, abierto para modificación")
    print("   → VIOLA OCP")
    print("=" * 80)