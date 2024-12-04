from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import sys

def read_image(file_path):
    with open(file_path, "rb") as file:
        image_bytes = file.read()
    return image_bytes

def save_modified_image(file_path, modified_bytes):
    with open(file_path, "wb") as file:
        file.write(modified_bytes)

def main():
    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    original_image_bytes = read_image(input_image_path)
    
    key = b'Luk3ImY0urFath3r'
    iv = b'Mi113nniumFa1c0n'
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ct_bytes = cipher.encrypt(pad(original_image_bytes, AES.block_size)) #cyphertext in bytes
    save_modified_image(output_image_path, ct_bytes)
    
if __name__ == "__main__":
    main()