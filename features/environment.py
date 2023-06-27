import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from Payload import *
from Utils import Logging


from pageObjects.BasePage import BasePage
from pageObjects.CheckWrappersPage import *


# def after_scenario(context, scenario):
#     if "library" in scenario.tags:
#         delete_data = {
#             "ID": context.Book_id
#         }
#
#         DelBook_response = requests.post(context.DelBook_Url, json=delete_data, headers=addbook_requestHeaders())
#         del_response_json = DelBook_response.json()
#         print(del_response_json)
#         assert del_response_json['msg'] == 'book is successfully deleted'
#         assert DelBook_response.status_code == 200

def before_scenario(context, scenario):
    if "GUI" in scenario.tags:
        print("I am executing before any  scenario")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        context.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", options=options)
        context.driver.maximize_window()

        environment = getConfig()["GUI"]["Environment"]
        print("Running in", environment, "  Environment ")
        Logging.getLogger().info("Executing in "+environment+" Environment")

        Url = getConfig()["GUI"][environment]
        context.driver.get(Url)


def after_scenario(context, scenario):
    if "GUI" in scenario.tags:
        context.driver.quit()
        Logging.getLogger().info("Browser Closed")
