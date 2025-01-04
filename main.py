from string import ascii_lowercase

def character_counter(string):
    print("Counting characters...")
    lowered = string.lower()
    count = {}
    for word in lowered:
        if word in count:
            count[word] += 1
        else: count[word] = 1

    return count

def main():
    book = "frankenstein"#input("Enter book title: ").lower()
    length = 0
    try:
        with open(f"books/{book}.txt") as f:
            file_contents = f.read()
        #print(file_contents)
        print("Counting words...")
        words = file_contents.split()
        for word in words:
            length += 1
        character_count = character_counter(file_contents)
        print(f"--- Begin report of books/{book}.txt ---")
        print(f"There are {length} words!\n")
        
        for letter in ascii_lowercase:
            print(f"The letter '{letter}' was found {character_count[letter]} times.")
        print(f"\n--- End of report ---")
    except Exception as e:
        print(f"Error: {e}")


    

main()
