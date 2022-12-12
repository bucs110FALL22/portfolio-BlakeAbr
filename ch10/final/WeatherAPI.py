import requests


class WeatherAPIs:
  
  def __init__(self,api_key = "1f5e0b85596839529fdb797024b0d8ec"):
    self.user_input = input("Enter the name of a city: ")
    self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.user_input}&units=imperial&APPID={api_key}"
    
    print(self.user_input)
  def get(self): 
    
      weatherData = requests.get(self.url)
      if weatherData.json()['cod'] == "404":
        print("https://http.dog/404.jpg")
      else:
        weather = weatherData.json()['weather'][0]['main']
        temp = weatherData.json()['main']['temp']
        humidity = weatherData.json()['main']['humidity']
        wind = weatherData.json()['wind']['speed']
        country = weatherData.json()['sys']['country']
        print("https://http.dog/200.jpg")


      print(f"The skies in {self.user_input} have/are: {weather}")
      print(f"The temperature in {self.user_input} is: {temp}°F")
      print(f"The humidity in {self.user_input} is: {humidity}%")
      print(f"The wind speed in {self.user_input} is: {wind} miles per hour")
      print(f"The country that  {self.user_input} is in: {country}")



wa = WeatherAPIs()
wa.get()

  



