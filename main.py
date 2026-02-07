import logging
import os
import asyncio
from dotenv import load_dotenv # Importamos el gestor de secretos
from src.interfaces import DataSource, DataTarget, DataTransformer
from src.extractor import AsyncAPIExtractor
from src.loader import SQLiteLoader
from src.transformer import NewsCleaner

# 1. Cargar las variables del archivo .env al sistema
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AurorIAPipeline:
    def __init__(self, source: DataSource, transformer: DataTransformer, target: DataTarget):
        self.source = source
        self.transformer = transformer
        self.target = target

    async def run(self):
        logging.info(f">>> INICIANDO PROTOCOLO EN ENTORNO: {os.getenv('ENVIRONMENT')} <<<")
        
        df_raw = await self.source.extract()
        if df_raw.empty: return

        df_clean = self.transformer.transform(df_raw)
        if df_clean.empty: return

        self.target.load(df_clean)
        
        logging.info(">>> PROTOCOLO FINALIZADO CON ÉXITO <<<")

if __name__ == "__main__":
    # --- CONFIGURACIÓN SEGURA ---
    # Ya no hay URLs ni rutas fijas aquí. Todo viene del .env
    
    # Leemos las variables. Si no existen, podemos poner un valor por defecto (fallback)
    API_URL = os.getenv("API_URL", "https://sitio-por-defecto.com")
    API_LIMIT = int(os.getenv("API_LIMIT", "10")) # Convertimos a entero
    
    DB_PATH = os.getenv("DB_PATH", "data/default.db")
    TABLE_NAME = os.getenv("DB_TABLE_NAME", "default_table")

    # Inyección de Dependencias usando variables de entorno
    extractor = AsyncAPIExtractor(url=API_URL, limit=API_LIMIT)
    cleaner = NewsCleaner()
    
    # Aseguramos que el directorio de la DB exista
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    loader = SQLiteLoader(db_path=DB_PATH, table_name=TABLE_NAME)

    pipeline = AurorIAPipeline(source=extractor, transformer=cleaner, target=loader)
    
    asyncio.run(pipeline.run())