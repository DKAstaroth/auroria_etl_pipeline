from abc import ABC, abstractmethod
import pandas as pd

# Interfaz: Fuente de Datos (Strategy Pattern)
class DataSource(ABC):
    """
    Contrato que debe cumplir cualquier clase que quiera extraer datos.
    No importa de dónde vengan, deben devolver un DataFrame.
    """
    @abstractmethod
    def extract(self) -> pd.DataFrame:
        pass

# Interfaz: Destino de Datos
class DataTarget(ABC):
    """
    Contrato que debe cumplir cualquier clase que quiera guardar datos.
    No importa si es SQLite, Postgres o un archivo .txt.
    """
    @abstractmethod
    def load(self, df: pd.DataFrame) -> bool:
        pass


# Interfaz: Transformador de Datos
class DataTransformer(ABC):
    """
    Contrato para cualquier clase que quiera manipular/limpiar datos.
    Recibe DataFrame sucio -> Devuelve DataFrame limpio.
    """
    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass