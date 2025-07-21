def sentiment_analysis():
    positive_words = ["good", "happy", "excellent", "amazing", "love", "great", "wonderful", "joy", "fantastic",
                      "positive"]
    negative_words = ["bad", "sad", "terrible", "awful", "hate", "poor", "horrible", "depressing", "negative", "worse"]


    paragraph = input("Enter a paragraph: ").lower()


    words = paragraph.split()

    
    sentiment_score = 0


    for word in words:
        if word in positive_words:
            sentiment_score += 1
        elif word in negative_words:
            sentiment_score -= 1
        else:
            sentiment_score += 0

    return sentiment_score



result = sentiment_analysis()
print(f"Sentiment Score: {result}")
