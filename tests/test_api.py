import requests

headers = {
    "Content-Type": "application/json"
}

uri= 'https://henry-prod.hasura.app/v1/graphql'
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

def test_status_200():
    response = requests.post(uri, headers=headers, json=request_data )
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_check_required_json_element():
    response = requests.post(uri, headers=headers, json=request_data )
    to_json = response.json()
    required_element = "data"
    assert required_element in to_json, f"Required element '{required_element}' not found in JSON response"

def test_404_on_get():
    response = requests.get(uri)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_error_message_404():
     response = requests.get(uri)
     required_message = "code"
     json_data = response.json()
     assert required_message in json_data, f"Require message '{required_message}' not found in JSON response"
     assert json_data[required_message] == 'not-found'