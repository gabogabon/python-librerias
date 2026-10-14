# 🐍 Python: ejemplos prácticos por librería

Colección de 12 scripts en Python, cada uno con un ejemplo funcional de una librería distinta.
Sirve como material de práctica y como referencia rápida.

## 📁 Estructura

```
python-librerias/
├── 01_math_potencias.py
├── 02_random_sorteo.py
├── 03_datetime_fechas.py
├── 04_csv_lectura_escritura.py
├── 05_fpdf_pdf.py
├── 06_reportlab_pdf.py
├── 07_numpy_arreglos.py
├── 08_pandas_analisis.py
├── 09_matplotlib_grafica.py
├── 10_requests_api.py
├── 11_flask_app.py
├── 12_sklearn_clasificacion.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Instalación

Requiere **Python 3.9 o superior**.

```bash
# 1. Clonar el repositorio
git clone https://github.com/gabogabon/python-librerias.git
cd python-librerias

# 2. (Opcional, recomendado) crear un entorno virtual
python -m venv venv
source venv/Scripts/activate      # Git Bash en Windows
# source venv/bin/activate        # Linux / macOS

# 3. Instalar dependencias
pip install -r requirements.txt
```

> `math`, `random`, `datetime` y `csv` forman parte de la biblioteca estándar de Python: no necesitan instalación.
> Para `fpdf` se instala el paquete **fpdf2** (versión mantenida y actual).

## ▶️ Ejecución

Cada script es independiente:

```bash
python 01_math_potencias.py
```

Los archivos generados (CSV, PDF, PNG) se guardan en la carpeta `salida/`, que se crea sola y no se sube a Git.

---

## 📚 Documentación de cada script

### 1. `math` — `01_math_potencias.py`
Operaciones matemáticas con la librería estándar: potencia (`math.pow`), raíz cuadrada, factorial, logaritmo, seno (con conversión de grados a radianes), área de un círculo con `math.pi` e hipotenusa con `math.hypot`.
**Salida:** resultados impresos en consola.

### 2. `random` — `02_random_sorteo.py`
Generación de datos aleatorios: entero y decimal aleatorio, elección de un ganador (`choice`), selección sin repetición (`sample`), mezcla de una lista (`shuffle`) y un generador de contraseñas seguras. Usa `random.seed(42)` para que los resultados sean reproducibles; quita esa línea para obtener valores distintos en cada ejecución.
**Salida:** resultados impresos en consola.

### 3. `datetime` — `03_datetime_fechas.py`
Manejo de fechas y horas: fecha actual con formato, suma de días con `timedelta`, días restantes para fin de año, cálculo de edad exacta a partir de una fecha de nacimiento y conversión de texto a fecha con `strptime`.
**Salida:** resultados impresos en consola.

### 4. `csv` — `04_csv_lectura_escritura.py`
Crea el archivo `salida/alumnos.csv` con calificaciones usando `csv.writer`, luego lo lee con `csv.DictReader` y calcula el promedio de cada alumno.
**Salida:** `salida/alumnos.csv` y promedios en consola.

### 5. `fpdf` — `05_fpdf_pdf.py`
Genera un PDF con título centrado, un párrafo y una tabla de productos usando `FPDF` (paquete fpdf2). Dibuja las celdas manualmente con `cell()`.
**Salida:** `salida/reporte_fpdf.pdf`.

### 6. `reportlab` — `06_reportlab_pdf.py`
Crea una factura en PDF con el módulo `platypus`: título, párrafo y una tabla con estilos (encabezado de color, bordes y fila de total calculada).
**Salida:** `salida/factura_reportlab.pdf`.

### 7. `NumPy` — `07_numpy_arreglos.py`
Cálculo numérico con arreglos: operaciones vectorizadas, media y desviación estándar, `linspace` y `arange`, multiplicación de matrices (`@`), determinante, inversa y resolución de un sistema de ecuaciones lineales con `np.linalg.solve`.
**Salida:** resultados impresos en consola.

### 8. `Pandas` — `08_pandas_analisis.py`
Análisis de datos con un `DataFrame` de ventas: vista previa, estadísticas (`describe`), filtrado por condición, agrupación por vendedor con `groupby` y exportación del resultado a CSV.
**Salida:** `salida/ventas_por_vendedor.csv` y tablas en consola.

### 9. `Matplotlib` — `09_matplotlib_grafica.py`
Dibuja una figura con dos gráficas: líneas (seno y coseno) y barras (ventas mensuales). Guarda la imagen y además abre una ventana con `plt.show()`.
**Salida:** `salida/graficas.png`.

### 10. `Requests` — `10_requests_api.py`
Consume la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com): una petición `GET` simple, un `GET` con parámetros y un `POST` con JSON. Incluye `timeout` y manejo de errores de red.
**Requiere conexión a internet.**
**Salida:** respuestas de la API en consola.

### 11. `Flask` — `11_flask_app.py`
Servidor web mínimo con tres rutas:

| Ruta | Descripción |
|------|-------------|
| `/` | Página de bienvenida en HTML |
| `/api/suma/<a>/<b>` | Devuelve en JSON la suma de dos enteros (ej. `/api/suma/3/4`) |
| `/api/hora` | Devuelve la hora actual en JSON |

Al ejecutarlo, abre **http://127.0.0.1:5000** en el navegador. Detén el servidor con `Ctrl + C`.

### 12. `scikit-learn` — `12_sklearn_clasificacion.py`
Ejemplo básico de machine learning: carga el dataset **Iris**, separa datos de entrenamiento y prueba (70/30), entrena un clasificador **K-Nearest Neighbors** (k=3), muestra la precisión y el reporte de clasificación, y predice la especie de una flor nueva.
**Salida:** métricas y predicción en consola.

---

## 🛠️ Tecnologías

Python · math · random · datetime · csv · fpdf2 · ReportLab · NumPy · Pandas · Matplotlib · Requests · Flask · scikit-learn

## 📄 Licencia

Proyecto de uso libre con fines educativos.
