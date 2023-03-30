from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class ProductPage:
    orderByDDL = "//select[@id='s-result-sort-select']"
    secondProductBTN = "(//div[@class='a-section aok-relative s-image-fixed-height'])[2]"
    addToCartBTN = "add-to-cart-button"
    cartBTN = "//a[contains(@data-csa-c-type,'button')]"

    def sort_by(self, descending_index):
        Select(self.find_element(By.XPATH, ProductPage.orderByDDL)).select_by_index(descending_index)

    def select_product(self, time):
        WebDriverWait(self, time).until(lambda d: d.find_element(By.XPATH, ProductPage.secondProductBTN))
        self.find_element(By.XPATH, ProductPage.secondProductBTN).click()

    def add_to_cart(self):
        self.find_element(By.ID, ProductPage.addToCartBTN).click()

    def go_to_cart_click_mouse(self, time):
        WebDriverWait(self, time).until(lambda d: d.find_element(By.XPATH, ProductPage.cartBTN))
        act = ActionChains(self)
        act.move_to_element(self.find_element(By.XPATH, ProductPage.cartBTN)).click().perform()
