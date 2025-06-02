#Pseudo code:
#Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a single string variable.
#Reprint this sentence as “The quick brown fox jumps over the lazy dog.” using the replace() function to replace every “!” exclamation mark with a blank space. 
#Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” using the upper() function 
#Print the sentence in reverse

#Python code:
single_string =  "The!quick!brown!fox!jumps!over!the!lazy!dog."
single_string = single_string.replace("!", " ")
print(single_string)
print(single_string.upper())
print(single_string[::-1])
