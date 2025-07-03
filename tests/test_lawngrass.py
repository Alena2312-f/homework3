import pytest

from src.lawngrass import LawnGrass


def test_lawngrass_init(product_grass1: LawnGrass) -> None:
    """Тестируем инициализацию объекта класса LawnGrass"""
    assert product_grass1.name == "Газонная трава"
    assert product_grass1.description == "Элитная трава для газона"
    assert product_grass1.price == 500.0
    assert product_grass1.quantity == 20
    assert product_grass1.country == "Россия"
    assert product_grass1.germination_period == "7 дней"
    assert product_grass1.color == "Зеленый"


def test_lawngrass_add(product_grass1, product_grass2):
    """Тестируем метод для ограничения сложения разных классов"""
    assert product_grass1 + product_grass2 == 35


def test_lawngrass_add_error(product_grass1, product_smartphone2):
    """Вызываем ошибку при попытке сложения разных классов"""
    with pytest.raises(TypeError):
        product_grass1 + product_smartphone2
