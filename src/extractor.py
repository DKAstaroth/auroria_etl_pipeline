import aiohttp
import asyncio
import pandas as pd
import logging
from pydantic import ValidationError # Importamos el manejo de errores
from .interfaces import DataSource
from .schemas import NewsSchema # Importamos nuestro guardia

class AsyncAPIExtractor(DataSource):
    def __init__(self, url: str, limit: int = 100):
        self.base_url = url
        self.limit = limit
        self.logger = logging.getLogger(__name__)

    async def fetch_one(self, session, id_noticia):
        url = f"{self.base_url}/{id_noticia}"
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                raw_data = await response.json()
                
                if not raw_data: return None

                # --- MOMENTO DE LA VERDAD (VALIDACIÓN) ---
                try:
                    # Intentamos forzar los datos al molde
                    validated_data = NewsSchema(**raw_data)
                    
                    # Si pasa, devolvemos los datos como diccionario limpio
                    # .model_dump() es el método moderno de Pydantic v2
                    # Si usa Pydantic v1 sería .dict()
                    return validated_data.model_dump() 
                
                except ValidationError as e:
                    self.logger.warning(f"Noticia {id_noticia} rechazada por validación: {e}")
                    return None

        except Exception as e:
            self.logger.error(f"Error bajando noticia {id_noticia}: {e}")
            return None

    async def extract(self) -> pd.DataFrame:
        self.logger.info(f"Iniciando descarga VALIDADA de {self.limit} noticias...")
        
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_one(session, i) for i in range(1, self.limit + 1)]
            results = await asyncio.gather(*tasks)
            
        clean_results = [r for r in results if r is not None]
        
        df = pd.DataFrame(clean_results)
        self.logger.info(f"Descarga finalizada. {len(df)} registros válidos obtenidos.")
        return df