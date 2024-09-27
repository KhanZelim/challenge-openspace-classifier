import re

def sure_quest():
    answ = input('Are you sure? Y/N')
    match answ:
        case "Y":
            return True
        case "N":
            return False
        case _:
            print("I think it's Yes")
            return True


def too_many_quest(names: list, table_num: int =6, number_of_seats: int =4) -> str:
    while True:
        flag = input(""" There is mot enough space in the openspace to fit all collegeus.
            What do you want to do ?
          Type:
            'T': Add one tabel
            'S': Add one seat for each tabel
            'B': Add one tabel or add one seat for each tabel
            'N': Nothing
            
          """)   
        if re.fullmatch("^[NBTS]$", flag):
            match flag:
                case 'T':
                    if len(names) > 1:
                        return flag
                    else:
                        while True:
                            flag = input("""Colleague shouldn't be alone.
                                    S: Add one seat to each table
                                    N: Nothing
                                  """)
                            if re.fullmatch('^[SN]$',flag):
                                return flag
                            else:
                                print("Incorrect input. Please, type 'S' or 'N'")
                                continue
                case 'S':
                    return flag
                case 'N':
                    if sure_quest():
                        return flag
                    else:
                        return 'S'
                case 'B':
                    len_names = len(names)
                    if len_names < number_of_seats and len_names < table_num:
                        if len_names <= 1:
                            print("Only adding seats is possible")
                            return 'S'
                        else:
                            while True:
                                flag = input("""
                                             Just adding a table or adding one seat per tabel will be enough
                                             T: Add a table
                                             S: Add one seat per tabel 
                                             """)
                                if re.fullmatch('^[TS]$', flag):
                                    return flag
                                else:
                                    print("Incorrect input. Please, type 'S' or 'T'")
                                    continue
                    elif len_names > number_of_seats + table_num or (len_names > number_of_seats and table_num < len_names):
                        return flag
                    elif len_names > table_num and len_names <= number_of_seats:
                        print("One table is enough")
                        return 'T'
                    elif len_names <= table_num and len_names > number_of_seats:
                        print('One seat per tabel is enough')
                        return 'S'
        else:
            print("Incorrect input. Please, type 'T', 'S', 'B' or 'N'")
            continue