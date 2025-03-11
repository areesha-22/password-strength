#make function
#conditions
#loop
#ui from st


import streamlit as st
import random
import string

def generate_password(length,digits,special_digits):
 string_character   = string.ascii_letters
 if digits:
     string_character += string.digits
 if special_digits:
     string_character += string.punctuation
 
                                            #      "_" it means "loop" ,"i"
 return ''.join(random.choice(string_character) for _ in range(length))

st.title("PASSWORD GENERATOR")
 
length = st.slider ("Select Password Length: ",max_value=30 ,min_value=6 ,value=12)

digits = st.checkbox("include numbers:")
special_digits = st.checkbox("include some special characters:")

if st.button("GENERATE PASSWORD" ):
   password = generate_password(length,digits,special_digits)
st.write(f"GENERATE PASSWORD:{password}")


st.write("-------------------------")
st.write("Created By AREESHA")