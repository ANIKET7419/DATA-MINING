list_=[['Aniket',90,90,85],['Abhishek',91,91,91]]
copy=[ [ y for y in x[1:] if y>85] for x in list_ ]
print(copy)
