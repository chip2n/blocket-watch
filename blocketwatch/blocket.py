#!/usr/bin/python
# coding=UTF8
#
# Copyright 2013 Andreas Arvidsson
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import re
import yaml
from bs4 import BeautifulSoup

app_name = 'BlocketWatch'
verify_url = 'https://www.notifymyandroid.com/publicapi/verify'
notify_url = 'https://www.notifymyandroid.com/publicapi/notify'

status_errors_verify = {
    400: 'The data supplied is in the wrong format, invalid length or null.',
    401: 'The apikey provided is not valid.',
    402: 'Maximum number of API calls per hour exceeded.',
    500: 'Internal server error. Please contact Notify My Android.'
}

status_errors_notify = {
    400: 'The data supplied is in thw wrong format, invalid length or null.',
    401: 'None of the API keys provided were valid',
    402: 'Maximum number of API calls per hour exceeded.',
    500: 'Internal server error. Please contact Notify My Android.'
}

def check_url(url):
    """Checks the provided URL for the latest item id,
       and returns it. If no item_id can be found 
       (due to invalid url or other erros), an exception
       will be raised."""
    # Get the page where the items are listed.
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception('Could not connect to the website.')

    # Find the last item id.
    soup = BeautifulSoup(r.text)
    latest_item = soup.find('div', id=re.compile('^item_\d+'))
    reg = re.compile('item_\d+')
    match = reg.search(str(latest_item))

    # If no match, there are no items to check.
    if match is None:
        raise Exception('Could not find any items.')

    item_id = match.group()
    return item_id


def send_notification(api_key, title, description, url="", priority=2):
    """Sends a notification to alert the user that a new item has been added."""
    # First check if the api key is valid.
    params = {'apikey': api_key}
    r = requests.get(verify_url, params=params)
    if r.status_code != 200:
        raise Exception(status_errors_verify[r.status_code])

    # Send a notification
    params = {
        'apikey': api_key,
        'application': app_name,
        'event': title,
        'description': description,
        'priority': priority,
        'url': url,
    }
    r2 = requests.post(notify_url, data=params)
    if r.status_code != 200:
        raise Exception(status_errors_notify[r.status_code])

