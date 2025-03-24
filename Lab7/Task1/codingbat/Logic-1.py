#alarm clock
def alarm_clock(day, vacation):
    if day in range(1,6):
        if vacation:
            return "10:00"
        else:
            return "7:00"
    else:
        if vacation:
            return "off"
        else:
            return "10:00"
        
#caught_speeding
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2
    
#love6
def love6(a, b):
    return a == 6 or b == 6 or a + b ==6 or abs(a - b) == 6

#in1to10
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return n in range(1,11)
    
#near_ten
def near_ten(num):
    return num % 10 in [0, 1, 2, 8, 9]

#cigar_party
def cigar_party(cigars, is_weekend):
    return cigars >= 40 if is_weekend else cigars in range(40, 61)

#date_fashion
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1
    
#squirrel_play
def squirrel_play(temp, is_summer):
    return temp in range(60, 101 if is_summer else 91)

#sorta_sum
def sorta_sum(a, b):
    return 20 if a + b in range(10, 20) else a + b