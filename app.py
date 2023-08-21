import streamlit as st

st.title("Greatest of three Numbers")

num1 = st.number_input('Enter the first number',step = 1)
num2 = st.number_input('Enter the second number',step = 1)
num3 = st.number_input('Enter the third number',step = 1)
largest = 0

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

button = st.button("Submit")
if button:
    st.write("The largest number is "+str(largest))
