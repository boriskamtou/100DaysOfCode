#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt

# Get list of names
with open("Input/Names/invited_names.txt") as file:
    contents = file.read()
    list_names = contents.split("\n")

    # for name in list_names:
    #     with open("Output/ReadyToSend/letters" mode="w") as file:




#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp