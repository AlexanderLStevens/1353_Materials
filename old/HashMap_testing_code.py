from old.hash_map import HashSet

def f(word:str)->str:# act like a hash sort our word!!!!
    letter_list=[]
    for letter in word:
        letter_list.append(letter.lower())
    sorted_letter_list=sorted(letter_list)
    sorted_word=''.join(sorted_letter_list)
    return sorted_word


def main():
    
    filename="testing_text.txt"
    wordlist=[]

    with open(filename, "r") as a_file:
        for line in a_file:
            word = line.strip()
            wordlist.append(word)
    
    map = {}
    for word in wordlist:
        key=f(word) #yay!
        if key in map:
            map[key].append(word)
        else:
            map[key]=[word]

    print(map)


if __name__ == "__main__":
    main()