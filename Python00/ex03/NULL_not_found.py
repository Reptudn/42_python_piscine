def NULL_not_found(object: any) -> int:
    objType = type(object)

    print(f"{objType.__name__.capitalize()} : {type(object)}")

    return 1 if objType == None else 0