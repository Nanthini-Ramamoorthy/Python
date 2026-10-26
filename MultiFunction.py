class MultipleFunctions():
    def subfields(list1):
        print('Sub-fields in AI are:')
        for field in list1:
            print(field)

    def checkOddEven():
        num = int(input('Enter a number :'))
        if(num%2 == 1):
            print(num, "is Odd Number")
        else:
            print(num, "is Even Number")

    def checkMarriageEligibility(age, gender):
        print('Your Gender :', gender)
        print('Your Age :', age)
        if(gender == 'Male' and age >= 21):
            status = 'ELIGIBLE'
        elif(gender == 'Female' and age >= 18):
            status = 'ELIGIBLE'
        else:
            status = 'NOT ELIGIBLE'
        return status
    
    def findPercentage(markList):
        i = 0
        total = 0
        maxMarks = len(markList) * 100
        for mark in markList:
            i = i+1
            print('Subject', i, '=', mark)
            total = total + mark
        percentage = (total/maxMarks) * 100
        print("Total : ", total)
        return percentage

    def triangle(h1, h2, breadth):
        areaFormula = (h1 * breadth)/2
        perimeterFormula = h1 + h2 + breadth
        print("Height :", h1, "\nBreadth :", breadth, "\nArea Formula : (height * breadth)/2 \nArea of Triangle :", areaFormula)
        print("Height1 :", h1, "\nHeight2 :", h2, "\nBreadth :", breadth, 
              "\nPerimeter Formula : height1 + height2 + breadth \nPerimeter of Triangle :", perimeterFormula)

                
