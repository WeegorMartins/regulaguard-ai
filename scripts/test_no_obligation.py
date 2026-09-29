from regulaguard.llm.gemini_client import (
    analyze_regulatory_text,
    create_client,
)


SAMPLE_TEXT = """
Art. 15. Esta Resolução entra em vigor em 1º de janeiro de 2027.
"""


def main() -> None:
    client = create_client()

    finding = analyze_regulatory_text(
        text=SAMPLE_TEXT,
        client=client,
    )

    print("\nResultado:\n")
    print(finding.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
