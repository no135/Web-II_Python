def wordcount(text):
    words = text.lower().split()
    wordcount ={}
    
    for word in words:
        if word:
            wordcount[word] = wordcount.get(word, 0) + 1
    
    totalwords = sum (wordcount.values())
    mostfrequent = max(wordcount, key=wordcount.get)

    print(f"total word count :{totalwords}")
    print("word frequency:")
    for word,count in wordcount.items():
        print(f"{word}: {count}")
    print(f"most frequent: {mostfrequent}  ")

def main():
    print("words counter")
    text = input("please enter the paragraph: ")
    wordcount(text)

if __name__ == "__main__":
    main()