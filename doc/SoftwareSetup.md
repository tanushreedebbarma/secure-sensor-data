# Software Setup

The software setup involves configuring the Raspberry Pi operating system, enabling necessary interfaces, setting up remote access tools, and installing all required packages and libraries to support sensor data acquisition and cryptographic operations.

# 1. System Update & I2C Configuration

# a) Update packages and enable I2C interface:
sudo apt update && sudo apt upgrade -y
run sudo raspi-config: 
* Navigate to `Interfacing Options → I2C → Enable`
* Reboot the Pi if prompted

# b) Check I2C device connection:
sudo apt install i2c-tools
i2cdetect -y 1  # Should show BME280 at address 0x77 or 0x76

# 2. Python Virtual Environment Setup
Create and activate a virtual environment:
python3 -m venv crypto-env
source crypto-env/bin/activate

# 3. Install Required Python Libraries
Install dependencies using pip:
pip install pycryptodome smbus2 adafruit-circuitpython-dht

# Installed Packages:

* `pycryptodome`: AES and RSA encryption
* `smbus2` and `bme280`: Communicate with the BME280 sensor
* `adafruit-circuitpython-dht`: Read data from DHT11 sensor
