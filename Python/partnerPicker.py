import random

def createPartners(students):
    results = [] 
    index = 0
    while len(students) >0:
        if len(students) > 1:
            results.append([])
            for i in range(2):
                randomNumber = random.randint(0,(len(students)-1))
                results[index].append(students[randomNumber])
                students.pop(randomNumber)
        else:
            results[index-1].append(students[0])
            students = []
        index+=1
    return results

def main():
    raw_list = input("please enter student names separated by a comma, press enter when complete\n")
    students = raw_list.split(",")
    partnerList = createPartners(students)
    print(partnerList)

if __name__ == "__main__":
    main()
