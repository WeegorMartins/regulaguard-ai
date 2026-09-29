from pydantic import ValidationError

from regulaguard.llm.gemini_client import (
    analyze_regulatory_text,
    create_client,
)


SAMPLE_REGULATION = """
Art. 7º A instituição deve manter procedimentos documentados
para identificação, avaliação, monitoramento e controle
dos riscos associados às suas operações.
"""


def main() -> None:
    try:
        client = create_client()

        finding = analyze_regulatory_text(
            text=SAMPLE_REGULATION,
            client=client,
        )

        print("\nAnálise concluída:\n")
        print(finding.model_dump_json(indent=2))

    except ValidationError as error:
        print("\nA resposta do modelo não respeitou o esquema esperado.\n")
        print(error)

    except Exception as error:
        print("\nOcorreu um erro durante a chamada ao modelo.\n")
        print(error)


if __name__ == "__main__":
    main()
