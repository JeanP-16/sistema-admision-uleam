"""
4 ISP 
 
CÓDIGO BUENO - APLICANDO PRINCIPIO I (SEGREGACIÓN DE INTERFACES)

SOLUCIÓN: Dividir la interfaz gigante en interfaces pequeñas y especificas

MEJORA:
- InterfazBasica: SOLO métodos básicos que TODOS usan
- InterfazCupos: SOLO métodos de cupos (si la carrera tiene cupos)
- InterfazModalidades: SOLO métodos de modalidades (si la carrera tiene modalidades)
- InterfazNivelacion: SOLO métodos de nivelación (si la carrera tiene nivelación)
- InterfazHorarios: SOLO métodos de horarios (si la carrera tiene horarios)

Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Refactorización SIMPLE: Noviembre 2025
"""

#-Principio de segregación de interfaz
#Este principio señala que se deben de definir interfaces pequeñas que resuelvan un problema específico,
#en lugar de tener interfaces grandes que hagan muchas cosas. 

# ==================== INTERFAZ 1: BÁSICA ====================
class InterfazBasica:
    """SOLO métodos básicos que TODAS las carreras necesitan"""
    
    def obtener_informacion(self):
        """Devuelve información básica de la carrera"""
        raise NotImplementedError("Debes implementar obtener_informacion()")
    
    def esta_disponible(self):
        """Verifica si la carrera está disponible"""
        raise NotImplementedError("Debes implementar esta_disponible()")


# ==================== INTERFAZ 2: CUPOS ====================
class InterfazCupos:
    """SOLO para carreras que manejan cupos"""
    
    def asignar_cupo(self, postulante):
        """Asigna un cupo a un postulante"""
        raise NotImplementedError("Debes implementar asignar_cupo()")
    
    def verificar_cupos_disponibles(self):
        """Verifica cupos disponibles"""
        raise NotImplementedError("Debes implementar verificar_cupos_disponibles()")


# ==================== INTERFAZ 3: MODALIDADES ====================
class InterfazModalidades:
    """SOLO para carreras que tienen diferentes modalidades"""
    
    def agregar_modalidad(self, modalidad):
        """Agrega una modalidad de estudio"""
        raise NotImplementedError("Debes implementar agregar_modalidad()")
    
    def listar_modalidades(self):
        """Lista modalidades disponibles"""
        raise NotImplementedError("Debes implementar listar_modalidades()")


# ==================== INTERFAZ 4: NIVELACIÓN ====================
class InterfazNivelacion:
    """SOLO para carreras que requieren nivelación"""
    
    def requiere_nivelacion(self):
        """Verifica si requiere nivelación"""
        raise NotImplementedError("Debes implementar requiere_nivelacion()")
    
    def asignar_nivel(self, postulante, nivel):
        """Asigna nivel de nivelación"""
        raise NotImplementedError("Debes implementar asignar_nivel()")


# ==================== INTERFAZ 5: HORARIOS ====================
class InterfazHorarios:
    """SOLO para carreras con horarios específicos"""
    
    def agregar_horario(self, horario):
        """Agrega un horario disponible"""
        raise NotImplementedError("Debes implementar agregar_horario()")
    
    def obtener_horarios(self):
        """Lista horarios disponibles"""
        raise NotImplementedError("Debes implementar obtener_horarios()")


# ==================== IMPLEMENTACIÓN 1: CARRERA BÁSICA ====================
class CarreraBasica(InterfazBasica):
    """Carrera simple - SOLO implementa InterfazBasica"""
    
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.disponible = True
    
    def obtener_informacion(self):
        return f"Carrera: {self.nombre} (Código: {self.codigo})"
    
    def esta_disponible(self):
        return self.disponible


# ==================== IMPLEMENTACIÓN 2: CARRERA CON CUPOS ====================
class CarreraConCupos(InterfazBasica, InterfazCupos):
    """Implementa SOLO lo que necesita: Básica + Cupos"""
    
    def __init__(self, codigo, nombre, cupos_totales):
        self.codigo = codigo
        self.nombre = nombre
        self.disponible = True
        self.cupos_totales = cupos_totales
        self.cupos_ocupados = 0
        self.postulantes = []
    
    # Implementa InterfazBasica
    def obtener_informacion(self):
        return f"Carrera: {self.nombre} - Cupos: {self.cupos_ocupados}/{self.cupos_totales}"
    
    def esta_disponible(self):
        return self.disponible and self.cupos_ocupados < self.cupos_totales
    
    # Implementa InterfazCupos
    def asignar_cupo(self, postulante):
        if self.cupos_ocupados < self.cupos_totales:
            self.postulantes.append(postulante)
            self.cupos_ocupados += 1
            print(f"Cupo asignado a {postulante} en {self.nombre}")
            return True
        print(f"No hay cupos disponibles en {self.nombre}")
        return False
    
    def verificar_cupos_disponibles(self):
        disponibles = self.cupos_totales - self.cupos_ocupados
        print(f"Cupos disponibles en {self.nombre}: {disponibles}/{self.cupos_totales}")
        return disponibles


# ==================== IMPLEMENTACIÓN 3: CARRERA CON MODALIDADES ====================
class CarreraConModalidades(InterfazBasica, InterfazModalidades):
    """Implementa SOLO lo que necesita: Básica + Modalidades"""
    
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.disponible = True
        self.modalidades = []
    
    # Implementa InterfazBasica
    def obtener_informacion(self):
        return f"Carrera: {self.nombre} - Modalidades: {len(self.modalidades)}"
    
    def esta_disponible(self):
        return self.disponible and len(self.modalidades) > 0
    
    # Implementa InterfazModalidades
    def agregar_modalidad(self, modalidad):
        self.modalidades.append(modalidad)
        print(f"Modalidad '{modalidad}' agregada a {self.nombre}")
    
    def listar_modalidades(self):
        print(f"\nModalidades de {self.nombre}:")
        for mod in self.modalidades:
            print(f"  - {mod}")
        return self.modalidades


# ==================== IMPLEMENTACIÓN 4: CARRERA COMPLETA ====================
class CarreraCompleta(InterfazBasica, InterfazCupos, InterfazModalidades, 
                     InterfazNivelacion, InterfazHorarios):
    """Carrera completa - Implementa TODAS las interfaces que necesita"""
    
    def __init__(self, codigo, nombre, cupos_totales):
        self.codigo = codigo
        self.nombre = nombre
        self.disponible = True
        self.cupos_totales = cupos_totales
        self.cupos_ocupados = 0
        self.postulantes = []
        self.modalidades = []
        self.horarios = []
        self.necesita_nivelacion = True
    
    # Implementa InterfazBasica
    def obtener_informacion(self):
        info = f"Carrera: {self.nombre}\n"
        info += f"Cupos: {self.cupos_ocupados}/{self.cupos_totales}\n"
        info += f"Modalidades: {len(self.modalidades)}\n"
        info += f"Horarios: {len(self.horarios)}"
        return info
    
    def esta_disponible(self):
        return self.disponible and self.cupos_ocupados < self.cupos_totales
    
    # Implementa InterfazCupos
    def asignar_cupo(self, postulante):
        if self.cupos_ocupados < self.cupos_totales:
            self.postulantes.append(postulante)
            self.cupos_ocupados += 1
            print(f"Cupo asignado a {postulante}")
            return True
        return False
    
    def verificar_cupos_disponibles(self):
        return self.cupos_totales - self.cupos_ocupados
    
    # Implementa InterfazModalidades
    def agregar_modalidad(self, modalidad):
        self.modalidades.append(modalidad)
    
    def listar_modalidades(self):
        return self.modalidades
    
    # Implementa InterfazNivelacion
    def requiere_nivelacion(self):
        return self.necesita_nivelacion
    
    def asignar_nivel(self, postulante, nivel):
        print(f"{postulante} asignado a nivel {nivel} en {self.nombre}")
    
    # Implementa InterfazHorarios
    def agregar_horario(self, horario):
        self.horarios.append(horario)
    
    def obtener_horarios(self):
        return self.horarios


# ==================== EJEMPLO DE USO ====================
if __name__ == "__main__":
    print("=" * 80)
    print("DEMOSTRACIÓN: PRINCIPIO I (ISP) - CÓDIGO BUENO")
    print("=" * 80)
    
    # EJEMPLO 1: Carrera básica
    print("\n1. CARRERA BÁSICA (solo interfaz básica):")
    carrera1 = CarreraBasica("001", "Filosofía")
    print(f"   {carrera1.obtener_informacion()}")
    print(f"   ¿Disponible? {carrera1.esta_disponible()}")
    # NO tiene métodos que no usa (cupos, modalidades, etc.)
    
    # EJEMPLO 2: Carrera con cupos
    print("\n2. CARRERA CON CUPOS:")
    carrera2 = CarreraConCupos("002", "Medicina", cupos_totales=50)
    print(f"   {carrera2.obtener_informacion()}")
    carrera2.verificar_cupos_disponibles()
    carrera2.asignar_cupo("Juan Pérez")
    carrera2.asignar_cupo("María López")
    carrera2.verificar_cupos_disponibles()
    # Solo implementa InterfazBasica + InterfazCupos
    
    # EJEMPLO 3: Carrera con modalidades
    print("\n3. CARRERA CON MODALIDADES:")
    carrera3 = CarreraConModalidades("003", "Administración")
    carrera3.agregar_modalidad("PRESENCIAL")
    carrera3.agregar_modalidad("SEMIPRESENCIAL")
    carrera3.agregar_modalidad("EN LÍNEA")
    carrera3.listar_modalidades()
    # Solo implementa InterfazBasica + InterfazModalidades
    
    # EJEMPLO 4: Carrera completa
    print("\n4. CARRERA COMPLETA (todas las interfaces):")
    carrera4 = CarreraCompleta("004", "Ingeniería en Sistemas", cupos_totales=100)
    print(f"   {carrera4.obtener_informacion()}")
    carrera4.agregar_modalidad("PRESENCIAL")
    carrera4.agregar_horario("MATUTINO")
    carrera4.agregar_horario("VESPERTINO")
    print(f"   ¿Requiere nivelación? {carrera4.requiere_nivelacion()}")
    carrera4.asignar_nivel("Pedro García", "NIVEL 1")
    # Implementa TODAS las interfaces porque las necesita
    
    print("\n" + "=" * 80)
    print("VENTAJAS DE ISP:")
    print("=" * 80)
    print("1. Cada clase implementa SOLO lo que necesita")
    print("2. CarreraBasica NO tiene métodos vacíos de cupos/modalidades")
    print("3. Fácil agregar nuevas interfaces sin afectar clases existentes")
    print("4. Clases pequeñas y cohesivas")
    print("5. No obligamos a implementar métodos que no se usan")
    print("=" * 80)
