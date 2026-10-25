from decimal import Decimal
import pytest
from canteen import calculate_total


def test_total_without_discount():
    assert calculate_total(100) == Decimal("100.00")


def test_total_at_discount_boundary():
    assert calculate_total(500) == Decimal("500.00")


def test_total_with_discount():
    assert calculate_total(600) == Decimal("540.00")


def test_total_just_above_boundary():
    assert calculate_total(501) == Decimal("450.90")


def test_zero_order():
    assert calculate_total(0) == Decimal("0.00")


def test_negative_subtotal():
    with pytest.raises(ValueError):
        calculate_total(-100)
