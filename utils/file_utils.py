import re
def sure_quest():
    """
    Function that we use to ask user if he/she sure, choise can be maded by pressing Y/N
    :return: bool, True when user is sure or has put incorrect inpu, otherways Fals
    
    
    """
    answ = input('Are uou sure?Y/N')
    match answ:
        case "Y":
            return True
        case "N":
            return False
        case _:
            print('I think its Yes')
            return True


def to_many_quest(names : list, tabel_num : int = 6,number_of_seat :int = 4) -> str:
    """
    Function implements dailog with user
    :param: names list of employe names 
    :param: tabel_num int number of tabel in the room, by default 6
    :param: number_of_seats int quantety of seats per one table
    :return: flag string that we use for desicion implementation in Openspace class
    
    """
    while True:
        flag = input(""" There is mot enough space in the openspace to fit all collegeus.
            What you want to do ?
          Press:
            'T' add one table
            'S' add one seat for each table 
            'B' add one table add one seat for each table 
            'N' Nothing. add extracolumn in your inpu
            
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
                    len_names = len(names )
                    if len_names< number_of_seat and len_names < tabel_num:
                        if len_names <=1:
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
