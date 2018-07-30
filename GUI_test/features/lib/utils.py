from datetime import datetime
import json, os
import platform
from selenium.webdriver.common.keys import Keys

def gen_event_data():
    """
    This function will generate a static test data for testing add events
    :return: data in json
    """
    event_data = {}
    tday = datetime.now()
    event_data["dialog-event-date"] = tday.strftime("%Y-%m-%d")
    event_data["dialog-event-type"] = "bbq"
    event_data["dialog-event-summary"] = "This is a test bbq"
    event_data["dialog-event-metric"] = "100"
    event_data[
        "modal-content"] = """Return the time zone name corresponding to the datetime object dt, 
        as a string. Nothing about string names is defined by the datetime module, 
        and there’s no requirement that it mean anything in particular. For example, 
        “GMT”, “UTC”, “-500”, “-5:00”, “EDT”, “US/Eastern”, “America/New York” are all valid replies. 
        Return None if a string name isn’t known. Note that this is a method rather than a fixed 
        string primarily because some tzinfo subclasses will wish to return different names depending 
        on the specific value of dt passed, especially if the tzinfo class is accounting for daylight time"""

    return event_data


def write_to_data_json(data):
    """
    Store data to runtime data file tmp/data.json
    :param data:  data needs to be a dict
    :return:
    """

    if type(data) is not dict:
        assert TypeError, "This is not a dict {0}".format(data)

    rt_data = get_data_json()
    rt_data.update(data)

    with open('tmp/data.json' , 'w') as outfile:
        json.dump(rt_data, outfile)


def get_data_json():
    """
    reading stored data from tmp/data.json file
    :return:
    """
    with open('tmp/data.json') as outfile:
        rt_data=json.load(outfile)

    return rt_data


def get_select_all():

    if platform.system() == "Darwin":
        rtn = Keys.COMMAND + "a"
    else:
        rtn = Keys.CONTROL + "a"

    return rtn


