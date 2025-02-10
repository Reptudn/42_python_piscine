def NULL_not_found(object: any) -> int:
    objType = type(object)

    if object is None:
        print(f"Nothing: {object} {objType}")
    elif objType is float:
        print(f"Cheese: {object} {objType}")
    elif objType is int:
        print(f"Zero: {object} {objType}")
    elif object == '':
        print(f"Empty: {object} {objType}")
    elif objType is bool:
        print(f"Fake: {object} {objType}")
    else:
        print("Type not found")
        return 1
    return 0
