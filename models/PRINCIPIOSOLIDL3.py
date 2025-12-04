"""
3 LISKOV

Se muestra un ejemplo de uso de CÓDIGO MALO - VIOLANDO MÚLTIPLES PRINCIPIOS SOLID

VIOLACIONES:
- S (SRP): Mezcla múltiples responsabilidades
- O (OCP): Usa if/elif en lugar de polimorfismo
- I (ISP): Interfaz grande que obliga métodos innecesarios
- D (DIP): Dependencias directas de implementaciones concretas

Autores: Jean Pierre Flores Piloso, 
         Braddy Londre Vera, 
         Bismark Grabriel Cevallos
"""
#. Liskov Substitution Principle (LSP) - Principio de Sustitución de Liskov
#"Las subclases deben ser sustituibles por sus clases base".

#En otras palabras, cualquier código que utilice una clase base debe poder funcionar con 
#una subclase sin saberlo. Esto significa que las subclases no deben romper las expectativas de la clase base.
class SedeCampus:
    """ CLASE PROBLEMÁTICA - Viola múltiples principios SOLID"""
    
    def __init__(self, codigo_sede, nombre_sede, tipo_sede='PRINCIPAL'):
        # Datos básicos
        self.codigo_sede = codigo_sede
        self.nombre_sede = nombre_sede
        
        #  VIOLA OCP: Tipo como string
        self.tipo_sede = tipo_sede  # 'PRINCIPAL', 'EXTENSION', 'VIRTUAL'
        
        #  VIOLA SRP: Responsabilidad 1 - Carreras
        self.carreras_disponibles = []
        
        #  VIOLA SRP: Responsabilidad 2 - Infraestructura
        self.edificios = []
        self.aulas = []
        self.laboratorios = []
        
        #  VIOLA SRP: Responsabilidad 3 - Personal
        self.personal = []
        self.directores = []
        
        #  VIOLA SRP: Responsabilidad 4 - Ubicación
        self.provincia = None
        self.canton = None
        self.direccion = None
        
        #  VIOLA SRP: Responsabilidad 5 - Estudiantes
        self.estudiantes_inscritos = []
        self.capacidad_total = 0
        
        #  VIOLA DIP: Crea instancias directamente
        self.base_datos = "MySQL"  # Hardcodeado
        self.sistema_notificaciones = "Email"  # Hardcodeado
    
    def agregar_carrera(self, carrera):
        """ VIOLA OCP: Lógica con if/elif según tipo de sede"""
        
        #  BRANCH 1: PRINCIPAL
        if self.tipo_sede == 'PRINCIPAL':
            self.carreras_disponibles.append(carrera)
            print(f" Carrera '{carrera}' agregada a sede PRINCIPAL {self.nombre_sede}")
        
        #  BRANCH 2: EXTENSION
        elif self.tipo_sede == 'EXTENSION':
            # Extensiones solo ciertas carreras
            carreras_permitidas = ['Administración', 'Turismo', 'Agropecuaria']
            if carrera in carreras_permitidas:
                self.carreras_disponibles.append(carrera)
                print(f" Carrera '{carrera}' agregada a EXTENSIÓN {self.nombre_sede}")
            else:
                print(f" Carrera '{carrera}' no permitida en extensión")
        
        #  BRANCH 3: VIRTUAL
        elif self.tipo_sede == 'VIRTUAL':
            # Virtual solo modalidad online
            self.carreras_disponibles.append(f"{carrera} (ONLINE)")
            print(f" Carrera '{carrera}' agregada en modalidad VIRTUAL")
        
        #  Para agregar nuevo tipo → modificar AQUÍ
        else:
            print(f" Tipo de sede '{self.tipo_sede}' no reconocido")
    
    def agregar_edificio(self, edificio):
        """ VIOLA OCP: Más if/elif"""
        
        if self.tipo_sede == 'PRINCIPAL':
            self.edificios.append(edificio)
            print(f" Edificio '{edificio}' agregado")
        elif self.tipo_sede == 'EXTENSION':
            print(f" Extensiones no tienen edificios propios")
        elif self.tipo_sede == 'VIRTUAL':
            print(f" Sedes virtuales no tienen edificios físicos")
    
    def agregar_aula(self, aula, capacidad):
        """ VIOLA SRP: Manejo de infraestructura mezclado"""
        self.aulas.append({'nombre': aula, 'capacidad': capacidad})
        self.capacidad_total += capacidad
        print(f" Aula '{aula}' agregada (capacidad: {capacidad})")
    
    def agregar_personal(self, nombre, cargo):
        """ VIOLA SRP: Manejo de personal mezclado"""
        self.personal.append({'nombre': nombre, 'cargo': cargo})
        if cargo == 'DIRECTOR':
            self.directores.append(nombre)
        print(f" Personal agregado: {nombre} - {cargo}")
    
    def establecer_ubicacion(self, provincia, canton, direccion):
        """ VIOLA SRP: Manejo de ubicación mezclado"""
        self.provincia = provincia
        self.canton = canton
        self.direccion = direccion
        print(f" Ubicación: {provincia}, {canton}")
    
    def inscribir_estudiante(self, estudiante):
        """ VIOLA SRP + DIP: Manejo de estudiantes + BD hardcodeada"""
        
        #  Lógica de negocio mezclada
        if len(self.estudiantes_inscritos) < self.capacidad_total:
            self.estudiantes_inscritos.append(estudiante)
            
            #  VIOLA DIP: Dependencia directa de implementación
            if self.base_datos == "MySQL":
                print(f" MySQL: Estudiante {estudiante} guardado")
            elif self.base_datos == "PostgreSQL":
                print(f" PostgreSQL: Estudiante {estudiante} guardado")
            
            #  VIOLA DIP: Otra dependencia directa
            if self.sistema_notificaciones == "Email":
                print(f" Email enviado a {estudiante}")
            elif self.sistema_notificaciones == "SMS":
                print(f" SMS enviado a {estudiante}")
            
            return True
        else:
            print(f" Capacidad completa en {self.nombre_sede}")
            return False
    
    def generar_reporte_completo(self):
        """ VIOLA SRP: Generación de reportes mezclada"""
        
        print("\n" + "=" * 70)
        print(f"REPORTE COMPLETO - {self.nombre_sede}")
        print("=" * 70)
        
        # Información básica
        print(f"\nTipo de Sede: {self.tipo_sede}")
        print(f"Código: {self.codigo_sede}")
        
        #  Lógica de presentación mezclada con datos
        if self.provincia:
            print(f"\nUbicación:")
            print(f"  Provincia: {self.provincia}")
            print(f"  Cantón: {self.canton}")
            print(f"  Dirección: {self.direccion}")
        
        print(f"\nCarreras Disponibles: {len(self.carreras_disponibles)}")
        for carrera in self.carreras_disponibles:
            print(f"  - {carrera}")
        
        print(f"\nInfraestructura:")
        print(f"  Edificios: {len(self.edificios)}")
        print(f"  Aulas: {len(self.aulas)}")
        print(f"  Laboratorios: {len(self.laboratorios)}")
        
        print(f"\nPersonal: {len(self.personal)}")
        print(f"  Directores: {len(self.directores)}")
        
        print(f"\nEstudiantes:")
        print(f"  Inscritos: {len(self.estudiantes_inscritos)}")
        print(f"  Capacidad Total: {self.capacidad_total}")
        
        print("=" * 70 + "\n")
    
    def validar_sede(self):
        """ VIOLA SRP: Validación mezclada"""
        
        errores = []
        
        if not self.nombre_sede:
            errores.append("Falta nombre de sede")
        
        if not self.provincia:
            errores.append("Falta ubicación")
        
        if len(self.carreras_disponibles) == 0:
            errores.append("No hay carreras disponibles")
        
        if len(errores) > 0:
            print(" ERRORES EN VALIDACIÓN:")
            for error in errores:
                print(f"  - {error}")
            return False
        
        print(" Sede validada correctamente")
        return True


# ==================== EJEMPLO DE USO ====================
if __name__ == "__main__":
    print("=" * 80)
    print("DEMOSTRACIÓN: CÓDIGO MALO - Violando múltiples principios SOLID")
    print("=" * 80)
    
    # Crear sede principal
    print("\n1. SEDE PRINCIPAL:")
    sede1 = SedeCampus("SEDE-001", "Campus Central Manta", tipo='PRINCIPAL')
    sede1.establecer_ubicacion("MANABÍ", "MANTA", "Av. Principal 123")
    sede1.agregar_edificio("Edificio A")
    sede1.agregar_aula("A-101", 40)
    sede1.agregar_aula("A-102", 35)
    sede1.agregar_carrera("Ingeniería en Sistemas")
    sede1.agregar_carrera("Medicina")
    sede1.agregar_personal("Dr. Juan Pérez", "DIRECTOR")
    sede1.inscribir_estudiante("María López")
    sede1.validar_sede()
    
    # Crear sede extensión
    print("\n2. SEDE EXTENSIÓN:")
    sede2 = SedeCampus("SEDE-002", "Extensión Pedernales", tipo='EXTENSION')
    sede2.establecer_ubicacion("MANABÍ", "PEDERNALES", "Calle Principal")
    sede2.agregar_edificio("Edificio B")  #  No debería poder
    sede2.agregar_carrera("Administración")  #  Permitida
    sede2.agregar_carrera("Medicina")  #  No permitida en extensión
    
    # Crear sede virtual
    print("\n3. SEDE VIRTUAL:")
    sede3 = SedeCampus("SEDE-003", "Campus Virtual", tipo='VIRTUAL')
    sede3.agregar_carrera("Marketing Digital")
    sede3.agregar_edificio("Edificio C")  #  Virtual no tiene edificios
    
    # Generar reportes
    print("\n4. REPORTES:")
    sede1.generar_reporte_completo()
    
    print("=" * 80)
    print(" PROBLEMAS DE ESTE CÓDIGO:")
    print("=" * 80)
    print("1. VIOLA S (SRP):")
    print("   - Una clase hace: gestión de carreras, infraestructura, personal,")
    print("     ubicación, estudiantes, reportes, validación, BD")
    print("")
    print("2. VIOLA O (OCP):")
    print("   - Usa if/elif para tipos de sede")
    print("   - Para agregar tipo nuevo → modificar múltiples métodos")
    print("")
    print("3. VIOLA I (ISP):")
    print("   - Todos los métodos están en una clase grande")
    print("   - SedeVirtual tiene métodos de edificios que no usa")
    print("")
    print("4. VIOLA D (DIP):")
    print("   - Dependencias hardcodeadas (MySQL, Email)")
    print("   - Difícil cambiar de BD o sistema de notificaciones")
    print("=" * 80)