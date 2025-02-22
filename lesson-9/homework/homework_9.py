class Students():
    x = 0

    def __init__(self, name):
        self.name = name

        Students.x += 1
    def pr_count(self):
        print(Students.x)

student1 = Students('John')
student2 = Students('Bob')
student2.pr_count()
