def enter_int(mesg):
    try:
        return int(input(mesg))
    except ValueError:
        print("Your velue isn't valid")
        return enter_int(mesg)
