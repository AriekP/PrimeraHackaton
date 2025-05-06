from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configuración de la conexión a la base de datos
DB_HOST = os.getenv("DB_HOST", "localhost")  # Valor por defecto para XAMPP
DB_PORT = os.getenv("DB_PORT", "3306")       # Puerto default de MySQL
DB_USER = os.getenv("DB_USER", "root")       # Usuario default de XAMPP
DB_PASSWORD = os.getenv("DB_PASSWORD", "")   # Contraseña vacía por defecto en XAMPP
DB_NAME = os.getenv("DB_NAME", "arca_rrhh")  # Nombre de tu base de datos

# Cadena de conexión para MySQL (XAMPP)
SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Configuración del motor de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,  # Verifica que la conexión esté activa antes de usarla
    pool_recycle=3600    # Recicla conexiones después de 1 hora
)

# Configuración de la sesión de base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para los modelos
Base = declarative_base()

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()