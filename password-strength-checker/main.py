import re  
import streamlit as st  

# Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔏", layout="centered")

# Page Title and Description
st.title("🔏 Password Strength Checker")
st.write("This is a simple password strength checker. Enter a password and it will tell you how strong or weak it is.")

# Function to check password strength
def password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("▫ Password should be at least 8 characters long.")

    # Uppercase & Lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("▫ Password should contain both uppercase (A-Z) and lowercase (a-z) letters.")

    # Digit check
    if re.search(r"\d", password):  
        score += 1
    else: 
        feedback.append("▫ Password should contain at least one number (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*()_+=\-[\]{};:'\",.<>?/|\\]", password):  
        score += 1
    else:
        feedback.append("▫ Password should contain at least one special character (!@#$%^&* etc.).")

    # Determine password strength
    if score == 4:
        st.success("✅ **Strong Password**. Your password is secure.")
    elif score == 3:
        st.info("⚠ **Moderate Password**. Try adding more features.")
    else:   
        st.error("❌ **Weak Password**. Add more features.")  # ✅ Fixed issue here

    # Show feedback in expander
    if feedback:
        with st.expander("🔍 Improve your Password"):
            for item in feedback:
                st.write(f"➡ {item}")

# Get User Input
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong.")

# Check Password Strength
if st.button("Check Password Strength"):
    if password.strip():  # Ensure password is not empty or spaces
        password_strength(password)
    else:
        st.warning("▪ Please enter a password first.")
