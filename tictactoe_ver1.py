

def get_verif(long,lag):
    if(long>2 or long<0 or lag>2 or lag<0):
        return False
    else :
        return True

def get_verif_win(mat,arg):
    count_x =0
    count_0 =0
#verif if there is winner in x axe
    z=''
    for z in mat:
        for arg in z:
            if(arg=='x'):
                count_x=count_x+1
            if count_x==3:
                return 'x'
            if(arg=='o'):
                count_0=count_0+1
            if(count_0==3):
                return '0'

        count_x = 0
        count_0 = 0

# verif if there is winner in y axe

    count_x=[0,0,0]
    count_0=[0,0,0]

    for n in range(0, 3, 1):
        for m in range(0,3,1):

            if mat[m][n]=='x':
                count_x[n]=count_x[n]+1
            if count_x[n]==3:
                return 'x'
            if mat[m][n]=='o':
                count_0[n]=count_0[n]+1
            if count_0[n]==3:
                return '0'

# verif if there is winner in left diagonal

    count_x=0
    count_0=0
    for n in range(0, 3, 1):
        if(mat[n][n]=='x'):
            count_x=count_x+1
        if(mat[n][n]=='o'):
            count_0=count_0+1
    if(count_x==3):
        return 'x'
    if(count_0==3):
        return 0

# verif if there is winner in right diagonal

    count_x=0
    count_0=0
    m=2
    for n in range (0,3,1):
        if(mat[m][n]=='x'):
            count_x=count_x+1
        if(mat[m][n]=='o'):
            count_0=count_0+1
        m=m-1

    if(count_x==3):
        return 'x'
    if(count_0==3):
        return 0

# verif if there is not winner

    z=''
    y=''
    count=0
    for z in mat:
        for y in z:
            if '_' in y:
                count=count+1
    if count==0:
        return False

def get_PlayGame(mat,arg):
    x = int(input("Input longitude: "))
    y = int(input("Input lagitude: "))
    res=False
    if(get_verif(x,y)==False):
        print("wrong numbers- inset number 0-2")
        PlayGame(mat,arg)
    if(get_verifEmpty(x,y,mat)==True):
        mat[x][y]=arg
    else:
        print("the case in not empy,try again")
        get_PlayGame(mat, arg)
    for n in range (0,3,1):
       print(mat[n])

    return(get_verif_win(mat,arg))

def get_verifEmpty(long,lag,mat):
    if(mat[long][lag])=='_':
        return True

def main():
    mat=[["_","_","_"],["_","_","_"], ["_","_","_"]]
#    mat=[["00","01","02"],["10","11","12"], ["20","21","22"]]
    for n in range(0,3,1):
       print(mat[n])

    while True:
       print("x play now")
       res=get_PlayGame(mat,'x')
       if res=='x':
           print("x Wins")
           break
       elif res==False:
           print("there is not winer")
           print("try an other game")
           mat = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
           get_PlayGame(mat, 'x')

       print("o play now")
       res=get_PlayGame(mat,'o')
       if res=='0':
           print("0 wins")
           break
       elif res==False:
           print("there is not winer")
           print("try an other game")
           mat = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
           get_PlayGame(mat, 'x')

main()
