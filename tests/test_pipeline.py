from unittest.mock import AsyncMock, MagicMock

import pandas as pd
import pytest

from main import AurorIAPipeline


# Marca para decirle a pytest: "Oye, este test es asíncrono, espéralo"
@pytest.mark.asyncio
async def test_pipeline_flujo_completo_async(mocker):
    """
    Prueba el flujo ASÍNCRONO completo usando Mocks.
    """

    # --- 1. ARRANGE (Preparar) ---

    # Mock del Extractor: Debe ser AsyncMock porque tiene métodos 'async def'
    mock_source = AsyncMock()
    df_fake_raw = pd.DataFrame([{"id": 1, "raw_data": "sucio"}])
    # Configurar el retorno de la corutina
    mock_source.extract.return_value = df_fake_raw

    # Mock del Transformer: Este sigue siendo síncrono (MagicMock normal)
    # Porque transform_data NO es async
    mock_transformer = MagicMock()
    df_fake_clean = pd.DataFrame([{"id": 1, "clean_data": "limpio"}])
    mock_transformer.transform.return_value = df_fake_clean

    # Mock del Loader: Síncrono también
    mock_target = MagicMock()
    mock_target.load.return_value = True

    # Inyectamos
    pipeline = AurorIAPipeline(
        source=mock_source, transformer=mock_transformer, target=mock_target
    )

    # --- 2. ACT (Acción) ---
    # Usamos 'await' porque pipeline.run() es asíncrono
    await pipeline.run()

    # --- 3. ASSERT (Verificación) ---

    # Verificamos que se haya llamado (y esperado) a la extracción
    mock_source.extract.assert_awaited_once()

    # Verificamos la transformación
    mock_transformer.transform.assert_called_once_with(df_fake_raw)

    # Verificamos la carga
    mock_target.load.assert_called_once_with(df_fake_clean)
