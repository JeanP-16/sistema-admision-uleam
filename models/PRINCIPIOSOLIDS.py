"""
Módulo: PRINCIPIOSOLIDS - RegistroNacional REFACTORIZADO
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Gabriel Cevallos
Fecha: Diciembre 2025
Descripción: Versión BUENA que aplica el Principio S (SRP - Single Responsibility Principle)

PRINCIPIO S (SRP) - SINGLE RESPONSIBILITY PRINCIPLE:
"Una clase debe tener una sola razón para cambiar"

REFACTORIZACIÓN APLICADA:
- Separamos DatosPersonales en su propia clase
- Creamos interfaz Validable para validaciones
- RegistroNacional ahora hereda de ambas usando herencia múltiple
- Cada clase tiene UNA responsabilidad específica
"""

from datetime import datetime
from typing import Optional
from abc import ABC, abstractmethod


# ===== CLASE BASE 1: DATOS PERSONALES =====
class DatosPersonales:
    """
    Responsabilidad ÚNICA: Manejar datos personales básicos
    Aplica SRP: Solo gestiona información de identificación
    """
    
    def __init__(self, identificacion: str, nombres: str, apellidos: str):
        self.identificacion = identificacion
        self.nombres = nombres
        self.apellidos = apellidos
    
    def obtener_nombre_completo(self) -> str:
        """Retorna el nombre completo del postulante"""
        return f"{self.nombres} {self.apellidos}"


# ===== INTERFAZ (CLASE ABSTRACTA): VALIDABLE =====
class Validable(ABC):
    """
    Responsabilidad ÚNICA: Definir el contrato de validación
    Aplica SRP: Solo define qué debe validarse, no cómo
    """
    
    @abstractmethod
    def validar_completitud(self) -> bool:
        """Método abstracto que debe implementar toda clase validable"""
        pass


# ===== CLASE PRINCIPAL: REGISTRO NACIONAL =====
class RegistroNacional(DatosPersonales, Validable):
    """
    Gestiona el Registro Nacional completo del postulante
    
    APLICA SRP mediante:
    - Herencia múltiple: combina DatosPersonales + Validable
    - Cada clase padre tiene UNA responsabilidad
    - Esta clase SOLO coordina y gestiona el registro
    
    ANTES (MALO):
    - Una clase gigante con 700+ líneas
    - Manejaba datos personales, ubicación, contacto, académicos, validación, etc.
    
    AHORA (BUENO):
    - Responsabilidades separadas en clases distintas
    - Fácil de mantener y extender
    - Cada cambio afecta solo a una clase
    """
    
    _contador = 0
    _registros_db = {}
    
    ESTADOS_REGISTRO = ['COMPLETO', 'INCOMPLETO']
    ESTADOS_HABILITACION = ['HABILITADO', 'NO HABILITADO', 'CONDICIONADO']
    
    def __init__(self, identificacion: str, nombres: str, apellidos: str):
        # Llamar al constructor de DatosPersonales
        super().__init__(identificacion, nombres, apellidos)
        
        RegistroNacional._contador += 1
        
        # Tipo de documento
        self.tipo_documento = 'CEDULA' if identificacion.isdigit() else 'PASAPORTE'
        self.nacionalidad = 'ECUATORIANA'
        self.codigo_nacionalidad = 218
        
        # Datos personales adicionales
        self.fecha_nacimiento = None
        self.estado_civil = 'S'
        self.sexo = None
        self.genero = None
        self.autoidentificacion = None
        self.pueblo_indigena = None
        self.edad = None
        
        # Discapacidad
        self.carnet_discapacidad = None
        self.tipo_discapacidad = None
        self.porcentaje_discapacidad = 0
        self.requiere_apoyo = None
        
        # Persona de apoyo
        self.identificacion_apoyo = None
        self.nombres_apoyo = None
        self.correo_apoyo = None
        
        # Ubicación
        self.pais_reside = 'ECUADOR'
        self.provincia_reside = None
        self.canton_reside = None
        self.parroquia_reside = None
        self.barrio_sector = None
        self.calle_principal = None
        
        # Contacto
        self.celular = None
        self.correo = None
        
        # Recursos tecnológicos
        self.internet_domicilio = 'NO'
        self.computadora_domicilio = 'NO'
        self.camara_web = 'NO'
        
        # Representante legal (para menores)
        self.tipo_doc_rep_legal = None
        self.numero_doc_rep_legal = None
        self.nombre_rep_legal = None
        self.celular_rep_legal = None
        self.email_rep_legal = None
        
        # Datos académicos
        self.titulo_homologado = 'NO'
        self.unidad_educativa = None
        self.tipo_unidad_educativa = None
        self.calificacion = None
        self.cuadro_honor = 'NO'
        self.ubicacion_cuadro_honor = None
        self.distincion_cuadro_honor = None
        
        self.titulo_tercer_nivel = 'NO'
        self.titulo_cuarto_nivel = 'NO'
        
        # Estado del registro
        self.fecha_registro_nacional = datetime.now()
        self.estado = 'INCOMPLETO'
        self.tipo_poblacion = None
        self.ppl = 'NO'
        self.nombre_centro_ppl = None
        self.acepta_cupo_anterior = 'NO'
        self.estado_registro_nacional = 'NO HABILITADO'
        
        # Observaciones
        self.observacion_estado = None
        self.observacion_poblacion = None
        self.observacion_acepta_cupo = None
        
        # Guardar en BD simulada
        RegistroNacional._registros_db[identificacion] = self
    
    def calcular_edad(self):
        """Calcula la edad del postulante"""
        if self.fecha_nacimiento:
            if isinstance(self.fecha_nacimiento, str):
                fecha_nac = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
            else:
                fecha_nac = self.fecha_nacimiento
            
            hoy = datetime.now()
            self.edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            return self.edad
        return None
    
    def completar_datos_personales(self, fecha_nac: str, sexo: str, autoidentificacion: str):
        """Completa datos personales básicos"""
        self.fecha_nacimiento = fecha_nac
        self.sexo = sexo.upper()
        self.genero = 'MASCULINO' if sexo.upper() == 'HOMBRE' else 'FEMENINO'
        self.autoidentificacion = autoidentificacion.upper()
        self.calcular_edad()
    
    def completar_ubicacion(self, provincia: str, canton: str, parroquia: str, barrio: str, calle: str):
        """Completa datos de ubicación"""
        self.provincia_reside = provincia
        self.canton_reside = canton
        self.parroquia_reside = parroquia
        self.barrio_sector = barrio
        self.calle_principal = calle
    
    def completar_contacto(self, celular: str, correo: str):
        """Completa datos de contacto"""
        self.celular = celular
        self.correo = correo.lower()
    
    def completar_datos_academicos(self, unidad_educativa: str, tipo_unidad: str, 
                                   calificacion: float, cuadro_honor: str = 'NO'):
        """Completa datos académicos"""
        self.unidad_educativa = unidad_educativa
        self.tipo_unidad_educativa = tipo_unidad.upper()
        self.calificacion = calificacion
        self.cuadro_honor = cuadro_honor.upper()
        
        if self.calificacion:
            self.tipo_poblacion = 'NO ESCOLARES'
        else:
            self.tipo_poblacion = 'ESCOLARES'
    
    def registrar_discapacidad(self, carnet: str, tipo: str, porcentaje: int):
        """Registra información de discapacidad"""
        self.carnet_discapacidad = carnet
        self.tipo_discapacidad = tipo.upper()
        self.porcentaje_discapacidad = porcentaje
        print(f" ✓ Discapacidad registrada: {tipo} ({porcentaje}%)")
    
    def asignar_persona_apoyo(self, identificacion: str, nombres: str, correo: str):
        """Asigna persona de apoyo para postulantes con discapacidad"""
        self.identificacion_apoyo = identificacion
        self.nombres_apoyo = nombres
        self.correo_apoyo = correo
        print(f" ✓ Persona de apoyo: {nombres}")
    
    # IMPLEMENTACIÓN del método abstracto de Validable (POLIMORFISMO)
    def validar_completitud(self) -> bool:
        """
        Implementa el método abstracto de la interfaz Validable
        Valida que el registro esté completo
        """
        if not all([self.nombres, self.apellidos, self.identificacion]):
            self.estado = 'INCOMPLETO'
            self.observacion_estado = "Faltan datos básicos"
            return False
        
        if not all([self.celular, self.correo]):
            self.estado = 'INCOMPLETO'
            self.observacion_estado = "Faltan datos de contacto"
            return False
        
        if not self.provincia_reside:
            self.estado = 'INCOMPLETO'
            self.observacion_estado = "Falta ubicación"
            return False
        
        if not self.unidad_educativa:
            self.estado = 'INCOMPLETO'
            self.observacion_estado = "Faltan datos académicos"
            return False
        
        self.estado = 'COMPLETO'
        self.estado_registro_nacional = 'HABILITADO'
        self.observacion_estado = None
        return True
    
    def mostrar_resumen_completo(self):
        """Muestra resumen completo del registro"""
        print("\n" + "=" * 80)
        print(" RESUMEN COMPLETO DEL REGISTRO NACIONAL")
        print("=" * 80)
        
        print("\n  DATOS PERSONALES:")
        print(f"   Identificación: {self.identificacion} ({self.tipo_documento})")
        print(f"   Nombres Completos: {self.obtener_nombre_completo()}")
        print(f"   Fecha de Nacimiento: {self.fecha_nacimiento if self.fecha_nacimiento else 'No registrada'}")
        print(f"   Edad: {self.edad} años" if self.edad else "   Edad: No calculada")
        print(f"   Sexo: {self.sexo if self.sexo else 'No registrado'}")
        print(f"   Autoidentificación: {self.autoidentificacion if self.autoidentificacion else 'No registrada'}")
        
        if self.provincia_reside:
            print("\n  UBICACIÓN:")
            print(f"   Provincia: {self.provincia_reside}")
            print(f"   Cantón: {self.canton_reside}")
            print(f"   Parroquia: {self.parroquia_reside}")
        
        if self.celular or self.correo:
            print("\n  CONTACTO:")
            if self.celular:
                print(f"   Celular: {self.celular}")
            if self.correo:
                print(f"   Correo: {self.correo}")
        
        if self.unidad_educativa:
            print("\n  DATOS ACADÉMICOS:")
            print(f"   Unidad Educativa: {self.unidad_educativa}")
            print(f"   Tipo: {self.tipo_unidad_educativa}")
            print(f"   Calificación: {self.calificacion}")
            print(f"   Cuadro de Honor: {self.cuadro_honor}")
        
        print("\n  ESTADO DEL REGISTRO:")
        print(f"   Estado: {self.estado}")
        print(f"   Habilitación: {self.estado_registro_nacional}")
        print(f"   Fecha de Registro: {self.fecha_registro_nacional.strftime('%d/%m/%Y %H:%M:%S')}")
        
        if self.observacion_estado:
            print(f"\n     Observación: {self.observacion_estado}")
        
        print("=" * 80)
    
    def obtener_datos_completos(self) -> dict:
        """Retorna diccionario con todos los datos"""
        return {
            'identificacion': self.identificacion,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'nombre_completo': self.obtener_nombre_completo(),
            'tipo_documento': self.tipo_documento,
            'fecha_nacimiento': self.fecha_nacimiento,
            'edad': self.edad,
            'sexo': self.sexo,
            'autoidentificacion': self.autoidentificacion,
            'provincia': self.provincia_reside,
            'canton': self.canton_reside,
            'celular': self.celular,
            'correo': self.correo,
            'unidad_educativa': self.unidad_educativa,
            'calificacion': self.calificacion,
            'cuadro_honor': self.cuadro_honor,
            'estado': self.estado,
            'estado_habilitacion': self.estado_registro_nacional,
            'fecha_registro': self.fecha_registro_nacional.strftime('%d/%m/%Y %H:%M')
        }
    
    @staticmethod
    def consultar_por_cedula(identificacion: str) -> Optional['RegistroNacional']:
        """Busca un registro por cédula"""
        return RegistroNacional._registros_db.get(identificacion)
    
    @staticmethod
    def existe_registro(identificacion: str) -> bool:
        """Verifica si existe un registro"""
        return identificacion in RegistroNacional._registros_db
    
    @staticmethod
    def listar_todos_registros():
        """Lista todos los registros"""
        if not RegistroNacional._registros_db:
            print("\n  No hay registros en el sistema")
            return
        
        print("\n" + "=" * 80)
        print(f" LISTA DE REGISTROS NACIONALES ({len(RegistroNacional._registros_db)} registros)")
        print("=" * 80)
        
        for i, (cedula, registro) in enumerate(RegistroNacional._registros_db.items(), 1):
            print(f"\n{i}. {registro.obtener_nombre_completo()}")
            print(f"   Cédula: {cedula}")
            print(f"   Estado: {registro.estado} | Habilitación: {registro.estado_registro_nacional}")
        
        print("\n" + "=" * 80)
    
    def __str__(self) -> str:
        return f"RegistroNacional({self.obtener_nombre_completo()}, CI: {self.identificacion}, Estado: {self.estado})"
    
    @classmethod
    def obtener_total_registros(cls) -> int:
        """Retorna el total de registros creados"""
        return cls._contador


# ==================== EJEMPLOS DE USO ====================
if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("DEMOSTRACIÓN: PRINCIPIO S (SRP) - SINGLE RESPONSIBILITY PRINCIPLE")
    print("=" * 80)
    print("\nVERSIÓN BUENA: RegistroNacional refactorizado")
    print("\nClases separadas con responsabilidades únicas:")
    print("  1. DatosPersonales  → Maneja datos personales básicos")
    print("  2. Validable        → Define contrato de validación")
    print("  3. RegistroNacional → Coordina el registro completo")
    print("=" * 80)
    
    # Ejemplo 1: Registro completo
    print("\n\n📝 EJEMPLO 1: Registro Completo")
    print("-" * 80)
    
    registro1 = RegistroNacional(
        identificacion="1316202082",
        nombres="JEAN PIERRE",
        apellidos="FLORES PILOSO"
    )
    registro1.completar_datos_personales("2007-05-15", "HOMBRE", "MESTIZO")
    registro1.completar_ubicacion("MANABI", "MANTA", "MANTA", "LOS ESTEROS", "AV. 24 DE MAYO")
    registro1.completar_contacto("0999999999", "florespilosojeanpierre@gmail.com")
    registro1.completar_datos_academicos("U.E. MANTA", "FISCAL", 9.5, "SI")
    
    if registro1.validar_completitud():
        print("\n✅ Registro validado exitosamente")
        registro1.mostrar_resumen_completo()
    
    # Ejemplo 2: Registro incompleto
    print("\n\n📝 EJEMPLO 2: Registro Incompleto")
    print("-" * 80)
    
    registro2 = RegistroNacional(
        identificacion="1234567890",
        nombres="MARÍA",
        apellidos="GARCÍA"
    )
    registro2.completar_datos_personales("2006-08-22", "MUJER", "MESTIZO")
    
    if not registro2.validar_completitud():
        print(f"\n❌ Registro incompleto: {registro2.observacion_estado}")
