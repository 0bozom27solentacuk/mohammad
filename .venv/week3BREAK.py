user_word = input("please enter a word : ").upper()
exit_letter = input("please enter exit letter : ").upper()
positon = 0
while positon < len(user_word):
    if user_word[positon]==exit_letter:
        print("breakin out of loop as encountered termination letter .")
        break
    else:
        print(user_word[positon])
    positon +=1
else:
    print("reached end of word")