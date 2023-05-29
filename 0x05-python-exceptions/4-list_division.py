#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides list 1 and 2 element by elements

    Args:
        my_list_1 (list): list 1
        my_list_2 (list): list 2
        list_length (int): elements count

    Returns:
        New list of results of length list_length
    """

    res_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            res_list.append(result)
    return (res_list)
