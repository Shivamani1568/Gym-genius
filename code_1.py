# Import necessary modules
import json
from datetime import datetime

# Create an empty list to store exercise logs
exercise_logs = []

# Define a function to add a new exercise log
def add_log():
    # Ask the user for details about the exercise
    exercise_type = input("Enter exercise type: ")
    duration = input("Enter exercise duration (in minutes): ")
    notes = input("Enter any notes (optional): ")

    # Create a dictionary to represent the exercise log
    log = {
        "type": exercise_type,
        "duration": duration,
        "date": str(datetime.now()),
        "notes": notes
    }

    # Add the log to the list of exercise logs
    exercise_logs.append(log)
    print("Log added successfully!")

# Define a function to view all exercise logs
def view_logs():
    # Loop through each log and print its details
    for i, log in enumerate(exercise_logs, start=1):
        print(f"\nLog {i}:")
        print(f"Type: {log['type']}")
        print(f"Duration: {log['duration']} minutes")
        print(f"Date: {log['date']}")
        print(f"Notes: {log['notes']}\n")

# Define a function to save exercise logs to a file
def save_logs_to_file():
    # Open a file in write mode and store the exercise logs in JSON format
    with open("exercise_logs.json", "w") as file:
        json.dump(exercise_logs, file)

# Define a function to load exercise logs from a file
def load_logs_from_file():
    # Use a try-except block to handle file not found error
    try:
        # Open a file in read mode and load exercise logs from JSON format
        with open("exercise_logs.json", "r") as file:
            exercise_logs = json.load(file)
    except FileNotFoundError:
        # If the file is not found, initialize an empty list
        exercise_logs = []

# Define the main function that controls the program flow
def main():
    # Load existing exercise logs from a file
    load_logs_from_file()

    # Start an infinite loop for the main menu
    while True:
        # Display the main menu options
        print("\nExercise Logging Application")
        print("1. Add Log")
        print("2. View Logs")
        print("3. Save and Quit")

        # Ask the user to choose an option
        choice = input("Enter your choice: ")

        # Process the user's choice
        if choice == "1":
            add_log()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            # Save exercise logs to a file and exit the program
            save_logs_to_file()
            print("Logs saved. Exiting program.")
            break
        else:
            # Handle an invalid choice
            print("Invalid choice. Please try again.")

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function to start the program
    main()
