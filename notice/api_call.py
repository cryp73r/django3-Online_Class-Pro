import json
from .models import Notice

def apiCall():
    raw_json = {"data": []}
    noticeData = Notice.objects.all().order_by('-date')
    for element in noticeData:
        raw_json["data"].append({
            "department": element.department,
            "designation": element.designation,
            "signatory": element.signatory,
            "date": str(element.date),
            "message": element.message,
        })
    return json.dumps(raw_json)