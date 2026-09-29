from enum import Enum

from pydantic import BaseModel, Field, model_validator


class FindingType(str, Enum):
    OBLIGATION = "obligation"
    EFFECTIVE_DATE = "effective_date"
    DEFINITION = "definition"
    SCOPE = "scope"
    EXCEPTION = "exception"
    REVOCATION = "revocation"
    OTHER = "other"


class RegulatoryAnalysis(BaseModel):
    finding_type: FindingType = Field(
        description="Tipo de disposição regulatória identificada."
    )

    has_obligation: bool = Field(
        description="Indica se o texto contém uma obrigação regulatória explícita."
    )

    obligation: str | None = Field(
        default=None,
        description="Obrigação regulatória explícita, quando existir."
    )

    article: str = Field(
        description="Artigo ou seção analisada."
    )

    evidence: str = Field(
        description="Trecho do texto que sustenta a classificação."
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confiança atribuída pelo modelo, entre 0 e 1."
    )

    notes: str | None = Field(
        default=None,
        description="Observação curta quando necessária."
    )

    @model_validator(mode="after")
    def validate_obligation_consistency(self):
        if self.has_obligation and not self.obligation:
            raise ValueError(
                "Se has_obligation=True, obligation precisa ser preenchido."
            )

        if not self.has_obligation and self.obligation is not None:
            raise ValueError(
                "Se has_obligation=False, obligation deve ser None."
            )

        if self.finding_type == FindingType.OBLIGATION and not self.has_obligation:
            raise ValueError(
                "finding_type=obligation exige has_obligation=True."
            )

        return self
