# FRC Head-to-Head Record

This website will allow you to view the head-to-head record of 2 FRC teams based on the data available on The Blue Alliance.
  
## How to use

First, you will need to go to **keys.yaml** and add an authentication key(X-TBA-Auth-Key). It will be used to pull data from The Blue Alliance. Run the code from your terminal by typing in "python main.py"

## Dependencies

Flask
```
pip install Flask
```

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

Note: Installing Matplotlib automatically installs Pillow. But if you face any issues with the installation of Pillow, install it using the command below.

```
pip install Pillow
```

Python standard libraries used:

- concurrent.futures

- datetime

- functools

- base64

- io


## How does it work

Once the user inputs 2 FRC teams, the backend code will iterate through all matches available for one of the teams ever since both teams existed. It will check for matches where the two teams played on opposite alliances. All this data will be collected and displayed. The user will see the pie chart showing what percent of matches each team has won and can look at scores from each match.

## Input Teams

<a href="https://drive.google.com/file/d/1u2HEUxGJIUWXWwi-g_UWAS_F-bT45lgT/view?usp=sharing"><img  src="https://drive.google.com/uc?export=view&id=1u2HEUxGJIUWXWwi-g_UWAS_F-bT45lgT"  style="width: 650px; max-width: 100%; height: auto"  title=""/>

## View Record

<a href="https://drive.google.com/file/d/1P8s0Um2h7Zd7HGYhsIBcqTmjIxrqgkNZ/view?usp=sharing"><img  src="https://drive.google.com/uc?export=view&id=1P8s0Um2h7Zd7HGYhsIBcqTmjIxrqgkNZ"  style="width: 650px; max-width: 100%; height: auto"  title=""/>
  
## Finally

Enjoy using this website, and let me know if you have any questions, comments, or concerns.