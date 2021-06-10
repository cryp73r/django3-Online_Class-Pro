from .models import Quiz
import datetime, json

def apiCallQuiz(depart):
    raw_json = {}
    if depart=="CS":
        depart = 'Computer Science & Engineering'
    else:
        depart = 'Information Technology'
    try:
        QuizData = Quiz.objects.filter(Department=depart).get(Date=datetime.date.today())
        raw_json["subject"] = QuizData.Subject
        raw_json["subcode"] = QuizData.SubCode
        raw_json["department"] = QuizData.Department
        raw_json["date"] = str(QuizData.Date)
        raw_json["url"] = QuizData.Url
    except:
        raw_json["subject"] = ""
        raw_json["subcode"] = ""
        raw_json["department"] = ""
        raw_json["date"] = ""
        raw_json["url"] = ""

    return json.dumps(raw_json)