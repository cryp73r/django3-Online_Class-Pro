import json
from .verifyCS import verifyCS
from .models import classdetailcs3334, classdetailcs3132, classdetailcs4142, classdetailcs4344, classdetailcs45
from .groupCS import groupCS


def apiCallCS(odd, wday):
    # IST = pytz.timezone('Asia/Kolkata')
    # wday = datetime.datetime.now(IST).weekday()
    groupA = classdetailcs3132
    groupB = classdetailcs3334
    groupC = classdetailcs45
    if odd:
        groupA = classdetailcs3132
        groupB = classdetailcs3334
    else:
        groupA = classdetailcs4142
        groupB = classdetailcs4344
    raw_json = {'groupA': {'count': {}, 'detail': []}, 'groupB': {'count': {}, 'detail': []}, 'groupC': {'count': {}, 'detail': []}, 'groupD': {'count': {}, 'detail': []}, 'groupE': {'count': {}, 'detail': []}}
    username = ['1', '2', '3', '4', '5']
    timeS = ["09:00", "10:00", "11:00", "12:00", "12:55", "01:35", "02:25", "03:15", "04:05"]
    timeE = ["10:00", "11:00", "12:00", "12:55", "01:35", "02:25", "03:15", "04:05", "04:55"]
    for user in username:
        t_table = verifyCS(user, wday)
        c = 0   # lectures counter
        d = 0   # tutes counter
        e = 0   # labs counter
        temp_list=[]
        i = -1
        for clad in t_table:
            i += 1
            if odd:
                if groupCS(user)=='3':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        raw_json['groupC']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 6):
                            c += 1
                        elif (int(clad) >= 7 and int(clad) <= 14):
                            d += 1
                        elif (int(clad) >= 15 and int(clad) <= 20):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        raw_json['groupC']['detail'].append({
                            'name': "One Hour Quiz",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupC']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                elif groupCS(user)=='4':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        raw_json['groupD']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 6):
                            c += 1
                        elif (int(clad) >= 7 and int(clad) <= 14):
                            d += 1
                        elif (int(clad) >= 15 and int(clad) <= 20):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        raw_json['groupD']['detail'].append({
                            'name': "One Hour Quiz",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupD']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                elif groupCS(user)=='1':
                    if (clad != ' ' and clad != '100'):
                        detail = groupA.objects.get(pk=int(clad))
                        raw_json['groupA']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 6):
                            c += 1
                        elif (int(clad) >= 7 and int(clad) <= 14):
                            d += 1
                        elif (int(clad) >= 15 and int(clad) <= 20):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        raw_json['groupA']['detail'].append({
                            'name': "One Hour Quiz",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupA']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                elif groupCS(user)=='2':
                    if (clad != ' ' and clad != '100'):
                        detail = groupA.objects.get(pk=int(clad))
                        raw_json['groupB']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 6):
                            c += 1
                        elif (int(clad) >= 7 and int(clad) <= 14):
                            d += 1
                        elif (int(clad) >= 15 and int(clad) <= 20):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        raw_json['groupB']['detail'].append({
                            'name': "One Hour Quiz",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupB']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
            else:
                if groupCS(user)=='3':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12' or clad == '18'):
                            raw_json['groupC']['detail'].append([{
                                'name': detail.title,
                                'code': detail.subcode,
                                'teach': detail.subteach,
                                'url': detail.url,
                                'id': detail.meetid,
                                'pwd': detail.password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            },
                            {
                                'name': groupB.objects.get(pk=int(clad)+1).title,
                                'code': groupB.objects.get(pk=int(clad)+1).subcode,
                                'teach': groupB.objects.get(pk=int(clad)+1).subteach,
                                'url': groupB.objects.get(pk=int(clad)+1).url,
                                'id': groupB.objects.get(pk=int(clad)+1).meetid,
                                'pwd': groupB.objects.get(pk=int(clad)+1).password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            }
                            ])
                        else:
                            raw_json['groupC']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        from quizExam.models import Quiz
                        import  datetime, pytz
                        IST = pytz.timezone('Asia/Kolkata')
                        QuizData = Quiz.objects.filter(Department='Computer Science & Engineering').get(Date=datetime.datetime.now(IST).strftime("%Y-%m-%d"))
                        raw_json['groupC']['detail'].append({
                            'name': QuizData.Subject,
                            'code': QuizData.SubCode,
                            'teach': "",
                            'url': QuizData.Url,
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupC']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                elif groupCS(user)=='4':
                    if (clad != ' ' and clad != '100'):
                        detail = groupB.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12' or clad == '18'):
                            raw_json['groupD']['detail'].append([{
                                'name': detail.title,
                                'code': detail.subcode,
                                'teach': detail.subteach,
                                'url': detail.url,
                                'id': detail.meetid,
                                'pwd': detail.password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            },
                            {
                                'name': groupB.objects.get(pk=int(clad)+1).title,
                                'code': groupB.objects.get(pk=int(clad)+1).subcode,
                                'teach': groupB.objects.get(pk=int(clad)+1).subteach,
                                'url': groupB.objects.get(pk=int(clad)+1).url,
                                'id': groupB.objects.get(pk=int(clad)+1).meetid,
                                'pwd': groupB.objects.get(pk=int(clad)+1).password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            }
                            ])
                        else:
                            raw_json['groupD']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        from quizExam.models import Quiz
                        import  datetime, pytz
                        IST = pytz.timezone('Asia/Kolkata')
                        QuizData = Quiz.objects.filter(Department='Computer Science & Engineering').get(Date=datetime.datetime.now(IST).strftime("%Y-%m-%d"))
                        raw_json['groupD']['detail'].append({
                            'name': QuizData.Subject,
                            'code': QuizData.SubCode,
                            'teach': "",
                            'url': QuizData.Url,
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupD']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                elif groupCS(user)=='1':
                    if (clad != ' ' and clad != '100'):
                        detail = groupA.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12' or clad == '18'):
                            raw_json['groupA']['detail'].append([{
                                'name': detail.title,
                                'code': detail.subcode,
                                'teach': detail.subteach,
                                'url': detail.url,
                                'id': detail.meetid,
                                'pwd': detail.password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            },
                            {
                                'name': groupB.objects.get(pk=int(clad)+1).title,
                                'code': groupB.objects.get(pk=int(clad)+1).subcode,
                                'teach': groupB.objects.get(pk=int(clad)+1).subteach,
                                'url': groupB.objects.get(pk=int(clad)+1).url,
                                'id': groupB.objects.get(pk=int(clad)+1).meetid,
                                'pwd': groupB.objects.get(pk=int(clad)+1).password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            }
                            ])
                        else:
                            raw_json['groupA']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        from quizExam.models import Quiz
                        import  datetime, pytz
                        IST = pytz.timezone('Asia/Kolkata')
                        QuizData = Quiz.objects.filter(Department='Computer Science & Engineering').get(Date=datetime.datetime.now(IST).strftime("%Y-%m-%d"))
                        raw_json['groupA']['detail'].append({
                            'name': QuizData.Subject,
                            'code': QuizData.SubCode,
                            'teach': "",
                            'url': QuizData.Url,
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupA']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                elif groupCS(user)=='2':
                    if (clad != ' ' and clad != '100'):
                        detail = groupA.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12' or clad == '18'):
                            raw_json['groupB']['detail'].append([{
                                'name': detail.title,
                                'code': detail.subcode,
                                'teach': detail.subteach,
                                'url': detail.url,
                                'id': detail.meetid,
                                'pwd': detail.password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            },
                            {
                                'name': groupB.objects.get(pk=int(clad)+1).title,
                                'code': groupB.objects.get(pk=int(clad)+1).subcode,
                                'teach': groupB.objects.get(pk=int(clad)+1).subteach,
                                'url': groupB.objects.get(pk=int(clad)+1).url,
                                'id': groupB.objects.get(pk=int(clad)+1).meetid,
                                'pwd': groupB.objects.get(pk=int(clad)+1).password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            }
                            ])
                        else:
                            raw_json['groupB']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 19):
                            d += 1
                        elif (int(clad) >= 20 and int(clad) <= 25):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        from quizExam.models import Quiz
                        import  datetime, pytz
                        IST = pytz.timezone('Asia/Kolkata')
                        QuizData = Quiz.objects.filter(Department='Computer Science & Engineering').get(Date=datetime.datetime.now(IST).strftime("%Y-%m-%d"))
                        raw_json['groupB']['detail'].append({
                            'name': QuizData.Subject,
                            'code': QuizData.SubCode,
                            'teach': "",
                            'url': QuizData.Url,
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupB']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                elif groupCS(user)=='5':
                    if (clad != ' ' and clad != '100'):
                        detail = groupC.objects.get(pk=int(clad))
                        if (clad == '6' or clad == '12'):
                            raw_json['groupE']['detail'].append([{
                                'name': detail.title,
                                'code': detail.subcode,
                                'teach': detail.subteach,
                                'url': detail.url,
                                'id': detail.meetid,
                                'pwd': detail.password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            },
                            {
                                'name': groupB.objects.get(pk=int(clad)+1).title,
                                'code': groupB.objects.get(pk=int(clad)+1).subcode,
                                'teach': groupB.objects.get(pk=int(clad)+1).subteach,
                                'url': groupB.objects.get(pk=int(clad)+1).url,
                                'id': groupB.objects.get(pk=int(clad)+1).meetid,
                                'pwd': groupB.objects.get(pk=int(clad)+1).password,
                                'timeS': timeS[i],
                                'timeE': timeE[i],
                            }
                            ])
                        else:
                            raw_json['groupE']['detail'].append({
                            'name': detail.title,
                            'code': detail.subcode,
                            'teach': detail.subteach,
                            'url': detail.url,
                            'id': detail.meetid,
                            'pwd': detail.password,
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                        if (int(clad) <= 7):
                            c += 1
                        elif (int(clad) >= 8 and int(clad) <= 13):
                            d += 1
                        elif (int(clad) >= 14 and int(clad) <= 16):
                            if clad not in temp_list:
                                temp_list.append(clad)
                    elif (clad == '100'):
                        from quizExam.models import Quiz
                        import  datetime, pytz
                        IST = pytz.timezone('Asia/Kolkata')
                        QuizData = Quiz.objects.filter(Department='Computer Science & Engineering').get(Date=datetime.datetime.now(IST).strftime("%Y-%m-%d"))
                        raw_json['groupE']['detail'].append({
                            'name': QuizData.Subject,
                            'code': QuizData.SubCode,
                            'teach': "",
                            'url': QuizData.Url,
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
                    else:
                        raw_json['groupE']['detail'].append({
                            'name': "BREAK",
                            'code': "",
                            'teach': "",
                            'url': "",
                            'id': "",
                            'pwd': "",
                            'timeS': timeS[i],
                            'timeE': timeE[i],
                        })
        e = len(temp_list)
        if groupCS(user)=='3':
            raw_json['groupC']['count'] = {
                'class': c,
                'tute': d,
                'lab': e
            }
        elif groupCS(user)=='4':
            raw_json['groupD']['count'] = {
                'class': c,
                'tute': d,
                'lab': e
            }
        elif groupCS(user)=='1':
            raw_json['groupA']['count'] = {
                'class': c,
                'tute': d,
                'lab': e
            }
        elif groupCS(user)=='2':
            raw_json['groupB']['count'] = {
                'class': c,
                'tute': d,
                'lab': e
            }
        elif groupCS(user)=='5':
            raw_json['groupE']['count'] = {
                'class': c,
                'tute': d,
                'lab': e
            }
    return json.dumps(raw_json)