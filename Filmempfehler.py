import requests
import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label, Frame
import tkinter.messagebox as msgbox
import pyperclip


API_KEY = "0df835a863cca9a11667106c5f9bf8f1"

def get_movie_id(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        return data['results'][0]['id']
    return None

def get_similar_movies(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return [movie['title'] for movie in data['results']]

def search_movies(event=None):
    movie_name = movie_entry.get()
    if not movie_name.strip():
        msgbox.showwarning("error!", "Bitte geben Sie den Namen des Films ein.")
        return

    movie_id = get_movie_id(movie_name)
    result_listbox.delete(0, tk.END)

    if movie_id:
        similar_movies = get_similar_movies(movie_id)
        if similar_movies:
            for title in similar_movies:
                result_listbox.insert(tk.END, title)
        else:
            result_listbox.insert(tk.END, "Keine ähnlichen Films gefunden.")
    else:
        result_listbox.insert(tk.END, "Es wurde kein Film mit diesem Namen gefunden.")

def copy_to_clipboard():
    movies = result_listbox.get(0, tk.END)
    if movies:
        text = "\n".join(movies)
        pyperclip.copy(text)
        msgbox.showinfo("Kopiert", "Die Filmliste wurde kopiert.")
    else:
        msgbox.showwarning("error", "هEs gibt keinen Film zum Kopieren.")

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

def quit_fullscreen(event=None):
    root.attributes("-fullscreen", False)
    root.geometry("800x600")  # یا هر اندازه دلخواه دیگر

# ---------- رابط گرافیکی ----------
root = tk.Tk()
root.title("Ähnliche Filme 🎬")

fullscreen = True
root.attributes("-fullscreen", fullscreen)

root.bind("<F11>", toggle_fullscreen)  # برای رفتن به حالت تمام صفحه
root.bind("<Escape>", quit_fullscreen)  # برای خروج از حالت تمام صفحه

style = Style("darkly")

font_main = ("Vazirmatn", 12)

frame = Frame(root)
frame.pack(pady=20)

movie_label = Label(frame, text="Filmname:", font=font_main)
movie_label.grid(row=0, column=0, padx=5)

movie_entry = Entry(frame, font=font_main, width=40)
movie_entry.grid(row=0, column=1, padx=5)
movie_entry.bind("<Return>", search_movies)

search_button = Button(frame, text="Suchen", bootstyle="success", command=search_movies)
search_button.grid(row=0, column=2, padx=5)

# دکمه کپی بالای لیست فیلم‌ها قرار داده می‌شود
copy_button = Button(root, text="📋 In die Zwischenablage kopieren", bootstyle="info", command=copy_to_clipboard)
copy_button.pack(pady=10, anchor="center")

result_listbox = tk.Listbox(root, font=font_main, height=25, width=100)
result_listbox.pack(pady=20)

root.mainloop()
