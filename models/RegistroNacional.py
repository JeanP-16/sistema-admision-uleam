"""
Módulo: RegistroNacional
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallo
Fecha: Octubre 2025
Descripcion: Gestiona el Registro Nacional del postulante segun SENESCYT
"""

from datetime import datetime
from typing import Optional, Dict
from abc import ABC, abstractmethod


# ===== CLASE BASE 1 =====
class DatosPersonales:
    """Clase para manejar datos personales basicos"""
    
    def __init__(self, identificacion: str, nombres: str, apellidos: str):
        self.identificacion = identificacion
        self.nombres = nombres
        self.apellidos = apellidos
    
    def obtener_nombre_completo(self) -> str:
        return f"{self.nombres} {self.apellidos}"


# ===== INTERFAZ (CLASE ABSTRACTA) =====
class Validable(ABC):
    """Interfaz para objetos que pueden ser validados"""
    
    @abstractmethod
    def validar_completitud(self) -> bool:
        """Metodo abstracto para validar completitud"""
        pass


# ===== HERENCIA MULTIPLE: RegistroNacional hereda de DatosPersonales y Validable =====
class RegistroNacional(DatosPersonales, Validable):
    """
    Gestiona el Registro Nacional completo del postulante.
    HERENCIA MULTIPLE: hereda de DatosPersonales y Validable
    """
    
    _contador = 0
    _registros_db = {}
    
    ESTADOS_REGISTRO = ['COMPLETO', 'INCOMPLETO']
    ESTADOS_HABILITACION = ['HABILITADO', 'NO HABILITADO', 'CONDICIONADO']
    
    def __init__(self, identificacion: str, nombres: str, apellidos: str):
        # Llamar al constructor de la primera clase padre
        super().__init__(identificacion, nombres, apellidos)
        
        RegistroNacional._contador += 1
        
        self.tipo_documento = 'CEDULA' if identificacion.isdigit() else 'PASAPORTE'
        self.nacionalidad = 'ECUATORIANA'
        self.codigo_nacionalidad = 218
        self.fecha_nacimiento = None
        self.estado_civil = 'S'
        self.sexo = None
        self.genero = None
        self.autoidentificacion = None
        self.pueblo_indigena = None
        self.edad = None
        
        self.carnet_discapacidad = None
        self.tipo_discapacidad = None
        self.porcentaje_discapacidad = 0
        self.requiere_apoyo = None
        
        self.identificacion_apoyo = None
        self.nombres_apoyo = None
        self.correo_apoyo = None
        
        self.pais_reside = 'ECUADOR'
        self.provincia_reside = None
        self.canton_reside = None
        self.parroquia_reside = None
        self.barrio_sector = None
        self.calle_principal = None
        
        self.celular = None
        self.correo = None
        
        self.internet_domicilio = 'NO'
        self.computadora_domicilio = 'NO'
        self.camara_web = 'NO'
        
        self.tipo_doc_rep_legal = None
        self.numero_doc_rep_legal = None
        self.nombre_rep_legal = None
        self.celular_rep_legal = None
        self.email_rep_legal = None
        
        self.titulo_homologado = 'NO'
        self.unidad_educativa = None
        self.tipo_unidad_educativa = None
        self.calificacion = None
        self.cuadro_honor = 'NO'
        self.ubicacion_cuadro_honor = None
        self.distincion_cuadro_honor = None
        
        self.titulo_tercer_nivel = 'NO'
        self.titulo_cuarto_nivel = 'NO'
        
        self.fecha_registro_nacional = datetime.now()
        self.estado = 'INCOMPLETO'
        self.tipo_poblacion = None
        self.ppl = 'NO'
        self.nombre_centro_ppl = None
        self.acepta_cupo_anterior = 'NO'
        self.estado_registro_nacional = 'NO HABILITADO'
        
        self.observacion_estado = None
        self.observacion_poblacion = None
        self.observacion_acepta_cupo = None
        
        RegistroNacional._registros_db[identificacion] = self
    
    def calcular_edad(self):
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
        self.fecha_nacimiento = fecha_nac
        self.sexo = sexo.upper()
        self.genero = 'MASCULINO' if sexo.upper() == 'HOMBRE' else 'FEMENINO'
        self.autoidentificacion = autoidentificacion.upper()
        self.calcular_edad()
    
    def completar_ubicacion(self, provincia: str, canton: str, parroquia: str, barrio: str, calle: str):
        self.provincia_reside = provincia
        self.canton_reside = canton
        self.parroquia_reside = parroquia
        self.barrio_sector = barrio
        self.calle_principal = calle
    
    def completar_contacto(self, celular: str, correo: str):
        self.celular = celular
        self.correo = correo.lower()
    
    def completar_datos_academicos(self, unidad_educativa: str, tipo_unidad: str, 
                                   calificacion: float, cuadro_honor: str = 'NO'):
        self.unidad_educativa = unidad_educativa
        self.tipo_unidad_educativa = tipo_unidad.upper()
        self.calificacion = calificacion
        self.cuadro_honor = cuadro_honor.upper()
        
        if self.calificacion:
            self.tipo_poblacion = 'NO ESCOLARES'
        else:
            self.tipo_poblacion = 'ESCOLARES'
    
    def registrar_discapacidad(self, carnet: str, tipo: str, porcentaje: int):
        self.carnet_discapacidad = carnet
        self.tipo_discapacidad = tipo.upper()
        self.porcentaje_discapacidad = porcentaje
        print(f" Discapacidad registrada: {tipo} ({porcentaje}%)")
    
    def asignar_persona_apoyo(self, identificacion: str, nombres: str, correo: str):
        self.identificacion_apoyo = identificacion
        self.nombres_apoyo = nombres
        self.correo_apoyo = correo
        print(f" Persona de apoyo: {nombres}")
    
    # IMPLEMENTACION del metodo abstracto de Validable (POLIMORFISMO)
    def validar_completitud(self) -> bool:
        """Implementa el metodo abstracto de la interfaz Validable"""
        if not all([self.nombres, self.apellidos, self.identificacion]):
            self.estado = 'INCOMPLETO'
            self.observacion_estado = "Faltan datos basicos"
            return False
        
        if not all([self.celular, self.correo]):
            self.estado = 'INCOMPLETO'
            self.observacion_estado = "Faltan datos de contacto"
            return False
        
        if not self.provincia_reside:
            self.estado = 'INCOMPLETO'
            self.observacion_estado = "Falta ubicacion"
            return False
        
        if self.tipo_poblacion == 'NO ESCOLARES' and not self.calificacion:
            self.estado = 'INCOMPLETO'
            self.observacion_poblacion = "Recuerda que para acceder a la educacion superior debes contar con un titulo de bachiller"
            return False
        
        self.estado = 'COMPLETO'
        self.estado_registro_nacional = 'HABILITADO'
        self.observacion_estado = None
        return True
    
    def validar_homologacion(self) -> bool:
        if self.nacionalidad == 'ECUATORIANA':
            return bool(self.calificacion)
        
        if self.titulo_homologado == 'SI':
            return True
        
        self.observacion_poblacion = "Titulo extranjero requiere homologacion del Ministerio de Educacion"
        return False
    
    def marcar_cupo_anterior(self, acepta: bool, periodo: str):
        self.acepta_cupo_anterior = 'SI' if acepta else 'NO'
        
        if acepta:
            self.estado_registro_nacional = 'CONDICIONADO'
            self.observacion_acepta_cupo = (f"Tiene un cupo aceptado en {periodo}, "
                                           "su proceso está condicionado al levantamiento "
                                           "del estado académico")
            print(f" Cupo anterior detectado: {periodo}")
    
    def mostrar_resumen_completo(self):
        print("\n" + "=" * 80)
        print(" RESUMEN COMPLETO DEL REGISTRO NACIONAL")
        print("=" * 80)
        
        # Datos personales
        print("\n  DATOS PERSONALES:")
        print(f"   Identificación: {self.identificacion} ({self.tipo_documento})")
        print(f"   Nombres Completos: {self.nombres} {self.apellidos}")
        print(f"   Fecha de Nacimiento: {self.fecha_nacimiento if self.fecha_nacimiento else 'No registrada'}")
        print(f"   Edad: {self.edad} años" if self.edad else "   Edad: No calculada")
        print(f"   Sexo: {self.sexo if self.sexo else 'No registrado'}")
        print(f"   Autoidentificacion: {self.autoidentificacion if self.autoidentificacion else 'No registrada'}")
        print(f"   Nacionalidad: {self.nacionalidad}")
        
        if self.provincia_reside:
            print("\n  UBICACIÓN:")
            print(f"   Provincia: {self.provincia_reside}")
            print(f"   Canton: {self.canton_reside}")
            print(f"   Parroquia: {self.parroquia_reside}")
            if self.barrio_sector:
                print(f"   Barrio/Sector: {self.barrio_sector}")
        
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
            print(f"   Calificacion: {self.calificacion}")
            print(f"   Cuadro de Honor: {self.cuadro_honor}")
            print(f"   Tipo Poblacion: {self.tipo_poblacion}")
        
        if self.carnet_discapacidad:
            print("\n  DISCAPACIDAD:")
            print(f"   Carnet: {self.carnet_discapacidad}")
            print(f"   Tipo: {self.tipo_discapacidad}")
            print(f"   Porcentaje: {self.porcentaje_discapacidad}%")
        
        # Estado del registro
        print("\n  ESTADO DEL REGISTRO:")
        print(f"   Estado: {self.estado}")
        print(f"   Habilitacion: {self.estado_registro_nacional}")
        print(f"   Fecha de Registro: {self.fecha_registro_nacional.strftime('%d/%m/%Y %H:%M:%S')}")
        
        if self.observacion_estado:
            print(f"\n     Observación: {self.observacion_estado}")
        
        print("=" * 80)
    
    def obtener_datos_completos(self) -> dict:
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
            'tipo_poblacion': self.tipo_poblacion,
            'fecha_registro': self.fecha_registro_nacional.strftime('%d/%m/%Y %H:%M'),
            'discapacidad': self.porcentaje_discapacidad if self.carnet_discapacidad else 'NO'
        }
    
    @staticmethod
    def consultar_por_cedula(identificacion: str) -> Optional['RegistroNacional']:
        return RegistroNacional._registros_db.get(identificacion)
    
    @staticmethod
    def existe_registro(identificacion: str) -> bool:
        return identificacion in RegistroNacional._registros_db
    
    @staticmethod
    def listar_todos_registros():
        if not RegistroNacional._registros_db:
            print("\n  No hay registros en el sistema")
            return
        
        print("\n" + "=" * 80)
        print(f" LISTA DE REGISTROS NACIONALES ({len(RegistroNacional._registros_db)} registros)")
        print("=" * 80)
        
        for i, (cedula, registro) in enumerate(RegistroNacional._registros_db.items(), 1):
            print(f"\n{i}. {registro.obtener_nombre_completo()}")
            print(f"   Cedula: {cedula}")
            print(f"   Estado: {registro.estado} | Habilitacion: {registro.estado_registro_nacional}")
            print(f"   Fecha: {registro.fecha_registro_nacional.strftime('%d/%m/%Y %H:%M')}")
        
        print("\n" + "=" * 80)
    
    def __str__(self) -> str:
        return f"RegistroNacional({self.obtener_nombre_completo()}, CI: {self.identificacion}, Estado: {self.estado})"
    
    @classmethod
    def obtener_total_registros(cls) -> int:
        return cls._contador
    
    @classmethod
    def cargar_registros_prueba(cls):
        """Carga 6 registros de prueba de forma silenciosa."""
        
        # 1. COMPLETO  - Jean Pierre
        r1 = cls("1316202082", "JEAN PIERRE", "FLORES PILOSO")
        r1.completar_datos_personales("2007-05-15", "HOMBRE", "MESTIZO")
        r1.completar_ubicacion("MANABI", "MANTA", "MANTA", "LOS ESTEROS", "AV. 24 DE MAYO")
        r1.completar_contacto("0999999999", "florespilosojeanpierre@gmail.com")
        r1.completar_datos_academicos("U.E. MANTA", "FISCAL", 9.5, "SI")
        r1.validar_completitud()
        
        # 2. INCOMPLETO  - María (Falta contacto)
        r2 = cls("1304567890", "MARÍA ELENA", "GARCÍA MENDOZA")
        r2.completar_datos_personales("2006-08-22", "MUJER", "MESTIZO")
        r2.completar_ubicacion("MANABI", "PORTOVIEJO", "PORTOVIEJO", "12 DE MARZO", "CALLE 10")
        r2.completar_datos_academicos("U.E. PORTOVIEJO", "FISCAL", 9.2, "NO")
        r2.validar_completitud()
        
        # 3. COMPLETO  - Braddy
        r3 = cls("1350432058", "BRADDY LONDRE", "VERA ANCHUNDIA")
        r3.completar_datos_personales("2007-03-20", "HOMBRE", "MONTUBIO")
        r3.completar_ubicacion("MANABI", "CHONE", "CHONE", "CENTRO", "CALLE PRINCIPAL")
        r3.completar_contacto("0988888888", "braddy.vera@uleam.edu.ec")
        r3.completar_datos_academicos("U.E. CHONE", "FISCAL", 9.0, "NO")
        r3.validar_completitud()
        
        # 4. INCOMPLETO  - Carlos (Falta ubicación)
        r4 = cls("1312345678", "CARLOS ANDRÉS", "MOREIRA CEDEÑO")
        r4.completar_datos_personales("2007-01-10", "HOMBRE", "MESTIZO")
        r4.completar_contacto("0966666666", "carlos.moreira@uleam.edu.ec")
        r4.completar_datos_academicos("U.E. CHONE", "FISCOMISIONAL", 8.7, "NO")
        r4.validar_completitud()
        
        # 5. COMPLETO  - Bismark
        r5 = cls("1360234567", "BISMARK GABRIEL", "CEVALLOS CEDEÑO")
        r5.completar_datos_personales("2007-07-10", "HOMBRE", "MESTIZO")
        r5.completar_ubicacion("MANABI", "MANTA", "MANTA", "TARQUI", "CALLE 10")
        r5.completar_contacto("0977777777", "bismark.cevallos@uleam.edu.ec")
        r5.completar_datos_academicos("U.E. PARTICULAR", "PARTICULAR", 8.8, "NO")
        r5.validar_completitud()
        
        # 6. INCOMPLETO  - Daniela (Falta datos académicos)
        r6 = cls("1355555555", "DANIELA STEFANIA", "MERA ANCHUNDIA")
        r6.completar_datos_personales("2006-11-15", "MUJER", "MESTIZO")
        r6.completar_ubicacion("MANABI", "JIPIJAPA", "JIPIJAPA", "CENTRO", "AV. PRINCIPAL")
        r6.completar_contacto("0955555555", "daniela.mera@uleam.edu.ec")
        r6.validar_completitud()
