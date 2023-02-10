from selenium.webdriver.common.by import By


class AddRemoveElementsPages:
    #url
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    #locators
    DELETE_BUTTON = (By.CSS_SELECTOR,'[onclick="deleteElement()"]')
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR,'[onclick="addElement()"]')

    def __init(self,browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_add_button(self):
        self.browser.find_element(*self.ADD_ELEMENT_BUTTON).click()

    def is_add_button_displayed(self):
        return self.browser.find_element(*self.ADD_ELEMENT_BUTTON).is_displayed()

    def click_delete_button(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()
        

