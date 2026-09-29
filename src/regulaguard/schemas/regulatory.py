from pydantic import BaseModel, Field


class RegulatoryFinding(BaseModel):
    obligation: str = Field(
        description="Obrigação regulatória identificada no texto."
    )

    article: str = Field(
        description="Artigo ou seção que sustenta a obrigação."
    )

    evidence: str = Field(
        description="Trecho do texto que sustenta a obrigação."
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confiança atribuída pelo modelo, entre 0 e 1."
    )
