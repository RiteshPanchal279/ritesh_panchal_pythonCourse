# 1. Write a function in Python to count and display the total number of words in a text file “ABC.txt” also count uppercase / lowercase character in same  text file

def upper_lower_words_count():
    file = open("D:/Python course/Questions LAB/Lab question/ABC.txt","r")
    upCount =0
    lowerCount =0
    wordCount=0
    data = file.read() # whole data
    words = data.split() # split by space=" "

    for word in words:
        wordCount+=1

    for letter in data:
        if letter.isupper():
            upCount+=1
        else:
            if letter.islower():
               lowerCount+=1
            
    print("Total Words : ", wordCount)
    print("Total Upper case : ", upCount)
    print("Total Lower case : ", lowerCount)
    
    file.close()
# calling the function 
upper_lower_words_count()



# 2. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.


def print_word():
    file=open("D:/Python course/Questions LAB/Lab question/story.txt","r")

    data=file.read()
    words = data.split()

    for word in words:
        if len(word) < 4:
            print(word,end=" ")

# calling the function 
print_word()