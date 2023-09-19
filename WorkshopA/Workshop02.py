def InputStudentDetail() :
    StudentID = input('รหัสนักเรียน : ')
    StudentName = input('ชื่อนักเรียน : ')
    return StudentID, StudentName

def InputScore() :
    Score1 = float(input('คะแนนเเรก : '))
    Score2 = float(input('คะเเนนที่สอง : '))
    Score3 = float(input('คะเเนนที่สาม : '))
    return Score1, Score2, Score3

def CalMidTermScore(Score1, Score2, Score3, StudentID, StudentName) :
    MidTermScore = (Score1 + Score2 + Score3) / 3
    print(f'รหัสคุณ {StudentID} ชื่อคุณคือ {StudentName} คะเเนนกลลางภาคคุณคือ{MidTermScore}')

StudentID, StudentName = InputStudentDetail()
Score1, Score2, Score3 = InputScore()
CalMidTermScore (Score1, Score2, Score3, StudentID, StudentName)