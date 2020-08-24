import dice

#a pre treatement function
    #to do: multiple dice rools 
def roll_command(dice_command):
    command=dice_command.split('+')
    dice_value=dice.roll(dice_command)
    flat_value=dice_value
    bonus=0
    for i in range(1,len(command)):
        temp=int(command[i])
        flat_value=flat_value - temp
        bonus=bonus + temp
    return  command[0],bonus,dice_value,flat_value


#formating the rolls output
def format_roll(dice_command,rerolls = 1):
    #this is basically me being lazy to add another case to check if the command has a plus in it or not lol
    dice_command= dice_command +"+0"
    if rerolls == 1: 
        dice,bonus,dice_value,flat_value = roll_command(dice_command)
        return "**Result**: " + dice +"("+ str(flat_value)+") + " + str(bonus)+ "\n**Total**: "+str(dice_value)
    else:
        print()