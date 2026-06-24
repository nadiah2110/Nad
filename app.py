import streamlit as st
import random

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Grammar Adventure!",
    page_icon="📚",
    layout="centered"
)

# ---------------------------
# Question Bank
# ---------------------------
QUESTIONS = [
    {
        "question": "Which word is a noun?",
        "options": ["run", "happy", "dog", "quickly"],
        "answer": "dog",
        "explanation": "A noun is a person, place, animal, or thing. 'Dog' is an animal."
    },
    {
        "question": "Choose the correct sentence.",
        "options": [
            "She are playing.",
            "She is playing.",
            "She am playing.",
            "She be playing."
        ],
        "answer": "She is playing.",
        "explanation": "'She' goes with 'is'."
    },
    {
        "question": "Which word is a verb?",
        "options": ["jump", "blue", "cat", "chair"],
        "answer": "jump",
        "explanation": "A verb is an action word. 'Jump' is an action."
    },
    {
        "question": "Fill in the blank: The bird ___ flying.",
        "options": ["is", "are", "am", "be"],
        "answer": "is",
        "explanation": "'Bird' is singular, so we use 'is'."
    },
    {
        "question": "Which sentence uses a capital letter correctly?",
        "options": [
            "my name is Tom.",
            "My name is tom.",
            "My name is Tom.",
            "my Name is Tom."
        ],
        "answer": "My name is Tom.",
        "explanation": "Names and the first word of a sentence need capital letters."
    },
    {
        "question": "Which word is an adjective?",
        "options": ["red", "run", "dog", "sing"],
        "answer": "red",
        "explanation": "An adjective describes something. 'Red' describes color."
    },
    {
        "question": "Choose the correct word: I have ___ apple.",
        "options": ["a", "an", "the", "many"],
        "answer": "an",
        "explanation": "We use 'an' before words that begin with a vowel sound."
    },
    {
        "question": "Which punctuation mark ends a question?",
        "options": [".", "!", ",", "?"],
        "answer": "?",
        "explanation": "Questions end with a question mark."
    },
    {
        "question": "Choose the correct sentence.",
        "options": [
            "The cats is sleeping.",
            "The cats are sleeping.",
            "The cats am sleeping.",
            "The cats be sleeping."
        ],
        "answer": "The cats are sleeping.",
        "explanation": "'Cats' is plural, so we use 'are'."
    },
    {
        "question": "Which word is a pronoun?",
        "options": ["house", "she", "yellow", "dance"],
        "answer": "she",
        "explanation": "Pronouns replace nouns. 'She' is a pronoun."
    }
]

# ---------------------------
# Session State
# ---------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "questions_answered" not in st.session_state:
    st.session_state.questions_answered = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(QUESTIONS)

# ---------------------------
# Header
# ---------------------------
st.title("📚 Grammar Adventure!")
st.subheader("Help the Grammar Wizard earn stars! ⭐")

# ---------------------------
# Scoreboard
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric("⭐ Score", st.session_state.score)

with col2:
    st.metric("📝 Questions", st.session_state.questions_answered)

st.divider()

# ---------------------------
# Current Question
# ---------------------------
q = st.session_state.current_question

st.markdown(f"### {q['question']}")

selected_answer = st.radio(
    "Choose your answer:",
    q["options"],
    key=f"radio_{st.session_state.questions_answered}"
)

# ---------------------------
# Submit Answer
# ---------------------------
if not st.session_state.answered:

    if st.button("🎯 Submit Answer"):

        st.session_state.answered = True
        st.session_state.questions_answered += 1

        if selected_answer == q["answer"]:
            st.session_state.score += 10

            st.success("🎉 Correct! Great job!")
            st.info(f"💡 {q['explanation']}")

            st.balloons()

        else:
            st.error("❌ Not quite.")

            st.info(
                f"✅ Correct answer: **{q['answer']}**\n\n"
                f"💡 {q['explanation']}"
            )

# ---------------------------
# Next Question
# ---------------------------
if st.session_state.answered:

    if st.button("➡️ Next Question"):

        st.session_state.current_question = random.choice(QUESTIONS)
        st.session_state.answered = False
        st.rerun()

# ---------------------------
# Progress Section
# ---------------------------
st.divider()

if st.session_state.score >= 100:
    st.success(
        "🏆 Amazing! You are a Grammar Champion!"
    )

elif st.session_state.score >= 50:
    st.success(
        "🌟 Great work! Keep going!"
    )

else:
    st.write("Keep collecting stars by answering correctly!")

# ---------------------------
# Reset Game
# ---------------------------
st.divider()

if st.button("🔄 Restart Game"):
    st.session_state.score = 0
    st.session_state.questions_answered = 0
    st.session_state.answered = False
    st.session_state.current_question = random.choice(QUESTIONS)
    st.rerun()
