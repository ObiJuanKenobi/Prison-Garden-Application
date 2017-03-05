import MySQLdb

class DataAccess:
    _connection = None
    _cursor = None

    #Establish DB connection on instantiation of a new DataAccess object
    def __init__(self):
        self._connection = MySQLdb.Connection(host = "sddb.ece.iastate.edu", port = 3306, user = "may1713", passwd="gawrA75Nac!&", db="may1713_PrisonGardenApp")
        self._cursor = self._connection.cursor()

    #Close the connection when this object is deleted or falls out of scope
    def __del__(self):
        self._cursor.execute("COMMIT")
        self._connection.close()

    def addUser(self, username, password, firstname, lastname):
        exists = cursor.execute("SELECT Username FROM Users WHERE Username = %s", [username])
        if not exists:
            self._cursor.execute("INSERT into Users (Username, Password, First_Name, Last_Name) values (%s, PASSWORD(%s), %s, %s)", (username, password, firstname, lastname))
            return True
        else:
            return False

    def addCourse(self, coursename, courseorder, courseHTMLpath):
        exists = self._cursor.execute("SELECT Course_Name FROM Courses WHERE Course_Name = %s", [coursename])
        if exists:
            self._cursor.execute("UPDATE Courses SET Course_Order = %s, Course_HTML_Path = %s WHERE Course_Name = %s", (courseorder, courseHTMLpath, coursename))
        else:
            self._cursor.execute("INSERT into Courses (Course_Name, Course_Order, Course_HTML_Path) values (%s, %s, %s)", (coursename, courseorder, courseHTMLpath))

    def addLesson(self, coursename, lessonname, lessonfilepath):
        exists = self._cursor.execute("SELECT Lesson_Name FROM Lessons WHERE Lesson_Name = %s", [lessonname])
        if exists:
            self._cursor.execute("UPDATE Lessons SET Lesson_File_Path = %s WHERE Lesson_Name = %s", (lessonfilepath, lessonname))
        else:
            self._cursor.execute("INSERT into Lessons (Course_Name, Lesson_Name, Lesson_File_Path) values (%s, %s, %s)", (coursename, lessonname, lessonfilepath))

    def getLesson(self, coursename, lessonname):
        self._cursor.execute("SELECT Lesson_File_Path FROM Lessons WHERE Course_Name = %s AND Lesson_Name = %s", (coursename, lessonname))
        lesson = ""
        for(Lesson_File_Path) in self._cursor:
            lesson = Lesson_File_Path
        return lesson[0]

    def addQuiz(self, coursename, questions):
        for question in questions:
            self._cursor.execute("INSERT into Quiz_Questions (Question_Text, Course_Name) values (%s, %s)", (question._Text, coursename))
            questionID = self._cursor.lastrowid
            for answer in question._Answers:
                self._cursor.execute("INSERT into Quiz_Answers (QuestionID, Answer_Text, IsCorrect) values (%s, %s, %s)", (questionID, answer._Text, answer._IsCorrect))

    def getQuizQuestions(self, coursename):
        self._cursor.execute("SELECT q.QuestionID as id, q.Question_Text as question, a.Answer_Text as answer, a.Is_Correct as correct FROM Quiz_Questions q, Quiz_Answers a WHERE q.Course_Name = %s AND q.QuestionID = a.QuestionID;", [coursename])
        
        results = self._cursor.fetchall()
        questions = {};
        for row in results:
            id = row[0];
            question = row[1];
            answer = row[2];
            correct = row[3];
            
            if id in questions:
                questions[id]["answers"].append({"answer": answer, "correct": bool(int.from_bytes(correct, byteorder='big'))});
            else:
                questions[id] = {"question": question, "id": id};
                questions[id]["answers"] = [{"answer": answer, "correct": bool(int.from_bytes(correct, byteorder='big'))}];
        
        questionsArr = [];
        for id in questions:
            questionsArr.append(questions[id])
        return questionsArr;
        
    def addQuizAttempt(self, coursename, username, passed):
        exists = self._cursor.execute("SELECT Attempts FROM Quiz_Attempts WHERE Course_Name = %s AND Username = %s", (coursename, username))
        if exists:
            self._cursor.execute("UPDATE Quiz_Attempts SET Attempts = Attempts + 1, Passed = %s WHERE Course_Name = %s AND Username = %s", (passed, coursename, username))
        else:
            self._cursor.execute("INSERT into Quiz_Attempts (Course_Name, Username, Attempts, Passed) values (%s, %s, %s, %s)", (coursename, username, 1, passed))

#Class for passing quiz questions to the DB in a convenient object
class QuizQuestion:
    _Text = None
    _Answers = None

    def __init__(self):
        _Text = ""
        _Answers = ["", "", "", ""]

#Class for passing quiz answers to the DB in a convenient object
class QuizAnswer:
    _Text = None
    _IsCorrect = None

    def __init__(self):
        _Text = ""
        _IsCorrect = False