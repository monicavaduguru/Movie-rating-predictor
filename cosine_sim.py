#train_user={1:0,2:0,3:0,4:0,5:0,6:3,7:0}
#test_user={7:4,1:10,2:4,3:8,4:0,5:4}
#train_user = {1:5,2:3,3:0,4:3,5:3,6:5,7:0,8:1,9:5,10:3}
from math import sqrt

def cosine_sim(train_user,test_user,IUF_train):

    count=0
    sum_xy=0
    sum_x2=0
    sum_y2=0

    for movie in test_user:
        if test_user[movie]!=0:
            if train_user[movie]!=0:
               count=count+1

    #print count
    '''if count ==1:
        for movie in test_user:
            if test_user[movie]!=0:
                if train_user[movie]!=0:
                    d=abs(test_user[movie]-train_user[movie])
                    sim=float(1)/float(d+1)
                    return sim'''

    if count==0 or count==1:
      return 0


    else:
        for movie in test_user:
            if test_user[movie]!=0:
                if train_user[movie]!=0:
                    sum_xy=sum_xy+train_user[movie]*test_user[movie]
                    sum_x2=sum_x2+train_user[movie]*train_user[movie]
                    #print sum_x2
                    sum_y2=sum_y2+test_user[movie]*test_user[movie]
    #print sum_xy,sum_y2,sum_x2
    denominator=((sqrt(sum_y2))*(sqrt(sum_x2)))
    b=float(sum_xy)/float(denominator)
    return(b)

#a=cosine_sim(train_user,test_user)
#print a

