import random
matrix=[[0,0,0],[0,0,0],[0,0,0]]
flag=1
check_list=[]
def generate_matrix():
    for i in range (3):
        for j in range(3):
            matrix[i][j]=random.randint(0,10)

def check_row(n):
    sum=0
    for i in range(3):
        sum+=matrix[n][i]
    return sum

def check_column(n):
    sum=0
    for i in range(3):
        sum+=matrix[i][n]
    return sum

def check_identical(lst):
    return all(x == lst[0] for x in lst)

while flag:
    generate_matrix()
    for i in range (3):
        check_list.append(check_row(i))
    if check_identical(check_list):
        for i in range (3):
            check_list.append(check_column(i))
    else:
        check_list=[]
        continue
    if check_identical(check_list):
        for i in range (3):
            for j in range(3):
                print("{:4d}".format(matrix[i][j]),end='')
            print()
            flag=0
    else:
        check_list=[]
        continue