from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configurar opciones del navegador
chrome_options = Options()
# Puedes agregar más opciones según sea necesario

# Inicializar el navegador con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options)

# Abrir página web
driver.get("https://ais.usvisa-info.com/es-co/niv/users/sign_in")

# Esperar a que la página cargue completamente
time.sleep(5)

# Encontrar el campo de texto para ingresar el correo electrónico y enviar las teclas
campo_correo = driver.find_element(By.XPATH, "//*[@id='user_email']")
campo_correo.send_keys("jaime.serrano2001@gmail.com")

# Esperar un momento para que se complete la acción
time.sleep(5)

# Encontrar el campo de texto y ingresar la contraseña
campo_password = driver.find_element(By.XPATH, "//*[@id='user_password']")
campo_password.send_keys("12345678")

# Esperar un momento para que se complete la acción
time.sleep(5)

# Seleccionar cuadro de aceptación de políticas
cuadro_politicas = driver.find_element(By.XPATH, "//*[@id='sign_in_form']/div[3]/label/div")
cuadro_politicas.click()

# Esperar un momento para que se complete la acción
time.sleep(5)

# Hacer clic en un botón Iniciar Sesión
boton_login = driver.find_element(By.XPATH, "//*[@id='sign_in_form']/p[1]/input")
boton_login.click()

# Esperar un momento para que se complete la acción
time.sleep(5)

# Extraer y almacenar la fecha
texto_fecha = driver.find_element(By.CSS_SELECTOR, "p.consular-appt").text
fecha = texto_fecha.split(":")[1].strip()

print("Fecha de la cita:", fecha)

# Esperar un momento para que se complete la acción
time.sleep(5)

# Hacer clic en un botón Continuar a Perfil
boton_continuar = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul/li/a")
boton_continuar.click()

# Esperar un momento para que se complete la acción
time.sleep(5)

# Localizar el elemento del acordeón
acordeon_reprogramar = driver.find_element(By.XPATH, "//*[@id='forms']/ul/li[4]")
acordeon_reprogramar.click()

# Esperar un momento para que se complete la acción
time.sleep(5)

# Localizar el elemento dentro del acordeón Reprogramar Cita
elemento_acordeon = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[4]/div/div/div[2]/p[2]/a")
elemento_acordeon.click()

# Esperar un momento para que se complete la acción
time.sleep(5)

# Localizar el elemento dentro del acordeón Reprogramar Cita
consulate_date = driver.find_element(By.XPATH, "//*[@id='consulate_date_time']")
consulate_date.click()

# Esperar un momento para que se complete la acción
time.sleep(5)


# No cerrar el navegador aquí
# driver.quit()
