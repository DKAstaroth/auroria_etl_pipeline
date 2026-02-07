import logging
import os
# Importamos las abstracciones y las implementaciones
from src.interfaces import DataSource, DataTarget
from src.extractor import APIExtractor
from src.loader import SQLiteLoader
from src.transformer import transform_data # Aún mantenemos este como función por ahora

# Configuración de Logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AurorIAPipeline:
    """
    La clase Maestra. Define el FLUJO, pero no los detalles.
    Principio de Inversión de Dependencias: Depende de abstracciones (DataSource), 
    no de concreciones (APIExtractor).
    """
    def __init__(self, source: DataSource, target: DataTarget):
        # Inyección de Dependencias: Le damos las herramientas al nacer
        self.source = source
        self.target = target

    def run(self):
        logging.info(">>> INICIANDO PROTOCOLO DE INGESTA <<<")
        
        # 1. Extracción (Polimorfismo: no sé qué fuente es, solo sé que tiene un método extract)
        df_raw = self.source.extract()
        
        if df_raw.empty:
            logging.error("Flujo abortado en extracción.")
            return

        # 2. Transformación
        df_clean = transform_data(df_raw)

        # 3. Carga (Polimorfismo: no sé qué base de datos es, solo sé que tiene un método load)
        success = self.target.load(df_clean)
        
        if success:
            logging.info(">>> PROTOCOLO FINALIZADO CON ÉXITO <<<")
        else:
            logging.error(">>> FALLO EN EL ALMACENAMIENTO <<<")

if __name__ == "__main__":
    # --- ZONA DE CONFIGURACIÓN (Composition Root) ---
    
    # Aquí decidimos qué piezas usar hoy. Mañana podríamos cambiar APIExtractor por CSVExtractor
    # y el pipeline NO tendría que cambiar ni una línea de código. (Open/Closed Principle)
    
    mi_fuente = APIExtractor(url="https://jsonplaceholder.typicode.com/posts")
    
    # Aseguramos que exista la carpeta data
    os.makedirs("data", exist_ok=True)
    mi_destino = SQLiteLoader(db_path="data/auroria_noticias.db", table_name="news_feed_v2")

    # Instanciamos el pipeline inyectándole las piezas
    app = AurorIAPipeline(source=mi_fuente, target=mi_destino)
    
    # Ejecutamos
    app.run()