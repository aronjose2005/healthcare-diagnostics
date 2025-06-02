import pytest
from src.diagnostics import generate_diagnostic_insights

def test_generate_diagnostic_insights():
    insights = generate_diagnostic_insights("I have a persistent cough")
    assert isinstance(insights, str)
    assert len(insights) > 0
