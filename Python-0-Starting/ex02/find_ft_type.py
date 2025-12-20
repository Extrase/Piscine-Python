def all_thing_is_obj(object: any) -> int:
    if object:
        bloc = [list, tuple, set, dict]
        names = ["List", "Tuple", "Set", "Dict"]
        title = ""
        for i in range(4) :
            if type(object) is bloc[i]:
                title = names[i]
                print(f"{title} : {bloc[i]}")
        if title == "" and type(object) is str:
                print(f"{object} is in the kitchen : {str}")
        elif title == "":
                print("Type not found")
        return 42