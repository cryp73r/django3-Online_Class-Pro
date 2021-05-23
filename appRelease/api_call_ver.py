import json
from .models import AppRelease

def apiCallVer():
    appData = AppRelease.objects.all().order_by('-releaseDate')[0]
    raw_json = {
        "ver": appData.ver,
        "size": appData.size,
        "url": appData.appFile.url
    }
    return json.dumps(raw_json)