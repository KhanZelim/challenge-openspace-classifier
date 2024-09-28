import re
def sure_quest()->bool:
    """
    Function asks the user if they are sure.
    :return: bool True if user is sure, False otherwise
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


def to_many_quest(names : list, tabel_num : int = 6,number_of_seat :int = 4,openspace_capasity :int=24) -> str:
    """
        Function that handles interaction with the user in case of insufficient seating in the openspace.        :param: list names  of colleagues names
        :param: int tabel_num quantity of tables in the room  
        :param: int number_of_seat quantity of seats per table
        :param: int openspace_capacity capacity of current openspace
        :return: str Flag for implemnt_decision function from openspace
    """
    while True:
        flag = input(""" There is mot enough space in the openspace to fit all collegeus.
            What you want to do ?
          Press:
            'T' add one tabel
            'S' add one seat for each tabel 
            'B' add one tabel add one seat for each tabel 
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
                    if len_names< openspace_capasity+number_of_seat and len_names < openspace_capasity+tabel_num:
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
                    elif len_names > (openspace_capasity+number_of_seat+tabel_num) or (len_names>(number_of_seat+openspace_capasity) and (tabel_num+openspace_capasity)< len_names):
                        return flag
                    elif len_names > openspace_capasity+tabel_num and len_names <= openspace_capasity+number_of_seat:
                        print("1 Table is enogh")
                        return 'T'
                    elif len_names <= openspace_capasity+tabel_num and len_names > number_of_seat+openspace_capasity:
                        print('One Seat per tabel is enough')
                        return 'S'

        else:
            print('Incorrect input. Please,enter T,S,B or N')
            continue
