def clean_memory(text):
    cleaned = text.strip().lower()
    return cleaned

def add_memory(memories, text):

    cleaned = clean_memory(text)

    if not cleaned:
        return False

    memory = {
        "id": len(memories) + 1,
        "content": cleaned
    }

    memories.append(memory)

    return True

def view_memories(memories):

    if not memories:
        print("No memories found.")
        return 
    
    for memory in memories:
        print(f"[{memory['id']}] {memory['content']}")
    

def main():

    memories = []

    while True:

        print("\n=== AI MEMORY LAB ===")
        print("1. Add Memory")
        print("2. View Memories")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter a memory: ")
            if add_memory(memories, text):
                print("Memory saved successfully!")
            else:
                print("Cannot save an empty memory.")

        elif choice == "2":
            view_memories(memories)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()