import requests
import random
import json
import string

# this is our main url:
main_url = "https://gorest.co.in"

# Auth token
auth_token = "Bearer 5244e92948724000e156c914d53e57f5da7cc796a6e63c6820c"

#Random Email
def random_email():
    domain = "ebal.com"
    email_lenthg = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range (email_lenthg))
    email = random_string + "@" + domain
    return email



# GET Request #
def get_request():
    url = main_url + "/public/v2/users"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("JSON GET Response Body:", json_str)
    print("**********************************")


# POST Request #
def post_request():
    url = main_url + "/public/v2/users"
    print("POST url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Nahuy Tebya",
        "email": random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("JSON POST response body: ", json_str)
    user_id = json_data["id"]

    # Validate the response code is 201
    assert response.status_code == 201

    # Validate "name" is in the response JSON and has the expected value
    assert "name" in json_data
    assert json_data["name"] == "Nahuy Tebya"

    # Return the user_id
    return user_id
    print("**********************************")

#PUT Request
def put_request(user_id):
    url = main_url + f"/public/v2/users/{user_id}"  # Added forward slash before {user_id}
    print("put url: " + url)  # Corrected the print statement to say "put url" instead of "post url"
    headers = {"Authorization": auth_token}
    data = {
        "name": "Ti Dolbayeb",
        "email": random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)  # Use requests.put for the PUT request

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("JSON PUT response body: ", json_str)
    assert response.status_code == 200
    assert json_data["id"] == user_id
    assert json_data["name"] == "Ti Dolbayeb"
    print("**********************************")


#DELETE Request
def delete_request(user_id):
    url = main_url + f"/public/v2/users/{user_id}"  # Added forward slash before {user_id}
    print("DELETE url: " + url)  # Corrected the print statement to say "put url" instead of "post url"
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("Deleting a user")
    print("**********************************")

get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
