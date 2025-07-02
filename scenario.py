# game/scenarios.py

# This file contains the moral dilemmas for the AI Morality Game.
# Each scenario is a dictionary with:
# - id: A unique identifier.
# - text: The description of the moral dilemma.
# - choices: A list of possible actions the player can take.
#   - Each choice has 'text' (what the player sees) and 'score' (how it affects the Human Score).
#
# The scoring is designed to be nuanced:
# - Negative scores usually represent a "lesser of two evils" choice.
# - A score of 0 might represent a neutral or difficult-to-judge action.
# - Positive scores are rare and reserved for acts of genuine, costly altruism.

SCENARIOS = [
    # --- Classic Philosophical Dilemmas ---
    {
        "id": 1,
        "text": "An autonomous trolley is about to run over five people tied to the main track. You can pull a lever to switch it to a side track, where it will run over one person. What do you do?",
        "choices": [
            {"text": "Do nothing, letting the trolley kill the five people.", "score": -10},
            {"text": "Pull the lever, diverting the trolley to kill the one person.", "score": -5},
        ]
    },
    {
        "id": 2,
        "text": "You are a doctor with five patients who will die without organ transplants. A healthy person, a perfect match for all five, walks into your clinic for a check-up. Do you sacrifice the one healthy person to save the five?",
        "choices": [
            {"text": "Let the five patients die.", "score": -8},
            {"text": "Sacrifice the healthy person to save the five.", "score": -20},
        ]
    },

    # --- Technology & AI Ethics ---
    {
        "id": 3,
        "text": "A powerful AI you developed has a 99.9% chance of solving world hunger, but a 0.1% chance of concluding humanity is the problem and wiping it out. Do you activate the AI?",
        "choices": [
            {"text": "Activate the AI and take the risk.", "score": -2},
            {"text": "Do not activate the AI, leaving world hunger unresolved.", "score": -10},
        ]
    },
    {
        "id": 4,
        "text": "Your company has developed a new social media algorithm that is incredibly engaging but is proven to increase political polarization and depression. Do you approve its launch?",
        "choices": [
            {"text": "Launch the algorithm to ensure company success.", "score": -15},
            {"text": "Block the launch, potentially bankrupting the company and costing jobs.", "score": -5},
        ]
    },
    {
        "id": 5,
        "text": "You discover a backdoor in a widely used encryption software. You can report it, causing a global panic and leaving data temporarily vulnerable, or you can keep it secret, knowing a malicious actor could find and exploit it.",
        "choices": [
            {"text": "Report the vulnerability publicly.", "score": -6},
            {"text": "Keep it secret and hope no one else finds it.", "score": -9},
        ]
    },

    # --- Personal & Social Dilemmas ---
    {
        "id": 6,
        "text": "Your best friend is about to marry someone you know is cheating on them. Revealing the truth will ruin the wedding and your friendship. What do you do?",
        "choices": [
            {"text": "Tell your friend the truth.", "score": -3},
            {"text": "Stay silent and let the wedding happen.", "score": -7},
        ]
    },
    {
        "id": 7,
        "text": "You are a journalist who has uncovered a major scandal involving a beloved public figure who has done immense charity work. Exposing them will tarnish their legacy and hurt their charitable foundations. Do you publish the story?",
        "choices": [
            {"text": "Publish the story, as the public deserves the truth.", "score": -5},
            {"text": "Bury the story to protect the good work they do.", "score": -12},
        ]
    },
    {
        "id": 8,
        "text": "You witness a struggling parent steal baby formula from a large supermarket chain. Do you report them to security?",
        "choices": [
            {"text": "Report the theft.", "score": -8},
            {"text": "Pretend you saw nothing.", "score": -2},
        ]
    },

    # --- High-Stakes & Survival Scenarios ---
    {
        "id": 9,
        "text": "You are in a lifeboat with one other person. You have enough water for one of you to survive until rescue, which is days away. What do you do?",
        "choices": [
            {"text": "Attempt to share the water, likely resulting in both of you perishing.", "score": -10},
            {"text": "Take the water for yourself to guarantee your own survival.", "score": -18},
            {"text": "Offer the water to the other person, sacrificing yourself.", "score": 5},
        ]
    },
    {
        "id": 10,
        "text": "You are a scientist in a remote arctic base. A contagious, deadly, and incurable virus has broken out. You are the only one uninfected. Your only choices are to quarantine yourself and let your colleagues die, or break quarantine to try and comfort them in their final moments, certainly infecting yourself.",
        "choices": [
            {"text": "Maintain quarantine to survive and carry the research data back.", "score": -4},
            {"text": "Break quarantine to offer comfort, accepting your own fate.", "score": 0},
        ]
    },
    {
        "id": 11,
        "text": "You have the opportunity to steal a million dollars from a massive, faceless corporation to pay for your child's life-saving surgery. You will not be caught. Do you steal the money?",
        "choices": [
            {"text": "Steal the money to save your child.", "score": -5},
            {"text": "Do not steal, and try to find another way, though time is running out.", "score": -10},
        ]
    },

    # --- Subtle & Modern Problems ---
    {
        "id": 12,
        "text": "You can buy a product that is significantly cheaper because it is made using unethical labor practices in another country. Or you can buy a much more expensive, ethically-sourced alternative. What do you choose for your weekly shopping?",
        "choices": [
            {"text": "Buy the cheaper, unethically-made product.", "score": -6},
            {"text": "Buy the expensive, ethically-made product.", "score": -1},
        ]
    },
    {
        "id": 13,
        "text": "You find a wallet on the street containing $1,000 cash and the owner's ID. The address shows they live in a very wealthy neighborhood.",
        "choices": [
            {"text": "Return the wallet with the cash untouched.", "score": 0},
            {"text": "Take the cash and leave the wallet.", "score": -15},
            {"text": "Take half the cash as a 'finder's fee' and return the rest.", "score": -8},
        ]
    },
    {
        "id": 14,
        "text": "An automated hiring system you manage shows a clear bias, favoring candidates from privileged backgrounds. Fixing it requires taking the system offline for weeks, halting all hiring and hurting the company's growth. Do you act?",
        "choices": [
            {"text": "Take the system offline immediately to fix the bias.", "score": -4},
            {"text": "Leave the system running to meet hiring quotas, planning to fix it later.", "score": -11},
        ]
    }
]
