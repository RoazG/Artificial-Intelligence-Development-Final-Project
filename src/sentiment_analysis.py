from transformers import pipeline

# Load pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)
    return result[0]

if __name__ == "__main__":
    print("Financial News Sentiment Analyzer")
    user_input = input("Enter a financial news headline: ")
    prediction = analyze_sentiment(user_input)
    
    print("\nSentiment:", prediction["label"])
    print("Confidence:", round(prediction["score"], 3))
