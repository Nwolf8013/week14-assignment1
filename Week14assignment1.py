#Name: Nick Wolf
#week 14 assignment1
#States in alphabetic order

#States file (open, alphabetize, close)
def function1 ():
    #open file
    States_file = open ('statesnames.txt', 'r')

    #readfile alphabetically
    States_alphabet = sorted(States_file.readlines())


    #close file
    States_file.close

    print (States_alphabet)

#Body
function1()
