from customtkinter import *
import requests

set_appearance_mode("System")
set_default_color_theme("blue")

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        city_name = data["name"]
        return f"{int(temp)}°C" # \n{description}
    else:
        return "Ошибка: не удалось получить данные. Проверь город."

class WeatherApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Погода")
        self.geometry("245x270")

        self.api_key = "59df953d220b16caf0f959e8be0a28cc" 

        self.label = CTkLabel(self, text="Узнать погоду", font=("Arial", 16))
        self.label.pack(pady=10)

        self.entry = CTkEntry(self, placeholder_text="Город")
        self.entry.pack(pady=10)

        self.button = CTkButton(self, text="Показать погоду", command=self.show_weather)
        self.button.pack(pady=10)

        self.result = CTkTextbox(self, width=120, height=100, font=('Dubai Medium', 50))
        self.result.pack(pady=10)
        self.result.configure(state="disabled")

    def show_weather(self):
        city = self.entry.get()
        if not city:
            return

        weather_text = get_weather(city, self.api_key)
        self.result.configure(state="normal")
        self.result.delete("1.0", "end")
        self.result.insert("1.0", weather_text)
        self.result.configure(state="disabled")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
