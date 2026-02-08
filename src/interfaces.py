from abc import ABC, abstractmethod

import pandas as pd


class DataSource(ABC):
    """
    Contrato actualizado para soportar ASINCRONÍA.
    """

    @abstractmethod
    async def extract(self) -> pd.DataFrame:  # <--- Note el 'async' aquí
        pass


class DataTarget(ABC):
    @abstractmethod
    def load(self, df: pd.DataFrame) -> bool:
        pass


class DataTransformer(ABC):
    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
