from adjustedcosine_sim import adjustedcosine_sim
from reco_item import reco_item
from operator import itemgetter

import logging as log

user_train={0:{0:3,1:0,2:0,3:2,4:3,5:1,6:0,7:0},1:{0:1,1:0,2:0,3:3,4:4,5:2,6:3,7:0},2:{0:0,1:0,2:3,3:2,4:3,5:1,6:0,7:0}}
user_test={3:{0:4,2:2,4:2,5:0},4:{0:0,3:3,5:2,6:1}}


def recommender_item(user_train,user_test,movie_train,k):
    count1=0
    user_avg={}
    for user in user_train:
        count2=0
        sum=0
        for movie in user_train[user]:
            if user_train[user][movie]!=0:
                sum=sum+user_train[user][movie]
                count2=count2+1
        #print count2
        if count2==0:
            avg=0
        else :
            avg=float(sum)/float(count2)
        user_avg[user]=avg
    #print 'user_avg'
    #print user_avg



    reco_item_dict={}
    for user in user_test:
        dict2={}
        for movie in user_test[user]:
            if user_test[user][movie]==0:

                sim_movie={}
                sim_movieabs={}
                for movie2 in user_test[user]:
                    if movie2!=movie and user_test[user][movie2]!=0:
                        sim=adjustedcosine_sim(movie_train[movie],movie_train[movie2],user_train,user_avg)
                        #print movie,movie_train[movie],movie2,movie_train[movie2]
                        sim_movie[movie2]=sim
                        sim_movieabs[movie2]=abs(sim)
                #print movie,user


                lista=sorted(sim_movie.items(),key=itemgetter(1), reverse=True)
                #print lista
                count=0
                topklistmovie=[]
                for movie1,sim in lista:
                    #print user1
                    #print movie
                    #print 'user'+str(user)
                    if user_test[user][movie1]!=0:
                        topklistmovie.append(movie1)
                        count=count+1
                        if count==k:
                            break

                rating=reco_item(user,movie,user_train,user_test,movie_train,topklistmovie,sim_movie,k)
                #print rating
                a=int(rating)
                dict2[movie]=a
        #reco_dict[user]=dict2
        reco_item_dict[user]=dict2
    #print reco_item_dict

    return reco_item_dict



#recommender(user_train,user_test,3)

 #user_train, user_test,k
