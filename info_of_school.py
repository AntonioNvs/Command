from src.error.actions import error_ocured
from src.error.classError import Error
from src.utils.selenium import SeleniumClass

from bs4 import BeautifulSoup
from constants import user, password
from time import sleep
from datetime import datetime

def login_portal(driver: SeleniumClass) -> None or Error:
  try:
    # Se não conseguir acessar o site, lance uma excessão
    error_ocured(driver.access_url('https://www2.fiemg.com.br/rm/WEB/APP/EDU/PORTALEDUCACIONAL/login/'), lambda: Exception())
    
    sleep(3)
    # Login
    driver.get_element_find_by_some_selection('id', 'User').send_keys(str(user))
    driver.get_element_find_by_some_selection('id','Pass').send_keys(str(password))
    driver.get_element_find_by_some_selection('xpath', '/html/body/div[2]/div[3]/form/div[4]/input').click()

    sleep(6)

    driver.try_to_find_element_until_it_appears('id', 'btnConfirmar').click()

  except Exception as e:
    print(e)
    return Error('Could not open the Chrome.')


def get_info_of_absences() -> int or Error:
  try:
    driver = SeleniumClass()

    _return = 0
    try:
      if isinstance(login_portal(driver), Error):
        Exception()

      sleep(2)
      driver.get_element_find_by_some_selection('class_name', 'list-unstyled').find_elements_by_tag_name('li')[2].click()
      driver.get_element_find_by_some_selection('id', 'EDU_PORTAL_ACADEMICO_CENTRALALUNO').click()
      driver.get_element_find_by_some_selection('id', 'EDU_PORTAL_ACADEMICO_CENTRALALUNO_FALTAS').click()

      sleep(2)
      table = driver.try_to_find_element_until_it_appears('tag_name', 'tbody')

      soup = driver.transform_element_in_soup(table)
      
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
    driver.exit_driver()
    return Error('Could not open the Chrome.')

  driver.exit_driver()

  return _return


if __name__ == '__main__':
  get_info_of_absences()