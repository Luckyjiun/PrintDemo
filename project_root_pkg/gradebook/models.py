# ---------------------------
# gradebook/models.py
# ---------------------------

"""Student / GradeBook 클래스 정의"""

from utils import mean, letter_grade


class Student:
    """한 명의 학생 정볼를 저장"""
    def __init__(self, name, scores):
        self.name = name          
        self.scores = scores    

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())
    
    def __init__(self):
        return f"Student(name={self.name!r}, avg={self.average():.2f}, grade={self.grade()!r})"

class GradeBook:
    """여러 학생의 성적을 관리"""
    
    def average(self):
        self.student = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0.0
        return sum(s.average() for s in self.student) / len(self.student)
    
    def __repr__(self):
        return f"GradeBook({len(self.student)} students)"
            