import random
import pyttsx3
from transformers import pipeline
from colorama import Fore, Style, init

# Initialize colorama for Windows support
init(autoreset=True)

# Load Sentiment Analysis Model
sentiment_pipeline = pipeline("sentiment-analysis")

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Define expressive responses with intensity levels
responses = {
    "POSITIVE": {
        "high": [
            "Wow, that's fantastic! Keep up the great energy! 🎉",
            "Amazing! I love hearing such great news! 🚀",
            "You're on fire! Keep shining! 🌟"
        ],
        "medium": [
            "That sounds great! 😊",
            "I'm happy to hear that! 🎊",
            "Nice! Keep going strong! 💪"
        ],
        "low": [
            "That's good to hear! 👍",
            "Great! What's next? 😃",
            "Nice! Keep it up! 😊"
        ]
    },
    "NEGATIVE": {
        "high": [
            "Oh no, that sounds really tough. I'm here for you. 💙",
            "I'm really sorry to hear that. You're not alone. 😞",
            "That must be so difficult. Remember, things will get better. 🌿"
        ],
        "medium": [
            "That sounds challenging. Want to talk about it?",
            "I'm sorry you're feeling this way. 💔",
            "I hope things get better for you soon. 💙"
        ],
        "low": [
            "I see, that sounds a bit frustrating. 😕",
            "That doesn’t sound great. Hope things improve! 🤞",
            "Stay strong! You've got this. 💪"
        ]
    },
    "NEUTRAL": {
        "high": [
            "Hmm, that’s quite something! Tell me more. 🤔",
            "Oh, that’s interesting! Could you explain more?",
            "That’s a deep thought! Let’s explore it. 🌍"
        ],
        "medium": [
            "I see. Can you elaborate a little?",
            "Hmm, interesting! What do you think about it?",
            "Got it! What else is on your mind?"
        ],
        "low": [
            "Okay, I hear you. 😊",
            "Alright! Anything else you'd like to share?",
            "Hmm, tell me more. 🤖"
        ]
    }
}

def analyze_sentiment(text):
    """Analyze sentiment and return chatbot's response."""
    result = sentiment_pipeline(text)
    sentiment_label = result[0]['label'].upper()
    confidence_score = round(result[0]['score'], 2)

    # Determine response intensity
    if confidence_score >= 0.85:
        intensity = "high"
    elif confidence_score >= 0.60:
        intensity = "medium"
    else:
        intensity = "low"

    # Select response based on intensity
    sentiment_response = random.choice(responses.get(sentiment_label, {}).get(intensity, ["I'm not sure how to respond. 🤖"]))

    return sentiment_response, sentiment_label, confidence_score

def speak(text):
    """Make the chatbot speak the response."""
    engine.say(text)
    engine.runAndWait()

def chatbot():
    """Run chatbot in the terminal with enhanced UI."""
    print(Fore.CYAN + "\n🤖 Welcome to the World of Mr.SentiBot! (Type 'exit' to quit)\n" + Style.RESET_ALL)

    while True:
        user_input = input(Fore.YELLOW + "👤 You: " + Style.RESET_ALL)
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(Fore.GREEN + "🤖 Chatbot: Goodbye! Have a wonderful day! 👋" + Style.RESET_ALL)
            speak("Goodbye! Have a wonderful day!")
            break

        bot_reply, sentiment, confidence = analyze_sentiment(user_input)

        # Apply colors based on sentiment
        if sentiment == "POSITIVE":
            color = Fore.GREEN
        elif sentiment == "NEGATIVE":
            color = Fore.RED
        else:
            color = Fore.BLUE

        print(color + f"🤖 Chatbot: {bot_reply} (Confidence: {confidence})\n" + Style.RESET_ALL)
        
        # Speak the chatbot's response
        speak(bot_reply)

if __name__ == "__main__":
    chatbot()
