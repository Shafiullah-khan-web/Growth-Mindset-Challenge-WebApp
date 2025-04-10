import streamlit as st
from datetime import datetime

# App title and intro
st.set_page_config(page_title="Growth Mindset Journal", page_icon="🧠")
st.title("🧠 Growth Mindset Journal")
st.write("Welcome! Write one thing you learned today or a challenge you overcame.")

# Text area for today's reflection
reflection = st.text_area("📝 What's on your mind today?", height=150)

# Save the reflection
if st.button("Save Reflection"):
    if reflection.strip():
        with open("journal.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {reflection.strip()}\n")
        st.success("✅ Reflection saved!")
    else:
        st.warning("⚠️ Please write something before saving.")

st.markdown("---")
# st.subheader("📖 Past Reflections")

# Load past reflections (with caching)
@st.cache_data
def load_reflections():
    try:
        with open("journal.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

entries = load_reflections()

# Display past reflections
if entries:
    for entry in reversed(entries[-10:]):  # Show last 10 reflections
        st.markdown(f"🗓️ *{entry.strip()}*")
else:
    st.info("No reflections yet. Start journaling to see them here!")

