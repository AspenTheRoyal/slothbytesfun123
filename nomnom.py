def small_nom_nom(tinylist,number):
    if number+1 < len(tinylist):
        if tinylist[number] > tinylist[number+1]:
            tinylist[number] = tinylist[number]+tinylist[number+1]
            del tinylist[number+1]
            return small_nom_nom(tinylist,number)
        else:
            return small_nom_nom(tinylist,number+1)
    else:
        return tinylist

def nom_nom(selectedlist):
    print(small_nom_nom(selectedlist,0))

nom_nom([5, 3, 7])
#output = [15]

nom_nom([5, 3, 9])
#output = [8, 9]

nom_nom([1, 2, 3])
#output = [1, 2, 3]

nom_nom([2, 1, 3])
#output = [3, 3]

nom_nom([8, 5, 9])
#output = [22]

nom_nom([6, 5, 6, 100])
#output = [17, 100]
