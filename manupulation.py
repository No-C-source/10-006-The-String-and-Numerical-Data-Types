#Pseudocode
#Ask the user to enter a sentence using the input() method and save the user’s response as str_manip.
#Use this string value and calculate the length.
#Find the last letter in str_manip sentence. Replace every occurrence of this letter in str_manip with ‘@’.  
#Print the last 3 characters in str_manip backwards.
#Create a five-letter word that is made up of the first three characters and the last two characters in str_manip. 


#Python code
str_manip = input("Please enter a sentence: ")
print(f"You entered: {str_manip}")
print(len(str_manip))
str_manip = str_manip.replace("-1", "@")
last_letter = str_manip.rstrip()[-1]
print(f"Last letter in str_manip: {last_letter}")
str_manip = str_manip.replace(last_letter, "@")
print(f"str_manip after replacing last letter with '@': {str_manip}")
first_three = str_manip[:3]
last_two = str_manip[-2:]
five_letter_word = first_three + last_two
print("Five-letter word:", five_letter_word)