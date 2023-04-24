# CTI-110
# P4HW1 - Score List
# Ezequiel Rossato
# 4/17/2023
#
scoreAmnt = int(input("How many scores do you want to enter? "))
count = 0
scoreList = [] 
for count in range(scoreAmnt):
    count +=1
    Score = float(input(f'Enter score # {count} : '))
    if Score >= 0 and Score <= 100:
        scoreList.append(Score)
    else:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        Score = float(input(f'Enter score # {count} again: '))
        scoreList.append(Score)
        
print("------------Results------------")
lowest = min(scoreList)

scoreList2 = scoreList
scoreList2.remove(lowest)

avrg = sum(scoreList2) / len(scoreList2)
if avrg >= 90:
    grade = 'A'
elif avrg >= 80:
    grade = 'B'
elif avrg >= 70:
    grade = 'C'
else:
    grade = 'D'
print(float(f'{"Lowest Score : ":<20}{lowest}'))
count2 = 0
print(float(f'{"Modified List : ":<20}{scoreList2})
printf'{"Score Average: ":<20}{avrg}')
print(f'{"Grade: ":<20}{grade}')
print("-------------------------------")
