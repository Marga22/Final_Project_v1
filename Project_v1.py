class Bond(object):
    def __init__(self, InitialInv, Principal, Price, InterestRate, maturity):
        self.InitialInv = InitialInv
        self.Principal = Principal
        self.Price = Price
        self.InterestRate = InterestRate
        self.maturity = maturity

    def MinPrice(self):
        min(Price) = Price
        return Price



class LT_Bond(Bond):
    def giveGrades(self):
        for student in self.studentsList:
            student.gradeStudent(self.teacher)
        for index, student in enumerate(self.studentsList):
            if index %2 ==0:
                if index+1 < len(self.studentsList):
                    student.grade = (student.grade + self.studentsList[index+1].grade)/2
                    else:
                        student.grade = self.studentsList[index-1].grade


class ST_Bond(Bond):
    def giveGrades(self):
        for student in self.studentsList:
            student.gradeStudent(self.teacher)
