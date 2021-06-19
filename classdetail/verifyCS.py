from .groupCS import groupCS

def verifyCS(username, wday):
    grou = groupCS(username)
    t_table = []
    odd = False
    # For Odd Semester
    if odd:
        if grou == '3':
            if wday == 0:
                t_table = ['100', '2', '3', '17', ' ', '16', '17', ' ']
                return t_table
            elif wday == 1:
                t_table = ['4', '3', '5', '1', ' ', '6', ' ', ' ']
                return t_table
            elif wday == 2:
                t_table = ['2', '5', '3', ' ', ' ', ' ', ' ', ' ']
                return t_table
            elif wday == 3:
                t_table = ['2', '6', '5', '1', ' ', '8', '10', ' ']
                return t_table
            elif wday == 4:
                t_table = ['100', '4', '3', '7', ' ', '6', '15', '15']
                return t_table
            elif wday == 5:
                t_table = [' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        elif grou == '4':
            if wday == 0:
                t_table = ['100', '2', '3', '19', ' ', '11', '18', '18']
                return t_table
            elif wday == 1:
                t_table = ['4', '3', '5', '1', ' ', '6', ' ', ' ']
                return t_table
            elif wday == 2:
                t_table = ['2', '5', '3', ' ', ' ', ' ', ' ', ' ']
                return t_table
            elif wday == 3:
                t_table = ['2', '6', '5', '1', ' ', ' ', '12', '20']
                return t_table
            elif wday == 4:
                t_table = ['100', '4', '3', '14', ' ', '6', '20', ' ']
                return t_table
            elif wday == 5:
                t_table = [' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        elif grou == '1':
            if wday == 0:
                t_table = ['100', '3', '5', '1', ' ', '6', '15', ' ']
                return t_table
            elif wday == 1:
                t_table = ['5', '2', '4', '8', ' ', ' ', ' ', ' ']
                return t_table
            elif wday == 2:
                t_table = ['4', '3', '1', '2', ' ', '6', '10', '15']
                return t_table
            elif wday == 3:
                t_table = ['5', '3', '2', '16', ' ', '17', '17', ' ']
                return t_table
            elif wday == 4:
                t_table = ['100', '3', '6', ' ', ' ', '7', ' ', ' ']
                return t_table
            elif wday == 5:
                t_table = [' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        elif grou == '2':
            if wday == 0:
                t_table = ['100', '3', '5', '1', ' ', '6', ' ', ' ']
                return t_table
            elif wday == 1:
                t_table = ['5', '2', '4', '11', ' ', '20', '20', ' ']
                return t_table
            elif wday == 2:
                t_table = ['4', '3', '1', '2', ' ', '6', ' ', ' ']
                return t_table
            elif wday == 3:
                t_table = ['5', '3', '2', '14', ' ', '18', '18', ' ']
                return t_table
            elif wday == 4:
                t_table = ['100', '3', '6', '19', ' ', '12', ' ', ' ']
                return t_table
            elif wday == 5:
                t_table = [' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        else:
            t_table = [' ']
            return t_table

    # For Even Semester
    else:
        if grou == '3':
            if wday == 0:
                t_table = ['100', '1', '6', '5', ' ', '22', '22', '9', ' ']
                return t_table
            elif wday == 1:
                t_table = ['1', '2', '3', '4', ' ', '5', '12', '20', '20']
                return t_table
            elif wday == 2:
                t_table = ['2', '3', '6', '5', ' ', ' ', ' ', ' ', ' ']
                return t_table
            elif wday == 3:
                t_table = ['2', '1', '4', '3', ' ', ' ', '12', ' ', ' ']
                return t_table
            elif wday == 4:
                t_table = ['100', '3', '6', '8', ' ', '11', '10', '21', '21']
                return t_table
            elif wday == 5:
                t_table = [' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        elif grou == '4':
            if wday == 0:
                t_table = ['100', '1', '6', '5', ' ', '23', '23', '14', ' ']
                return t_table
            elif wday == 1:
                t_table = ['1', '2', '3', '4', ' ', '5', '18', '15', ' ']
                return t_table
            elif wday == 2:
                t_table = ['2', '3', '6', '5', ' ', '25', '25', '24', '24']
                return t_table
            elif wday == 3:
                t_table = ['2', '1', '4', '3', ' ', '17', '18', ' ', ' ']
                return t_table
            elif wday == 4:
                t_table = ['100', '3', '6', '16', ' ', ' ', ' ', ' ', ' ']
                return t_table
            elif wday == 5:
                t_table = [' ', '24', '24', ' ', ' ', ' ', ' ', ' ', ' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        elif grou == '5':
            if wday == 0:
                t_table = ['100', '2', '6', '3', ' ', '1', '5', ' ', ' ']
                return t_table
            elif wday == 1:
                t_table = ['3', '1', '5', '2', ' ', '4', '12', ' ', ' ']
                return t_table
            elif wday == 2:
                t_table = ['3', '4', '6', '1', ' ', ' ', '11', '14', '14']
                return t_table
            elif wday == 3:
                t_table = ['15', '15', '5', '10', ' ', '8', '12', '9', ' ']
                return t_table
            elif wday == 4:
                t_table = ['100', '3', '6', '2', ' ', '16', '16', ' ', ' ']
                return t_table
            elif wday == 5:
                t_table = [' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        elif grou == '1':
            if wday == 0:
                t_table = ['100', '1', '6', '3', ' ', '11', '9', '22', '22']
                return t_table
            elif wday == 1:
                t_table = ['2', '3', '4', '5', ' ', '10', '12', '21', '21']
                return t_table
            elif wday == 2:
                t_table = ['1', '2', '6', '3', ' ', ' ', ' ', ' ', ' ']
                return t_table
            elif wday == 3:
                t_table = ['1', '4', '3', '5', ' ', '8', '12', '20', '20']
                return t_table
            elif wday == 4:
                t_table = ['100', '2', '6', '5', ' ', ' ', ' ', ' ', ' ']
                return t_table
            elif wday == 5:
                t_table = [' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        elif grou == '2':
            if wday == 0:
                t_table = ['100', '1', '6', '3', ' ', '24', '24', ' ', ' ']
                return t_table
            elif wday == 1:
                t_table = ['2', '3', '4', '5', ' ', '15', '18', '25', '25']
                return t_table
            elif wday == 2:
                t_table = ['1', '2', '6', '3', ' ', '17', '16', ' ', ' ']
                return t_table
            elif wday == 3:
                t_table = ['1', '4', '3', '5', ' ', ' ', '18', '17', ' ']
                return t_table
            elif wday == 4:
                t_table = ['100', '2', '6', '5', ' ', '23', '23', ' ', ' ']
                return t_table
            elif wday == 5:
                t_table = [' ']
                return t_table
            elif wday == 6:
                t_table = [' ']
                return t_table

        else:
            t_table = [' ']
            return t_table
