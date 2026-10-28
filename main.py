def clean_memory(text):
    cleaned = text.strip().lower()
    return cleaned

def main():
    print("=== AI Memory Lab ===")

    memory = input("Enter a memory: ")

    cleaned_memory = clean_memory(memory)

    print("Cleaned memory:", cleaned_memory)


if __name__ == "__main__":
    main()