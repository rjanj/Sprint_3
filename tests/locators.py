from selenium.webdriver.common.by import By


class MainLocators:  # Главная страница
    login_button = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    personal_account_button = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")  # Раздел "Конструктор"
    main_logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип сайта
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"

    # Конструктор
    section_sauces = (By.XPATH, "//div[2]")  # Секция "Соусы"
    section_topping = (By.XPATH, "//div[3]")  # Секция "Начинки"
    section_buns = (By.XPATH, "//section[1]/div[1]/div[1]")  # Секция "Булки"
    element_buns = (By.XPATH, "//h2[1]")  # Текст "Булки"
    element_sauce = (By.XPATH, "//h2[2]")  # Текст "Соусы"
    element_topping = (By.XPATH, "//h2[3]")  # Текст "Начинки"


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
    profile_email = (By.XPATH, '//li[2]/div/div/input')  # Почта пользователя


class RegistrationPageLocators:  # Страница регистрации
    name_field = (By.XPATH, "//fieldset[1]/div/div/input")  # Поле Имя
    email_field = (By.XPATH, "//fieldset[2]/div/div/input")  # Поле email
    password_field = (By.XPATH, "//fieldset[3]/div/div/input")  # Поле password
    registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка зарегистрироваться
    login_button = (By.XPATH, "//a[text()='Войти']")  # Кнопка "Войти"
    password_error = (By.XPATH, "//fieldset[3]/div/p")  # Надпись "Неккоректный пароль"
