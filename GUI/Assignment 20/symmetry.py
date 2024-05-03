def symmetry(li):
    if len(li) % 2 != 0:
        t=len(li) // 2
        first_list=li[:t]
        second_list=li[t+1:]
        second_list.reverse()
        if first_list == second_list:
            return "Your list is symmetry"
        else:
            return "Your list is not symmetry"
    else:
        return "Your list must be odd"
    

print(symmetry([1, 4, 3, 4, 1]))

