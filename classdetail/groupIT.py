from .verify import verify

def groupIT(username):
    if username=='1':
        return '1'
    elif username=='2':
        return '2'
    elif username=='3':
        return '3'
    elif username=='4':
        return '4'
    elif username=='5':
        return '5'
    else:
        branchtup = verify(username)
        branchlis = []
        branchlis.append(branchtup[0])
        branchlis.append(int(branchtup[1]))
        if (branchlis[0]=='13' and len(username)==13):
            if (branchlis[1]>=68 and branchlis[1]<=100):
                return '3'
            elif (branchlis[1]>=101 and branchlis[1]<=134):
                return '4'
            elif (branchlis[1]>=1 and branchlis[1]<=33):
                return '1'
            elif (branchlis[1]>=34 and branchlis[1]<=67):
                return '2'
            else:
                return None
        else:
            return None