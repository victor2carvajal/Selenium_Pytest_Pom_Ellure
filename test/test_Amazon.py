import unittest

import pytest
from selenium import webdriver
from src.pages.home_page import HomePage
from src.pages.product_page import ProductPage
from src.pages.cart_page import CartPage

url = "https://www.amazon.com/-/es/"
productOne = "iphone 14 pro"
productTwo = "washing machine"
descendingIndex = 1
time = 10
deleteMessageExpected = "se ha eliminado del Carrito."
deleteMessageExpected2 = "loca"
driver = ""


class AddToCart(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        HomePage.open_page(driver, url)

    @pytest.mark.run
    def test_addToCartAndDeleteOne(self):
        HomePage.search_product(driver, productOne)
        ProductPage.sort_by(driver, descendingIndex)
        ProductPage.select_product(driver, time)
        ProductPage.add_to_cart(driver)
        ProductPage.go_to_cart_click_mouse(driver, time)
        CartPage.verify_add(driver, time)
        CartPage.delete_product(driver)
        CartPage.verify_delete(driver, deleteMessageExpected)

    @pytest.mark.run
    def test_addToCartAndDeleteTwo(self):
        HomePage.search_product(driver, productTwo)
        ProductPage.sort_by(driver, descendingIndex)
        ProductPage.select_product(driver, time)
        ProductPage.add_to_cart(driver)
        ProductPage.go_to_cart_click_mouse(driver, time)
        CartPage.verify_add(driver, time)
        CartPage.delete_product(driver)
        CartPage.verify_delete(driver, deleteMessageExpected)

    def tearDown(self):
        driver.close()


if __name__ == '__main__':
    var = unittest.main
