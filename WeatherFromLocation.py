import requests
def get_location():
    url = "https://api.ipify.org"
    headers = {
        "User-Agent": "Mozilla/5.0",  # Specify a User-Agent header to identify your request
        "Accept": "application/json"  # Specify the type of response you expect (JSON, in this case)
    }
    response = requests.get(url, headers=headers)
    ip_address = response.text
#    print("IP obtained",ip_address)

    api_key = "IP Geolocation api key"
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"
    response = requests.get(url).json()
    data = response
#    print(url)

    return data

def weather(loc):
    api_key = "open weather maps api key"
    city_name = loc
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        temperature -=  273.15
        temperature = round(temperature,2)
        print(f"Temperature in {city_name} is {temperature} Degree Celsius.")
        print(url)
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    print("Started")
    location_data = get_location()
    print(f"city is {location_data['city']}")
    weather(location_data['city'])
    print("Done")
    
