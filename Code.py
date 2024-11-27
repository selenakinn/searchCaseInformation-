# Prompt the user to enter the string to search for
word = input("Enter case number or defendant or plaintiff to access the Line Number and Line: ")

# Open the file for reading
def searchCase(word):
    file_path = r"C:\Users\selen\OneDrive\Masaüstü\file organization\courtCases.txt"
    with open(file_path, 'r') as fp:

    # Read all lines in a list
    lines = fp.readlines()
    
    # Iterate through each line
    for line_num, line in enumerate(lines, 1):
        # Check if the string is present on the current line and print the line and line number
        if word in line:
            print(f"'{word}' string exists in file.")
            print('Line Number:', line_num)
            print('Line:', line)
        return 
searchCase(word)
        
