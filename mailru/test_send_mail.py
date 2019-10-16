from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# для упрощения параметры  для отправки почты храним в переменных
link = "https://mail.ru/"
email_to = "e.g.izotova@gmail.com"
mail_body = "This is test email message body"


def test_send_email(driver, login, password):
    """
    test login and send email from mail ru service
    :param driver: webdirver
    :param login: login to mail.ru
    :param password: password for mail.ru account
    :return:
    """

    driver.get(link)

    # заполняем логин
    input_mail = driver.find_element_by_id("mailbox:login")
    input_mail.send_keys(login)

    button_password = driver.find_element_by_css_selector("#mailbox\:submit > input")
    button_password.click()

    # заполняем пароль
    input_password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "mailbox:password")))
    input_password.send_keys(password)

    button_login = driver.find_element_by_css_selector("#mailbox\:submit > input")
    button_login.click()

    driver.implicitly_wait(7)

    # нажимаем кнопку написать письмо
    new_mail_button = driver.find_element_by_class_name("compose-button__wrapper")
    new_mail_button.click()

    driver.implicitly_wait(7)

    # заполняем поле 'кому'
    address_text = driver.find_element_by_class_name("container--H9L5q.size_s_compressed--2c-eV.dark--7GF6F")
    address_text.send_keys(email_to)

    # заполняем текст письма
    body = driver.find_element_by_class_name("cke_editable_inline")
    body.send_keys(mail_body)

    # отпарвляем письмо
    send_button = driver.find_element_by_class_name("button2_primary")
    send_button.click()
