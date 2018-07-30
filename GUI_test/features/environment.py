from selenium import webdriver
from datetime import datetime
from os import mkdir, remove
import json
import os

def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")
        return


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return


def before_all(context):

    runtime_filename = 'tmp/data.json'

    if os.path.exists(runtime_filename):
        remove(runtime_filename)
    else:
        os.mkdir('tmp')

    with open(runtime_filename , 'w') as outfile:
        json.dump({}, outfile)

    context.browser = webdriver.Chrome()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()


def after_all(context):
    context.browser.quit()