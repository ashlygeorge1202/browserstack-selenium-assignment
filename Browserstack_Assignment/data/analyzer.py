from collections import Counter

def analyze_titles(titles):
    print("\n--- Analyzing Translated Titles ---")
    words = " ".join(titles).lower().split()
    counter = Counter(words)
    repeated = {word: count for word, count in counter.items() if count > 2}

    if repeated:
        print("Words repeated more than twice:")
        for word, count in repeated.items():
            print(f"{word}: {count}")
    else:
        print("No words repeated more than twice.")
