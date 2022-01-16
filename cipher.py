# Simple Cipher static class to encrypt and decrypt message using the full key generated by Diffie-Hellman algorithm
class SimpleCipher:
    def encrypt_message(message, key):
        encrypted_message = ""
        for c in message:
            encrypted_message += chr(ord(c)+key)
        encrypted_message.encode('utf-8')
        return encrypted_message
    
    def decrypt_message(encrypted_message, key):
        decrypted_message = ""
        for c in encrypted_message:
            decrypted_message += chr(ord(c)-key)
        return decrypted_message