# Python Email Scraper
### English Below

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


