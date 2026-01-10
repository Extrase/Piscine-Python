def NULL_not_found(object: any) -> int:
    if object == "Brian":
        print("Type not Found")
        return 1
    if object:
        bloc = [None, float("NaN"), 0, "", False]
        names = ["Nothing", "Cheese", "Zero", "Empty", "Fake"]
        types = ["'NoneType'", "'float'", "'int'", "'str'", "'bool'"]
        title = ""
        for i in range(5) :
            if type(object) is not bloc[i]:
                title = names[i]
                print(f"{title}: {bloc[i]} <class {types[i]}>")
        return 1