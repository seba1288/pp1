def f(dice):
    for i in str(dice):
        most_row = 0
        count = 0
        range = 0
        for j in str(dice):
            if j == str(len(dice)):
                break
            elif j == dice[j+1]:
                count += 1
        if count > most_row:
            most_row = i
    print( most_row)

     
          


f("5233165554211") 
f("2133") 

