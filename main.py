import logging
import os
from src.interfaces import DataSource, DataTarget, DataTransformer
from src.extractor import APIExtractor
from src.loader import SQLiteLoader
from src.transformer import NewsCleaner # Ahora importamos la CLASE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AurorIAPipeline:
    """
    Arquitectura 1000/1000:
    El Pipeline recibe TRES estrategias. Es totalmente agnóstico.
    """
    def __init__(self, source: DataSource, transformer: DataTransformer, target: DataTarget):
        # Inyección TOTAL de dependencias
        self.source = source
        self.transformer = transformer # La pieza que faltaba
        self.target = target

    def run(self):
        logging.info(">>> INICIANDO PROTOCOLO DE INGESTA <<<")
        
        # 1. Extracción
        df_raw = self.source.extract()
        if df_raw.empty: return

        # 2. Transformación (Delegada al objeto inyectado)
        df_clean = self.transformer.transform(df_raw)
        if df_clean.empty: return

        # 3. Carga
        self.target.load(df_clean)
        
        logging.info(">>> PROTOCOLO FINALIZADO CON ÉXITO <<<")

if __name__ == "__main__":
    # --- CONFIGURACIÓN DE NIVEL DIOS ---
    # Aquí ensamblamos el robot con las piezas que queramos hoy.
    
    # Pieza 1: El Extractor
    extractor = APIExtractor(url="https://jsonplaceholder.typicode.com/posts")
    
    # Pieza 2: El Transformador (¡Ahora es intercambiable!)
    cleaner = NewsCleaner()
    
    # Pieza 3: El Cargador
    os.makedirs("data", exist_ok=True)
    loader = SQLiteLoader(db_path="data/auroria_noticias.db", table_name="news_feed_v3")

    # Inyección
    pipeline = AurorIAPipeline(source=extractor, transformer=cleaner, target=loader)
    
    # Ejecución
    pipeline.run()