import random
from transformers import pipeline

# Load Sentiment Analysis Model
sentiment_pipeline = pipeline("sentiment-analysis")

# Responses
responses = {
    "POSITIVE": [
        "That sounds amazing! 😊 (Sentiment: Positive)",
        "I'm happy to hear that! 🎉 (Sentiment: Positive)",
        "That's great! Keep it up! 🚀 (Sentiment: Positive)",
        "You're doing awesome! 🌟 (Sentiment: Positive)"
    ],
    "NEGATIVE": [
        "I'm sorry to hear that. 😔 (Sentiment: Negative)",
        "That sounds tough. Want to talk about it? (Sentiment: Negative)",
        "I hope things get better soon. 💙 (Sentiment: Negative)",
        "Stay strong! You're not alone. 💪 (Sentiment: Negative)"
    ],
    "NEUTRAL": [
        "I see. Tell me more! 🤔 (Sentiment: Neutral)",
        "Hmm, interesting! Could you elaborate? (Sentiment: Neutral)",
        "Okay! What else is on your mind? (Sentiment: Neutral)",
        "Got it! Anything else you'd like to share? (Sentiment: Neutral)"
    ]
}

def analyze_sentiment(text):
    """Analyze sentiment and return chatbot's response."""
    result = sentiment_pipeline(text)
    sentiment_label = result[0]['label'].upper()
    confidence_score = round(result[0]['score'], 2)

    sentiment_response = random.choice(responses.get(sentiment_label, ["I'm not sure how to respond to that. 🤖"]))
    
    return sentiment_response, sentiment_label, confidence_score

def chatbot():
    """Run chatbot in the terminal."""
    print("\n🤖 Welcome to the World of Mr.SentiBot (Type 'exit' to quit)\n")

    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            break

        bot_reply, sentiment, confidence = analyze_sentiment(user_input)

        print(f"🤖 Chatbot: {bot_reply} (Confidence: {confidence})\n")

if __name__ == "__main__":
    chatbot()
