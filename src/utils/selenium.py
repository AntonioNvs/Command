from src.error.classError import Error
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from bs4 import BeautifulSoup

class SeleniumClass:
  def __init__(self) -> None:
    self.chromedriver_path = "files/chromedriver.exe"

    self.__driver = webdriver.Chrome(executable_path=self.chromedriver_path)

  def access_url(self, url) -> None or Error:
    try:
      self.__driver.get(url)
    except:
      return Error('Does not possible access the URL')

  def transform_element_in_soup(self, element: WebElement):
    element_html = element.get_attribute("outerHTML") 
    return BeautifulSoup(element_html, 'html.parser')

  def get_element_find_by_some_selection(self, at_what: str, string_selection: str, element: WebElement = "") -> WebElement or Error:
    if element == "": element = self.__driver
    
    try:
      if at_what == "css_selector":
        return element.find_element_by_css_selector(string_selection)
      elif at_what == "xpath":
        return element.find_element_by_xpath(string_selection)
      elif at_what == "name":
        return element.find_element_by_name(string_selection)
      elif at_what == "id":
        return element.find_element_by_id(string_selection)
      elif at_what == "tag_name":
        return element.find_element_by_tag_name(string_selection)
      elif at_what == "classes_name":
        return element.find_elements_by_class_name(string_selection)
      elif at_what == "class_name":
        return element.find_elements_by_class_name(string_selection)
      else:
        return Exception("Selector invalid")
    except:
      return Error("Not found element")

  def try_to_find_element_until_it_appears(self, at_what: str, string_selection: str) -> WebElement:
    while True:
      element = self.get_element_find_by_some_selection(at_what, string_selection)

      if isinstance(element, WebElement):
        return element


  def exit_driver(self):
    self.__driver.quit()
