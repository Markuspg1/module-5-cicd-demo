import pytest

from pipeline_demo import calculate_total, render_summary


def test_calculate_total_applies_discount():
    assert calculate_total(100, 0.15) == 85


def test_calculate_total_rejects_negative_subtotal():
    with pytest.raises(ValueError, match="subtotal"):
        calculate_total(-1, 0.15)


def test_calculate_total_rejects_invalid_discount():
    with pytest.raises(ValueError, match="discount_rate"):
        calculate_total(100, 1.5)


def test_render_summary_includes_environment():
    summary = render_summary("qa")

    assert "ambiente=qa" in summary
    assert "total=85" in summary
