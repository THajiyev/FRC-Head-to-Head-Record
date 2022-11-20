[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://shields.io/) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) 

# FRC Head-to-Head Record

This website will allow you to view the head-to-head record of 2 FRC teams based on the data available on The Blue Alliance.

## Input Teams

<a  href="https://drive.google.com/file/d/1R1Egl5CHWHSyMykftGw7s2eiMyMTyJZn/view?usp=sharing"><img  src="https://drive.google.com/uc?export=view&id=1R1Egl5CHWHSyMykftGw7s2eiMyMTyJZn"  style="width: 650px; max-width: 100%; height: auto"  title=""/>

## View Record

<a  href="https://drive.google.com/file/d/1f2qRmGM6XFkebKO-1YCW4IT3rji7QCKe/view?usp=sharing"><img  src="https://drive.google.com/uc?export=view&id=1f2qRmGM6XFkebKO-1YCW4IT3rji7QCKe"  style="width: 650px; max-width: 100%; height: auto"  title=""/>

## Set up

First, go to **keys.yaml** and add an authentication key(X-TBA-Auth-Key). It will be used to pull data from The Blue Alliance. 

``` yaml
auth: your-key
```

Then to run the website, type in the following command in the terminal. 

```
python main.py
```

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

## License

MIT