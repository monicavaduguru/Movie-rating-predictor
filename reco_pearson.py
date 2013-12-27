#user_train={0:{0:3,1:0,2:0,3:2,4:3,5:1,6:0,7:0},1:{0:3,1:0,2:0,3:3,4:4,5:2,6:3,7:0},2:{0:0,1:0,2:3,3:2,4:3,5:1,6:0,7:0}}
#user_test={3:{0:4,2:2,4:2,5:0},4:{0:0,3:3,5:2,6:1}}
#sim_user={3: {0: 0.9486832980505138, 1: 0.8944271909999159, 2: 1.0}, 4: {0: 0.9922778767136677, 1: 0.9116846116771036, 2: 0.9922778767136677}}
#topklist=[2,0,1]
#movie=5
#user=3
#k=2

'''user_train={1:{1:4,2:4,3:1,4:4,5:3},
            2:{1:2,2:1,3:4,4:2,5:5},
            3:{1:3,2:1,3:3,4:2,5:1}}
user_test={4:{1:5,2:4,3:2,4:0,5:3}}
sim_user={4:{1:0.9,2:-0.7,3:0}}
topklist=[1,2,3]
k=3
user=4
movie=4'''
#user,movie,user_train,user_test,topklist,sim_user,k
def reco_pearson(user,movie,user_train,user_test,topklist,sim_user,user_avg,k):
    sum_wr=0
    sum_w=0
    count=0
    sum_user_test=0

    for movie1 in user_test[user]:
        if user_test[user][movie1] !=0:
            count=count+1
            sum_user_test=sum_user_test+user_test[user][movie1]
    #print sum_user_test
    #print count
    avg_user_test=float(sum_user_test)/float(count)
    #print 'avg_user_test='+str(avg_user_test)

    count=0
    for user1 in sim_user:
        for user2 in topklist:
            if sim_user[user1][user2]!=0:
                count=count+1

    if len(topklist)==1 or len(topklist)==0 or count==0 or count==1:
        rating =round(avg_user_test)
        if rating==0:
            return 1
        else:
        #sim_user[user][topklist[0]]*user_train[topklist[0]][movie]
            return rating

    if len(topklist)<k:
        a=len(topklist)
    else:
        a=k
    #print 'a='+str(a)
    for i in range(0,a):
        sum_wr=sum_wr+sim_user[user][topklist[i]]*(user_train[topklist[i]][movie]-user_avg[topklist[i]])
        sum_w=sum_w+abs(sim_user[user][topklist[i]])

    if sum_w==0:
        rating=round(avg_user_test)
        if rating==0:
            return 1
        else:
            return rating

    rating= round(avg_user_test+float(sum_wr)/float(sum_w))

    if rating >5:
        return 5
    if rating<0:
        rating= round(abs(rating))
        if rating==0:
            return 1
        else:
            return rating
    if rating==0:
        return 1

    return rating

#a=reco_pearson()
#print a
