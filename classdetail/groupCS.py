from .verify import verify

def groupCS(username):
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
        if (branchlis[0]=='10' and len(username)==13):
            if (branchlis[1]>=58 and branchlis[1]<=86):
                return '3'
            elif (branchlis[1]>=87 and branchlis[1]<=117):
                return '4'
            elif (branchlis[1]>=1 and branchlis[1]<=28):
                return '1'
            elif (branchlis[1]>=29 and branchlis[1]<=57):
                return '2'
            elif (branchlis[1]>=118 and branchlis[1]<=145):
                return '5'
            else:
                return None
        else:
            return None