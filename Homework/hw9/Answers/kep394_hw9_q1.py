class Student:
    def __init__(self, name, NYU_id, net_id):
        self.name = name
        self.NYU_id = NYU_id
        self.net_id = net_id
        self.grades_list = []

    def add_grade(self, catalog_name, grade):
        self.grades_list.append((catalog_name, grade))

    def average(self):
        count = 0
        sum = 0
        for i in self.grades_list:
            if str(i[1]).isnumeric():
                sum += int(i[1])
                count += 1
        return round(sum/count)


    def get_email(self):
        return str(self.net_id) + "@nyu.edu"

def load_students(students_data_filename):
    fileIn = open(students_data_filename, "r")
    header = (fileIn.readline()).split(",")
    student_lst = []
    for i in fileIn:
        line = i.split(",")
        student = Student(line[1], line[0], line[2])
        for j in range(3, 10):
            if line[j].isnumeric():
                student.add_grade(header[j], int(line[j]))
        student_lst.append(student)
    fileIn.close()
    return student_lst


def generate_performance_report(students_lst, out_filename):
    fileOut = open(out_filename, "w")
    print("NYU ID, Average", file = fileOut)
    for student in students_lst:
        average = str(student.average())
        NYU_id = student.NYU_id
        print(NYU_id,",", average, sep="", file = fileOut)

def generate_course_mailing_list(catalog_name, student_lst, out_filename):
    fileOut = open(out_filename, "w")
    exists = False
    for student in student_lst():
        for i in student.grades_list:
            if i[0] == catalog_name:
                exists = True
        if exists == True:
            email = str(student.get_email())
            print(email, file = fileOut)

def main():
    generate_performance_report(load_students("hw9 - students grades.csv"), "performance report.csv")
    courseList = ["CS-UY 1114", "MA-UY 1024", "EG-UY 1001", "EG-UY 1003", "CS-UY 1122", "CS-UY 1134", "MA-UY 1124"]
    for course in courseList:
        generate_course_mailing_list(course, student_lst, str(course + "mailing list.csv"))


main()