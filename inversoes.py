# reverse_examples.py

def reverse_chars(s: str) -> str:
    return s[::-1]

def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])

if __name__ == "__main__":
    sample = "olá mundo exemplo"
    print("Original: ", sample)
    print("Invertendo caracteres:", reverse_chars(sample))
    print("Invertendo palavras:  ", reverse_words(sample))