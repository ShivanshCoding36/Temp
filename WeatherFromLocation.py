import requests
def get_location():

    ip_address = requests.get("https://api.ipify.org").text
#    print("IP obtained",ip_address)

    api_key = "3e17fd00bdf342bfb86590d0c889e444"
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"
    response = requests.get(url).json()
    data = response
    print(data)
#    print(url)

    return data

def weather(loc):
    api_key = "b55e90a4e47d360175b25a1a4b578363"
    city_name = loc
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
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
    print(location_data)
    print(f"city is {location_data['city']}")
    
    weather(location_data['city'])
    print("Done")
    