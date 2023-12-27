while True:
    pel=input()
    if pel=="0":
        break
    pel_list=[x for x in pel]
    pel_list_reverse=list(reversed(pel_list))
    if pel_list_reverse==pel_list:
        print("yes")
    else:
        print("no")
