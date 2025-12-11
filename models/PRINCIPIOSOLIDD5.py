"""
5 DOP 

CÓDIGO BUENO - APLICANDO PRINCIPIO D (INVERSIÓN DE DEPENDENCIAS)

SOLUCIÓN: Depender de abstracciones, NO de implementaciones concretas

MEJORA:
- InterfazBaseDatos: Abstracción para cualquier BD
- InterfazEmail: Abstracción para cualquier servicio de email
- Inscripcion recibe las dependencias (inyección de dependencias)

VENTAJAS:
- Fácil cambiar de MySQL a PostgreSQL
- Fácil cambiar de Gmail a Outlook
- Fácil hacer testing con mocks
- Bajo acoplamiento

Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
"""

#-Principio de inversión de dependencia
#Este principio señala que los módulos de alto nivel no deben de depender de los módulos de bajo nivel,
# ambos deben de depender de abstracciones y no de clases concretas.

from datetime import datetime


# ==================== ABSTRACCIÓN 1: BASE DE DATOS ====================
class InterfazBaseDatos:
    """Abstracción - Define QUÉ debe hacer cualquier BD"""
    
    def guardar_inscripcion(self, inscripcion):
        """Guarda una inscripción"""
        raise NotImplementedError("Debes implementar guardar_inscripcion()")
    
    def buscar_inscripcion(self, numero_inscripcion):
        """Busca una inscripción"""
        raise NotImplementedError("Debes implementar buscar_inscripcion()")


# ==================== ABSTRACCIÓN 2: SERVICIO DE EMAIL ====================
class InterfazEmail:
    """Abstracción - Define QUÉ debe hacer cualquier servicio de email"""
    
    def enviar_confirmacion(self, email, mensaje):
        """Envía email de confirmación"""
        raise NotImplementedError("Debes implementar enviar_confirmacion()")


# ==================== IMPLEMENTACIÓN CONCRETA: MySQL ====================
class BaseDatosMySQL(InterfazBaseDatos):
    """Implementación concreta de BD con MySQL"""
    
    def __init__(self):
        self.inscripciones = {}  # Simula tabla en MySQL
        print("Conectado a MySQL")
    
    def guardar_inscripcion(self, inscripcion):
        self.inscripciones[inscripcion.numero_inscripcion] = inscripcion
        print(f"MySQL: Inscripción {inscripcion.numero_inscripcion} guardada")
    
    def buscar_inscripcion(self, numero_inscripcion):
        return self.inscripciones.get(numero_inscripcion)


# ==================== IMPLEMENTACIÓN CONCRETA: PostgreSQL ====================
class BaseDatosPostgreSQL(InterfazBaseDatos):
    """Implementación alternativa con PostgreSQL"""
    
    def __init__(self):
        self.inscripciones = {}  # Simula tabla en PostgreSQL
        print("Conectado a PostgreSQL")
    
    def guardar_inscripcion(self, inscripcion):
        self.inscripciones[inscripcion.numero_inscripcion] = inscripcion
        print(f"PostgreSQL: Inscripción {inscripcion.numero_inscripcion} guardada")
    
    def buscar_inscripcion(self, numero_inscripcion):
        return self.inscripciones.get(numero_inscripcion)


# ==================== IMPLEMENTACIÓN CONCRETA: Gmail ====================
class ServicioGmail(InterfazEmail):
    """Implementación concreta con Gmail"""
    
    def __init__(self):
        print("Servicio Gmail inicializado")
    
    def enviar_confirmacion(self, email, mensaje):
        print(f"Gmail: Email enviado a {email}")
        print(f"   Mensaje: {mensaje}")


# ==================== IMPLEMENTACIÓN CONCRETA: Outlook ====================
class ServicioOutlook(InterfazEmail):
    """Implementación alternativa con Outlook"""
    
    def __init__(self):
        print("Servicio Outlook inicializado")
    
    def enviar_confirmacion(self, email, mensaje):
        print(f"Outlook: Email enviado a {email}")
        print(f"   Mensaje: {mensaje}")


# ==================== CLASE PRINCIPAL: INSCRIPCION ====================
class Inscripcion:
    """
    APLICA DIP: Depende de ABSTRACCIONES (InterfazBaseDatos, InterfazEmail)
    NO depende de IMPLEMENTACIONES concretas (MySQL, Gmail)
    """
    
    _contador = 0
    
    def __init__(self, postulante, carrera, periodo, 
                 base_datos: InterfazBaseDatos,      # Abstracción
                 servicio_email: InterfazEmail):     # Abstracción
        
        Inscripcion._contador += 1
        self.numero_inscripcion = f"INS-{Inscripcion._contador:04d}"
        
        # Datos de la inscripción
        self.postulante = postulante
        self.carrera = carrera
        self.periodo = periodo
        self.fecha_inscripcion = datetime.now()
        self.estado = 'PENDIENTE'
        
        # INYECCIÓN DE DEPENDENCIAS
        self.base_datos = base_datos           # Puede ser MySQL, PostgreSQL, etc.
        self.servicio_email = servicio_email   # Puede ser Gmail, Outlook, etc.
    
    def procesar_inscripcion(self):
        """Procesa la inscripción usando las dependencias inyectadas"""
        
        print(f"\n Procesando inscripción {self.numero_inscripcion}...")
        print(f"   Postulante: {self.postulante}")
        print(f"   Carrera: {self.carrera}")
        print(f"   Periodo: {self.periodo}")
        
        # 1. Guardar en base de datos (usa la abstracción)
        self.base_datos.guardar_inscripcion(self)
        
        # 2. Cambiar estado
        self.estado = 'CONFIRMADA'
        
        # 3. Enviar email (usa la abstracción)
        mensaje = f"Tu inscripción {self.numero_inscripcion} ha sido confirmada para {self.carrera}"
        self.servicio_email.enviar_confirmacion("postulante@mail.com", mensaje)
        
        print(f"Inscripción {self.numero_inscripcion} procesada exitosamente\n")
    
    def __str__(self):
        return f"Inscripcion[{self.numero_inscripcion}]: {self.postulante} -> {self.carrera} ({self.estado})"


# ==================== EJEMPLO DE USO ====================
if __name__ == "__main__":
    print("=" * 80)
    print("DEMOSTRACIÓN: PRINCIPIO D (DIP) - CÓDIGO BUENO")
    print("=" * 80)
    
    # EJEMPLO 1: Usando MySQL + Gmail
    print("\n1. CONFIGURACIÓN: MySQL + Gmail")
    print("-" * 40)
    bd_mysql = BaseDatosMySQL()
    email_gmail = ServicioGmail()
    
    inscripcion1 = Inscripcion(
        postulante="Juan Pérez",
        carrera="Ingeniería en Sistemas",
        periodo="2025-1",
        base_datos=bd_mysql,      # Inyectamos MySQL
        servicio_email=email_gmail # Inyectamos Gmail
    )
    inscripcion1.procesar_inscripcion()
    
    # EJEMPLO 2: Cambiamos a PostgreSQL + Outlook (¡SIN MODIFICAR Inscripcion!)
    print("\n2. CONFIGURACIÓN: PostgreSQL + Outlook")
    print("-" * 40)
    bd_postgres = BaseDatosPostgreSQL()
    email_outlook = ServicioOutlook()
    
    inscripcion2 = Inscripcion(
        postulante="María López",
        carrera="Medicina",
        periodo="2025-1",
        base_datos=bd_postgres,      # Inyectamos PostgreSQL
        servicio_email=email_outlook  # Inyectamos Outlook
    )
    inscripcion2.procesar_inscripcion()
    
    # EJEMPLO 3: Mezcla MySQL + Outlook
    print("\n3. CONFIGURACIÓN: MySQL + Outlook")
    print("-" * 40)
    inscripcion3 = Inscripcion(
        postulante="Pedro García",
        carrera="Administración",
        periodo="2025-1",
        base_datos=bd_mysql,          # MySQL
        servicio_email=email_outlook  # Outlook
    )
    inscripcion3.procesar_inscripcion()
    
    print("=" * 80)
    print("VENTAJAS DE DIP:")
    print("=" * 80)
    print("1. Cambiamos de MySQL a PostgreSQL SIN modificar clase Inscripcion")
    print("2. Cambiamos de Gmail a Outlook SIN modificar clase Inscripcion")
    print("3. Fácil hacer testing: inyectamos mocks en lugar de servicios reales")
    print("4. Bajo acoplamiento: Inscripcion no conoce implementaciones concretas")
    print("5. Inversión de dependencias: dependemos de abstracciones")
    print("")
    print("COMPARACIÓN:")
    print("MALO: Inscripcion crea instancias (self.bd = BaseDatosMySQL())")
    print("BUENO: Inscripcion recibe instancias (inyección de dependencias)")
    print("=" * 80)
