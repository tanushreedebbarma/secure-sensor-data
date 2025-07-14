# Hardware Setup

# Step 1: Set Up the Raspberry Pi

# i) Flash Raspberry Pi OS:
Use the Raspberry Pi Imager to install Raspberry Pi OS (32-bit) on a microSD card.

# ii) Enable SSH and Wi-Fi for Headless Setup: 
  * After flashing, insert the SD card into your computer.
  * Create an empty file named `ssh` (no extension) in the `/boot` directory.
  * Create a `wpa_supplicant.conf` file with your Wi-Fi credentials:
    conf:
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="Your_SSID"
        psk="Your_PASSWORD"
    }
    
# iii) Insert and Boot
* Insert the microSD card into the Raspberry Pi.
* Connect the Raspberry Pi to power and optionally an Ethernet cable for reliable internet access.
* Wait for it to boot.

# iv) Find the Pi's IP Address
* Use your router’s admin panel or `nmap`(e.g., nmap -sn 192.168.0.0/24)
  Or try:
  ping raspberrypi.local
  ssh pi@raspberrypi.local
  
# Step 2: Access the Raspberry Pi Remotely

# i) SSH Access
ssh pi@<raspberry-pi-ip-address>
Default credentials:
Username: pi
Password: raspberrypi

# ii) Enable VNC (GUI Access)
sudo raspi-config
* Navigate to `Interfacing Options → VNC → Enable`
* Reboot the Pi if prompted.

# iii) Use RealVNC Viewer
* Download and install [RealVNC Viewer]
* Open RealVNC Viewer and connect to the Pi using its IP address (e.g., `192.168.0.100`)
* Login with the same Raspberry Pi credentials (`pi / raspberrypi`)

This provides a full graphical desktop environment.

# Step 3: Connect the Sensors

# i) DHT11 Wiring
* VCC → 5V (pin 2)
* Data → GPIO18 (pin 12)
* GND → GND (pin 6)

# ii) BME280 Wiring
* VCC → 3.3V (pin 1)
* GND → GND (pin 9)
* SCL → GPIO3 (pin 5)
* SDA → GPIO2 (pin 3)
