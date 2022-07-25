import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# Add to basket button in different languages
basket_buttons_lang = ['أضف الى سلة التسوق', 'Afegeix a la cistella', 'Vložit do košíku', 'Læg i kurv', 'In Warenkorb legen',
                       'Add to basket', 'Προσθήκη στο καλάθι', 'Añadir al carrito', 'Lisää koriin', 'Ajouter au panier', 
                       'Aggiungi al carrello', '장바구니 담', 'Voeg aan winkelmand toe', 'Dodaj do koszyka', 'Adicionar ao carrinho', 
                       'Adicionar à cesta', 'Adauga in cos', 'Pridať do košíka', 'Добавить в корзину', 'Додати в кошик']


def test_product_page_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    # Find the button and check if it is in the list
    basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    basket_button_text = basket_button.text
    assert basket_button_text in basket_buttons_lang, "Basket button was not found"
