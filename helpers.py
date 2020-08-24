#helper file 

#insert a string inside another string in a specific index
def insert_sting_middle(str, word, index):
    if(index == -1):
        print("index not valid")
    else: 
	    return str[:index] + word + str[index:]