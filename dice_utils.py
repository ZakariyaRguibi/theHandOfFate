from d20 import roll

# formating the rolls output
def format_roll(dice_command, rerolls=1):
    # this is basically me being lazy to add another case to check if the command has a plus in it or not lol
    rolls = []
    results = ""
    rrtotal = 0
    for i in range(0, rerolls):
        rolls.append(roll(dice_command))
        results = results + str(rolls[i]) + "\n"
        rrtotal = rrtotal + rolls[i].total
    header = "**Rolling...:**\n"
    tail = "**Total:** " + str(rrtotal)
    return header + results + tail
