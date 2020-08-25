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
        if(bonus != 0):
            return "**Result**: " + dice +"("+ str(flat_value)+") + " + str(bonus)+ "\n**Total**: "+str(dice_value)
        else:
            return "**Result**: " + dice +"("+ str(flat_value)+") \n**Total**: "+str(dice_value)
    else:
        header = "**Rolling...**:\n"
        body=""
        total=0
        for i in range(0,int(rerolls)):
            dice,bonus,dice_value,flat_value = roll_command(dice_command)
            if(bonus != 0):
                body=body+dice +"("+ str(flat_value)+") + " + str(bonus) +" = "+str(dice_value)+"\n"
            else:
                body=body+dice +"("+ str(flat_value)+") = "+str(dice_value)+"\n"
            total=total+dice_value
        tail= "**Total** : " +str(total)

        return header + body + tail