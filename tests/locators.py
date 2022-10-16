from selenium.webdriver.common.by import By


class MainLocators:  # Главная страница
    login_button = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    personal_account_button = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")  # Раздел "Конструктор"
    main_logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип сайта
    section_sauces = (By.XPATH, "//span[text()='Соусы']")  # Разделы "Соусы"
    section_topping = (By.XPATH, "//span[text()='Начинки']")  # Раздел "Начинки"
    section_buns = (By.XPATH, "//span[text()='Булки']")  # Раздел "Булки"


class LoginPageLocators:  # Страница входа на сайт
    registration_button = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    email_field = (By.XPATH, "//fieldset[1]/div/div/input")  # Поле email
    password_field = (By.XPATH, "//fieldset[2]/div/div/input")  # Поле password
    login_button = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    recovery_button = (By.XPATH, "//a[text()='Восстановить пароль']")  # "Восстановить пароль"


class ForgotPasswordPageLocators:  # Страница восстановления пароля
    login_button = (By.XPATH, "//a[text()='Войти']")  # Кнопка Войти


class PageProfileLocators:  # Страница профиля
    exit_button = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка "Выйти"
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")  # Раздел "Конструктор


class RegistrationPageLocators:  # Страница регистрации
    name_field = (By.XPATH, "//fieldset[1]/div/div/input")  # Поле Имя
    email_field = (By.XPATH, "//fieldset[2]/div/div/input")  # Поле email
    password_field = (By.XPATH, "//fieldset[3]/div/div/input")  # Поле password
    registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка зарегистрироваться
    login_button = (By.XPATH, "//a[text()='Войти']")  # Кнопка "Войти"
    password_error = (By.XPATH, "//fieldset[3]/div/p")  # Надпись "Неккоректный пароль"
