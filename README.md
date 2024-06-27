# Sourdough Starter Spy 🍞

Building a sourdough monitor that measures the temperature, humidity and distance of a sourdough starter. 
This is a personal project that demonstrates my skills as well as my motivation and passion for programming. 
I am using an ESP32 device and programming it using MicroPython on the VSCode IDE with the PyMakr extension. 
My final goal is to to send the data to a website and visualise the ideal state of growth of a sourdough starter.

## Installation (Ongoing)

## Build Microcontroller 

* [ESP32 NodeMCU](https://www.berrybase.de/esp32-nodemcu-development-board)
* [DHT22](https://www.berrybase.de/DHT22-Digitaler-Temperatur-und-Luftfeuchtesensor)
* [HCSR04](https://www.berrybase.de/seeed-grove-ultraschall-abstandssensor)
* female-male jumper 
* led light

<p align="center">
<a>
  <img height="60" src="images/image_one.png" HSPACE="50"/>
</a>
<a>
  <img height="60" src="images/image_two.png" HSPACE="50"/>
</a>


### Install Microcontroller

1. Download micropython firmware (.bin folder)
2. Connect Esp32 to computer (while connecting hold boot button. This will reset microcontroller)
3. [Flash Micropython on devise](https://electrocredible.com/micropython-on-esp32-thonny-example/)


### Setup IDE

1. Clone the repository
2. Make sure you have the latest Python version
3. Install latest Node version
4. Install PyMakr extension in code
5. Open Project: `in search panel`
6. Install venv: `python3 -m venv venv`
7. Run venv: `source venv/bin/activate`


## Requirements 

### Package manager
Micropython has its own package manager `mip` 

```bash
# set up package manger 
Import mip

# list all files on devise
uos.listdir()
```


#### Libraries

The following dependency have to be installed manually on the microcontroller directly. 

```bash
# install library 
mip.install ("dht")
```