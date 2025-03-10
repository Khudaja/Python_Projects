import streamlit as st
import random # Importing the random module
import string # Importing the string module

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  #string provide specific letters. uppercaae, lowercase, digits and special characters

    if use_digits:
        characters += string.digits #+= is used to add the string to the characters. add numbers (0-9). selection is done on ui.

    if use_special:
        characters += string.punctuation #special characters means punctuation(!,%,$,etc)

    return ''.join(random.choice(characters) for _ in range(length)) #join is used to join the characters. random.choice is used to select the random characters. range is used to select the length of the password. i or_ or loop variable is used to iterate the loop. 

st.title("⭐Password Generator") #title of the page
st.write("Welcome to the Password Generator! Please select the options below to generate a password.") #description of the page

length = st.slider("Length of the password", min_value=4, max_value=20, value=8) #slider is used to select the length of the password. 4 is the minimum length, 30 is the maximum length and 8 is the default length of the password.

use_digits = st.checkbox("Use digits") #checkbox is used to select the digits. if clicked, digits will be included in the password.
use_special = st.checkbox("Use special characters") #checkbox is used to select the special characters. if clicked, special characters will be included in the password.

if st.button ("Generate Password"): 
    password = generate_password(length, use_digits, use_special) #password is generated using the generate_password function.
    st.write(f"Your password is: {password}") #password displayed

st.write("Build with ❤️ by [Khudaja](https://github.com/Khudaja/Python_Projects/tree/main/password-generator)") #footer of the page