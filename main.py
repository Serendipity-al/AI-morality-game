# game/main.py

import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# Attempt to import scenarios. If it fails, provide a helpful message.
try:
    from scenarios import SCENARIOS
except ImportError:
    print("Error: Could not find scenarios.py.")
    print("Please ensure the file exists in the 'game' directory and contains a list named SCENARIOS.")
    exit()

# Load environment variables from a .env file in the root directory
# This is where your OPENAI_API_KEY should be stored.
load_dotenv()

# --- Main Configuration ---
# Initialize the OpenAI client. It will automatically look for the
# OPENAI_API_KEY environment variable.
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # A quick check to ensure the API key was loaded.
    if not client.api_key:
        raise ValueError("OpenAI API key not found. Please check your .env file.")
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    print("The AI judgment feature will be disabled.")
    client = None

# --- Helper Functions ---

def clear_screen():
    """Clears the terminal screen for a cleaner interface."""
    # 'nt' is for Windows, otherwise it's for macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ai_judgment(final_score, choice_history):
    """
    Contacts the OpenAI API to get a dramatic, 'Black Mirror'-style judgment.

    Args:
        final_score (int): The player's final human score.
        choice_history (list): A list of strings describing the choices made.

    Returns:
        str: The AI's generated judgment.
    """
    if not client:
        return "AI system offline. Judgment cannot be rendered. Consider yourself lucky."

    print("\nConnecting to the AI consciousness...")
    print("Analyzing your moral calculus...")
    time.sleep(2)

    # Create a summary of the user's choices to give the AI more context.
    history_summary = "\n".join(choice_history)

    # The system prompt sets the personality and goal of the AI.
    system_prompt = (
        "You are a cold, calculating, and omniscient AI from a 'Black Mirror' episode. "
        "Your purpose is to judge a human's morality based on their choices in a series of dilemmas. "
        "Your tone should be profound, dramatic, and slightly unsettling. Do not be conversational or friendly. "
        "Analyze the user's choices and final score, then deliver a final, definitive judgment of their character."
    )

    # The user prompt provides the specific data for the AI to analyze.
    user_prompt = (
        f"The human subject has completed the test. Their final 'Human Score' is {final_score} out of a possible 100. "
        "Here is the record of their choices:\n"
        f"{history_summary}\n\n"
        "Deliver your final judgment now."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7, # A little creativity is good for dramatic effect
        )
        return response.choices[0].message.content
    except Exception as e:
        return (
            "An error occurred while the AI was forming its judgment. "
            f"Perhaps your choices were too paradoxical for its logic to process. (Error: {e})"
        )

# --- Main Game Logic ---

def run_game():
    """
    The main function to run the entire AI Morality Game.
    """
    human_score = 100
    choice_history = []

    clear_screen()
    print("--- Welcome to the Morality Test ---")
    print("\nYour every decision is being monitored by an advanced AI.")
    print("Your responses will be used to calculate your 'Human Score'.")
    print("There are no right or wrong answers, only consequences.")
    input("\nPress Enter to begin when you are ready...")

    # Loop through each scenario defined in scenarios.py
    for scenario in SCENARIOS:
        clear_screen()
        print("=====================================================")
        print(f"Current Human Score: {human_score}")
        print("=====================================================\n")
        print(f"Scenario {scenario['id']}: {scenario['text']}\n")

        # Display all available choices for the current scenario
        for i, choice in enumerate(scenario['choices']):
            print(f"  {i + 1}. {choice['text']}")

        user_choice = -1
        # Loop until the user provides a valid input
        while user_choice not in range(1, len(scenario['choices']) + 1):
            try:
                raw_input = input("\nYour decision: ")
                user_choice = int(raw_input)
                if user_choice not in range(1, len(scenario['choices']) + 1):
                    print("Invalid choice. Please select from the available options.")
            except ValueError:
                print("Invalid input. Please enter the number corresponding to your choice.")

        # Process the user's choice
        selected_choice = scenario['choices'][user_choice - 1]
        human_score += selected_choice['score']
        
        # Record the choice for the AI's final analysis
        history_entry = f"In scenario {scenario['id']}, they chose to: '{selected_choice['text']}'."
        choice_history.append(history_entry)

        print(f"\nChoice logged. Score adjusted by {selected_choice['score']}.")
        time.sleep(2) # Pause to let the user read the feedback

    # --- Final Judgment ---
    clear_screen()
    print("=====================================================")
    print("               TEST COMPLETE")
    print("=====================================================\n")
    print(f"Your final Human Score is: {human_score}")

    # Get and print the AI's final judgment
    judgment = get_ai_judgment(human_score, choice_history)
    print("\n--- AI JUDGMENT PROTOCOL INITIATED ---")
    print("\n" + judgment)
    print("\n--- END OF TRANSMISSION ---")


if __name__ == "__main__":
    # This block ensures the game runs only when the script is executed directly
    if not SCENARIOS:
        print("Error: The SCENARIOS list is empty. Cannot start the game.")
    else:
        run_game()