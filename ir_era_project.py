def ir_era(era, ip, from_first, from_second, from_third, pitcher_type):
    #calculates games pitched from ip paramenter
    gp = ip / 9
    #calculates amount of earned runs; might need to be a whole number
    er = gp * era
    #calculates how many of the earned runs were not due to second pitcher
    f_er = er - (from_first + from_second + from_third)
    #calculates a new earned runs total after accounting for new metric specifications
    ir_er = f_er + (from_first * .25) + (from_second * .50) + (from_third * .75)
    #calculates the new era value, or irERA, from the new total earned runs and previous games played
    ir_era_calc = ir_er / gp
    #returns and prints the new statistic
    return ir_era_calc
    print(ir_era_calc)

brad_stats = ir_era(3.94, 158.66, 3, 5, 6, "SP")
print(brad_stats)