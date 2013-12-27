
from parsing_text import parse_train
from parse_test import parse_test
from recommender2 import recommender2
from reco import reco
from recommender import recommender
from recommender_item import recommender_item
from output import output


user_train,movie_train=parse_train('train.txt')
user_test5=parse_test('test5.txt')
user_test10=parse_test('test10.txt')
user_test20=parse_test('test20.txt')
user_test1=parse_test('test1.txt')
k=4
reco_dict=recommender(user_train,user_test20,movie_train,k)
#reco_dict1=recommender(user_train,user_test20,movie_train,k)
#reco_dict2=recommender2(user_train,user_test20,movie_train,k)
#reco_dict=reco(reco_dict1,reco_dict2)
#reco_item=recommender_item(user_train,user_test20,movie_train,k)
output(reco_dict,'test20.txt','result20.txt')
#output(reco_item,'test20.txt','result20.txt')
