import logging
import os
import asyncio
from src.interfaces import DataSource, DataTarget, DataTransformer
from src.extractor import AsyncAPIExtractor
from src.loader import SQLiteLoader
from src.transformer import NewsCleaner

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AurorIAPipeline:
    def __init__(self, source: DataSource, transformer: DataTransformer, target: DataTarget):
        self.source = source
        self.transformer = transformer
        self.target = target

    async def run(self):
        logging.info(">>> INICIANDO PROTOCOLO ASÍNCRONO <<<")
        
        # await es obligatorio aquí porque extract es asíncrono
        df_raw = await self.source.extract()
        
        if df_raw.empty: return

        df_clean = self.transformer.transform(df_raw)
        
        if df_clean.empty: return

        self.target.load(df_clean)
        
        logging.info(">>> PROTOCOLO FINALIZADO CON ÉXITO <<<")

if __name__ == "__main__":
    url_base = "https://jsonplaceholder.typicode.com/posts"
    
    # Probamos con 50 peticiones concurrentes
    extractor = AsyncAPIExtractor(url=url_base, limit=50)
    cleaner = NewsCleaner()
    
    os.makedirs("data", exist_ok=True)
    loader = SQLiteLoader(db_path="data/auroria_noticias.db", table_name="news_feed_async")

    pipeline = AurorIAPipeline(source=extractor, transformer=cleaner, target=loader)
    
    # Punto de entrada al Loop de Eventos
    asyncio.run(pipeline.run())