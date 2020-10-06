from selenium import webdriver

# Librerías de python
import unittest
import time


class SearchCases(unittest.TestCase):

    def test_search_no_elements(self):

        driver = webdriver.Chrome('chromedriver.exe')
        # Abrir el browser
        driver.get('http://automationpractice.com/index.php')
        # Encontrando o localizando el elemento por ID,
        # luego mediante send_keys ingresamos el texto Hola
        driver.find_element_by_id('search_query_top').send_keys('hola')
        # Hacemos click sobre el botón submit_search
        driver.find_element_by_name('submit_search').click()
        # Vamos a esperar dos segundos, para que cargue la página
        # con sus elementos.
        time.sleep(2)

        # Verificamos que si ingreso un texto que no existe,
        # se muestre el mensaje en la página  => No results were found for your search "hola"
        # Mediante el assertEqual, comparamos si las dos variables son iguales.
        # cuando encontremos el xpath, vamos a extraer el texto, para asignarlo a la variable
        # result y así compararla con el texto de la variable expected_result
        #result = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        #expected_result = 'No results were found for your search "hola"'

        # Comentamos las dos variables de arriba, en el assert reemplazamos los valores de las
        # variables y nos ahorramos dos lineas de código
        self.assertEqual(driver.find_element_by_xpath('//*[@id="center_column"]/p').text, 'No results were found for your search "hola"')

        # Cerrar el browser
        driver.close()

        # Cerrar la sesión del webdriver
        driver.quit()


    def test_search_find_dresses(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_id('search_query_top').send_keys('dress')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)

        # Mediante el assertTrue.
        # cuando encontremos el xpath, vamos a extraer el texto, para asignarlo a la variable
        # result y así compararla con el texto de la variable expected_result
        #result = driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text
        #expected_result = "DRESS"

        # el texto DRESS se encuentra en el texto que tiene la variable result.
        # Comentamos las dos variables de arriba, en el assert reemplazamos los valores de las
        # variables y nos ahorramos dos lineas de código
        self.assertTrue("DRESS" in driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)

        driver.close()
        driver.quit()


if __name__ == '__main__':
    # Las pruebas que encuentre acá, las va a ir ejecutando.
    unittest.main()
