# goal_setting_module.py
from transformers import pipeline

def initialize_goal_generator():
    return pipeline("text-generation", model="distilgpt2")  # Using "distilgpt2" instead of "gpt-2"

def suggest_daily_goal(generator):
    response = generator("Suggest a productive daily goal:", max_length=50)
    return response[0]['generated_text']
