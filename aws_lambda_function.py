import json
import os
import urllib.request

def lambda_handler(event, context):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    city = event.get('city', 'Delhi')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            processed_data = {
                "cloud_provider": "AWS Lambda",
                "source": "OpenWeatherMap API",
                "location": data.get("name"),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"]
            }
            return {
                "statusCode": 200,
                "body": json.dumps(processed_data)
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }