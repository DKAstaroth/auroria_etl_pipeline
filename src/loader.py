from sqlalchemy import create_engine
import pandas as pd
import logging
from .interfaces import DataTarget

class SQLiteLoader(DataTarget):
    """
    Implementación concreta: Guarda datos en una base SQLite local.
    """
    def __init__(self, db_path: str, table_name: str):
        # Yo configuro la conexión una sola vez al instanciar la clase
        self.connection_str = f'sqlite:///{db_path}'
        self.table_name = table_name
        self.logger = logging.getLogger(__name__)

    def load(self, df: pd.DataFrame) -> bool:
        if df.empty:
            self.logger.warning("Yo recibí un DataFrame vacío. Nada que guardar.")
            return False

        try:
            engine = create_engine(self.connection_str)
            self.logger.info(f"Yo (SQLiteLoader) guardando en tabla: {self.table_name}")
            
            with engine.connect() as conn:
                df.to_sql(self.table_name, con=conn, if_exists='append', index=False)
            
            self.logger.info("Carga exitosa.")
            return True
            
        except Exception as e:
            self.logger.error(f"Error crítico en base de datos: {e}")
            return False