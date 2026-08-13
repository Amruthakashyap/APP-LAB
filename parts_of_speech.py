parts_of_speech = {
    "Noun": ["dog", "cat", "car", "house"],
    "Verb": ["run", "jump", "swim", "drive"],   
    "Adjective": ["happy", "sad", "fast", "slow"],
    "Adverb": ["quickly", "slowly", "happily", "sadly"]
}
print("Select a word from the following list")
for words in parts_of_speech.values():
    for word in words:
        print(word, end=" , ")
word = input("\nEnter a word: ").lower()
match word:
    case "dog" | "cat" | "car" | "house":
        print(f"{word} is a Noun")
    case "run" | "jump" | "swim" | "drive":
        print(f"{word} is a Verb")
    case default:
        print(f"{word} is not in the list")