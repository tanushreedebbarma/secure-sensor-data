from Crypto.PublicKey import RSA

# Generate 2048-bit RSA key
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save keys to disk
with open("private.pem", "wb") as prv_file:
    prv_file.write(private_key)
with open("public.pem", "wb") as pub_file:
    pub_file.write(public_key)

print("RSA key pair generated: private.pem and public.pem")
