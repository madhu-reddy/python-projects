import argparse
parser = argparse.ArgumentParser()
parser.add_argument("word", help="Print the word in upper case letters")  #positional arguments, argument passed is stored in variable “word”
parser.add_argument("-c", "--count", action="store_true", dest="counttotal", default=False, help="Count number of character in word")  # Optional arguments.
#If option -c is provided than it will have value true based on action attribute. That value will be accessible via attribute value of dest.
args = parser.parse_args()
if args.counttotal:
   print (len(args.word))
else:
   print(args.word.upper())


#Output
'''
python argparse-positional-args.py -c madhu
4


python testtemporaryfile.py madhu
MADHU


python testtemporaryfile.py -h
usage: testtemporaryfile.py [-h] [-c] word

positional arguments:
  word         Print the word in upper case letters

optional arguments:
  -h, --help   show this help message and exit
  -c, --count  Count number of character in word

'''

