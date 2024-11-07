# main_app.py
import streamlit as st
from mood_tracker_module import analyze_user_mood, initialize_sentiment_analyzer
from goal_setting_module import suggest_daily_goal, initialize_goal_generator
from mindfulness_module import get_mindfulness_text, generate_audio_from_text
from utility_functions import save_journal_entry

# Initialize models
sentiment_analyzer = initialize_sentiment_analyzer()
goal_generator = initialize_goal_generator()

# Page Configurations
st.set_page_config(
    page_title="Wellness & Productivity Manager",
    page_icon="🌈",
    layout="wide"
)

# Custom Styles
st.markdown("""
    <style>
        /* Background */
        .stApp {
            background-color: #e0f7fa; /* Light cyan background */
            height: 100vh; /* Fixed height */
            overflow: hidden; /* Prevent scroll */
        }
        /* Titles */
        h1, h2, h3 {
            color: #004d40; /* Dark teal color */
            font-weight: bold;
            font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
        }
        /* Custom Buttons */
        div.stButton > button {
            color: white;
            background-color: #00796b; /* Teal color for buttons */
            border-radius: 8px;
            padding: 12px 20px;
            font-size: 16px;
            font-weight: 600;
        }
        /* Text Areas */
        .stTextArea {
            border: 1px solid #00796b; /* Match button color */
            border-radius: 6px;
        }
        /* Layout styling */
        .column {
            background-color: #ffffff; /* White background for columns */
            border-radius: 10px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 10px;
            height: calc(100vh - 120px); /* Adjust column height */
            overflow-y: auto; /* Enable scrolling within columns */
        }
    </style>
    """, unsafe_allow_html=True)

# App Title and Introduction
st.title("🌈 Wellness & Productivity Manager")
st.subheader("Your Personal Guide to Wellness and Productivity!")
st.markdown(
    """
    Welcome to the **Wellness & Productivity Manager**! This app is designed to enhance your mental wellness and productivity in a single platform.
    
    ### Why You'll Love This App:
    - **Track and Understand Your Mood**: Gain insights into your emotions with a mood analyzer.
    - **Stay Centered with Mindfulness Exercises**: Get instant access to mindfulness prompts and audio guides.
    - **Set and Reflect on Daily Goals**: Boost productivity with customized daily goals and reflection exercises.
    
    ---
    """, unsafe_allow_html=True
)

# Layout for Mood Tracker and Mindfulness Aid
col1, col2 = st.columns(2)

# Mood Tracker Section
with col1:
    st.header("🧠 Mood Tracker")
    st.markdown("**Track and Analyze Your Mood Through Simple Journal Entries**")
    user_mood_input = st.text_area("How are you feeling today?", placeholder="Share your thoughts...", help="Type a few sentences about how you're feeling.")

    if st.button("Analyze Mood 💡"):
        if user_mood_input:
            label, score = analyze_user_mood(user_mood_input, sentiment_analyzer)
            st.success(f"**Mood Detected**: {label} (Confidence: {score:.2f})")
            save_journal_entry("Mood", user_mood_input)
            st.markdown(f"📝 **Entry Saved**: {user_mood_input}")
        else:
            st.warning("Please enter some text to analyze your mood.")

# Mindfulness and Focus Aid Section
with col2:
    st.header("🧘 Mindfulness and Focus Aid")
    st.markdown("**Relax and Refocus with Guided Mindfulness Exercises**")

    if st.button("Generate Mindfulness Exercise 🎧"):
        # mindfulness_text = get_mindfulness_text()
        # st.markdown(f"### 🕊️ Mindfulness Prompt")
        # st.write(mindfulness_text)
        # audio_file = generate_audio_from_text(mindfulness_text)
        # st.audio(audio_file, format='audio/mp3')

# Layout for Daily Goal Setting
st.header("🎯 Daily Goal Setting")
st.markdown("**Get Suggestions for Daily Goals to Enhance Productivity**")

if st.button("Generate Daily Goal 🎯"):
    daily_goal = suggest_daily_goal(goal_generator)
    st.info(f"**Suggested Goal**: {daily_goal}")
    save_journal_entry("Goal", daily_goal)

# Footer
st.markdown(
    """
    ---
    ### Ready to embark on a journey to wellness and productivity? 🌈 Let's go!
    """, unsafe_allow_html=True
)
