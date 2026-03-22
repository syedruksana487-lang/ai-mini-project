# AI Mini Project: Simple Fake News Detection (Basic Version)
news_data = [
    ("Breaking: Market crashes due to global crisis", "REAL"),
    ("You won a lottery of 1 crore! Click here", "FAKE"),
    ("Government announces new education policy", "REAL"),
    ("Earn money fast without doing anything", "FAKE")
]
def predict_news(news):
    fake_keywords = ["lottery", "click", "earn money", "fast"]
    
    for word in fake_keywords:
        if word.lower() in news.lower():
            return "FAKE"
    return "REAL"
print("---- Fake News Detection ----")
user_input = input("Enter a news headline: ")

result = predict_news(user_input)

print("Prediction:", result)
