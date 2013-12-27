from cosine_sim import cosine_sim
#from pearson_sim import pearson_sim
from reco_cosine import reco_cosine
from operator import itemgetter
#from reco_pearson import reco_pearson
#from cosinecaseamp_sim import cosinecaseamp_sim
from math import log10
#from pearson_sim_IUF import pearson_sim_IUF
#import logging as log
#from pearson_sim_IUF_caseamp import pearson_sim_IUF_caseamp
#from pearson_sim_caseamp import pearson_sim_caseamp

user_train={0:{0:3,1:0,2:0,3:2,4:3,5:1,6:0,7:0},1:{0:1,1:0,2:0,3:3,4:4,5:2,6:3,7:0},2:{0:0,1:0,2:3,3:2,4:3,5:1,6:0,7:0}}
user_test={3:{0:4,2:2,4:2,5:0},4:{0:0,3:3,5:2,6:1}}


def recommender(user_train,user_test,movie_train,k):

    user_avg={}
    for user in user_train:
        count2=0
        sum=0
        for movie in user_train[user]:
            if user_train[user][movie]!=0:
                sum=sum+user_train[user][movie]
                count2=count2+1

        if count2==0:
            avg=0
        else :
            avg=float(sum)/float(count2)
        user_avg[user]=avg

    IUF_train={}
    for movie in movie_train:
        count2=0
        for user in movie_train[movie]:
            if  movie_train[movie][user]!=0:
                count2=count2+1
        if count2 ==0:
            IUF==0
        else:
            a=1000/count2
            IUF=log10(a)
        IUF_train[movie]=IUF

    sim_user={}
    sim_userabs={}
    for user in user_test:
        dict1={}
        dict2={}
        for user1 in user_train:
            if user!=user1:
                '''if user==201 and user1==2:
                    print 'user_train'
                    print user_train[user1]
                    print 'user_test'
                    print user_test[user]'''
                #print 'train '+ str(user1)+' '+'test '+ str(user)
                sim=cosine_sim(user_train[user1],user_test[user],IUF_train)
                dict1[user1]=sim
                dict2[user1]=abs(sim)
        sim_user[user]=dict1
        sim_userabs[user]=dict2



    reco_dict1={}
    for user in user_test:
        dict2={}
        for movie in user_test[user]:
            if user_test[user][movie]==0:
                #print user
                #print movie
                lista=sorted(sim_userabs[user].items(),key=itemgetter(1), reverse=True)
                #print lista
                count=0
                topklist=[]
                for user1,sim in lista:
                    #print user1
                    #print movie
                    #print 'user'+str(user)
                    if user_train[user1][movie]!=0:
                        topklist.append(user1)
                        count=count+1
                        if count==k:
                            break


                rating=reco_cosine(user,movie,user_train,user_test,topklist,sim_user,user_avg,k)
                #print rating

                a=int(rating)
                #a=int(round(rating))
                #if a==0:
                #   a=1
                dict2[movie]=a
        #reco_dict[user]=dict2
        reco_dict1[user]=dict2

    #print reco_dict[205]

    return reco_dict1



#recommender(user_train,user_test,3)

 #user_train, user_test,k
