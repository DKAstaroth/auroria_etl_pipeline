from sqlalchemy import create_engine
import pandas as pd
import logging
from .interfaces import DataTarget

class SQLiteLoader(DataTarget):
    def __init__(self, db_path: str, table_name: str):
        self.connection_str = f'sqlite:///{db_path}'
        self.table_name = table_name
        self.logger = logging.getLogger(__name__)

    def load(self, df: pd.DataFrame) -> bool:
        if df.empty:
            self.logger.warning("DataFrame vacío, omitiendo carga.")
            return False

        try:
            engine = create_engine(self.connection_str)
            with engine.connect() as conn:
                df.to_sql(self.table_name, con=conn, if_exists='append', index=False)
            
            self.logger.info(f"Carga exitosa en tabla '{self.table_name}'.")
            return True
            
        except Exception as e:
            self.logger.error(f"Error guardando en BD: {e}")
            return False