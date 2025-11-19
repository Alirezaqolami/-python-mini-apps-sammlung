import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
import time
import random
import json
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

sätze = [
    "Das Wetter ist heute schön.",
    "Ich liebe es, neue Sprachen zu lernen.",
    "Python ist eine großartige Programmiersprache.",
    "Übung macht den Meister.",
    "Die Katze schläft auf dem Sofa."
]

class TippTrainer:
    def __init__(self, root):
        self.root = root
        self.root.title("Tipptrainer 🇩🇪")
        self.root.geometry("800x600")

        self.style = Style("darkly")
        self.dark_mode = True

        self.aktueller_satz = ""
        self.startzeit = None
        self.history_file = "tippverlauf.json"
        self.verlauf = self.lade_verlauf()

        self.frame = tk.Frame(self.root, bg="#2b2b2b")
        self.frame.pack(pady=20, fill="both", expand=True)

        self.label_satz = tk.Label(self.frame, text="Klicke auf 'Start', um zu beginnen", font=("Helvetica", 16), fg="white", bg="#2b2b2b")
        self.label_satz.pack(pady=20)

        self.entry = tk.Entry(self.frame, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.beende_test)

        self.label_ergebnis = tk.Label(self.frame, text="", font=("Helvetica", 14), fg="white", bg="#2b2b2b")
        self.label_ergebnis.pack(pady=10)

        self.button_start = tk.Button(self.frame, text="▶️ Start", command=self.starte_test)
        self.button_start.pack(pady=5)

        self.button_dark = tk.Button(self.frame, text="🌙 Dark/Light", command=self.toggle_dark_mode)
        self.button_dark.pack(pady=5)

        self.button_verlauf = tk.Button(self.frame, text="📈 Verlauf anzeigen", command=self.zeige_verlauf)
        self.button_verlauf.pack(pady=5)

    def starte_test(self):
        self.aktueller_satz = random.choice(sätze)
        self.label_satz.config(text=self.aktueller_satz)
        self.entry.delete(0, tk.END)
        self.label_ergebnis.config(text="")
        self.startzeit = time.time()

    def beende_test(self, event=None):
        ende = time.time()
        eingegeben = self.entry.get()
        dauer = round(ende - self.startzeit, 2)

        wpm = len(eingegeben.split()) / (dauer / 60)
        genauigkeit = self.berechne_genauigkeit(self.aktueller_satz, eingegeben)

        self.label_ergebnis.config(text=f"⏱️ Zeit: {dauer}s | 🧠 Genauigkeit: {genauigkeit}% | ⌨️ WPM: {int(wpm)}")
        self.speichere_verlauf(dauer, genauigkeit, int(wpm))

    def berechne_genauigkeit(self, original, eingegeben):
        korrekt = sum(1 for o, e in zip(original, eingegeben) if o == e)
        return round((korrekt / max(len(original), 1)) * 100)

    def speichere_verlauf(self, dauer, genauigkeit, wpm):
        eintrag = {"zeit": dauer, "genauigkeit": genauigkeit, "wpm": wpm, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
        self.verlauf.append(eintrag)
        with open(self.history_file, "w") as f:
            json.dump(self.verlauf, f)

    def lade_verlauf(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                return json.load(f)
        return []

    def zeige_verlauf(self):
        if not self.verlauf:
            messagebox.showinfo("Info", "Noch kein Verlauf vorhanden.")
            return

        zeiten = [e["zeit"] for e in self.verlauf[-10:]]
        genauigkeiten = [e["genauigkeit"] for e in self.verlauf[-10:]]
        wpms = [e["wpm"] for e in self.verlauf[-10:]]

        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(zeiten, label="Zeit (s)")
        ax.plot(genauigkeiten, label="Genauigkeit (%)")
        ax.plot(wpms, label="WPM")
        ax.set_title("Letzte 10 Trainingseinheiten")
        ax.legend()
        ax.grid(True)

        top = tk.Toplevel(self.root)
        top.title("📊 Verlauf")
        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def toggle_dark_mode(self):
        if self.dark_mode:
            self.style.theme_use("flatly")
            self.frame.config(bg="white")
            self.label_satz.config(bg="white", fg="black")
            self.label_ergebnis.config(bg="white", fg="black")
        else:
            self.style.theme_use("darkly")
            self.frame.config(bg="#2b2b2b")
            self.label_satz.config(bg="#2b2b2b", fg="white")
            self.label_ergebnis.config(bg="#2b2b2b", fg="white")
        self.dark_mode = not self.dark_mode


if __name__ == "__main__":
    root = tk.Tk()
    app = TippTrainer(root)
    root.mainloop()
