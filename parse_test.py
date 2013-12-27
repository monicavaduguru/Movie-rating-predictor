def parse_test(file_name):

    user_test={}
    try:
        fd=open(file_name, "r")
        for line in fd:
            if line[-1] == '\n' and line:
                data = line[0:-1].split(' ')
                dict1={int(data[1]):int(data[2])}
            else:
                data = line.split(' ')
                dict1={int(data[1]):int(data[2])}

            if user_test.get(int(data[0])):
                user_test[int(data[0])].update(dict1)
            else:
                user_test[int(data[0])] = dict1
        fd.close()
        #print user_test
        return user_test

    except Exception as e:
        print 'Exception'
        print e


#parse_test('test1.txt')
