userinput = str(input("Enter a Phrase: ")) # take the input pharse from user
t = userinput.split() # Use split() for splitting sentense
s = " "  
for i in t:w  # Run a loop for splitting every word in sentence and making first letter of each word capital
        s = s+str(i[0]).upper()
    
print("Acronym for"+userinput+ " is"+s+".") # Print the acronym of the phrase

