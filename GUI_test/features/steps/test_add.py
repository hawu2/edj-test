from behave import *

from GUI_test.features.lib.utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import platform


@given("I open eventlist test page")
def step_impl(context):
    context.browser.get("http://localhost:8080/eventlist/")


@then("The page open")
def step_impl(context):
    assert "Edjuster Assignment" == context.browser.title

@given("I am already on the landing page")
def step_impl(context):
    assert "Edjuster Assignment" == context.browser.title

@when("Click on Events link")
def step_impl(context):
    elem = context.browser.find_element_by_link_text("Events")
    print(elem)
    elem.click()

@then("I can see Events Manager Page in the page")
def step_impl(context):
    pagename = context.browser.find_elements_by_xpath("//*[contains(text(), 'Events Manager Page')]")
    assert pagename


@when("Click on Add button to open Event Summary Dialog")
def step_impl(context):
    addbutton = context.browser.find_element(By.XPATH, '//button[text()="Add"]')
    assert addbutton
    addbutton.click()
    mdl_dialog = context.browser.find_element_by_id('dialog')
    assert mdl_dialog.text, "Event summary page not open"


@then("Input event data and save")
def step_impl(context):

    event_data = gen_event_data()
    write_to_data_json(event_data)

    for k, v in event_data.items():
        event = context.browser.find_element_by_id(k)
        assert event
        event.click()
        event.send_keys(v)

    btnSave = context.browser.find_element_by_id("btnSave")
    btnSave.click()

    mdl_dialog = context.browser.find_element_by_id('dialog')
    assert not mdl_dialog.text, "Event summary page didn't close."


@then("Verify from GUI")
def step_impl(context):

    #  verify data matches stored data
    # blar blar..
    pass
