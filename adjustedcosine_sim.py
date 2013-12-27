#train_user={1:0,2:0,3:0,4:0,5:0,6:3,7:0}
#train_movie={movie1:{user1:rating,user2:rating},movie2:
#test_user={7:4,1:10,2:4,3:8,4:0,5:4}
#train_user = {1:5,2:3,3:0,4:3,5:3,6:5,7:0,8:1,9:5,10:3}
from math import sqrt

def adjustedcosine_sim(test_movie_movie1,test_movie_movie2,user_train,user_avg):
    count=0
    sum_xy=0
    sum_x2=0
    sum_y2=0
    denominator=0
    for user in test_movie_movie1:
        if test_movie_movie1[user]!=0:
            if test_movie_movie2[user]!=0:
                count=count+1
    #print count

    '''if count ==1:
        for user in test_movie_movie1:
            if test_movie_movie1[user]!=0:
                if test_movie_movie2[user]!=0:
                    d=abs(test_movie_movie2[user]-test_movie_movie1[user])
                    sim=float(1)/float(d+1)
                    #print 'sim'+str(sim)
                    return sim'''
    #print count

    if count==0 or count==1:
        return 0



    else:
        for user in test_movie_movie1:
            count1=0
            sum_user=0

            avg_user=user_avg[user]

            #print 'avg_user '+str(avg_user)+'user'+str(user)
            if test_movie_movie1[user]!=0:
                if test_movie_movie2[user]!=0:

                    #print '(test_movie_movie1[user]-avg_user)'+ str((test_movie_movie1[user]-avg_user))
                    #print '(test_movie_movie2[user]-avg_user)'+ str((test_movie_movie2[user]-avg_user))
                    sum_xy=sum_xy+(test_movie_movie1[user]-avg_user)*(test_movie_movie2[user]-avg_user)
                    sum_x2 += (test_movie_movie1[user]-avg_user)*(test_movie_movie1[user]-avg_user)
                    #print sum_x2
                    sum_y2 += (test_movie_movie2[user]-avg_user)*(test_movie_movie2[user]-avg_user)

    #print sum_xy,sum_y2,sum_x2
    denominator=((sqrt(sum_y2))*(sqrt(sum_x2)))
    if denominator==0:
        return 0
    b=float(sum_xy)/float(denominator)
    #print 'rating'+str(b)
    return(b)



