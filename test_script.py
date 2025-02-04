import requests

# Define the Flask API URL
FLASK_API_URL = "http://localhost:5005/predict"

# Define a test file path (update with a valid file path on your system)
test_audio_file_path = "C:\\Users\\HP\\Downloads\\trap-beat-loop-ken-carson-drums_152bpm.wav"

# Create the test data payload
test_payload = {
    "filePath": test_audio_file_path
}

try:
    # Send a POST request to the Flask API
    response = requests.post(FLASK_API_URL, json=test_payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("API Response:", response.json())
    else:
        print(f"API Error (Status Code: {response.status_code}):", response.json())

except requests.exceptions.RequestException as e:
    print("Error connecting to the Flask API:", str(e))
