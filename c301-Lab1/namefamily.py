import math

class Student:
    
    name = ""
    family = ""
    
    def __init__(self, name, family, courseMarks={}):
        self.name = name
        self.family = family
        self.courseMarks = courseMarks

    def addCourseMark(self, course, mark):
        # Modify base code by putting mark in 
        # array to append to a list of values 

        """
        >>> a = Student("John", "Smith")

        >>> a.courseMarks
        {}

        >>> a.addCourseMark("CMPUT410", 75)
        >>> a.courseMarks["CMPUT410"]
        75

        >>> a.addCourseMark("CMPUT301", 85)
        >>> a.courseMarks["CMPUT301"]
        85

        >>> a.courseMarks["CMPUT410"]
        75
        >>> a.addCourseMark("CMPUT410", 95)
        >>> a.courseMarks["CMPUT410"]
        95
        >>> a.courseMarks["CMPUT301"]
        85

        """
        self.courseMarks[course] = mark         


    def average(self):
        """
        >>> b = Student("Happy", "Smith", {})
        >>> b.courseMarks
        {}

        >>> b.average()
        0

        >>> b.addCourseMark("CMPUT410", 75)
        >>> b.average()
        75.0

        >>> b.addCourseMark("CMPUT301", 85)
        >>> b.average()
        80.0

        >>> b.addCourseMark("CMPUT310", 50)
        >>> b.average()
        70.0

        """
        t_average = []

        if self.courseMarks == {}:
            return 0

        else:
            for course in self.courseMarks:
                t_average = t_average + [self.courseMarks[course]]

            return math.fsum(t_average)/len(t_average)
        
        



