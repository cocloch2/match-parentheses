# read file
with open("test.txt") as file:
    # Creates string to store mismatched lines
    mismatchedLines = ''
    # iterates through lines
    for line in file:
        #set match counters to 0
        brackets=0
        parentheses=0
        carrots=0
        braces=0
        #iterates through characters in each line
        for char in line:
            #increment match counters
            if char == "(":
                parentheses+=1
            elif char == ")":
                parentheses-=1
            elif char == "[":
                brackets+=1
            elif char == "]":
                brackets-=1
            elif char == "{":
                braces+=1
            elif char == "}":
                braces-=1
            elif char == "<":
                carrots+=1
            elif char == ">":
                carrots-=1
        # Add lines to mismatched lines if it's mismatched
        if brackets != 0 or braces != 0 or carrots != 0 or parentheses != 0:
            mismatchedLines += line
    # create output file
    with open('output.txt', 'w') as output:
        # write mismatched lines to output file
        output.write(mismatchedLines)