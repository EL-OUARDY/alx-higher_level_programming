#!/usr/bin/python3
if __name__ == "__main__":  # works only on direct execution
    """ prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    names_list = dir(hidden_4)
    for name in names_list:  # loop through defined names
        if name[:2] != "__":  # not start with __
            print(name)
