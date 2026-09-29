from regulaguard.llm.gemini_client import (
    analyze_regulatory_text,
    create_client,
)


SAMPLE_TEXT = """
Art. 7º A instituição deve manter procedimentos documentados
para identificação, avaliação, monitoramento e controle
dos riscos associados às suas operações.
"""


def main() -> None:
    client = create_client()

    analysis = analyze_regulatory_text(
        text=SAMPLE_TEXT,
        client=client,
    )

    print("\nResultado:\n")
    print(analysis.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
