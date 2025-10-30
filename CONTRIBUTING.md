# 🤝 Guía de Contribución

Sistema de Admisión ULEAM - Equipo 3ro TI "C"

## 👥 Equipo de Desarrollo

- **Jean Pierre Flores Piloso** - Líder del Proyecto / Backend
- **Braddy Londre Vera Anchundia** - Frontend / Interfaz
- **Bismark Gabriel Cevallos Cedeño** - Base de Datos

**Tutor:** Ing. Jharol Antonio Ormaza Sabando  
**Materia:** Programación Orientada a Objetos  
**Periodo:** Octubre 2025

---

## 🌿 Flujo de Trabajo con Git

### 1. Clonar el Repositorio
```bash
git clone https://github.com/TU-USUARIO/sistema-admision-uleam.git
cd sistema-admision-uleam
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Trabajar en Tu Rama

**Jean Pierre (Líder - Backend):**
```bash
git checkout jean-pierre/backend
git pull origin main
# ... trabajar ...
git add .
git commit -m "feat: descripción"
git push origin jean-pierre/backend
```

**Braddy (Frontend):**
```bash
git checkout braddy/frontend
git pull origin main
# ... trabajar ...
git add .
git commit -m "feat: descripción"
git push origin braddy/frontend
```

**Bismark (Database):**
```bash
git checkout bismark/database
git pull origin main
# ... trabajar ...
git add .
git commit -m "feat: descripción"
git push origin bismark/database
```

---

## 📝 Convenciones de Commits

Usar prefijos descriptivos:

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Documentación
- `refactor:` Refactorización de código
- `test:` Añadir o modificar tests
- `style:` Cambios de formato (sin afectar código)

**Ejemplos:**
```bash
git commit -m "feat: añadir validación de cédula"
git commit -m "fix: corregir cálculo de puntaje"
git commit -m "docs: actualizar README con ejemplos"
```

---

## 🔄 Pull Requests

1. Termina tu trabajo en tu rama
2. Ve a GitHub.com
3. Click en "Pull Requests" → "New pull request"
4. Selecciona: `base: main` ← `compare: tu-rama`
5. Describe los cambios
6. Solicita revisión de Jean Pierre (líder)
7. Espera aprobación para hacer merge

---

## ✅ Estándares de Código Python

### Nombres de Variables
```python
# ✅ Correcto
nombre_estudiante = "Jean Pierre"
puntaje_final = 850

# ❌ Incorrecto
n = "Jean Pierre"
p = 850
```

### Nombres de Clases
```python
# ✅ Correcto
class Postulante:
    pass

# ❌ Incorrecto
class postulante:
    pass
```

### Docstrings
```python
def calcular_puntaje(nota_grado, puntaje_eval):
    """
    Calcula el puntaje final de postulación.
    
    Args:
        nota_grado (float): Nota de grado (0-10)
        puntaje_eval (float): Puntaje de evaluación (0-1000)
    
    Returns:
        float: Puntaje final ponderado
    """
    return (nota_grado * 100 * 0.3) + (puntaje_eval * 0.7)
```

---

## 🧪 Testing

Antes de hacer commit, prueba tu código:

```bash
# Probar el sistema completo
python main.py

# Ejecutar tests
python test_sistema.py

# Probar módulos individuales
python models/Postulante.py
```

---

## 📞 Contacto y Ayuda

**Líder del Proyecto:** Jean Pierre Flores Piloso  
**Email:** florespilosojeanpierre@gmail.com

**Grupo de WhatsApp:** Equipo 3ro TI "C"

---

## 📚 Recursos

- [Documentación Git](https://git-scm.com/docs)
- [PEP 8 - Python Style Guide](https://pep8.org/)
- [Documentación SENESCYT](https://www.senescyt.gob.ec/)

---

¡Gracias por contribuir! 🚀