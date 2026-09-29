from datetime import date
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl


class DocumentType(str, Enum):
    REGULATION = "regulation"
    INTERNAL_POLICY = "internal_policy"


class DocumentStatus(str, Enum):
    ACTIVE = "active"
    REVOKED = "revoked"
    UNKNOWN = "unknown"


class RegulatoryDocument(BaseModel):
    document_id: str = Field(
        min_length=1,
        description="Identificador único do documento."
    )

    document_type: DocumentType = Field(
        description="Tipo do documento."
    )

    issuer: str = Field(
        min_length=1,
        description="Órgão ou entidade responsável pelo documento."
    )

    number: str | None = Field(
        default=None,
        description="Número oficial do documento, quando existir."
    )

    title: str = Field(
        min_length=1,
        description="Título oficial ou identificador legível."
    )

    published_at: date | None = Field(
        default=None,
        description="Data de publicação."
    )

    status: DocumentStatus = Field(
        default=DocumentStatus.UNKNOWN,
        description="Situação atual do documento."
    )

    source_url: HttpUrl | None = Field(
        default=None,
        description="Endereço da fonte original."
    )

    version: str = Field(
        default="1",
        description="Versão do documento dentro do RegulaGuard."
    )

    content: str = Field(
        min_length=1,
        description="Conteúdo textual integral do documento."
    )
