#user_train={0:{0:3,1:0,2:0,3:2,4:3,5:1,6:0,7:0},1:{0:5,1:0,2:0,3:3,4:4,5:2,6:3,7:0},2:{0:0,1:0,2:3,3:2,4:3,5:1,6:0,7:0}}
#sim_user={3: {0: 0.9486832980505138, 1: 0.6507913734559685, 2: 1.0}, 4: {0: 0.9922778767136677, 1: 0.9116846116771036, 2: 0.9922778767136677}}
#topklist=[2, 0,1]
#movie=5
#user=3
#user,movie,user_train,user_test,topklist,sim_user,k
def reco_cosine(user,movie,user_train,user_test,topklist,sim_user,user_avg,k):
    sum_wr=0
    sum_w=0
    count=0
    sum_user_test=0
    '''print user
    print movie
    for a in topklist:
        print 'topklist'+str(a)
    print len(topklist)'''
    for movie1 in user_test[user]:
        if user_test[user][movie1] !=0:
            count=count+1
            sum_user_test=sum_user_test+user_test[user][movie1]
    avg_user_test=float(sum_user_test)/count

    if len(topklist)<k:
        a=len(topklist)
    else:
        a=k
    #print 'a'+str(a)
    if a==1:
        rating=round(avg_user_test)
        #rating= round(sim_user[user][topklist[0]]*user_train[topklist[0]][movie])
        if rating==0:
            return 1
        return rating
    for i in range(0,a):
        #print i,topklist[i],movie
        if user==201 and movie ==7:
            print 'sim_user[user][topklist[i]]'+str(sim_user[user][topklist[i]])
            print 'user_train[topklist[i]][movie]'+ str(user_train[topklist[i]][movie])
        sum_wr=sum_wr+sim_user[user][topklist[i]]*user_train[topklist[i]][movie]
        sum_w=sum_w+sim_user[user][topklist[i]]
    '''if user==201 and movie ==7:
        print 'sum_w'
        print sum_w
        print 'sum_wr'
        print sum_wr
        #print 'end'''''
    if sum_w==0:
        rating=round(avg_user_test)
        if rating==0:
            return 1
        return rating
    rating=round((float(sum_wr)/float(sum_w)))
    if rating==0:
        return 1
    #print 'rating'+str(rating)
    return rating

#a=reco_cosine()
#print a
#user,movie,user_train,user_test,topklist,sim_user
