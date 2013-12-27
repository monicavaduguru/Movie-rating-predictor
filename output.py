#reco_dict={3: {5: 1.0}, 4: {0: 2.0}}
#file_i='test1.txt'
#file_o='test2.txt'

#reco_dict,file_i,file_o
def output(reco_dict,file_i,file_o):

    with open(file_o,'w') as fo:
        with open(file_i,'r') as fd:
            for line in fd:
                if line[-1] == '\n':
                    data = line[0:-1].split(' ')
                    #for a in data:
                        #print a
                    if int(data[2])==0:
                        data[2] = str(reco_dict[int(data[0])][int(data[1])])
                        fo.write(' '.join(data))
                        fo.write('\n')
                    #for a in data:
                        #print a
                else:
                    print 'here'
                    data = line.split(' ')
                    if data[2]==0:
                       data[2]=str(reco_dict[int(data[0])][int(data[1])])

                    fo.write(' '.join(data))
                    #for a in data:
                        #print a
                #print 'here'
                #fo.write(' '.join(data))
                #fo.write('\n')

#output()


