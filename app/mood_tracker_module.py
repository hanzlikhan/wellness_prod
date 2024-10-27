# mood_tracker_module.py
from transformers import pipeline

def initialize_sentiment_analyzer():
    return pipeline("sentiment-analysis")

def analyze_user_mood(text, analyzer):
    result = analyzer(text)
    sentiment = result[0]
    return sentiment['label'], sentiment['score']
