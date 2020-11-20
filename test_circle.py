"""Модуль с тестами для окружности"""
from figures import Circle, Triangle
from pytest import approx
import pytest


def test_create_circle():
    """Тест создания окружности"""
    circle = Circle(radius=10)
    assert circle.name == 'Circle'


def test_circle_perimeter():
    """Тест вычисления периметра окружности"""
    circle = Circle(radius=10)
    assert int(circle.find_perimeter()) == approx(62, abs=2e-1)


def test_circle_area():
    """Тест вычисления площади окружности"""
    circle = Circle(radius=10)
    assert int(circle.find_area()) == approx(314, abs=2e-1)


def test_add_areas():
    """Тест вычисления суммы площадей двух фигур"""
    circle = Circle(radius=10)
    triangle = Triangle(a=5, b=6)
    assert circle.add_area(triangle) == approx(329, abs=2e-1)


def test_add_areas_error():
    """Тест вызова исключения с невалидными параметрами"""
    var = 10
    circle = Circle(radius=10)
    with pytest.raises(AttributeError):
        circle.add_area(var)
