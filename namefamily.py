import math

class Student:
    
    name = ""
    family = ""
    
    # ??? Family 
    def __init__(self, name, family, courseMarks={}):
        self.name = name
        self.family = family
        self.courseMarks = courseMarks


    def addCourseMark(self, course, mark):
        # Modify base code by putting mark in 
        # array to append to a list of values 

        if course in self.courseMarks:
            self.courseMarks[course].append(mark)

        else:
            self.courseMarks[course] = [mark]         

    #def courseAverage(self, course):
    #    math.fsum(self.courseMarks[course])

    def average(self):
        t_average = []

        if self.courseMarks == {}:
            return 0

        else:
            for course in self.courseMarks:
                t_average = t_average + self.courseMarks[course]

            return math.fsum(t_average)/len(t_average)
        
        



