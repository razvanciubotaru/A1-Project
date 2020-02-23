from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

CSS_Language = 'EN'
ID_Cookie = 'onetrust-accept-btn-handler'
CSS_Solutions = 'Solutions'
CSS_Virtual_Infrastructure='Virtual infrastructure'
CSS_Exoscale = '[href="/en-de/solutions/infrastructure/virtual-infrastructure/exoscale-european-cloud-infrastructure/"]'

@when('we go to initial page')
def step_impl(context):
   context.driver.get('https://www.a1.digital')
   time.sleep(5)
   context.driver.find_element_by_id(ID_Cookie).click()

@then('it should have title "{title}"')
def step_impl(context,title):
   assert title in context.driver.title

@when('we select english language')
def step_impl(context):
   context.driver.find_element_by_link_text(CSS_Language).click()

@when('we go to solutions page')
def step_impl(context):
   context.driver.find_element_by_link_text(CSS_Solutions).click()

@when('we go to virtual infrastructure page')
def step_impl(context):
   context.driver.find_element_by_link_text(CSS_Virtual_Infrastructure).click()

@when('we go to exoscale page')
def step_impl(context):
   context.driver.find_element_by_css_selector(CSS_Exoscale).click()


