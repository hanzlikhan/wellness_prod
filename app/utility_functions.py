# utility_functions.py
import os
from datetime import datetime

def save_journal_entry(entry_type, text):
    with open("data/user_journal_entries.txt", "a") as f:
        f.write(f"{datetime.now()} - {entry_type}: {text}\n")
