# 📰 Auror-IA: News Ingestion Pipeline

## 📌 Descripción del Proyecto
Este repositorio contiene el módulo de Ingeniería de Datos (ETL) para el proyecto **Auror-IA**. Su objetivo es automatizar la extracción, limpieza y almacenamiento de noticias desde fuentes externas para alimentar modelos de Inteligencia Artificial destinados a la detección de Fake News.

## 🚀 Arquitectura del Pipeline
El sistema sigue una arquitectura ETL modular:
1.  **Extract (E):** Conexión a APIs REST externas para la ingesta de datos crudos.
2.  **Transform (T):** Limpieza de datos con **Pandas**, normalización de fechas y eliminación de registros corruptos.
3.  **Load (L):** Persistencia de datos estructurados en **SQLite** para análisis histórico.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Procesamiento:** Pandas, NumPy
* **Base de Datos:** SQLite, SQLAlchemy
* **Orquestación:** Scripting modular con Logging avanzado

## ⚙️ Instalación y Uso
1.  Clonar el repositorio:
    ```bash
    git clone [https://github.com/SU_USUARIO/auroria_etl_pipeline.git](https://github.com/SU_USUARIO/auroria_etl_pipeline.git)
    ```
2.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ejecutar el pipeline:
    ```bash
    python main.py
    ```

## 📂 Estructura del Proyecto
```text
├── data/           # Almacenamiento local (SQLite)
├── logs/           # Registros de ejecución y errores
├── src/            # Código fuente modular (Extractor, Transformer, Loader)
├── main.py         # Orquestador principal
└── requirements.txt


Desarrollado por Juan Pablo Andrés Vega Lagos - Estudiante de Ingeniería en Informática.


---

### Paso 4: Inicializar Git (Localmente)
Ahora guardaremos la primera "foto" de su proyecto en su historial local.

Ejecute estos comandos en su terminal uno por uno:

1.  **Iniciar el repositorio:**
    ```powershell
    git init
    ```
    *(Debería decir: "Initialized empty Git repository...")*

2.  **Preparar los archivos (Stage):**
    ```powershell
    git add .
    ```
    *(Esto agrega todo lo que NO está en el .gitignore).*

3.  **Confirmar los cambios (Commit):**
    ```powershell
    git commit -m "feat: initial release of ETL pipeline modules"
    ```

---
