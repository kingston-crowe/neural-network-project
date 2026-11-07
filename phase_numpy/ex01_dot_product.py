def main(): 
    list1 = [1,2]
    list2 = [4,5,6]
    print(dot_product(list1, list2))
def dot_product(list1,list2):
    total = 0
    if range(len(list1)) != range(len(list2)):
        raise ValueError("Vectors not the same dimension")
    for i in range(len(list1)):
        total += (list1[i] * list2[i])
    return total

main()