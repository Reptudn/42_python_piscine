def all_thing_is_obj(object: any) -> int:
    objType = type(object)

    if objType == int:          # doesnt make sense
        print("Type not found") # everything in python is an object which means it has a type
    elif objType == str:
        print(f"{object} is in the kitchen : {objType}")
    else:
        print(f"{objType.__name__.capitalize()} : {type(object)}")
    return 42