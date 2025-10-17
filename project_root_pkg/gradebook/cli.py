# --------------------------
# gradebook/__cli__.py
# --------------------------

"""명령형 실행 인터페이스 (CLI)"""

from .models import Student, GradeBook
from .io.cvsio import load_students_from_cvs


def run_cli():
    """터미널에서 실행할 간단한 CLI"""
    print("📘GradeBook CLI 실행중...")

    # CVS 파일로부터 데이터 불러오기 (예시)
    try:
        students = load_students_from_cvs("students.cvs")
    except FileNotFoundError:
        print("students.cvs파일이 없습니다. 기본 데이터 사용.")
        students = [
            students("Alice", [90, 85, 92]),
            students("Bob", [70, 75, 68]),
                   
        ]
          
       
    gb = GradeBook()
    for s in students:
        gb.add_students(s)
        
    print(f"\n전체 반 평균 점수: {gb.class_average():.2f}\n")
    for s in gb.students:
        print(f"{s.name}: 평균={s.average():.1f}\n")