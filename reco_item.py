

def reco_item(user,movie,user_train,user_test,movie_train,topklistmovie,sim_movie,k):
    sum_w=0
    count1=0
    sum_wr=0
    count2=0
    sum_user_test_movie=0
    for movie1 in user_test[user]:
        if user_test[user][movie1]!=0:
            count1=count1+1
            sum_user_test_movie=sum_user_test_movie+user_test[user][movie1]
    avg_user_test_movie=float(sum_user_test_movie)/float(count1)
    #print 'avg'
    #print avg_user_test_movie

    for movie1 in topklistmovie:
        if sim_movie[movie1]!=0:
            count2=count2+1


    if len(topklistmovie)==0 or count2==0 or len(topklistmovie)==1 or count2==1:
        return avg_user_test_movie



    if len(topklistmovie)<k:
        a=len(topklistmovie)
    else:
        a=k

    for i in range (0,a):
        sum_w=sum_w+abs(sim_movie[topklistmovie[i]])
        sum_wr=sum_wr+sim_movie[topklistmovie[i]]*user_test[user][topklistmovie[i]]
    #print 'sum_wr'+str (sum_wr) +'sum_w'+str(sum_w)
    rating=round(float(sum_wr)/float(sum_w))
    #rating=round((rating+5)/2)
    if rating <=1:
        return avg_user_test_movie
    if rating==0:
        return avg_user_test_movie
    if rating>5:
        return 5
    return abs(rating)


