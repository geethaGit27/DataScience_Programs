import csv

class Students:
    '''instance variables -> student id and student name'''

    def __init__(self, stu_id, stu_name):

        self.stu_id = stu_id
        self.stu_name = stu_name

    def __repr__(self):

        return f"Students({self.stu_id}, {self.stu_name})"

    def to_list(self):

        return [self.stu_id,self.stu_name]
    
class StudentData:

    def __init__(self, filename = "students.csv"):

        self.filename = filename

    def add_data(self, student):

        with open(self.filename,"a",newline='') as file:

            writer = csv.writer(file)
            writer.writerow(student.to_list())

    def get_data(self):

        students = []

        with open(self.filename,"r", newline='') as file:

            read = csv.reader(file)
            for row in read:
                students.append(row)
            return students
        

sd = StudentData()

s1 = Students(1234,"Geetha")
s2 = Students(1234,"Gita")

sd.add_data(s1)

sd.add_data(s2)

file_data = sd.get_data()

for fd in file_data:

    print(fd)



    

