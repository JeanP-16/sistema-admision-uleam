<<<<<<< HEAD
"""
Módulo: SedeCampus
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripción:
    Gestiona las sedes y campus de la Universidad Laica Eloy Alfaro de Manabí (ULEAM),
    aplicando herencia y polimorfismo básico para integrar la información con otros módulos.
"""

from abc import ABC, abstractmethod


# ==============================
# CLASE BASE ABSTRACTA
# ==============================

class EntidadUniversitaria(ABC):
    """Clase base abstracta para entidades de la universidad (sede, carrera, laboratorio, etc.)."""

    @abstractmethod
    def obtener_info(self) -> dict:
        """Devuelve información estructurada de la entidad."""
        pass

    @abstractmethod
    def mostrar_info(self) -> None:
        """Muestra información de la entidad."""
        pass


# ==============================
# CLASE PRINCIPAL: SEDE / CAMPUS
# ==============================

class SedeCampus(EntidadUniversitaria):
    """
    Representa una sede o campus de ULEAM.
    Hereda de EntidadUniversitaria y redefine métodos de información.
    """

    _contador = 0

    SEDES_ULEAM = {
        1: {'nombre': 'Matriz - Manta', 'canton': 'MANTA', 'provincia': 'MANABÍ'},
        2: {'nombre': 'Chone', 'canton': 'CHONE', 'provincia': 'MANABÍ'},
        3: {'nombre': 'El Carmen', 'canton': 'EL CARMEN', 'provincia': 'MANABÍ'},
        4: {'nombre': 'Pedernales', 'canton': 'PEDERNALES', 'provincia': 'MANABÍ'},
        5: {'nombre': 'Bahía de Caráquez', 'canton': 'SUCRE', 'provincia': 'MANABÍ'},
        6: {'nombre': 'Tosagua', 'canton': 'TOSAGUA', 'provincia': 'MANABÍ'},
        7: {'nombre': 'Santo Domingo', 'canton': 'SANTO DOMINGO', 'provincia': 'SANTO DOMINGO DE LOS TSÁCHILAS'},
        8: {'nombre': 'Flavio Alfaro', 'canton': 'FLAVIO ALFARO', 'provincia': 'MANABÍ'},
        9: {'nombre': 'Pichincha', 'canton': 'PICHINCHA', 'provincia': 'MANABÍ'}
    }

    def __init__(self, sede_id: int):
        """
        Inicializa una sede o campus según su ID oficial ULEAM.
        """
        if sede_id not in self.SEDES_ULEAM:
            raise ValueError(f"Sede ID {sede_id} no existe en ULEAM.")

        SedeCampus._contador += 1
        datos = self.SEDES_ULEAM[sede_id]

        self.sede_id = sede_id
        self.nombre_sede = datos['nombre']
        self.canton = datos['canton']
        self.provincia = datos['provincia']
        self.activa = True
        self.total_carreras = 0
        self.total_cupos = 0
        self.total_laboratorios = 0

        print(f"Sede creada: {self.nombre_sede} ({self.canton}).")

    # ==============================
    # HERENCIA Y POLIMORFISMO
    # ==============================

    def obtener_info(self) -> dict:
        """Devuelve información estructurada de la sede."""
        return {
            'sede_id': self.sede_id,
            'nombre': self.nombre_sede,
            'canton': self.canton,
            'provincia': self.provincia,
            'carreras': self.total_carreras,
            'cupos_totales': self.total_cupos,
            'laboratorios': self.total_laboratorios,
            'activa': self.activa
        }

    def mostrar_info(self) -> None:
        """Polimorfismo aplicado: muestra la información general de la sede."""
        print("\n" + "=" * 60)
        print(f"SEDE UNIVERSITARIA ULEAM")
        print("=" * 60)
        print(f"ID Sede: {self.sede_id}")
        print(f"Nombre: {self.nombre_sede}")
        print(f"Cantón: {self.canton}")
        print(f"Provincia: {self.provincia}")
        print(f"Carreras registradas: {self.total_carreras}")
        print(f"Cupos totales: {self.total_cupos}")
        print(f"Laboratorios: {self.total_laboratorios}")
        print(f"Activa: {'Sí' if self.activa else 'No'}")
        print("=" * 60)

    # ==============================
    # MÉTODOS PROPIOS DE SEDE
    # ==============================

    def agregar_carrera(self, nombre_carrera: str, cupos: int):
        """Registra una carrera en la sede."""
        self.total_carreras += 1
        self.total_cupos += cupos
        print(f"Carrera agregada: {nombre_carrera} ({cupos} cupos).")

    @classmethod
    def listar_todas_sedes(cls):
        """Lista todas las sedes disponibles."""
        print("\n" + "=" * 60)
        print("LISTADO OFICIAL DE SEDES ULEAM 2025")
        print("=" * 60)
        for id_sede, datos in cls.SEDES_ULEAM.items():
            print(f"{id_sede}. {datos['nombre']:<30} | {datos['canton']:<16}")
        print("=" * 60)

    @classmethod
    def obtener_sede_por_canton(cls, canton: str):
        """Busca sede por cantón."""
        canton = canton.upper()
        for id_sede, datos in cls.SEDES_ULEAM.items():
            if datos['canton'] == canton:
                return id_sede
        return None

    @classmethod
    def obtener_total_sedes(cls) -> int:
        """Total de sedes creadas."""
        return cls._contador


=======
"""
Módulo: SedeCampus
Autores: Jean Pierre Flores Piloso, Braddy Londre Vera, Bismark Grabriel Cevallos
Fecha: Octubre 2025
Descripción:
    Gestiona las sedes y campus de la Universidad Laica Eloy Alfaro de Manabí (ULEAM),
    aplicando herencia y polimorfismo básico para integrar la información con otros módulos.
"""

from abc import ABC, abstractmethod


# ==============================
# CLASE BASE ABSTRACTA
# ==============================

class EntidadUniversitaria(ABC):
    """Clase base abstracta para entidades de la universidad (sede, carrera, laboratorio, etc.)."""

    @abstractmethod
    def obtener_info(self) -> dict:
        """Devuelve información estructurada de la entidad."""
        pass

    @abstractmethod
    def mostrar_info(self) -> None:
        """Muestra información de la entidad."""
        pass


# ==============================
# CLASE PRINCIPAL: SEDE / CAMPUS
# ==============================

class SedeCampus(EntidadUniversitaria):
    """
    Representa una sede o campus de ULEAM.
    Hereda de EntidadUniversitaria y redefine métodos de información.
    """

    _contador = 0

    SEDES_ULEAM = {
        1: {'nombre': 'Matriz - Manta', 'canton': 'MANTA', 'provincia': 'MANABÍ'},
        2: {'nombre': 'Chone', 'canton': 'CHONE', 'provincia': 'MANABÍ'},
        3: {'nombre': 'El Carmen', 'canton': 'EL CARMEN', 'provincia': 'MANABÍ'},
        4: {'nombre': 'Pedernales', 'canton': 'PEDERNALES', 'provincia': 'MANABÍ'},
        5: {'nombre': 'Bahía de Caráquez', 'canton': 'SUCRE', 'provincia': 'MANABÍ'},
        6: {'nombre': 'Tosagua', 'canton': 'TOSAGUA', 'provincia': 'MANABÍ'},
        7: {'nombre': 'Santo Domingo', 'canton': 'SANTO DOMINGO', 'provincia': 'SANTO DOMINGO DE LOS TSÁCHILAS'},
        8: {'nombre': 'Flavio Alfaro', 'canton': 'FLAVIO ALFARO', 'provincia': 'MANABÍ'},
        9: {'nombre': 'Pichincha', 'canton': 'PICHINCHA', 'provincia': 'MANABÍ'}
    }

    def __init__(self, sede_id: int):
        """
        Inicializa una sede o campus según su ID oficial ULEAM.
        """
        if sede_id not in self.SEDES_ULEAM:
            raise ValueError(f"Sede ID {sede_id} no existe en ULEAM.")

        SedeCampus._contador += 1
        datos = self.SEDES_ULEAM[sede_id]

        self.sede_id = sede_id
        self.nombre_sede = datos['nombre']
        self.canton = datos['canton']
        self.provincia = datos['provincia']
        self.activa = True
        self.total_carreras = 0
        self.total_cupos = 0
        self.total_laboratorios = 0

        print(f"Sede creada: {self.nombre_sede} ({self.canton}).")

    # ==============================
    # HERENCIA Y POLIMORFISMO
    # ==============================

    def obtener_info(self) -> dict:
        """Devuelve información estructurada de la sede."""
        return {
            'sede_id': self.sede_id,
            'nombre': self.nombre_sede,
            'canton': self.canton,
            'provincia': self.provincia,
            'carreras': self.total_carreras,
            'cupos_totales': self.total_cupos,
            'laboratorios': self.total_laboratorios,
            'activa': self.activa
        }

    def mostrar_info(self) -> None:
        """Polimorfismo aplicado: muestra la información general de la sede."""
        print("\n" + "=" * 60)
        print(f"SEDE UNIVERSITARIA ULEAM")
        print("=" * 60)
        print(f"ID Sede: {self.sede_id}")
        print(f"Nombre: {self.nombre_sede}")
        print(f"Cantón: {self.canton}")
        print(f"Provincia: {self.provincia}")
        print(f"Carreras registradas: {self.total_carreras}")
        print(f"Cupos totales: {self.total_cupos}")
        print(f"Laboratorios: {self.total_laboratorios}")
        print(f"Activa: {'Sí' if self.activa else 'No'}")
        print("=" * 60)

    # ==============================
    # MÉTODOS PROPIOS DE SEDE
    # ==============================

    def agregar_carrera(self, nombre_carrera: str, cupos: int):
        """Registra una carrera en la sede."""
        self.total_carreras += 1
        self.total_cupos += cupos
        print(f"Carrera agregada: {nombre_carrera} ({cupos} cupos).")

    @classmethod
    def listar_todas_sedes(cls):
        """Lista todas las sedes disponibles."""
        print("\n" + "=" * 60)
        print("LISTADO OFICIAL DE SEDES ULEAM 2025")
        print("=" * 60)
        for id_sede, datos in cls.SEDES_ULEAM.items():
            print(f"{id_sede}. {datos['nombre']:<30} | {datos['canton']:<16}")
        print("=" * 60)

    @classmethod
    def obtener_sede_por_canton(cls, canton: str):
        """Busca sede por cantón."""
        canton = canton.upper()
        for id_sede, datos in cls.SEDES_ULEAM.items():
            if datos['canton'] == canton:
                return id_sede
        return None

    @classmethod
    def obtener_total_sedes(cls) -> int:
        """Total de sedes creadas."""
        return cls._contador
>>>>>>> d4f7eac51555ebae2693ce93b24af2bc4943b607
