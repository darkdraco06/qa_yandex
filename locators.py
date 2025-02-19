# Определение локаторов элементов на странице Stellar Burgers

#Локаторы для проверки Входа
LOGON_IN_ACCOUNT_BUTTON_XPATH = '//button[text()="Войти в аккаунт"]' # Локатор кнопки "Войти в аккаунт"
LOGON_IN_PERSONAL_ACCOUNT_XPATH = '//p[text()="Личный Кабинет"]' # Локатор для ссылки "личный кабинет"
LOGON_IN_REGISTER_FORM_XPATH = '//a[text()="Войти"]' # Локатор для кнопки войти в форме регитсрации
LOGON_BUTTON_XPATH = '//button[text()="Войти"]' # Локатор кнопки "Войти"
LOGON_TITLE_XPATH = "//h2[text()='Вход']" # Локатор для титульной страницы Вход
LOGON_EMAIL_XPATH = '//form/fieldset[1]/div/div/input' # Локатор поля "Email" при регистрации
LOGON_PASSWORD_XPATH = '//input[@name="Пароль"]' # Локатор поля "Пароль" при регистрации
LOGON_BUTTON_ORDER_XPATH = '//button[text()="Оформить заказ"]' # Локатор кнопки из личного кабинета
LOGON_FORGOT_PASSWORD_XPATH = '//a[text()="Восстановить пароль"]' # Локатор ссылки для перехода на страницу восстановления пароля

#Локаторы для проверки Регистрации
NAME_XPATH = '//form/fieldset[1]/div/div/input' # Локатор поля "Имя" при регистрации
EMAIL_XPATH = '//form/fieldset[2]/div/div/input' # Локатор поля "Email" при регистрации
PASSWORD_XPATH = '//input[@name="Пароль"]' # Локатор поля "Пароль" при регистрации
REGISTER_HREF_XPATH = '//a[text() ="Зарегистрироваться"]'# Локатор ссылки на раздел Зарегистрироваться
REGISTER_BUTTON_XPATH = "//button[text()='Зарегистрироваться']" # Локатор кнопки Зарегистрироваться
ERROR_MESSAGE_XPATH = "//p[@class='input__error text_type_main-default']" # Локатор для сообщения об ошибке при некорректном пароле

#Локаторы для проверки в личный кабинет
ACCOUNT_BUTTON_PROFILE = '//a[text()="Профиль"]' # Локатор кнопки Профиль из личного кабинета
#Локаторы для проверки для раздела конструктор
BUILDER_BUTTON_XPATH = '//p[text()="Конструктор"]' # Локатор страницы Конструктора
BUILDER_MAKE_BURGER_XPATH = '//h1[text()="Соберите бургер"]' # Локатор текста "Соберите бургер"
BUILDER_LOGO_XPATH = '//div[@class="AppHeader_header__logo__2D0X2"]/a' # Локатор логотипа

#Локаторы для проверки Выхода
LOGOUT_BUTTON_EXIT_XPATH = '//button[text()="Выход"]' # Локатор кнопки выхода

#Локаторы для проверки разделов Соусы, Начинки, Булки
BUILDER_BUNS_XPATH = "//span[text()='Булки']" # Локатор ссылки "Булки"
BUILDER_SAUCES_XPATH = "//span[text()='Соусы']" # Локатор ссылки "Соусы"
BUILDER_FILLINGS_XPATH = '//span[text()="Начинки"]' # Локатор ссылки "Начинки"

BUILDER_FILLINGS_ACTIVE_XPATH = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]' # Локатор активного раздела Начинки
BUILDER_SAUCES_ACTIVE_XPATH = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]'# Локатор активного раздела Соуссы
BUILDER_BUNS_ACTIVE_XPATH = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]'# Локатор кнопки из личного Булки