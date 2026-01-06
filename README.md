# Financial Reconciliation Engine 📊

> **Herramienta automatizada de conciliación de datos financieros (ETL) construida con Python y Pandas.**

Este proyecto simula un entorno real de Operaciones Técnicas donde se requiere validar la integridad de las transacciones entre un sistema interno (Ventas) y una fuente externa (Extracto Bancario/Pasarela de Pagos). El objetivo es identificar discrepancias financieras de forma automatizada y escalable.

---

## 🏗 Arquitectura del Proyecto

El proyecto sigue una arquitectura modular separando la ingesta, la limpieza y la lógica de negocio, lo que permite un mantenimiento sencillo y reutilización de código.

```
reconciler-project/
├── data/
│   ├── raw/              # Landing zone para archivos CSV crudos (Source A & B)
│   └── output/           # Reportes finales generados (Excel/CSV)
├── src/
│   ├── loaders.py        # Capa de Ingesta: Lectura agnóstica de archivos
│   ├── sanitation.py     # Capa de Normalización: Limpieza de tipos y formatos
│   └── logic.py          # Capa de Negocio: Algoritmo de comparación (Merge)
├── generate_dummy.py     # Script auxiliar para generar datos de prueba (Seed Data)
├── main.py               # Orquestador del pipeline
└── requirements.txt      # Dependencias del proyecto
```

---

## 🚀 Stack Tecnológico

- **Lenguaje**: Python 3.10+
- **Procesamiento de Datos**: Pandas (Enfoque vectorizado para alto rendimiento)
- **Cálculo Numérico**: NumPy
- **Gestión de Dependencias**: Virtualenv / Pip

---

## ⚙️ Cómo funciona (Lógica del Motor)

El motor realiza una comparación basada en conjuntos (**Set-based comparison**) utilizando un **FULL OUTER JOIN**, lo que garantiza que no se pierda información de ninguna de las dos fuentes.

### Flujo del Pipeline

1. **Ingesta**: Carga de datasets crudos desde `data/raw/`.

2. **Sanitización (ETL)**:
   - Estandarización de IDs (Eliminación de espacios, mayúsculas)
   - Conversión segura de montos a tipos numéricos
   - Eliminación de duplicados técnicos

3. **Cruce (Merge)**: Unión total de ambas fuentes preservando datos huérfanos.

4. **Clasificación**: El algoritmo etiqueta cada transacción en una de estas categorías:
   - ✅ **Match**: Coincidencia perfecta (Integridad y Exactitud)
   - ⚠️ **Data Mismatch**: El ID existe en ambos, pero el monto difiere
   - ❌ **Missing in Sales**: Existe en Banco pero no en el sistema interno
   - ❌ **Missing in Bank**: Existe en Ventas pero no en el banco

---

## 🚦 Estado del Proyecto

Actualmente el proyecto se encuentra en desarrollo activo:

- [x] Configuración de Entorno: Estructura de carpetas y entorno virtual
- [x] Generador de Datos: Script (`generate_dummy.py`) para crear escenarios de prueba
- [x] Módulo de Ingesta: Lectura robusta de CSVs (`src/loaders.py`)
- [ ] Módulo de Sanitización: Limpieza de datos previa al cruce
- [ ] Motor de Conciliación: Lógica de comparación y detección de diferencias
- [ ] Reportes: Exportación de resultados a Excel/CSV

---

## 🛠️ Instrucciones de Ejecución

Sigue estos pasos para probar el proyecto en tu máquina local:

### 1. Clonar el repositorio

```bash
git clone https://github.com/LeoQuintero/reconcilier-project.git
cd reconciler-project
```

### 2. Crear entorno virtual e instalar dependencias

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Generar datos de prueba

Si no tienes archivos reales, ejecuta este script para crear datos simulados en la carpeta `data/raw/`.

```bash
python generate_dummy.py
```

### 4. Ejecutar la conciliación

Correr el script principal para procesar los archivos.

```bash
python main.py
```

---

## 📋 Requisitos

- Python 3.10 o superior
- Pandas
- NumPy

---

## 🎯 Casos de Uso

Este motor está diseñado para:

- Validar transacciones entre sistemas de ventas y extractos bancarios
- Detectar discrepancias en pasarelas de pago
- Auditoría financiera automatizada
- Procesos de reconciliación contable

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👤 Autor

**Leonardo Quintero**

- GitHub: [@LeoQuintero](https://github.com/LeoQuintero)
- Rol: Technical Operations & Integrations Enthusiast

---

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio.
