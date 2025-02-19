# Определение локаторов элементов на странице Stellar Burgers

#Локаторы для проверки Входа
logon_in_account_button_xpath = '//button[text()="Войти в аккаунт"]' # Локатор кнопки "Войти в аккаунт"
logon_in_personal_account_xpath = '//p[text()="Личный Кабинет"]' # Локатор для ссылки "личный кабинет"
logon_in_register_form_xpath = '//a[text()="Войти"]' # Локатор для кнопки войти в форме регитсрации
logon_button_xpath = '//button[text()="Войти"]' # Локатор кнопки "Войти"
logon_title_xpath = "//h2[text()='Вход']" # Локатор для титульной страницы Вход
logon_email_xpath = '//form/fieldset[1]/div/div/input' # Локатор поля "Email" при регистрации
logon_password_xpath = '//input[@name="Пароль"]' # Локатор поля "Пароль" при регистрации
logon_button_order_xpath = '//button[text()="Оформить заказ"]' # Локатор кнопки из личного кабинета
logon_forgot_password_xpath = '//a[text()="Восстановить пароль"]' # Локатор ссылки для перехода на страницу восстановления пароля

#Локаторы для проверки Регистрации
name_xpath = '//form/fieldset[1]/div/div/input' # Локатор поля "Имя" при регистрации
email_xpath = '//form/fieldset[2]/div/div/input' # Локатор поля "Email" при регистрации
password_xpath = '//input[@name="Пароль"]' # Локатор поля "Пароль" при регистрации
register_href_xpath = '//a[text() ="Зарегистрироваться"]'# Локатор ссылки на раздел Зарегистрироваться
register_button_xpath = "//button[text()='Зарегистрироваться']" # Локатор кнопки Зарегистрироваться
error_message_xpath = "//p[@class='input__error text_type_main-default']" # Локатор для сообщения об ошибке при некорректном пароле

#Локаторы для проверки в личный кабинет
account_button_profile = '//a[text()="Профиль"]' # Локатор кнопки Профиль из личного кабинета
#Локаторы для проверки для раздела конструктор
builder_button_xpath = '//p[text()="Конструктор"]' # Локатор страницы Конструктора
builder_make_burger_xpath = '//h1[text()="Соберите бургер"]' # Локатор текста "Соберите бургер"
builder_logo_xpath = '//div[@class="AppHeader_header__logo__2D0X2"]/a' # Локатор логотипа

#Локаторы для проверки Выхода
logout_button_exit_xpath = '//button[text()="Выход"]' # Локатор кнопки выхода

#Локаторы для проверки разделов Соусы, Начинки, Булки
builder_buns_xpath = "//span[text()='Булки']" # Локатор ссылки "Булки"
builder_sauces_xpath = "//span[text()='Соусы']" # Локатор ссылки "Соусы"
builder_fillings_xpath = '//span[text()="Начинки"]' # Локатор ссылки "Начинки"

builder_fillings_active_xpath = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]' # Локатор активного раздела Начинки
builder_sauces_active_xpath = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]'# Локатор активного раздела Соуссы
builder_buns_active_xpath = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]'# Локатор кнопки из личного Булки