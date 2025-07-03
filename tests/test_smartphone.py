import pytest

from src.smartphone import Smartphone


def test_smartphone_init(product_smartphone1: Smartphone) -> None:
    """Тестируем инициализацию объекта класса Smartphone"""
    assert product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone1.price == 180000.0
    assert product_smartphone1.quantity == 5
    assert product_smartphone1.efficiency == 95.5
    assert product_smartphone1.model == "S23 Ultra"
    assert product_smartphone1.memory == 256
    assert product_smartphone1.color == "Серый"


def test_smartphone_add(product_smartphone1, product_smartphone2):
    """Тестируем метод для ограничения сложения разных классов"""
    assert product_smartphone1 + product_smartphone2 == 13


def test_smartphone_add_error(product_grass1, product_smartphone2):
    """Вызываем ошибку при попытке сложения разных классов"""
    with pytest.raises(TypeError):
        product_grass1 + product_smartphone2
