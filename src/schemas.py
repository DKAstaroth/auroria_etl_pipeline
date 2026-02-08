from pydantic import BaseModel, validator


class NewsSchema(BaseModel):
    """
    Contrato de datos estricto.
    Si la API no cumple esto, Pydantic lanzará un error.
    """

    userId: int  # Debe ser entero obligatoriamente
    id: int  # Debe ser entero
    title: str  # Debe ser texto
    body: str  # Debe ser texto

    # --- Validaciones Extra (Nivel Dios) ---
    @validator("title")
    def title_must_not_be_empty(cls, v):
        if len(v) < 5:
            raise ValueError("El título es sospechosamente corto")
        return v
