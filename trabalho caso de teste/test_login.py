from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_sucesso():


    driver = webdriver.Edge()

    try:
        print("Abrindo site...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        print("Preenchendo usuário...")
        user = driver.find_element(By.ID, "user-name")
        for letra in "standard_user":
            user.send_keys(letra)
            time.sleep(0.1)

        print("Preenchendo senha...")
        password = driver.find_element(By.ID, "password")
        for letra in "secret_sauce":
            password.send_keys(letra)
            time.sleep(0.1)

        print("Clicando em Login...")
        time.sleep(1)
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        time.sleep(3)

        print("Verificando resultado...")
        titulo = driver.find_element(By.CLASS_NAME, "title").text
        assert titulo == "Products"
        print("Login OK 👌")

    except Exception as e:
        print(f"Erro encontrado: {e}")

    finally:
        time.sleep(5)
        print("Fechando o navegador...")
        driver.quit()

test_login_sucesso()
