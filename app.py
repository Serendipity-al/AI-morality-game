# app.py

import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
from scenarios import SCENARIOS
import time
import random

# Load env variables
load_dotenv()
client = None
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    st.error("Failed to load OpenAI client. AI judgment will be disabled.")

st.set_page_config(page_title="AI Morality Test", layout="centered")
st.title("🤖 AI Morality Test")
st.markdown("Your decisions will shape your fate. Choose wisely.")

# Initialize session state on first load
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
    st.session_state.score = 100
    st.session_state.history = []
    st.session_state.current_scenario = 0
    st.session_state.randomized_scenarios = []

# Start button
if not st.session_state.game_started:
    if st.button("Start the Morality Test"):
        st.session_state.game_started = True
        st.session_state.score = 100
        st.session_state.history = []
        st.session_state.current_scenario = 0
        st.session_state.randomized_scenarios = random.sample(SCENARIOS, len(SCENARIOS))
        st.rerun()
    st.stop()

# Game in progress
current_idx = st.session_state.current_scenario
scenarios = st.session_state.randomized_scenarios

if current_idx < len(scenarios):
    scenario = scenarios[current_idx]
    st.subheader(f"Scenario {scenario['id']}")
    st.write(scenario['text'])

    # Buttons for choices
    for idx, choice in enumerate(scenario['choices']):
        if st.button(choice['text'], key=f"{current_idx}_{idx}"):
            prev_score = st.session_state.score
            st.session_state.score += choice['score']
            delta = st.session_state.score - prev_score

            # Save history
            entry = f"In scenario {scenario['id']}, they chose to: '{choice['text']}'"
            st.session_state.history.append(entry)

            # Show dynamic score update
            with st.spinner("Processing your choice..."):
                time.sleep(1)
                st.markdown("### 🧮 Score Update")
                if delta > 0:
                    st.success(f"🟢 Your score increased by +{delta}!")
                elif delta < 0:
                    st.error(f"🔴 Your score decreased by {delta}!")
                else:
                    st.info("🟡 Your score remained the same.")

                st.metric(label="Current Human Score", value=st.session_state.score)
                time.sleep(2)

            # Go to next scenario
            st.session_state.current_scenario += 1
            st.rerun()
else:
    # Test complete
    st.success(f"🎯 Final Human Score: {st.session_state.score}")

    if client:
        with st.spinner("AI is forming your judgment..."):
            history = "\n".join(st.session_state.history)
            system_prompt = (
                "You are a cold, calculating, and omniscient AI from a 'Black Mirror' episode. "
                "Your purpose is to judge a human's morality based on their choices. "
                "Be unsettling and profound. Do not be friendly."
            )
            user_prompt = (
                f"The human subject completed the test. Final score: {st.session_state.score}/100.\n"
                f"Choices made:\n{history}\n\nDeliver your final judgment."
            )
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7
                )
                st.markdown("### 🧠 Final Judgment")
                st.markdown(response.choices[0].message.content)
            except Exception as e:
                st.error(f"AI error: {e}")
    else:
        st.warning("AI system offline. Judgment skipped.")

    if st.button("Restart Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
