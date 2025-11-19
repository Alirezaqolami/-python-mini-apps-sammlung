import requests
import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label, Frame
import tkinter.messagebox as msgbox

API_KEY = "0bd74eea5c854a72bc6114158252104"

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&lang=de"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Fehler bei der Anfrage: {response.status_code}")
        return None

    try:
        data = response.json()
        return data
    except requests.exceptions.JSONDecodeError:
        print("Fehler beim Decodieren der JSON-Daten")
        return None

def search_weather(event=None):
    city_name = city_entry.get()
    if not city_name.strip():
        msgbox.showwarning("Fehler", "Bitte geben Sie einen Städtenamen ein.")
        return

    weather_data = get_weather(city_name)

    if weather_data:
        if "current" in weather_data:
            temp_celsius = weather_data["current"]["temp_c"]
            condition = weather_data["current"]["condition"]["text"]
            temp_label.config(text=f"Temperatur: {temp_celsius}°C")
            condition_label.config(text=f"Bedingung: {condition}")
        else:
            msgbox.showwarning("Fehler", "Keine Wetterdaten gefunden für diese Stadt!")
    else:
        msgbox.showwarning("Fehler", "Es gab ein Problem bei der Anfrage.")

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        style.configure('TButton', background='#333', foreground='#fff')
        style.configure('TLabel', background='#333', foreground='#fff')
        root.configure(background='#333')
    else:
        style.configure('TButton', background='#f0f0f0', foreground='#000')
        style.configure('TLabel', background='#f0f0f0', foreground='#000')
        root.configure(background='#f0f0f0')

root = tk.Tk()
root.title("Wettervorhersage 🌤️")
root.geometry("800x600")

style = Style("darkly")

dark_mode = False

frame = Frame(root)
frame.pack(pady=20)

city_label = Label(frame, text="🌍 Stadtname:", font=("Arial", 12))
city_label.grid(row=0, column=0, padx=5)

city_entry = Entry(frame, font=("Arial", 12), width=40)
city_entry.grid(row=0, column=1, padx=5)
city_entry.bind("<Return>", search_weather)

search_button = Button(frame, text="🔍 Suchen", bootstyle="success", command=search_weather)
search_button.grid(row=0, column=2, padx=5)

temp_label = Label(root, font=("Arial", 12))
temp_label.pack(pady=10)

condition_label = Label(root, font=("Arial", 12))
condition_label.pack(pady=10)

dark_mode_button = Button(root, text="🌙 Dark Mode", bootstyle="info", command=toggle_dark_mode)
dark_mode_button.pack(pady=10)

root.mainloop()
