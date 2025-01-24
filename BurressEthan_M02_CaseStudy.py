def main():
    print("Student GPA Qualifier App\n") 
    # Display an introduction message for app functionality

    while True:
        # Ask for student's last name
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ").strip() # Prompt for user's entry
        if last_name.upper() == 'ZZZ':
            print("Exiting the app. Goodbye!")
            break

        # Ask for student's first name
        first_name = input("Enter student's first name: ").strip()

        # Ask for student's GPA
        try:
            gpa = float(input("Enter student's GPA: ")) # Converts GPA input into floatand handles non-numeric inputs
        except ValueError:
            print("Invalid input. Please enter a numeric GPA.\n")
            continue

        # Test for Dean's List and Honor Roll
        if gpa >= 3.5: # Check if GPA qualifies for the Dean's list
            print(f"{first_name} {last_name} has made the Dean's List!\n")
        elif gpa >= 3.25: # Check if GPA qualifies for the Honor Roll
            print(f"{first_name} {last_name} has made the Honor Roll!\n")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.\n")

# Run the application
if __name__ == "__main__":
    main()