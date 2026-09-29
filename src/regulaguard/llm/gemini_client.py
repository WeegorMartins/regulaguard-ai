from google import genai

from regulaguard.schemas.regulatory import RegulatoryAnalysis


MODEL_NAME = "gemini-3.5-flash-lite"


SYSTEM_INSTRUCTION = """
Você é o componente de análise regulatória do RegulaGuard.

Analise exclusivamente o texto fornecido.

Primeiro classifique a natureza principal da disposição regulatória.

Valores possíveis:
- obligation: obrigação explícita;
- effective_date: vigência ou entrada em vigor;
- definition: definição de conceito;
- scope: escopo ou aplicabilidade;
- exception: exceção;
- revocation: revogação;
- other: outra categoria.

Regras:
1. Não invente artigos, obrigações ou evidências.
2. Use somente informações presentes no texto.
3. Não transforme vigência, definição ou escopo em obrigação.
4. has_obligation deve ser true somente quando houver obrigação explícita.
5. Quando has_obligation=false, obligation deve ser null.
6. Quando has_obligation=true, obligation deve descrever somente a obrigação explícita.
7. A evidência deve reproduzir apenas o trecho necessário.
8. A confiança deve ser um número entre 0 e 1.
"""


def create_client() -> genai.Client:
    return genai.Client()


def analyze_regulatory_text(
    text: str,
    client: genai.Client,
) -> RegulatoryAnalysis:
    interaction = client.interactions.create(
        model=MODEL_NAME,
        system_instruction=SYSTEM_INSTRUCTION,
        input=text,
        generation_config={
            "temperature": 0.1,
        },
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": RegulatoryAnalysis.model_json_schema(),
        },
    )

    analysis = RegulatoryAnalysis.model_validate_json(
        interaction.output_text
    )

    return analysis
