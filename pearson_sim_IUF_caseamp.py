
from math import sqrt
def pearson_sim_IUF_caseamp(train_user,test_user,IUF_train):
    count=0
    sum_xy=0
    sum_x2=0
    sum_y2=0
    sum_y=0
    sum_x=0
    avg_x=0
    avg_y=0
    for movie in test_user:
        if test_user[movie]!=0:
            if train_user[movie]!=0:
               count=count+1
    #print count
    '''
    if count==1:
        for movie in test_user:
            if test_user[movie]!=0:
                if train_user[movie]!=0:
                    d=abs(test_user[movie]-train_user[movie])
                    sim=float(1)/float(d+1)
                    return sim
                    move it down
    '''
    if count==0 or count==1:
        return 0


    else:
        count=0
        for movie in test_user:
            if test_user[movie]!=0:
                    sum_y=sum_y+test_user[movie]*IUF_train[movie]
                    count=count+1
        avg_y=float(sum_y)/count
        #print 'avg_x,avg_y'
        #print avg_x,avg_y

        count=0
        for movie in train_user:
            if train_user[movie]!=0:
                sum_x=sum_x+train_user[movie]*IUF_train[movie]
                count=count+1
        avg_x=float(sum_x)/count


        for movie in test_user:
            if test_user[movie]!=0:
                if train_user[movie]!=0:
                    sum_xy=sum_xy+(train_user[movie]*IUF_train[movie]-avg_x)*(test_user[movie]*IUF_train[movie]-avg_y)
                    sum_x2=sum_x2+(train_user[movie]*IUF_train[movie]-avg_x)*(train_user[movie]*IUF_train[movie]-avg_x)
                    sum_y2=sum_y2+(test_user[movie]*IUF_train[movie]-avg_y)*(test_user[movie]*IUF_train[movie]-avg_y)
                    #print (train_user[movie]-avg_x),(test_user[movie]-avg_y)
    #print 'sum_xy,sum_x2,sum_y2'
    #print sum_xy,sum_x2,sum_y2
    denominator=float(sqrt(sum_y2)*sqrt(sum_x2))
    numerator=float(sum_xy)
    if denominator==0:
        return 0
    else:
        sim=numerator/denominator
        sim=sim*pow(abs(sim),1.5)
        return sim

#a=pearson_sim(train_user,test_user)
#print a
