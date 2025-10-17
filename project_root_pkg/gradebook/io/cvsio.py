# --------------------------
# gradebook/io/__cvsio__.py
# --------------------------

"""CVs 파일로부터 학생 정보를 읽고 쓰는 모듈"""

import cvs
from ..models import Student


def load_students_from_cvs(path):
    """CVS파일에서 학생 목록을 읽어옴
    CVS 형식: name,score1,score2,score3...
    """
    Students = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = cvs.reader(f)
        for row in reader:
            name = row[0]
            scores = [float(x) for x in row[1:]] 
            Students.append(Student(name, scores))
    return Students