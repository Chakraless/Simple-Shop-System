from tkinter import *
import requests

# Weather API, made with Python

# Works with any City

# National
# Global


# Works with Countries also


# Thank you
window = Tk()
window.geometry('500x500')
window.title('Weather API')

def get_weather_data(city):
    api_key = '7e001aa0e9f9aea1693ba37ef382f4d4'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    return response.json()
    # Process the response and return the weather data
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


kelvin_temperature = 300  # Example Kelvin temperature
fahrenheit_temperature = kelvin_to_fahrenheit(kelvin_temperature)
print(fahrenheit_temperature)

def get_entry():
    city = weather_Entry.get()
    weather_data = get_weather_data(city)
    temperature = kelvin_to_fahrenheit(weather_data['main']['temp'])
    description = weather_data['weather'][0]['description']
    weather_label.config(text=f'Weather of City: {city}\nTemperature: {round(temperature)} °F\nDescription: {description}')


Entry_label = Label(window, text='Input city name', font=('Arial 25'))
Entry_label.pack()
frame = Frame()
frame.pack()
weather_label = Label(window, text='Weather of City: ', font=('Arial 25'))
weather_label.pack()
weather_Entry = Entry(frame, font=('Arial 20'))
weather_Entry.grid(row=0, column=0)
submit = Button(frame, text='submit', font=('Arial 15'), command=get_entry)
submit.grid(row=0, column=1, rowspan=2)  # Set rowspan to 2

if __name__ == "__main__":
    window.mainloop()