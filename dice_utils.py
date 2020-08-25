import dice

#a pre treatement function
#it takes a dice command, split it by "+" sign, then roll the original dice and add the bonuses
#returns the original dice command (eg 1d6), the total number of bonuses, the result of the rolls, and the flat value of the dice
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
    dice_type,bonus,dice_value,flat_value = roll_command(dice_command)
    max_dice=dice.roll_max(dice_type)
    min_dice=dice.roll_min(dice_type)
    if rerolls == 1: 
        if(bonus != 0):
            str_bonus="+"+str(bonus)
        else:
            str_bonus=""
        str_flat_value= format_critical(flat_value,min_dice,max_dice)
        return "**Result:** " + dice_type +" ("+ str_flat_value+") " + str_bonus+ "\n**Total**: `"+str(dice_value)+"`"

    else:
        header = "**Rolling...:**\n"
        body=""
        total=0
        if(bonus != 0):
            str_bonus="+"+str(bonus)
        else:
            str_bonus=""
        for i in range(0,int(rerolls)):
            dice_type,bonus,dice_value,flat_value = roll_command(dice_command)
            str_flat_value= format_critical(flat_value,min_dice,max_dice)
            body=body+"1"+dice_type +"("+ str_flat_value +") " + str_bonus +" = `"+str(dice_value)+"`\n"

            total=total+dice_value
        tail= "**Total:** " +str(total)

        return header + body + tail

#make a critical failure or a critical success bold
def format_critical(dice_flat_value,roll_min,roll_max):
    if (dice_flat_value==roll_min[0])or(dice_flat_value==roll_max[0]):
         return "**"+str(dice_flat_value)+"**"
    else:
        return str(dice_flat_value)