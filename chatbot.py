import random
import pyttsx3
from transformers import pipeline
from colorama import Fore, Style, init

init(autoreset=True)

sentiment_pipeline = pipeline("sentiment-analysis")
engine = pyttsx3.init()
responses = {
    "POSITIVE": {
        "high": [
            "Wow, that's fantastic! Keep up the great energy! 🎉 (Sentiment: Positive)",
            "Amazing! I love hearing such great news! 🚀 (Sentiment: Positive)",
            "You're on fire! Keep shining! 🌟 (Sentiment: Positive)"
        ],
        "medium": [
            "That sounds great! 😊 (Sentiment: Positive)",
            "I'm happy to hear that! 🎊 (Sentiment: Positive)",
            "Nice! Keep going strong! 💪 (Sentiment: Positive)"
        ],
        "low": [
            "That's good to hear! 👍 (Sentiment: Positive)",
            "Great! What's next? 😃 (Sentiment: Positive)",
            "Nice! Keep it up! 😊 (Sentiment: Positive)"
        ]
    },
    "NEGATIVE": {
        "high": [
            "Oh no, that sounds really tough. I'm here for you. 💙 (Sentiment: Negative)",
            "I'm really sorry to hear that. You're not alone. 😞 (Sentiment: Negative)",
            "That must be so difficult. Remember, things will get better. 🌿 (Sentiment: Negative)"
        ],
        "medium": [
            "That sounds challenging. Want to talk about it? (Sentiment: Negative)",
            "I'm sorry you're feeling this way. 💔 (Sentiment: Negative)",
            "I hope things get better for you soon. 💙 (Sentiment: Negative)"
        ],
        "low": [
            "I see, that sounds a bit frustrating. 😕 (Sentiment: Negative)",
            "That doesn’t sound great. Hope things improve! 🤞 (Sentiment: Negative)",
            "Stay strong! You've got this. 💪 (Sentiment: Negative)"
        ]
    },
    "NEUTRAL": {
        "high": [
            "Hmm, that’s quite something! Tell me more. 🤔 (Sentiment: Neutral)",
            "Oh, that’s interesting! Could you explain more? (Sentiment: Neutral)",
            "That’s a deep thought! Let’s explore it. 🌍 (Sentiment: Neutral)"
        ],
        "medium": [
            "I see. Can you elaborate a little? (Sentiment: Neutral)",
            "Hmm, interesting! What do you think about it? (Sentiment: Neutral)",
            "Got it! What else is on your mind? (Sentiment: Neutral)"
        ],
        "low": [
            "Okay, I hear you. 😊 (Sentiment: Neutral)",
            "Alright! Anything else you'd like to share? (Sentiment: Neutral)",
            "Hmm, tell me more. 🤖 (Sentiment: Neutral)"
        ]
    }
}

def analyze_sentiment(text):
    """Analyze sentiment and return chatbot's response with explicit sentiment label."""
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

    sentiment_response = random.choice(responses.get(sentiment_label, {}).get(intensity, ["I'm not sure how to respond. 🤖 (Sentiment: Neutral)"]))

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
            farewell = "Goodbye! Have a wonderful day! (Sentiment: Neutral)"
            print(Fore.GREEN + f"🤖 Chatbot: {farewell}" + Style.RESET_ALL)
            speak(farewell)
            break

        bot_reply, sentiment, confidence = analyze_sentiment(user_input)
        if sentiment == "POSITIVE":
            color = Fore.GREEN
        elif sentiment == "NEGATIVE":
            color = Fore.RED
        else:
            color = Fore.BLUE

        print(color + f"🤖 Chatbot: {bot_reply} (Sentiment: {sentiment}, Confidence: {confidence})\n" + Style.RESET_ALL)
        speak(bot_reply)

if __name__ == "__main__":
    chatbot()
