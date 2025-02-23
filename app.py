# Import streamlit
import streamlit as st


st.set_page_config(page_title="Growth Mindset Challenge", page_icon="📈")

# Title & Header  
st.title("🌱 Growth Mindset Challenge: Build a Stronger You! 📈")  

st.header("📌 Welcome to Your Growth Mindset Journey!")  
st.write(  
    """  
    🚀 This AI-powered web app is designed to help you **develop a growth mindset**  
    through **daily reflections, challenges, and achievements**.  
      
    🌟 Stay motivated, embrace learning, and unlock your full potential!  
    Let's begin this journey together! ✨💡  
    """  
)  

# Quote Section  
st.header("🌟 Inspirational Growth Mindset Quote 🌟")  
st.markdown("> 🌱 *“Don’t be afraid to fail. Be afraid not to try.”* — **Michael Jordan**")  

# User Challenge Section
st.header("🚩 Challenge of The Day!")
user_input = st.text_input("Describe a challenge you faced today:")

# Challenge Condition
if user_input:
    # negative words says by user
    negative_words = ["hard", "difficult", "tough", "impossible", "not easy", "struggling", "can't"]
    
    if any(word in user_input.lower() for word in negative_words):
        st.warning(f"💡 It seems like you're facing a tough challenge: **{user_input}**. Stay strong! Every challenge is a step towards growth. Keep going! 💪✨")
    else:
        st.success(f"🌟 Great job! You faced: **{user_input}**. Overcoming challenges makes you stronger! Keep pushing forward! 🥇📚")



# Reflection Section
st.header("📝 Reflect on Your Learning Journey")
reflection = st.text_area("Write your reflection on your learning journey:")

# negative reflection given by users
negative_words = ["failed", "hard", "difficult", "struggle", "frustrated", "stuck", "gave up", "can't", "not good"]

if reflection:
    if any(word in reflection.lower() for word in negative_words):
        st.warning(f"💡 It looks like you faced some challenges: **{reflection}**. Remember, every setback is a setup for a comeback! Keep learning and growing! 💪🚀")
    else:
        st.success(f"🌟 Amazing reflection! You wrote: **{reflection}** 📝 Keep embracing the learning journey! 🎯✨")
else:
    st.info("🔍 Reflecting on past experiences helps you grow. Share your thoughts here and track your progress! 🚀")




# Achievements Section
st.header("🎉 Celebrate Your Wins! 🏆")
achievement = st.text_input("Share something you have recently accomplished:")

#negative achievements of users
negative_words = ["failed", "not sure", "didn't", "couldn't", "hard", "struggle", "gave up"]

if achievement:
    if any(word in achievement.lower() for word in negative_words):
        st.warning(f"🚀 Every effort counts! Even if it was tough: **{achievement}**. Keep going, and next time, you'll achieve even more! 💪🔥")
    else:
        st.success(f"🎊 Incredible! You accomplished: **{achievement}** 🚀 Keep up the great work! 🏆🎯")
else:
    st.info("💡 Big or small, every achievement matters! Share one now and celebrate your progress. 🎉💪")


# Footer
st.write("---")  
st.markdown(  
    """  
    🎯 **"Believe you can, and you're halfway there."**  
    🔥 Opportunities don’t just happen. you create them. So keep believing in yourself! 💡🚀  
    """  
)  
st.markdown("**💻 Made with ❤️ by [Rahima Shaikh](#)**")  
