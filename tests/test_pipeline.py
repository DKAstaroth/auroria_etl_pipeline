import pytest
import pandas as pd
from main import AurorIAPipeline # Importamos su cerebro orquestador

# Pytest inyecta automáticamente 'mocker' gracias a la librería pytest-mock
def test_pipeline_flujo_completo(mocker):
    """
    Prueba que verifica que el Pipeline llame a Extract, Transform y Load en el orden correcto.
    NO usa internet ni base de datos real.
    """
    
    # --- 1. ARRANGE (Preparar el Escenario) ---
    
    # Creamos un Extractor Falso (Mock)
    mock_source = mocker.Mock()
    # Le enseñamos a mentir: "Cuando te llamen, devuelve este DataFrame falso"
    df_fake_raw = pd.DataFrame([{'id': 1, 'raw_data': 'sucio'}])
    mock_source.extract.return_value = df_fake_raw

    # Creamos un Transformador Falso (Mock)
    mock_transformer = mocker.Mock()
    # Le enseñamos a mentir: "Devuelve este otro DataFrame limpio"
    df_fake_clean = pd.DataFrame([{'id': 1, 'clean_data': 'limpio'}])
    mock_transformer.transform.return_value = df_fake_clean

    # Creamos un Cargador Falso (Mock)
    mock_target = mocker.Mock()
    # Le enseñamos a decir: "Todo salió bien (True)"
    mock_target.load.return_value = True

    # Inyectamos los actores falsos en el Pipeline Real
    # Aquí se ve la magia de la Inyección de Dependencias
    pipeline = AurorIAPipeline(source=mock_source, transformer=mock_transformer, target=mock_target)

    # --- 2. ACT (Acción) ---
    pipeline.run()

    # --- 3. ASSERT (Verificación Policial) ---
    
    # Verificamos: ¿El Pipeline llamó al extractor?
    mock_source.extract.assert_called_once()
    
    # Verificamos: ¿El Pipeline llamó al transformador CON los datos que salieron del extractor?
    mock_transformer.transform.assert_called_once_with(df_fake_raw)
    
    # Verificamos: ¿El Pipeline llamó al cargador CON los datos que salieron del transformador?
    mock_target.load.assert_called_once_with(df_fake_clean)