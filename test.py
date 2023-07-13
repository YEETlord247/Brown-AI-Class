class Student:
    def __init__(self, name, grade, classes, grades):
        self.name = name
        self.grade = grade
        self.classes = classes
        self.grades = grades
    
    def addCourse(self, course):
        self.classes.append(course)

    def removeCourse(self, course):
        idx = self.classes.index(course)
        del self.classes[idx]
    
    def printInfo(self):
        print(self.name, " is in ", self.grade, "th grade and is taking ", self.classes)


class Teacher:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes
    
    def addCourse(self, course):
        self.classes.append(course)

    def removeCourse(self, course):
        idx = self.classes.index(course)
        del self.classes[idx]
    
    def printCourses(self):
        print(self.classes)

s1 = Student("Henry", 10, ["Biology", "Chemistry", "Physics"], [99, 98, 97])
t1 = Teacher("Benedict Quartey", ["AI", "AI 2"])

s1.printInfo()
s1.addCourse("Math")
s1.printInfo()

