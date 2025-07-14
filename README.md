# Secure Sensor Data Transmission Using Raspberry Pi and Hybrid Cryptography

# Abstract

This project implements a secure sensor data transmission system using a Raspberry Pi and a hybrid cryptographic approach that combines AES (Advanced Encryption Standard) and RSA (Rivest-Shamir-Adleman) algorithms. Environmental data is collected from two sensors: DHT11 and BME280, which measure temperature, humidity, and pressure.

The sensor data is encrypted using symmetric AES encryption to ensure fast and efficient data confidentiality. To secure the AES key during transmission, RSA asymmetric encryption is employed. The encrypted sensor data and the RSA-encrypted AES key are transmitted and subsequently decrypted using the corresponding RSA private key, followed by AES decryption of the data.

This system demonstrates an end-to-end encryption framework that ensures the confidentiality and integrity of data in IoT applications. Future enhancements include secure key storage using Trusted Applications in OP-TEE and integration with cloud key management services such as Google Cloud KMS.

# Quick Start

1. Set up your Raspberry Pi and connect the sensors
2. Install the required software and dependencies
3. Run the sender and receiver scripts

📎 [Hardware Setup](docs/HardwareSetup.md)  
📎 [Software Setup](docs/SoftwareSetup.md)

# Project Setup

secure-sensor-data/
├── AES_RSA_DHT_BME.py/ # Script to read, encrypt, and transmit data
├── docs/ # Documentation
│ ├── HardwareSetup.md
│ └── SoftwareSetup.md
├── generate_keys.py # RSA key generation script
└── README.md

# Components/Libraries Used
- Raspberry Pi (tested with Pi 3 Model B)
- Python 3
- AES & RSA encryption (PyCryptodome)
- DHT11 & BME280 sensors
- smbus2, Adafruit CircuitPython DHT
- SSH / VNC for remote access

# Future Work

- Secure key storage via OP-TEE Trusted Applications  
- Integration with cloud key managers (e.g., Google Cloud KMS)  

# License

This project is licensed under the MIT License.

# Contributions

Contributions and feedback are welcome! Feel free to fork, open issues, or submit pull requests.
