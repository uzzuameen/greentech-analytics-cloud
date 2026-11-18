import json
import urllib.request
import ssl

def test_openweathermap():
    api_key = "180d923381fb11dc3c7cfa54c45a8b1f"  
    city = "Delhi"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # SSL context bypass for local testing
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        with urllib.request.urlopen(url, context=ctx) as response:
            data = json.loads(response.read().decode())
            print("--- OpenWeatherMap API Test Successful ---")
            print(f"City: {data.get('name')}")
            print(f"Temperature: {data['main']['temp']} °C")
            print(f"Condition: {data['weather'][0]['description']}")
    except Exception as e:
        print("OpenWeatherMap Error:", str(e))

def test_kaggle_data():
    print("\n--- Kaggle Climate Dataset Simulation ---")
    sample_climate_record = {
        "Source": "Kaggle Global Climate Change Dataset",
        "Year": 2023,
        "Average_Temp_C": 15.2,
        "CO2_Concentration_ppm": 421.5
    }
    print(json.dumps(sample_climate_record, indent=4))

if __name__ == "__main__":
    test_openweathermap()
    test_kaggle_data()