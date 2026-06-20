FEATURE_MESSAGE = "Modulo 5: pruebas automatizadas activas cambio en dev"


def calculate_total(subtotal: float, discount_rate: float) -> float:
    if subtotal < 0:
        raise ValueError("subtotal must be positive")
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("discount_rate must be between 0 and 1")

    return round(subtotal * (1 - discount_rate), 2)


def render_summary(environment: str) -> str:
    total = calculate_total(100, 0.15)
    return f"{FEATURE_MESSAGE} | ambiente={environment} | total={total}"
