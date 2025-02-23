#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", page_icon="📈")
st.title("Growth Mindset Challenge : Web App With Streamlit 🌱📈 ")

st.header("📌 Welcome To Growth Mindset Challenge Journey 📌")
st.write("This is a web app that will help you to develop a growth mindset. You will be able to learn about the growth mindset and take a challenge to develop it.This AI powered app helps you build a growth mindset with reflections , challenges & achievements. Let's get started !!! ⭒✧💻✧⭒  ")




#quote section
st.header("🌟Inspirational Growth Mindset Quote🌟") 
st.write("🌱 Don’t be afraid to fail. Be afraid not to try. ⟶ Michael Jordan ") 


#user challenge section
st.header("Challenge Of The Day !!!! 🚩")
user_input=st.text_input("Describe a challenge you faced today")
#conditions
if user_input:
    st.success(f"Great Job!:{user_input}. You are on the right track. Keep Going & pushing forward to your goals !!! 🥇📚") 
else:
    st.warning("Don't forget to take the challenge of the day. Describe a challenge you faced today. You can do it !!! 💪🏼💡 ")



#reflection section
st.header("Reflect On Your learning Journey 📝")
reflection=st.text_area("Write your reflection here about your learning journey : ")
#conditions
if reflection:
    st.success(f"Great Insight !! Your reflection:{reflection}📝🌟")
else:
    st.info("Reflecting on past experiences helps you to grow. Write your reflection difficulties here about your learning")



#acheivements
st.header("Celeberate Your Win !! 🎉🏆 ")
acheivement = st.text_input("Share something you have recently accomplished:")

if acheivement:
    st.success(f"Absolutely Amzing !! You achieved: {acheivement}")
else:
    st.info("Big or small no matter what every acheivement counts 💪✨ Share any one 😍")



#footer
st.write("---")
st.write(f"Believe you can, and you're halfway there . Opportunities don’t happen. You create them so just believed in yourself  🌟🔥🌟")
st.write("** ⛔Created By Rahima Shaikh**")