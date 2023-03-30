from selenium.webdriver.common.by import By


class HomePage:
    searchTXT = "twotabsearchtextbox"
    submitBTN = "nav-search-submit-button"

    def open_page(self, url):
        self.get(url)
        self.maximize_window()

    def search_product(self, product):
        self.find_element(By.ID, HomePage.searchTXT).send_keys(product)
        self.find_element(By.ID, HomePage.submitBTN).click()
