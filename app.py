# Import streamlit
import streamlit as st


st.set_page_config(page_title="Growth Mindset Challenge", page_icon="📈")


st.title("🌱 Growth Mindset Challenge: Web App With Streamlit 📈")

st.header("📌 Welcome To Your Growth Mindset Journey 📌")
st.write(
    """
    This web app helps you develop a **growth mindset** by learning, 
    reflecting, and taking challenges daily. Powered by **AI**, this app 
    guides you through **self-reflection, challenges, and achievements** to help 
    you stay motivated. Let's get started! ⭒✧💻✧⭒
    """
)

# Quote Section
st.header("🌟 Inspirational Growth Mindset Quote 🌟")
st.write("🌱 *“Don’t be afraid to fail. Be afraid not to try.”* — **Michael Jordan**")

# User Challenge Section
st.header("🚩 Challenge of The Day!")
user_input = st.text_input("Describe a challenge you faced today:")

# Challenge Condition
if user_input:
    st.success(f"Great job! You faced: **{user_input}**. Keep pushing forward towards your goals! 🥇📚")
else:
    st.warning("Don't forget to take the challenge! Describe a challenge you faced today. You got this! 💪🏼💡")

# Reflection Section
st.header("📝 Reflect on Your Learning Journey")
reflection = st.text_area("Write your reflection on your learning journey:")

# Reflection Condition
if reflection:
    st.success(f"Great insight! Your reflection: **{reflection}** 📝🌟")
else:
    st.info("Reflecting on past experiences helps you grow. Share your thoughts here!")

# Achievements Section
st.header("🎉 Celebrate Your Wins! 🏆")
achievement = st.text_input("Share something you have recently accomplished:")

# Achievement Condition
if achievement:
    st.success(f"Amazing! You achieved: **{achievement}** 🎊🔥")
else:
    st.info("Big or small, every achievement counts! Share one now. 💪✨")

# Footer
st.write("---")
st.write("🌟 *Believe you can, and you're halfway there!* 🌟")
st.write("💡 Opportunities don’t happen. You create them, so believe in yourself! 🔥")
st.write("⛔ Created by Rahima Shaikh")
