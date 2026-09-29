from google import genai

from regulaguard.schemas.regulatory import RegulatoryFinding


MODEL_NAME = "gemini-3.5-flash-lite"


SYSTEM_INSTRUCTION = """
Você é o componente de análise regulatória do RegulaGuard.

Sua tarefa é analisar exclusivamente o texto recebido.

Regras:
1. Não invente artigos, obrigações ou evidências.
2. Use somente informações presentes no texto fornecido.
3. Identifique uma obrigação regulatória explícita.
4. Informe o artigo ou seção correspondente.
5. A evidência deve conter apenas o trecho necessário.
6. A confiança deve ser um número entre 0 e 1.
"""


def create_client() -> genai.Client:
    return genai.Client()


def analyze_regulatory_text(
    text: str,
    client: genai.Client,
) -> RegulatoryFinding:
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
            "schema": RegulatoryFinding.model_json_schema(),
        },
    )

    finding = RegulatoryFinding.model_validate_json(
        interaction.output_text
    )

    return finding
