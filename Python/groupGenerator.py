import random
#todo input validation 
#limit groups parameters to no larger than number of students and no smaller than 1

def inputInt(prompt):
    success = False
    while (not success):
        groupCount = input(prompt)
        try:
            groupCount = int(groupCount)
            success = True
        except:
            print("[ERROR] Input must be an integer")
    return groupCount
    
def buildGroupsByGroupCount(students, groupCount):
    groupSize = len(students)//groupCount
    results = []
    for i in range(groupCount):
        results.append([])
    groupNumber = 0
    while (len(students)) > 0:
        randomNumber = random.randint(0,(len(students)-1))
        results[groupNumber].append(students[randomNumber])
        students.pop(randomNumber)
        if groupNumber == groupCount-1:
            groupNumber = 0
        else:
            groupNumber += 1
        
    return results

def buildGroupsBySize(students, groupSize):
    results = []
    index = 0
    while len(students) > 0:
        if len(students) > groupSize:
            results.append([])
            for i in range(groupSize):
                randomNumber = random.randint(0,(len(students)-1))
                results[index].append(students[randomNumber])
                students.pop(randomNumber)
        else:
            results.append(students)
            students = []
        index += 1
        print(results)
    return results


def main():
    rawStudentNames = input("please enter all student names, separate names with a comma\n")
    students = rawStudentNames.split(",")
    howToGroup = inputInt("how would you like to organize your groups?\n1) Number of students in each group\n2) Number of total groups\n")
    print(howToGroup)
    while howToGroup !=1 and howToGroup != 2:
        print("[Error] Invalid option")
        howToGroup = inputInt("how would you like to organize your grous?\n1)Number of students in each group\n2) Number of total groups\n")
        print(howToGroup)

    if howToGroup == 2:
        groupCount = inputInt("please enter the desired number of groups, students will be evenly divided among the given groups ")
        results = buildGroupsByGroupCount(students, groupCount)
    else:
        groupSize = inputInt("how many students should each group have? ")
        results = buildGroupsBySize(students, groupSize)
    print("\n\n")
    for i in range (len(results)):
        print("group ", (i+1), "\n", results[i],"\n")

if __name__ == "__main__":
    main()
