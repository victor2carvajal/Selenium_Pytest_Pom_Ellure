import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from allure_commons.types import AttachmentType


class CartPage:
    addedProductIMG = "//div[@class='sc-list-item-content']"
    deleteBTN = "//input[@data-action='delete']"
    deletedMSG = "//div[contains(.,'se ha eliminado del Carrito.')]/span"

    def verify_add(self, time):
        WebDriverWait(self, time).until(lambda d: d.find_element(By.XPATH, CartPage.addedProductIMG))
        allure.attach(self.get_screenshot_as_png(), name="Added Product", attachment_type=AttachmentType.PNG)
        assert self.find_element(By.XPATH, CartPage.addedProductIMG), exit()

    def delete_product(self):
        self.find_element(By.XPATH, CartPage.deleteBTN).click()

    def verify_delete(self, delete_message):
        allure.attach(self.get_screenshot_as_png(), name="deleted Product", attachment_type=AttachmentType.PNG)
        delete_get_text = self.find_element(By.XPATH, CartPage.deletedMSG).text
        assert delete_message in delete_get_text
