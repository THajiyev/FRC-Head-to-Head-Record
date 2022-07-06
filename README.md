# FRC Head-to-Head Record 

This website will allow you to view the head-to-head record of 2 FRC teams based on the data available on The Blue Alliance. 


# How to use

First, you will need to go to keys.yaml and add an authentication key(X-TBA-Auth-Key). It will be used to pull data from The Blue Alliance. Run the code from your terminal by typing in "python main.py"

## Dependencies
You will need the following dependencies to run the website

Requests
```
pip install requests
```
PyYAML
```
pip install PyYAML
```
Matplotlib
```
pip install matplotlib
```
Flask
```
pip install Flask
```
Pillow
```
pip install Pillow
```

Python standard libraries used"
- concurrent.futures
- datetime
- functools
- base64
- io


## How does it work
Once the user inputs 2 FRC teams, the backend code will iterate through all matches available for one of the teams since both teams existed. It will check for matches where the two teams played on opposite alliances. All this data will be collected and displayed. The user will see the pie chart showing what percent of matches each team has won and can look at scores from each match. 

## Input Teams
<a href="https://drive.google.com/uc?export=view&id=<FILEID>"><img src="https://drive.google.com/uc?export=view&id=1hcSJw_dicGwlK-qTbPse1tIbBIx2nssy" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture"/>

## View Record
<a href="https://drive.google.com/uc?export=view&id=<FILEID>"><img src="https://drive.google.com/uc?export=view&id=1gmRDvPIb7ppb4Bd6T0OQnI0FduE5vXlB" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture"/>

## Finally
Enjoy using this website and let me know if you have any questions, comments, or concerns.