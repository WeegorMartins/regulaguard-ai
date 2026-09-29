import pytest
from pydantic import ValidationError

from regulaguard.schemas.regulatory import RegulatoryAnalysis


def test_effective_date_without_obligation_is_valid():
    analysis = RegulatoryAnalysis(
        finding_type="effective_date",
        has_obligation=False,
        obligation=None,
        article="Art. 15",
        evidence="Esta Resolução entra em vigor em 1º de janeiro de 2027.",
        confidence=0.95,
    )

    assert analysis.finding_type.value == "effective_date"
    assert analysis.has_obligation is False
    assert analysis.obligation is None


def test_obligation_is_valid():
    analysis = RegulatoryAnalysis(
        finding_type="obligation",
        has_obligation=True,
        obligation="A instituição deve manter procedimentos documentados.",
        article="Art. 7º",
        evidence="A instituição deve manter procedimentos documentados.",
        confidence=0.90,
    )

    assert analysis.finding_type.value == "obligation"
    assert analysis.has_obligation is True
    assert analysis.obligation is not None


def test_non_obligation_cannot_contain_obligation_text():
    with pytest.raises(ValidationError):
        RegulatoryAnalysis(
            finding_type="effective_date",
            has_obligation=False,
            obligation="Cumprir a data de vigência.",
            article="Art. 15",
            evidence="Esta Resolução entra em vigor em 1º de janeiro de 2027.",
            confidence=0.95,
        )


def test_confidence_cannot_be_greater_than_one():
    with pytest.raises(ValidationError):
        RegulatoryAnalysis(
            finding_type="obligation",
            has_obligation=True,
            obligation="A instituição deve manter controles.",
            article="Art. 7º",
            evidence="A instituição deve manter controles.",
            confidence=85,
        )
