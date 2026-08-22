class student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avarage marks are",sum/len(self.marks))



s1 = student("arjun", [99, 98, 97])
s1.avg_marks()

s2 = student("sania", [100, 99, 98])
s2.avg_marks()