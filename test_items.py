
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_ad_to_basket(browser):
    browser.get(link)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) == 1, 'Button ad to basket not find'
