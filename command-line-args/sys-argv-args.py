import sys

print("the total args passed are: {}".format(sys.argv))

print("python script name being run is: {}".format(sys.argv[0]))

print("python total no: of arguments passed are: {}".format(len(sys.argv[1:])))

sum = 0
for val in sys.argv[1:]:
    sum += int(val)

print("Addition of total args passed is: {}".format(sum))


#Output
'''
madhu@madhu-Inspiron-5567:$ python testtemporaryfile.py 3 4 5 6
the total args passed are: ['testtemporaryfile.py', '3', '4', '5', '6']
python script name being run is: testtemporaryfile.py
python total no: of arguments passed are: 4
Addition of total args passed is: 18


madhu@madhu-Inspiron-5567:$ python testtemporaryfile.py 3 4 5 6 7
the total args passed are: ['testtemporaryfile.py', '3', '4', '5', '6', '7']
python script name being run is: testtemporaryfile.py
python total no: of arguments passed are: 5
Addition of total args passed is: 25

'''
