import pytest
from selenium.webdriver.common.by import By

from conftest import driver
from pages.home_page import HomePage


def test_home_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.show_title()

    assert home_page.show_title() == "Rozetka.pl – kupuj elektronikę, sprzęt AGD, ubrania i wiele innych rzeczy"


def test_show_categories(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.show_categories()
    assert home_page.show_categories().__contains__("AGD")
