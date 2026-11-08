# 1----------
def count_passing_students(grades:list[int],passingGrade:int)->int:
    count=0
    for ball in grades:
        if ball >= passingGrade:
            count += 1
    return count
grades=[45,60,75,30,90]
passingGrade=60
print(count_passing_students(grades,passingGrade))