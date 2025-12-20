ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
convertLst = list(ft_tuple)
convertLst[1] = "France!"
ft_tuple = tuple(convertLst)
ft_set.clear()
ft_set.update(['Hello', 'Paris!'])
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)