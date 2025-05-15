import base64
import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
import Adafruit_DHT
import time

# DHT11 Setup
sensor = Adafruit_DHT.DHT11
gpio = 18

# BME280 Setup
import bme280
from smbus2 import SMBus
bus = SMBus(1)
address = 0x77

# AES Settings
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s)-1:])]

# AES Encryption Functions
def aes_encrypt(raw, key):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8")))

def aes_decrypt(enc, key):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:])).decode("utf-8")

# Generate AES key from password
password = "Netid"
aes_key = hashlib.sha256(password.encode("utf-8")).digest()

# RSA Encryption of AES key
with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())
rsa_cipher = PKCS1_OAEP.new(public_key)

# RSA Decryption of AES key
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())
rsa_cipher_decrypt = PKCS1_OAEP.new(private_key)

# Loop to read the sensors 5 times
for i in range(5):
    print(f"--- Reading {i+1} ---")
    
    # Read from DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    
    # Read from BME280
    bme280_data = bme280.sample(bus, address)
    bme280_temp = bme280_data.temperature
    bme280_humidity = bme280_data.humidity
    bme280_pressure = bme280_data.pressure
    
    # Prepare message
    message = (
        "DHT11 => Temp: {0:0.1f}C, Humidity: {1:0.1f}% | "
        "BME280 => Temp: {2:0.2f}C, Humidity: {3:0.2f}%, Pressure: {4:0.2f} hPa"
    ).format(temperature, humidity, bme280_temp, bme280_humidity, bme280_pressure)
    
    print(message)
    
    # Encrypt message using AES
    encrypted_message = aes_encrypt(message, aes_key)

    # Encrypt AES key using RSA
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    # Simulate transmission
    print("\n--- Encrypted Output ---")
    print("Encrypted AES key:", base64.b64encode(encrypted_aes_key).decode("utf-8"))
    print("Encrypted Message:", encrypted_message.decode("utf-8"))

    # RSA Decrypt AES key
    decrypted_aes_key = rsa_cipher_decrypt.decrypt(encrypted_aes_key)

    # Decrypt message using decrypted AES key
    decrypted_message = aes_decrypt(encrypted_message, decrypted_aes_key)

    print("\n--- Decrypted Output ---")
    print("Decrypted AES key:", base64.b64encode(decrypted_aes_key).decode("utf-8"))
    print("Decrypted Message:", decrypted_message)
    
    # Add a small delay between readings
    time.sleep(1)
