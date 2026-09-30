
#make a program to take notes and search the notes with keywords  whenever required


import json
import os
from datetime import datetime

FILENAME = "notes.json"

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_notes():
    if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

def save_notes(notes_data):
    with open(FILENAME, "w") as f:
        json.dump(notes_data, f, indent=4)

def add_note():
    content = input("Enter your note: ").strip()
    if not content:
        print("Empty note discarded.")
        return
    notes_data = load_notes()
    timestamp = get_timestamp()
    notes_data[timestamp] = content
    
    save_notes(notes_data)
    print(f"Saved note under [{timestamp}]")

def view_notes():
    notes_data = load_notes()
    if not notes_data:
        print("No notes found.")
        return
    print("\n--- All Notes ---")
    for timestamp, text in notes_data.items():
        print(f"[{timestamp}] {text}")
    print("-----------------\n")


def search_notes():
    notes_data = load_notes()
    if not notes_data:
        print("No notes found after search.")
        return
    query = input("Enter word or date to search: ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return
    
    matches = {}
    for timestamp, content in notes_data.items():
        if query in timestamp.lower() or query in content.lower():
            matches[timestamp] = content
    
    if matches:
        print(f"\n--- Found {len(matches)} matching note(s) ---")
        for timestamp, content in matches.items():
            print(f"[{timestamp}] {content}")
        print("----------------------------------------\n")
    else:
        print(f"No notes found matching '{query}'.")


while True:
    print("1. Add a note")
    print("2. View all notes")
    print("3. Search notes (by word or date)")
    print("4. Exit")
    
    choice = input("Enter your choice --> ").strip()
    
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please enter 1, 2, 3, or 4.\n")

