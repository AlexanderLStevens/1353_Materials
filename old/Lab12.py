from old.hash_map import HashSet

def f(word):
	word_list=[str.lower(letter) for letter in word]# ['b', 'a', 'd']
	sorted_words=sorted(word_list) #['a', 'b', 'd']
	key=''.join(sorted_words)
	return key


def main():
    map ={} #HashMap() #python dictionary!!!!!
    file_name="Dictionary.txt"
    with open(file_name, "r") as a_file:
        for line in a_file:
            word = line.strip() 
            key=f(word)
            if key in map:
                word_list=map.get(key)
                word_list.append(word)
            else:
                map[key]=[word]
            

    # for item in map.items(): #this is what the items look like!!!
    #     print(item)
    print(map[f('weakliness')])
    

if __name__ == "__main__":
    main()








#Q1
# Using the data structure you created, print out the anagrams of the word listen. Copy/paste the resulting anagrams into the text box below in alphabetical order, including the word listen, separated by commas.
# (Your code may not print the anagrams in this order, but typing them here in alphabetical order makes it easier for Canvas to autograde your answer.)

# Q2:
#How many anagrams does the word trance have? Include itself.


#Q3:
#Among all words in the dictionary, what is the largest number of anagrams? (include each word itself in its list)

#Q4:
# What is an anagram of the word weakliness?