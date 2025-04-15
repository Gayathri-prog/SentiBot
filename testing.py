import pandas as pd
from transformers import pipeline
from sklearn.metrics import accuracy_score

sentiment_pipeline = pipeline("sentiment-analysis")
df = pd.read_csv("chat_dataset.csv")  #Add ur CSV file
predicted_sentiments = []
for text in df["message"]:
    result = sentiment_pipeline(text)
    predicted_label = result[0]["label"].upper()
    predicted_sentiments.append(predicted_label)
    
df["Predicted Sentiment"] = predicted_sentiments


true_labels = df["sentiment"].str.upper()   # Calculate Accuracy
accuracy = accuracy_score(true_labels, predicted_sentiments)

print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")
