import dice

#a pre treatement function
    #to do: multiple dice rools 
def roll_command(dice_command):
    command=dice_command.split('+')
    dice_value=dice.roll(dice_command)
    flat_value=dice_value
    for i in range(1,len(command)):
        flat_value=flat_value- int(command[i])
    return "**Result**: " + command[0] +"("+ str(flat_value)+")" + "\n **Total**: "+str(dice_value)