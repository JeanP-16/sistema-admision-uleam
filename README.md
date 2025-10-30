# 🎓 Sistema de Admisión ULEAM - Versión Profesional 2025

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ULEAM](https://img.shields.io/badge/Universidad-ULEAM-red.svg)](https://www.uleam.edu.ec)

Sistema completo de Inscripción, Evaluación y Asignación de Cupos para la Universidad Laica Eloy Alfaro de Manabí, integrado con datos oficiales SENESCYT 2025.

---

## 👥 Equipo de Desarrollo

| Nombre | Rol | GitHub |
|--------|-----|--------|
| Jean Pierre Flores Piloso | Backend & Modelos | [@jeanpierre](https://github.com/tu-usuario) |
| Braddy Londre Vera Anchundia | Frontend & UI | [@braddy](https://github.com/tu-usuario) |
| Bismark Gabriel Cevallos Cedeño | Base de Datos | [@bismark](https://github.com/tu-usuario) |

**📚 Curso:** 3ro TI "C"  
**🏫 Materia:** Programación Orientada a Objetos  
**👨‍🏫 Tutor:** Ing. Jharol Antonio Ormaza Sabando  
**📅 Fecha:** Octubre 2025

---

## 📋 Descripción del Proyecto

Sistema automatizado que gestiona el proceso completo de admisión universitaria con integración de datos oficiales:

### ✨ Características Principales

- ✅ **Registro Nacional Completo** - Integrado con normativa SENESCYT
- ✅ **Política de Acción Afirmativa (PAA)** - 7 segmentos de asignación
- ✅ **Sedes Oficiales ULEAM** - 9 campus reales
- ✅ **Ofertas Reales** - Datos del PDF oficial ULEAM (IES_ID: 102)
- ✅ **Sistema de Homologación** - Para títulos extranjeros
- ✅ **Cálculo de Puntajes** - Según normativa (70% eval + 30% grado)
- ✅ **Asignación Automatizada** - Por orden de segmentos obligatorio
- ✅ **Sistema de Auditoría** - Trazabilidad completa

---

## 🏗️ Arquitectura del Sistema

### Diagrama de Clases

```
┌─────────────────────┐
│  RegistroNacional   │
└──────────┬──────────┘
           │
           ├──────────────────────────────┐
           │                              │
    ┌──────▼──────┐            ┌─────────▼────────┐
    │  Postulante │            │       PAA        │
    └──────┬──────┘            └─────────┬────────┘
           │                              │
           ├──────────────────────────────┤
           │                              │
    ┌──────▼──────┐            ┌─────────▼────────┐
    │ Inscripcion │            │   Evaluacion     │
    └──────┬──────┘            └─────────┬────────┘
           │                              │
           └──────────┬───────────────────┘
                      │
              ┌───────▼────────┐
              │    Puntaje     │
              └───────┬────────┘
                      │
              ┌───────▼────────┐
              │  Asignacion    │
              └────────────────┘
                      │
              ┌───────▼────────┐
              │ OfertaCarrera  │
              └────────────────┘
```

---

## 📁 Estructura del Proyecto

```
sistema-admision-uleam/
│
├── models/                          # 📦 Modelos de datos
│   ├── Postulante.py               # Datos básicos del postulante
│   ├── RegistroNacional.py         # Registro Nacional SENESCYT
│   ├── PoliticaAccionAfirmativa.py # Segmentos y PAA
│   ├── Inscripcion.py              # Inscripción a carreras
│   ├── Evaluacion.py               # Evaluaciones y exámenes
│   ├── PuntajePostulacion.py       # Cálculo de puntajes
│   ├── OfertaCarrera.py            # Ofertas con datos reales
│   ├── SedeCampus.py               # Sedes oficiales ULEAM
│   ├── Asignacion.py               # Asignación de cupos
│   ├── AntecedenteAcademico.py     # Antecedentes académicos
│   └── LogAuditoria.py             # Sistema de auditoría
│
├── controllers/                     # 🎮 Lógica de negocio
│   ├── RegistroController.py
│   ├── InscripcionController.py
│   ├── EvaluacionController.py
│   └── AsignacionController.py
│
├── services/                        # 🔌 Servicios externos
│   ├── DIGERCICService.py          # Mock servicio DIGERCIC
│   ├── MINEDUCService.py           # Mock servicio MINEDUC
│   └── NotificacionService.py      # Notificaciones
│
├── utils/                          # 🛠️ Utilidades
│   ├── validadores.py              # Funciones de validación
│   ├── calculadoras.py             # Cálculos auxiliares
│   └── constantes.py               # Constantes del sistema
│
├── tests/                          # 🧪 Pruebas
│   ├── test_postulante.py
│   ├── test_inscripcion.py
│   ├── test_paa.py
│   └── test_asignacion.py
│
├── docs/                           # 📚 Documentación
│   ├── diagrama_clases.png
│   ├── manual_usuario.pdf
│   └── normativa_senescyt.pdf
│
├── config/                         # ⚙️ Configuración
│   └── settings.py
│
├── main.py                         # 🚀 Punto de entrada
├── test_sistema.py                 # 🧪 Test de integración
├── requirements.txt                # 📦 Dependencias
├── .gitignore                      # 🚫 Archivos ignorados
├── LICENSE                         # 📄 Licencia MIT
├── CONTRIBUTING.md                 # 🤝 Guía de contribución
└── README.md                       # 📖 Este archivo
```

---

## 🚀 Instalación y Uso

### Requisitos Previos

- Python 3.8 o superior
- Git instalado
- VS Code (recomendado)

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/sistema-admision-uleam.git
cd sistema-admision-uleam

# 2. Crear entorno virtual (opcional pero recomendado)
python -m venv venv

# 3. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar el sistema
python main.py
```

### Ejecución Rápida

```bash
# Ejecutar el sistema principal
python main.py

# Ejecutar pruebas de integración
python test_sistema.py

# Ejecutar pruebas unitarias
python -m pytest tests/
```

---

## 💻 Uso del Sistema

### Menú Principal

Al ejecutar `python main.py` verás:

```
╔═══════════════════════════════════════════════════════╗
║              MENÚ PRINCIPAL - SISTEMA ULEAM           ║
╠═══════════════════════════════════════════════════════╣
║  1. 📝 Ver Sedes Disponibles                          ║
║  2. 📚 Ver Ofertas de Carreras Reales                 ║
║  3. 👤 Registrar Postulante (Registro Nacional)       ║
║  4. 🎯 Crear Inscripción                              ║
║  5. 📊 Ejecutar Demo Completo con Datos Reales        ║
║  6. 🏆 Ver Ranking de Postulantes                     ║
║  7. 📈 Ver Estadísticas del Sistema                   ║
║  0. 🚪 Salir                                          ║
╚═══════════════════════════════════════════════════════╝
```

### Ejemplo de Uso: Crear Postulante

```python
from models.Postulante import Postulante
from models.RegistroNacional import RegistroNacional

# 1. Crear Registro Nacional
registro = RegistroNacional(
    identificacion="1316202082",
    nombres="JEAN PIERRE",
    apellidos="FLORES PILOSO"
)

# 2. Completar datos
registro.completar_datos_personales("2007-05-15", "HOMBRE", "MESTIZO")
registro.completar_ubicacion("MANABÍ", "MANTA", "MANTA", "LOS ESTEROS", "AV. 24")
registro.completar_contacto("0999999999", "email@example.com")
registro.completar_datos_academicos("U.E. MANTA", "FISCAL", 9.5, "SI")

# 3. Validar
if registro.validar_completitud():
    print("✅ Registro completo - Puede continuar")
```

---

## 🎯 Funcionalidades Principales

### 1. Registro Nacional (RF01)
- ✅ Validación de cédula con DIGERCIC
- ✅ Verificación de estado académico MINEDUC
- ✅ Homologación de títulos extranjeros

### 2. Política de Acción Afirmativa (PAA)
Orden obligatorio de segmentos:
1. 🎯 CUOTAS (5-10%)
2. 🏚️ VULNERABILIDAD SOCIOECONÓMICA
3. 🏆 MÉRITO ACADÉMICO
4. 🎖️ RECONOCIMIENTOS
5. 🌍 PUEBLOS Y NACIONALIDADES
6. 🎓 BACHILLERES ÚLTIMO AÑO
7. 👥 POBLACIÓN GENERAL

### 3. Cálculo de Puntaje (RF05)
```python
puntaje_final = (eval_score × 0.7) + (school_score × 0.3) + bonus_points
# Escala: 0-1000 puntos
```

### 4. Asignación de Cupos (RF06)
- ✅ Proceso automatizado por segmentos
- ✅ Ordenamiento por puntaje dentro de cada segmento
- ✅ Trazabilidad completa (por qué se asignó/rechazó)

---

## 📊 Datos Reales Integrados

### Sedes ULEAM Oficiales
1. Matriz - Manta
2. Chone
3. El Carmen
4. Pedernales
5. Bahía de Caráquez (Sucre)
6. Tosagua
7. Santo Domingo de los Colorados
8. Flavio Alfaro
9. Pichincha

### Ofertas de Carreras Reales
- **Tecnologías de la Información** (OFA_ID: 245912, CUS_ID: 350708)
- **Software** (OFA_ID: 247664, CUS_ID: 349116)
- **Medicina** (OFA_ID: 249494, CUS_ID: 349824)
- **Administración de Empresas** (OFA_ID: 247357, CUS_ID: 350275)
- Y más...

---

## 🧪 Pruebas

```bash
# Ejecutar todas las pruebas
python -m pytest tests/ -v

# Ejecutar pruebas con cobertura
python -m pytest --cov=models tests/

# Ejecutar test de integración
python test_sistema.py
```

---

## 🌿 Flujo de Trabajo con Git

### Ramas Principales
- `main` → Producción (código estable)
- `develop` → Desarrollo (integración)
- `feature/*` → Nuevas funcionalidades

### Comandos Básicos

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Commit
git commit -m "feat: descripción del cambio"

# Subir a GitHub
git push origin main

# Crear rama nueva
git checkout -b feature/nueva-funcionalidad
```

---

## 📚 Documentación Adicional

- 📄 [Manual de Usuario](docs/manual_usuario.pdf)
- 📊 [Diagrama de Clases](docs/diagrama_clases.png)
- 📋 [Normativa SENESCYT 2025](docs/normativa_senescyt.pdf)
- 🤝 [Guía de Contribución](CONTRIBUTING.md)

---

## 🔒 Seguridad y Privacidad

- ✅ Cumplimiento Ley de Protección de Datos
- ✅ Cifrado de datos sensibles
- ✅ Control de accesos por roles
- ✅ Logs de auditoría inmutables
- ✅ Validación de todas las entradas

---

## 📈 Roadmap

### Fase 1 (Completado) ✅
- [x] Estructura del proyecto
- [x] Clases principales implementadas
- [x] Integración con datos reales ULEAM
- [x] Sistema de PAA funcional

### Fase 2 (En Desarrollo) 🔄
- [ ] Base de datos SQLite
- [ ] Interfaz web con Flask
- [ ] Reportes en PDF
- [ ] Sistema de notificaciones

### Fase 3 (Planificado) ⏳
- [ ] Dashboard administrativo
- [ ] API RESTful
- [ ] Integración real con SENESCYT
- [ ] Deploy en producción

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) para detalles sobre nuestro código de conducta y el proceso para enviar pull requests.

### Convenciones de Commits
```
feat: Nueva funcionalidad
fix: Corrección de bug
docs: Cambios en documentación
test: Añadir o modificar tests
refactor: Refactorización de código
```

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

---

## 📞 Contacto

**Universidad Laica Eloy Alfaro de Manabí**  
Facultad de Ciencias de la Vida y Tecnologías  
Carrera de Tecnología de la Información

- 📧 Email: florespilosojeanpierre@gmail.com
- 🌐 Web: [www.uleam.edu.ec](https://www.uleam.edu.ec)
- 📱 WhatsApp: Grupo del equipo

---

## 🙏 Agradecimientos

- **Ing. Jharol Antonio Ormaza Sabando** - Tutor del proyecto
- **SENESCYT** - Por la normativa y datos oficiales
- **ULEAM** - Por el apoyo institucional
- **Comunidad Python** - Por las herramientas open source

---

## 📊 Estadísticas del Proyecto

![GitHub repo size](https://img.shields.io/github/repo-size/tu-usuario/sistema-admision-uleam)
![GitHub contributors](https://img.shields.io/github/contributors/tu-usuario/sistema-admision-uleam)
![GitHub stars](https://img.shields.io/github/stars/tu-usuario/sistema-admision-uleam?style=social)
![GitHub forks](https://img.shields.io/github/forks/tu-usuario/sistema-admision-uleam?style=social)

---

**Hecho con ❤️ por el equipo 3ro TI "C" - ULEAM 2025**

**#Python #POO #ULEAM #SENESCYT #SistemaDeAdmision**