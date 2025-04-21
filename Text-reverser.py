def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def save_to_file(text):
    try:
        with open("reversed_output.txt", "w") as file:
            file.write(text)
        print("Reversed text saved to 'reversed_output.txt'.")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    while True:
        print("\n--- Text Reverser ---")
        print("1. Reverse Characters")
        print("2. Reverse Word Order")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '3':
            print("Goodbye!")
            break

        text = input("Enter text: ").strip()

        if not text:
            print("Error: Empty input. Please enter some text.")
            continue

        if choice == '1':
            result = reverse_characters(text)
            print("Reversed Characters:", result)

        elif choice == '2':
            result = reverse_words(text)
            print("Reversed Words:", result)

        else:
            print("Invalid choice. Please try again.")
            continue

        save = input("Do you want to save the result to a file? (yes/no): ").strip().lower()
        if save == 'yes':
            save_to_file(result)

if __name__ == "__main__":
    main()
