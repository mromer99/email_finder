# Python Email Scraper
# English Below
## German
Dieses Repository enthält ein Python-Skript (emails.py) zum Extrahieren von E-Mails aus einer Liste von Websites.

## Voraussetzungen

Bevor Sie `emails.py` ausführen können, müssen Sie Python und einige Python-Bibliotheken auf Ihrem Computer installiert haben. Wenn Sie Python noch nicht installiert haben, laden Sie es von der [offiziellen Python-Website](https://www.python.org/downloads/) herunter.

Hier sind die Python-Bibliotheken, die Sie benötigen:

- pandas
- requests
- beautifulsoup4
- urllib3
- openpyxl
- lxml

Sie können diese Bibliotheken mit pip installieren:

```bash
pip install pandas
pip install requests
pip install beautifulsoup4
pip install urllib3
pip install openpyxl
pip install lxml
```

Schließlich benötigen Sie eine Excel-Datei namens 'gruenderwettberbe.xlsx' im selben Verzeichnis wie `emails.py`. Diese Datei sollte die Websites enthalten, die Sie durchsuchen möchten.

## Ausführung des Skripts

1. Öffnen Sie eine Eingabeaufforderung. Sie können dies tun, indem Sie `Windows-Taste + R` drücken, `cmd` in das Ausführen-Fenster eingeben und `Enter` drücken.

2. Navigieren Sie mit dem `cd`-Befehl zum Verzeichnis, das `emails.py` enthält:

    ```bash
    cd pfad_zu_deinem_skript
    ```
3. Führen Sie `emails.py` aus:

    ```bash
    python emails.py
    ```

Das Skript wird die Websites in 'gruenderwettberbe.xlsx' durchsuchen und eine neue Excel-Datei, 'gruenderwettberbe_email.xlsx', im selben Verzeichnis erstellen. Diese neue Datei enthält die gescrapten E-Mails.

## Anpassung
Wenn Sie eine andere Excel-Datei verwenden möchten, müssen Sie die folgende Zeile in `emails.py` ändern:

```python
df = pd.read_excel('gruenderwettberbe.xlsx', engine='openpyxl')
```
Ändern Sie 'gruenderwettberbe.xlsx' in den Namen Ihrer Excel-Datei. Zum Beispiel, wenn Ihre Datei 'my_websites.xlsx' heißt, sollte die Zeile lauten:

```python
df = pd.read_excel('my_websites.xlsx', engine='openpyxl')
```

Um die Ausgabedatei zu ändern:

```python
df.to_excel('gruenderwettberbe_email.xlsx', index=False, engine='openpyxl')
```

Ändern Sie 'gruenderwettberbe_email.xlsx' in den Namen Ihrer gewünschten Ausgabedatei. Zum Beispiel, wenn Sie möchten, dass die Ausgabedatei 'my_emails.xlsx' heißt, sollte die Zeile lauten:
```python
df.to_excel('my_emails.xlsx', index=False, engine='openpyxl')
```

## Fehlerbehebung

- Wenn Python `emails.py` nicht finden kann, stellen Sie sicher, dass Ihre Eingabeaufforderung im richtigen Verzeichnis ist und dass `emails.py` in diesem Verzeichnis liegt.
- Wenn Sie auf einen `ImportError` stoßen, stellen Sie sicher, dass Sie alle notwendigen Python-Bibliotheken installiert haben. Sie können überprüfen, welche Bibliotheken mit `pip list` installiert sind.
- Wenn Python das Modul 'openpyxl' nicht finden kann, versuchen Sie es mit `pip install openpyxl` zu installieren.

Bitte behandeln Sie die gesammelten Daten verantwortungsbewusst. Befolgen Sie alle geltenden Gesetze und Vorschriften und respektieren Sie die Privatsphäre der Einzelpersonen.

Ersetzen Sie einfach `pfad_zu_deinem_skript` im Abschnitt "Ausführung des Skripts" durch den tatsächlichen Pfad zu `emails.py` auf Ihrem Computer.

<br/><br/> 

# English
###
This repository contains a Python script (`emails.py`) for extracting emails from a list of websites.

## Prerequisites

Before you can run `emails.py`, you'll need to have Python and a few Python libraries installed on your computer. If you don't have Python installed yet, download it from [Python's official site](https://www.python.org/downloads/).

Here are the Python libraries you'll need:

- pandas
- requests
- beautifulsoup4
- urllib3
- openpyxl
- lxml

You can install these libraries with pip:

```bash
pip install pandas
pip install requests
pip install beautifulsoup4
pip install urllib3
pip install openpyxl
pip install lxml
```


Lastly, you'll need an Excel file named 'gruenderwettberbe.xlsx' in the same directory as `emails.py`. This file should contain the websites you want to scrape.

## Running the Script

1. Open a Command Prompt. You can do this by pressing `Windows Key + R`, typing `cmd` in the Run window, and pressing `Enter`.

2. Navigate to the directory containing `emails.py` using the `cd` command:

```bash
cd path_to_your_script
```
3. Run `emails.py`:

    ```bash
    python emails.py
    ```

    The script will scrape the websites in 'gruenderwettberbe.xlsx' and create a new Excel file, 'gruenderwettberbe_email.xlsx', in the same directory. This new file will contain the scraped emails.

## Customization
If you want to use another Excel file, you'll need to modify the following line in `emails.py`:

```python
df = pd.read_excel('gruenderwettberbe.xlsx', engine='openpyxl')
```
Change 'gruenderwettberbe.xlsx' to the name of your Excel file. For example, if your file is named 'my_websites.xlsx', the line should be:

To change the output file:

```python
df.to_excel('gruenderwettberbe_email.xlsx', index=False, engine='openpyxl')
```

## Troubleshooting

- If Python can't find `emails.py`, make sure your command prompt is in the correct directory and that `emails.py` is in that directory.
- If you encounter an `ImportError`, make sure you've installed all the necessary Python libraries. You can check which libraries are installed with `pip list`.
- If Python can't find the 'openpyxl' module, try installing it with `pip install openpyxl`.

Please handle the data you collect responsibly. Comply with all applicable laws and regulations and respect individuals' privacy.

Just remember to replace `path_to_your_script` in the "Running the Script" section with the actual path to `emails.py` on your computer.


