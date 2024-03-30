import requests
import json

# Replace 'YOUR_API_URL' with your actual API URL
api_url = 'http://localhost:5000/products'

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Specify the filename for the JSON file
    json_filename = 'output.json'

    # Save the data to a JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Data successfully saved to {json_filename}')
else:
    print(f'Error: Unable to fetch data from the API. Status code: {response.status_code}')
