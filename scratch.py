from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json

#driver = webdriver.Chrome('./chromedriver')
#driver.get("https://www.python.org")
#print(driver.title)
#search_bar = driver.find_element_by_name("q")
#search_bar.clear()
#search_bar.send_keys("getting started with python")
#search_bar.send_keys(Keys.RETURN)
#print(driver.current_url)
#driver.close()
headers = {
    "Content-Type": "application/json"
}

uri= 'https://henry-prod.hasura.app/v1/graphql'
body = '{"operationName":"cappedAvailableTimes","variables":{"minimumDate":"2023-09-24T02:44:58.549Z","maximumDate":"2023-10-05T02:44:58.549Z","state":"utah","treatmentShortId":"weightloss"},"query":"query cappedAvailableTimes($state: String!, $treatmentShortId: String!, $minimumDate: timestamptz!, $maximumDate: timestamptz!) {\n  cappedAvailableTimes: appointment_capped_available_appointment_slots(\n    where: {start_time: {_gt: $minimumDate, _lt: $maximumDate}, state: {_eq: $state}, treatment_object: {short_id: {_eq: $treatmentShortId}}, language: {_eq: \"en-US\"}, provider: {_and: {id: {_is_null: false}}}}\n    order_by: {start_time: asc}\n  ) {\n    ...CappedAvailableSlotsFragment\n    __typename\n  }\n}\n\nfragment CappedAvailableSlotsFragment on appointment_capped_available_appointment_slots {\n  startTime: start_time\n  endTime: end_time\n  provider {\n    id\n    displayName: display_name\n    __typename\n  }\n  __typename\n}"}'
body2 = """
{
  "operationName": "cappedAvailableTimes",
  "variables": {
    "minimumDate": "2023-09-24T02:44:58.549Z",
    "maximumDate": "2023-10-05T02:44:58.549Z",
    "state": "utah",
    "treatmentShortId": "weightloss"
  },
  "query": "query cappedAvailableTimes($state: String!, $treatmentShortId: String!, $minimumDate: timestamptz!, $maximumDate: timestamptz!) {\n  cappedAvailableTimes: appointment_capped_available_appointment_slots(\n    where: {start_time: {_gt: $minimumDate, _lt: $maximumDate}, state: {_eq: $state}, treatment_object: {short_id: {_eq: $treatmentShortId}}, language: {_eq: \"en-US\"}, provider: {_and: {id: {_is_null: false}}}}\n    order_by: {start_time: asc}\n  ) {\n    ...CappedAvailableSlotsFragment\n    __typename\n  }\n}\n\nfragment CappedAvailableSlotsFragment on appointment_capped_available_appointment_slots {\n  startTime: start_time\n  endTime: end_time\n  provider {\n    id\n    displayName: display_name\n    __typename\n  }\n  __typename\n}"
}
"""

query = """
query cappedAvailableTimes($state: String!, $treatmentShortId: String!, $minimumDate: timestamptz!, $maximumDate: timestamptz!) {
  cappedAvailableTimes: appointment_capped_available_appointment_slots(
    where: {
      start_time: {_gt: $minimumDate, _lt: $maximumDate},
      state: {_eq: $state},
      treatment_object: {short_id: {_eq: $treatmentShortId}},
      language: {_eq: "en-US"},
      provider: {_and: {id: {_is_null: false}}}
    }
    order_by: {start_time: asc}
  ) {
    ...CappedAvailableSlotsFragment
    __typename
  }
}

fragment CappedAvailableSlotsFragment on appointment_capped_available_appointment_slots {
  startTime: start_time
  endTime: end_time
  provider {
    id
    displayName: display_name
    __typename
  }
  __typename
}

"""
request_data = {
    "query": query,
    "variables": {
        "state": "utah",
        "treatmentShortId": "weightloss",
        "minimumDate": "2023-09-24T02:44:58.549Z",
        "maximumDate": "2023-10-05T02:44:58.549Z"
    }
}


#json_body=json.loads(body)

#response = requests.get('https://henry-prod.hasura.app/v1/graphql')
response = requests.post(uri, headers=headers, json=request_data )
to_json = response.json()
print(response)
print(to_json)