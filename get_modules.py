import requests


# PLACE YOUR INSTANCE BETWEEN THE QUOTES BELOW
INSTANCE = "YOUR INSTANCE HERE"
# PLACE YOUR TOKEN BETWEEN THE QUOTES BELOW
TOKEN = "YOUR TOKEN HERE"

URL = f"https://{INSTANCE}.beta.instructure.com/api/v1"

headers = {
        "authorization": f"Bearer {TOKEN}"}

# EDIT COURSE ID TO ONE OF YOUR CHOICE
course_id = 101

response = requests.get(url=f"{URL}/courses/{course_id}/modules?per_page=100", headers=headers).json()

print(response)
