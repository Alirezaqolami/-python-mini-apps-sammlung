# Python Mini Applications Sammlung 🐍

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Automation](https://img.shields.io/badge/🤖-Automatisierung-green.svg)
![GUI](https://img.shields.io/badge/🖥️-GUI_Apps-orange.svg)


## 📦 PROJEKTÜBERSICHT
Eine umfassende Sammlung von Python-Anwendungen, die verschiedene Aspekte der Softwareentwicklung demonstrieren. Ideal für Bewerbungen als Anwendungsentwickler in Deutschland.

## 🎯 ENTHALTENE PROJEKTE

### 1. 🖋️ TIPPTRAINER
**Datei:** TippTrainer.py
**Beschreibung:** Ein interaktives Tipptraining-Programm zur Verbesserung der Tippgeschwindigkeit und Genauigkeit.

**Funktionen:**
- Zufällige deutsche Sätze zum Abtippen
- Echtzeit-Statistiken (WPM, Genauigkeit, Zeit)
- Dunkel/Hell-Modus Umschaltung
- Verlaufsdiagramme der letzten 10 Versuche
- Automatische Speicherung des Trainingsverlaufs

**Verwendung:**
python TippTrainer.py

### 2. 🌦️ WETTERVORHERSAGE
**Datei:** Wetter.py
**Beschreibung:** Echtzeit-Wettervorhersage für Städte weltweit mit API-Integration.

**Funktionen:**
- Wetterdaten von WeatherAPI
- Temperatur in Celsius
- Wetterbedingungen in Deutsch
- Dunkelmodus-Unterstützung
- Schnellsuche mit Enter-Taste

**API-Konfiguration:**
- API Key erforderlich von weatherapi.com
- Aktueller Key in Code vorhanden

**Verwendung:**
python Wetter.py

### 3. 🎬 FILMEMPFEFEHLER
**Datei:** Movie_Suggester.py
**Beschreibung:** Intelligentes Filmempfehlungssystem basierend auf TMDB-Datenbank.

**Funktionen:**
- Ähnliche Filme finden
- Vollbildmodus (F11)
- Kopieren der Liste in Zwischenablage
- Persische Schriftunterstützung
- Dunkles Design

**API:**
- The Movie Database (TMDB) API
- Aktueller Key integriert

**Verwendung:**
python "Movie_Suggester.py"

### 4. 🖼️ BILDVERARBEITUNG - DREI ANWENDUNGEN

#### A) Stapelbild-Verarbeiter (fold.py)
**Funktion:** Batch-Verarbeitung mehrerer Bilder
- Größenänderung auf 1200x800 Pixel
- Konvertierung zu WEBP-Format
- Automatische Namensbereinigung

#### B) Hintergrund-Entferner (image_G.py)
**Funktion:** Automatische Hintergrundentfernung
- Entfernt Bildhintergrund mit rembg
- Ersetzt durch weißen Hintergrund
- Größenanpassung auf 800x800

#### C) Bildgrößen-Anpassung (Image_800.py)
**Funktion:** Einfache Größenänderung
- Skaliert Bilder auf 800x800
- WEBP-Konvertierung
- Verarbeitet neueste Datei im Ordner

**Verwendung:**
python Stapelbild-Verarbeiter.py
python Hintergrund-Entferner.py
python Bildgroessen-Aenderung.py

## 🛠️ TECHNISCHE VORAUSSETZUNGEN

### Python Version
- Python 3.8 oder höher

### Installation aller Abhängigkeiten:
pip install -r requirements.txt

### Requirements.txt Inhalt:
tkinter==0.1.0
ttkbootstrap==1.10.1
requests==2.31.0
matplotlib==3.7.2
Pillow==10.0.1
rembg==2.0.50
pyperclip==1.8.2
opencv-python==4.8.1.78
numpy==1.24.3

## 📁 PROJEKTSTRUKTUR

python-mini-apps-sammlung/
│
├── 📄 TippTrainer.py
├── 📄 Wetter.py
├── 📄 Movie_Suggester.py
├── 📁 bildverarbeiter/
│   ├── 📄 Stapelbild-Verarbeiter.py
│   ├── 📄 Hintergrund-Entferner.py
│   └── 📄 Bildgroessen-Aenderung.py
├── 📄 requirements.txt
└── 📄 README.md

## 🚀 SCHNELLSTART

1. Repository klonen:
git clone https://github.com/[username]/python-mini-apps-sammlung.git

2. Abhängigkeiten installieren:
pip install -r requirements.txt

3. Gewünschte Anwendung starten:
python TippTrainer.py

## ⚙️ KONFIGURATION

### API Keys:
- WeatherAPI: In Wetter.py integriert
- TMDB: In Movie_Suggester.py integriert

### Pfade anpassen:
In den Bildverarbeitungs-Skripten die Pfade anpassen:
input_folder = "C:/Users/DELL/Desktop/img1"
output_folder = "C:/Users/DELL/Desktop/img2"

## 🎨 BESONDERE FUNKTIONEN

### TippTrainer:
- JSON-basierte Speicherung des Verlaufs
- Matplotlib-Diagramme für Fortschritt
- Responsive GUI mit ttkbootstrap

### Wettervorhersage:
- Echtzeit-Datenabfrage
- Deutsche Lokalisierung
- Elegante Fehlerbehandlung

### Filmempfehler:
- Vollbild-Unterstützung
- Zwischenablage-Integration
- Persische Schriftkompatibilität

### Bildverarbeitung:
- Batch-Verarbeitung
- Automatische Formatkonvertierung
- Hintergrundentfernung mit KI
