# ⚡ Auror-IA: High-Performance ETL Pipeline

![CI Pipeline](https://github.com/DKAstaroth/auroria_etl_pipeline/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)
![Type Checker](https://img.shields.io/badge/type%20checker-mypy-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> **"Más allá de un script: Ingeniería de Software aplicada a Datos."**

**Auror-IA** es un motor de extracción, transformación y carga (ETL) de próxima generación. A diferencia de los scripts lineales tradicionales, este sistema implementa una **Arquitectura Orientada a Objetos** robusta, **Concurrencia Asíncrona** y **Validación Estricta de Tipos**.

Diseñado para ser agnóstico a la fuente de datos, escalable y mantenible bajo estándares empresariales (SOLID, Clean Code).

---

## 🏗️ Arquitectura del Sistema

El proyecto utiliza el patrón de diseño **Strategy** para desacoplar la lógica de extracción, transformación y carga. El orquestador (`Pipeline`) no conoce los detalles de implementación, solo las interfaces (contratos).

```mermaid
graph LR
    A[Async API Source] -->|Raw Data| B(Pipeline Orchestrator)
    B -->|Validation| C{Pydantic Guard}
    C -- Invalid --> X[Log Error & Discard]
    C -- Valid --> D[Transformer Strategy]
    D -->|Clean Data| E[Loader Strategy]
    E -->|Persist| F[(Database / Warehouse)]


🚀 Stack Tecnológico
Este proyecto demuestra el dominio del ecosistema moderno de Python (2025):

Core: Python 3.10+ (Type Hinting, Dataclasses).

Concurrencia: AsyncIO + aiohttp (Rendimiento 10x superior a requests sincrónico).

Validación de Datos: Pydantic v2 (Contratos de datos y manejo de errores "Fail-Fast").

Persistencia: SQLAlchemy (ORM compatible con SQLite, PostgreSQL, MySQL).

Calidad de Código (Governance):

Ruff: Linter y formateador de alto rendimiento.

MyPy: Chequeo estático de tipos (Static Type Checking).

Pre-commit: Hooks de Git para asegurar calidad antes de cada commit.

Testing & CI/CD:

Pytest + Pytest-Asyncio + Pytest-Mock.

GitHub Actions: Pipeline automatizado de pruebas y linting.

Seguridad: Gestión de secretos mediante variables de entorno (python-dotenv).


📂 Estructura del Proyecto

auroria_etl_pipeline/
├── .github/workflows/    # CI/CD: Automatización con GitHub Actions
├── data/                 # Almacenamiento local (SQLite, Parquet, Logs)
├── src/                  # Código Fuente
│   ├── extractor.py      # Lógica de extracción asíncrona (AsyncIO)
│   ├── interfaces.py     # Contratos abstractos (Protocolos/ABCs)
│   ├── loader.py         # Lógica de carga a Base de Datos
│   ├── schemas.py        # Modelos Pydantic (Validación)
│   └── transformer.py    # Lógica de limpieza y normalización
├── tests/                # Suite de pruebas unitarias (Mocks)
├── .env                  # Variables de entorno (Ignorado por Git)
├── .pre-commit-config.yaml # Configuración de Hooks de Git
├── main.py               # Punto de entrada (Orquestador)
├── pyproject.toml        # Configuración centralizada (Ruff, MyPy)
└── requirements.txt      # Dependencias

🛠️ Instalación y Configuración
Sigue estos pasos para levantar el entorno de desarrollo localmente:

1. Clonar el repositorio

git clone [https://github.com/DKAstaroth/auroria_etl_pipeline.git](https://github.com/DKAstaroth/auroria_etl_pipeline.git)
cd auroria_etl_pipeline

2. Configurar Entorno Virtual

# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Instalar Dependencias

pip install -r requirements.txt

4. Configurar Variables de Entorno
Crea un archivo .env en la raíz del proyecto basándote en este ejemplo:

# .env
API_URL=[https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)
API_LIMIT=100
DB_PATH=data/auroria.db
DB_TABLE_NAME=news_feed
ENVIRONMENT=DEVELOPMENT

5. Configurar Hooks de Calidad (Opcional pero recomendado)
Instala los git hooks para que revisen tu código automáticamente antes de cada commit:

pre-commit install

▶️ Ejecución
Para correr el pipeline completo (Extracción Asíncrona -> Validación -> Transformación -> Carga):

python main.py

Aquí tiene, mi señor.

Este README.md está diseñado estratégicamente. No es solo documentación; es una carta de venta para cualquier reclutador o líder técnico que visite su perfil.

Cópielo íntegramente y reemplazo el contenido actual de su README.md.

Markdown
# ⚡ Auror-IA: High-Performance ETL Pipeline

![CI Pipeline](https://github.com/DKAstaroth/auroria_etl_pipeline/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)
![Type Checker](https://img.shields.io/badge/type%20checker-mypy-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> **"Más allá de un script: Ingeniería de Software aplicada a Datos."**

**Auror-IA** es un motor de extracción, transformación y carga (ETL) de próxima generación. A diferencia de los scripts lineales tradicionales, este sistema implementa una **Arquitectura Orientada a Objetos** robusta, **Concurrencia Asíncrona** y **Validación Estricta de Tipos**.

Diseñado para ser agnóstico a la fuente de datos, escalable y mantenible bajo estándares empresariales (SOLID, Clean Code).

---

## 🏗️ Arquitectura del Sistema

El proyecto utiliza el patrón de diseño **Strategy** para desacoplar la lógica de extracción, transformación y carga. El orquestador (`Pipeline`) no conoce los detalles de implementación, solo las interfaces (contratos).

```mermaid
graph LR
    A[Async API Source] -->|Raw Data| B(Pipeline Orchestrator)
    B -->|Validation| C{Pydantic Guard}
    C -- Invalid --> X[Log Error & Discard]
    C -- Valid --> D[Transformer Strategy]
    D -->|Clean Data| E[Loader Strategy]
    E -->|Persist| F[(Database / Warehouse)]
🚀 Stack Tecnológico
Este proyecto demuestra el dominio del ecosistema moderno de Python (2025):

Core: Python 3.10+ (Type Hinting, Dataclasses).

Concurrencia: AsyncIO + aiohttp (Rendimiento 10x superior a requests sincrónico).

Validación de Datos: Pydantic v2 (Contratos de datos y manejo de errores "Fail-Fast").

Persistencia: SQLAlchemy (ORM compatible con SQLite, PostgreSQL, MySQL).

Calidad de Código (Governance):

Ruff: Linter y formateador de alto rendimiento.

MyPy: Chequeo estático de tipos (Static Type Checking).

Pre-commit: Hooks de Git para asegurar calidad antes de cada commit.

Testing & CI/CD:

Pytest + Pytest-Asyncio + Pytest-Mock.

GitHub Actions: Pipeline automatizado de pruebas y linting.

Seguridad: Gestión de secretos mediante variables de entorno (python-dotenv).

📂 Estructura del Proyecto
Plaintext
auroria_etl_pipeline/
├── .github/workflows/    # CI/CD: Automatización con GitHub Actions
├── data/                 # Almacenamiento local (SQLite, Parquet, Logs)
├── src/                  # Código Fuente
│   ├── extractor.py      # Lógica de extracción asíncrona (AsyncIO)
│   ├── interfaces.py     # Contratos abstractos (Protocolos/ABCs)
│   ├── loader.py         # Lógica de carga a Base de Datos
│   ├── schemas.py        # Modelos Pydantic (Validación)
│   └── transformer.py    # Lógica de limpieza y normalización
├── tests/                # Suite de pruebas unitarias (Mocks)
├── .env                  # Variables de entorno (Ignorado por Git)
├── .pre-commit-config.yaml # Configuración de Hooks de Git
├── main.py               # Punto de entrada (Orquestador)
├── pyproject.toml        # Configuración centralizada (Ruff, MyPy)
└── requirements.txt      # Dependencias
🛠️ Instalación y Configuración
Sigue estos pasos para levantar el entorno de desarrollo localmente:

1. Clonar el repositorio
Bash
git clone [https://github.com/DKAstaroth/auroria_etl_pipeline.git](https://github.com/DKAstaroth/auroria_etl_pipeline.git)
cd auroria_etl_pipeline
2. Configurar Entorno Virtual
Bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Instalar Dependencias
Bash
pip install -r requirements.txt
4. Configurar Variables de Entorno
Crea un archivo .env en la raíz del proyecto basándote en este ejemplo:

Ini, TOML
# .env
API_URL=[https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)
API_LIMIT=100
DB_PATH=data/auroria.db
DB_TABLE_NAME=news_feed
ENVIRONMENT=DEVELOPMENT
5. Configurar Hooks de Calidad (Opcional pero recomendado)
Instala los git hooks para que revisen tu código automáticamente antes de cada commit:

Bash
pre-commit install
▶️ Ejecución
Para correr el pipeline completo (Extracción Asíncrona -> Validación -> Transformación -> Carga):

Bash
python main.py
✅ Testing y Calidad
Este proyecto no acepta código sin validar. Puedes ejecutar la suite de calidad manualmente:

Ejecutar Tests Unitarios (con Mocks Asíncronos)

python -m pytest

Verificar Estilo de Código (Linting)

ruff check .

Verificar Tipado Estático

mypy src

👤 Autor
Juan Pablo Andrés Vega Lagos Ingeniero Informatico

Desarrollado con pasión por la excelencia técnica.

