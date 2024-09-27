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


def to_many_quest(names : list, tabel_num : int = 6,number_of_seat :int = 4) -> str:
    while True:
        flag = input(""" There is mot enough space in the openspace to fit all collegeus.
            What you want to do ?
          Press:
            'T' add one tabel
            'S' add one seat for each tabel
            'B' add one tabel or add one seat for each tabel
            'N' Nothing. add extra column in your input
            
          """)
    
        if re.fullmatch("^[NBTS]$",flag):
            match flag:
                case 'T':
                    if len(names) > 1:
                        return flag
                    else:
                        while True:
                            flag = input(""" Employ shouldn't be alone.
                                    S : one seat to each table
                                    N : Nothing
                                  """)
                            if re.fullmatch('^[SN]$',flag):
                                return flag
                            else:
                                print('Incorrect input. Please, enter S or N')
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
                    if len_names < number_of_seat and len_names < tabel_num:
                        if len_names <= 1:
                            print("only adding seats is possible")
                            return 'S'
                        else:
                            while True:
                                flag = input("""
                                             Just tabel or just one seat per each tabel will be enough
                                             T : add tabel
                                             S : add one seat for each tabel 
                                             """)
                                if re.fullmatch('^[TS]$',flag):
                                    return flag
                                else:
                                    print('Incorrect input. Please, enter S or T')
                                    continue
                    elif len_names > number_of_seat+tabel_num or (len_names>number_of_seat and tabel_num< len_names):
                        return flag
                    elif len_names > tabel_num and len_names <= number_of_seat:
                        print("1 Table is enogh")
                        return 'T'
                    elif len_names <= tabel_num and len_names > number_of_seat:
                        print('One Seat per tabel is enough')
                        return 'S'

        else:
            print('Incorrect input. Please,enter T,S,B or N')
            continue