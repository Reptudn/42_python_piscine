ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"

lst = list(ft_tuple)
lst[1] = "Germany"
ft_tuple = tuple(lst)

ft_set.remove("tutu!")
ft_set.add("Heilbronn")

ft_dict["Hello"] = "42Heilbronn"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
