
def reco(reco_dict1,reco_dict2):
    reco_dict={}
    for user in reco_dict1:
        dict1={}
        for movie in reco_dict1[user]:
            avg=(reco_dict1[user][movie]+reco_dict2[user][movie])/2
            dict1[movie]=round(avg)
        reco_dict[user]=dict1
    return reco_dict
