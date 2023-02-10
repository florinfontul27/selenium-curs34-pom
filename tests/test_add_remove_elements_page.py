from pages.add_remove_elements_pages import AddRemoveElementsPages


def test_add_remove_page_(browser):
    add_remove_page = AddRemoveElementsPages(browser)
    add_remove_page.load_page()
    assert add_remove_page.is_add_button_displayed()

def test_add_remove_page2(browser):
    add_remove_page = AddRemoveElementsPages(browser)
    add_remove_page.load_page()
    assert add_remove_page.is_add_button_displayed() == False


    # add_element_button.click()
    # # delete_button = chrome.find_element(By.CSS_SELECTOR,'[onclick="deleteElement()"]')
    # # assert delete_button.is_displayed()
    # # delete_button.click()
    # # assert delete_button.is_displayed() == False
    # # o sa am o lista cu toate elementele ce au selectorul [onclick = ....
    # delete_button_list = chrome.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
    # assert delete_button_list[0].is_displayed()
    # assert len(delete_button_list) == 1
    # delete_button_list[0].click()
    # delete_button_list = chrome.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
    # # daca vreau sa verific ca un element nu mai e vizibil , verific ca lungimea liste e 0, ca nu mai am nici un webeleemnt cu seectorul respectiv
    # assert len(delete_button_list) == 0
    # # cum verifica ca am mai multe butone de delete element
    # for i in range(11):
    #     add_element_button.click()
    # delete_button_list = chrome.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
    # assert len(delete_button_list) == 11, "Number of delete button is not ok"
    # delete_button_list[10].click()
    # delete_button_list = chrome.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
    # assert len(delete_button_list) == 10, "Number of delete button is not ok"