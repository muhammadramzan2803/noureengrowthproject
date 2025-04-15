#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project",project_icon="★")
st.title("Growth Mindset Challenge: Web App With Streamlit ")

st.header(" Welcome to Your Growth Journey !")
st.write  ("Embrace challenges,learn from mistake, and unlock your full potential.This AI-powerd app helps you build a growth mindset with reflection,challenges, and achievements! ✫")

#quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not final,failure is not fatal: it is the courage to continue that counts")

st.header("🔧 What's Your Challenge Today? ")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input: 
    st.success(f" ✶ You're facing: {user_input}. keep pushing forward towords your goal! ✶")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header(" Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f" ✶ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")


#Acheivements
st.header(" ⭐ Celebrate Your Wins!")
acheivment = st.text_input("Share something you've recently accomplished:")


if acheivment:
    st.success(f"⭐ Amazing! You Achieved: {acheivment}")

else:
    st.info("Big or small , every acheivement counts! Share one now 😃")


#footer 
st.write("- - -")
st.write("😃 keep believing in yourself. Growth is a journey, not a destination! 😃")
st.write(""" 😃Created by Noureen Rafiq""")