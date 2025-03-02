import streamlit as st

st.title('🔄 Unit Convertor App')
st.markdown("### Convert Length , Weight And Time Instantly")
st.write("Welcome! Select a category, enter a value and get a converted value in istantly.")
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.62137
        elif unit == "Miles to Kilometers":
            return value / 0.62137
        elif unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Meters to Kilometers":
            return value / 1000
        elif unit == "Meter to Centimeter":
            return value * 100
        elif unit == "Centimeter to Meter":
            return value / 100
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Kilograms to Gram":
            return value * 1000
        elif unit == "Gram to Kilograms":
            return value / 1000
        elif unit == "Gram to Pounds":
            return value / 453.592
        elif unit == "Pounds to Gram":
            return value * 453.592
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60   
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
             return value / 60       
        elif unit == "Hours to Minutes":
             return value * 60
        elif unit == "Days to Hours":
             return value * 24  
        elif unit == "Hours to Days":
             return value / 24
        elif unit == "Days to Weeks":
             return value / 7
        elif unit == "Weeks to Days":
             return value * 7
        elif unit == "Seconds to Days":
             return value / 86400   
        elif unit == "Days to Seconds":
             return value * 86400
        elif unit == "Seconds to Hours":
             return value / 3600
        elif unit == "Hours to Seconds":
             return value * 3600
    return None  # Return None explicitly if no match found
    
if category == "Length":
    unit = st.selectbox("📏 Select Conversation", ["Kilometers to Miles", "Miles to Kilometers",  "Kilometers to Meters", "Meters to Kilometers", "Meter to Centimeter", "Centimeter to Meter", "Meters to Feet", "Feet to Meters" ]) 
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversation", ["Kilograms to Pounds", "Pounds to Kilograms", "Gram to Pounds", "Pounds to Gram", "Kilograms to Gram", "Gram to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏲ Select Conversation", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Days to Hours", "Hours to Days", "Days to Weeks", "Weeks to Days", "Seconds to Days", "Days to Seconds", "Seconds to Hours", "Hours to Seconds"])

value = st.number_input("Enter the Value to Convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion! Please check your inputs.")