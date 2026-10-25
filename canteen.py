from decimal import Decimal, ROUND_HALF_UP

DISCOUNT_THRESHOLD = Decimal("500")
DISCOUNT_RATE = Decimal("0.10")


def calculate_total(subtotal):
    amount = Decimal(str(subtotal))
    if amount < 0:
        raise ValueError("Subtotal cannot be negative")
    if amount > DISCOUNT_THRESHOLD:
        amount -= amount * DISCOUNT_RATE
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)