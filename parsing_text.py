
def parse_train(file_name):
    with open(file_name,'r') as fd:
        data = fd.readline()
        #print 'here'
        #print data[2002]

    user_train={}
    for j in range(1,201):
        data_dict1={}
        for i in range(0,2000,2):
            data_dict1[(i+2)/2]=int(data[(j-1)*2000+i])
        user_train[j]=data_dict1
    #print user_train[22]
    #print user_dict
    #print user_train'''


    movie_train={}
    for i in range(1,1001):
        data_movie1={}
        for j in range(1,201):
            data_movie1[j]=user_train[j][i]
        movie_train[i]=data_movie1
    #print movie_train[1]
    #print movie_train[597]'''

    return user_train,movie_train



#parse_train('train.txt')
