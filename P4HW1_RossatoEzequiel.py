# CTI-110
# P4HW1 - Score List
# Ezequiel Rossato
# 4/17/2023
#
scoreAmnt = int(input("How many scores do you want to enter? "))
count = 0
for count in range(scoreAmnt):
    count +=1
    Score = int(input(f'Enter score # {count} : '))
    if Score >= 0 and Score <= 100:
        continue
    else:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        Score = int (input(f'Enter score # {count} again: '))
    scoreList[count] = Score
        
print("------------Results------------")
lowest = min(scoreList)
avrg = scoreList / len(scoreList)
if avrg >= 90:
    grade = 'A'
elif avrg >= 80:
    grade = 'B'
elif avrg >= 70:
    grade = 'C'
else:
    grade = 'D'
print(f'{"Lowest Score : ":<20}{lowest}')
print(f'{"Lowest Score : ":<20}{lowest}')
