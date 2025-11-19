
# Film Similarity Finder 🎬

Dieses Python-Programm hilft dabei, ähnliche Filme basierend auf einem eingegebenen Filmtitel zu finden. Es verwendet das "The Movie Database (TMDb)" API, um Filminformationen zu durchsuchen und ähnliche Filme anzuzeigen.

## Funktionen

- **Filme suchen**: Geben Sie den Namen eines Films ein und das Programm zeigt ähnliche Filme an.
- **Kopieren der Ergebnisse**: Sie können die Liste der ähnlichen Filme in die Zwischenablage kopieren, um sie später zu verwenden.
- **Vollbildmodus**: Das Programm unterstützt den Wechsel in den Vollbildmodus (drücken Sie F11, um in den Vollbildmodus zu wechseln, und Esc, um zurückzukehren).

## Installation

1. Klonen Sie dieses Repository oder laden Sie die Datei herunter.
2. Installieren Sie die notwendigen Python-Bibliotheken:
    ```bash
    pip install requests ttkbootstrap pyperclip
    ```

3. Erstellen Sie ein Konto auf [The Movie Database](https://www.themoviedb.org/) und erhalten Sie Ihren API-Schlüssel.

4. Ersetzen Sie den `API_KEY` in der `api_key`-Variable mit Ihrem eigenen Schlüssel.

## Benutzung

1. Starten Sie das Programm.
2. Geben Sie den Namen eines Films in das Textfeld ein und klicken Sie auf "Suchen" oder drücken Sie die Eingabetaste.
3. Das Programm zeigt eine Liste ähnlicher Filme an.
4. Klicken Sie auf "📋 Kopyieren", um die Liste der ähnlichen Filme in die Zwischenablage zu kopieren.

## Quellcode

Der Quellcode verwendet folgende Bibliotheken:

- `requests`: Zum Abrufen von Filmdaten von der TMDb API.
- `tkinter`: Für die Erstellung der grafischen Benutzeroberfläche.
- `pyperclip`: Um die Ergebnisse in die Zwischenablage zu kopieren.
- `ttkbootstrap`: Für das Styling der GUI.

## Screenshots

![Screenshot](https://via.placeholder.com/600x400?text=Screenshot+coming+soon)

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.
