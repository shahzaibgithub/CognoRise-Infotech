print(
    '''
    Welcome to Password Generator Application
    
    '''
    )

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(characters, length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print("Generated password:", password)

main()
