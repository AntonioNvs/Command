from src.error.classError import Error
from selenium import webdriver
from bs4 import BeautifulSoup
from constants import user, password
from time import sleep
from datetime import datetime


def get_info_of_absences() -> int or Error:
  try:
    driver = webdriver.Chrome(executable_path=f"files/chromedriver.exe")
    
    driver.get('https://www2.fiemg.com.br/rm/WEB/APP/EDU/PORTALEDUCACIONAL/login/')
    
    _return = 0
    try:
      # Login
      sleep(3)
      driver.find_element_by_id('User').send_keys(str(user))
      driver.find_element_by_id('Pass').send_keys(str(password))
      driver.find_elements_by_class_name('form__field')[6].find_element_by_tag_name('input').click()
      
      # Acessar parte de faltas
      sleep(6)
      driver.find_element_by_id('btnConfirmar').click()

      sleep(3)
      driver.find_element_by_class_name('list-unstyled').find_elements_by_tag_name('li')[2].click()
      driver.find_element_by_id('EDU_PORTAL_ACADEMICO_CENTRALALUNO').click()
      driver.find_element_by_id('EDU_PORTAL_ACADEMICO_CENTRALALUNO_FALTAS').click()

      sleep(2)
      table = driver.find_element_by_tag_name('tbody')
      table_html = table.get_attribute("outerHTML")
      soup = BeautifulSoup(table_html, 'html.parser')
      
      init = datetime(2021, 2, 1, 0, 0, 0)
      diff = 6*4.3*(datetime.utcnow() - init).days / 7

      faults = 0
      for tr in soup.findAll('tr'):
        allTd = tr.findAllNext('td')[3:5]
        faults += sum([int(i.text) for i in allTd if i.text != ''])

      _return = round(faults*100/diff, 3)
    except:
      driver.quit()
      return Error('Could not get frequency.')
  except:
    driver.quit()
    return Error('Could not open the Chrome.')

  driver.quit()

  return _return


if __name__ == '__main__':
  get_info_of_absences()