# CLI-Notes-App
A lightweight, interactive Command Line Interface (CLI) note-taking application written in Python. This tool allows users to quickly record notes, view saved entries, and search through past notes with automatic timestamp tracking and local JSON persistence.

## Overview

The **CLI Notes Manager** provides a distraction-free, terminal-based way to store quick thoughts, reminders, and logs. Every note is saved alongside a readable creation timestamp in a local JSON file (`notes.json`), ensuring your data remains persistent across sessions without requiring a database server.

## Features

* **Add Notes**: Record notes interactively with automatic timestamps (`YYYY-MM-DD HH:MM:SS`).

* **Input Validation**: Automatically rejects and ignores empty note entries.

* **View All Notes**: Inspect all recorded notes chronologically in a clean terminal layout.

* **Keyword & Date Search**: Perform case-insensitive search queries across note contents and timestamps.

* **Local Persistence**: Stores data human-readably in a local `notes.json` file.

* **Zero Third-Party Dependencies**: Runs strictly on standard Python libraries.

## Technologies & Tools Used

* **Language**: [Python 3.x](https://www.python.org/)

* **Built-in Modules**:

  * `json` — Handles serialization and deserialization of notes data.

  * `os` — Verifies file existence and file size before reading.

  * `datetime` — Formats and logs accurate creation timestamps.

* **Storage**: Local JSON file (`notes.json`).

## Steps to Install & Run

### Prerequisites

Ensure you have Python 3 installed on your machine:

```
python --version
# or
python3 --version

```

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your-username/cli-notes-manager.git
   cd cli-notes-manager
   
   ```

2. (Optional) Ensure your script file (e.g., `main.py` or `notes.py`) is located in the root directory.

### Running the Application

Execute the script with Python:

```
python main.py
# or
python3 main.py

```

Upon launch, you will be presented with the interactive menu:

```
1. Add a note
2. View all notes
3. Search notes (by word or date)
4. Exit
Enter your choice -->

```

## Instructions for Testing

Follow these steps to manually test all paths and verify project functionality:

### 1. Test Adding Notes

* Select option `1` and press `Enter`.

* Type a test note (e.g., `Meeting with project lead`) and press `Enter`.

* **Expected Outcome**: Confirmation message `Saved note under [YYYY-MM-DD HH:MM:SS]`.

* Check your directory to confirm `notes.json` is created and contains your note.

### 2. Test Input Validation

* Select option `1` and press `Enter` without typing anything (or just spaces).

* **Expected Outcome**: Terminal displays `Empty note discarded.` and returns to the menu.

### 3. Test Viewing Notes

* Select option `2`.

* **Expected Outcome**: Formatted list displaying all saved timestamps and their corresponding notes.

* If testing on a fresh run with no `notes.json`, verify that `No notes found.` is displayed.

### 4. Test Search Functionality

* Select option `3`.

* **Content Query**: Enter a keyword from a saved note (e.g., `meeting`).

  * **Expected Outcome**: Shows matching note(s) with total count.

* **Date Query**: Enter a date segment (e.g., `2026` or the current month).

  * **Expected Outcome**: Shows notes created matching that timestamp filter.

* **Empty Query**: Press `Enter` without input.

  * **Expected Outcome**: Displays `Search query cannot be empty.`.

* **Non-existent Query**: Enter a query that does not exist (e.g., `xyz999`).

  * **Expected Outcome**: Displays `No notes found matching 'xyz999'.`.

### 5. Test Exit

* Select option `4`.

* **Expected Outcome**: Displays `Goodbye!` and terminates the process cleanly.
