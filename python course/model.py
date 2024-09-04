import cryptography


from cryptography.fernet import Fernet

key = 'jwf2UwL78Rhmbta9YltFpUIu6E1wE_SNNWZLNbEZ2Zo='
fernet = Fernet(key)


decMessage = fernet.decrypt(b'gAAAAABmspcfP9iGn4-KbJil18YHzun8w3Md3RtKUv9ffW3StP-DF9AW9AcvVzPQE0s3yDJ6DoOoW5_AfXEJWvQGMycCCsy-rD_T4wzQDzIlM1ZLogXGEmM=').decode()

print("decrypted string: ", decMessage)