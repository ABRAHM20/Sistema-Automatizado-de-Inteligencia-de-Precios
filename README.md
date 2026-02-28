Bot Automático de Monitoreo de Precios (E-commerce) -> Telegram
Este proyecto es un sistema de backend robusto y completamente automatizado que extrae, compara y almacena los precios de productos tecnológicos en tiempo real desde las plataformas de e-commerce más grandes (Falabella y Plaza Vea).

El sistema utiliza un web scraper inteligente integrado con una API RESTful asíncrona, guarda el historial de fluctuaciones en PostgreSQL y notifica las diferencias de precio directamente a un dispositivo móvil vía Telegram, operando de manera autónoma 24/7.

🚀 Características Principales
Automatización Autónoma (APScheduler): Integración de un reloj interno que ejecuta el pipeline completo de extracción y notificación cada 4 horas de manera silenciosa en un hilo secundario (background task), sin bloquear el servidor principal.

Scraping Avanzado (Ingeniería Inversa): Evasión de bloqueos tradicionales mediante la extracción de datos desde el estado inicial de frameworks modernos:

Falabella (Next.js): Extracción desde la etiqueta <script id="__NEXT_DATA__">.

Plaza Vea (VTEX): Consumo directo de la API oculta del catalog_system.

Arquitectura Asíncrona: Construido con FastAPI y SQLAlchemy Async (asyncpg), garantizando un rendimiento ultra rápido y manejo eficiente de múltiples peticiones.

Persistencia Inteligente: Conexión segura a PostgreSQL con creación automática de tablas durante el ciclo de vida de inicio del servidor (lifespan).

Seguridad de Credenciales: Manejo estricto de variables de entorno mediante python-dotenv para aislar tokens y accesos a bases de datos.

Alertas Push Asíncronas: Integración nativa con la API de Telegram usando httpx para envíos HTTP no bloqueantes.

📂 Estructura del Proyecto
```Plaintext
BOT_PRECIOS/
├── database/
│   └── db.py                 # Configuración y motor asíncrono de PostgreSQL
├── models/
│   └── producto.py           # Modelo ORM de SQLAlchemy (Tablas)
├── routes/
│   └── routes.py             # Endpoints, lógica de negocio y cliente HTTPX de Telegram
├── schemas/
│   └── schema_producto.py    # Validación estricta de datos con Pydantic
├── scrapper/
│   └── main_scraper.py       # Lógica de extracción BeautifulSoup/Requests
├── .env.example              # Plantilla segura de variables de entorno
├── .gitignore                # Reglas de exclusión para Git
└── main.py                   # Raíz de la aplicación, Lifespan y Scheduler
⚙️ Requisitos Previos
Python 3.10+

PostgreSQL (Ejecutándose localmente o en la nube)

Un Bot de Telegram (Creado mediante @BotFather)

💻 Instalación y Despliegue Local
1. Clonar el repositorio:

Bash
git clone https://github.com/TU_USUARIO/Sistema-Automatizado-de-Inteligencia-de-Precios.git
cd Sistema-Automatizado-de-Inteligencia-de-Precios
2. Crear y activar el entorno virtual:

Bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
3. Instalar dependencias:

Bash
pip install fastapi uvicorn sqlalchemy asyncpg requests bs4 httpx pydantic python-dotenv apscheduler
4. Configuración Segura (Variables de Entorno):

Crea un archivo llamado .env en la raíz del proyecto (puedes guiarte de .env.example).

Agrega tus credenciales reales:

Plaintext
DB_USER=tu_usuario_postgres
DB_PASSWORD=tu_contraseña_postgres
DB_HOST=localhost

TOKEN_ID=tu_token_de_botfather
CHAT_ID=tu_id_de_chat_o_grupo
5. Encender el Motor:
Ejecuta el siguiente comando para levantar el servidor. El sistema creará las tablas automáticamente, enviará el primer reporte a Telegram de inmediato, y programará los siguientes escaneos cada 4 horas.

Bash
uvicorn main:app --reload
⚠️ Aviso Ético
Este software fue desarrollado estrictamente con fines educativos y de investigación para demostrar arquitecturas de backend y
procesamiento de datos. Los creadores no se hacen responsables del uso indebido de las funciones de web scraping.
