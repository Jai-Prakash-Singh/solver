#! /usr/bin/env python



import sys, random #importing system  and random module 


def word_generator(alphabet, length, wmaximum):          
    
   
    #here
    #creating blank list  word_list and word_matched

    word_list = []
    word_matched = []
    

    #xrange is for moving from 0 to wmaximum
    #random.sample is used to generate collection of random--
    #--alphabet in a list named "random_selection" of length "lenght"
    #join is to make a lsit in a simple string 
    #strip is for  remonving Extra space from a string 
    #here we r generating  a possible number of words from a given alphabet
    # maximum possible word will be of length wmaximum

    for count in xrange(0,wmaximum):
      random_selection = random.sample(alphabet, length)
      string = "".join(random_selection)
      string = string.strip()

    #here
    #entering of word tankes place in a list
    #named as word_list
    # such that only unique word will enter in it 

      if string not in word_list:
          word_list.append(string)
    
    #here 
    #we r reading  a file  named dictionary.txt
    # which contains a list of words

    f = open("dictionary.txt", "r")

    #here
    #we r capturing  words line by line 
    #and r striping them 
    for line in f:
        line = line.strip()
    
    #here 
    #we r looking the captured words in list
    #named word_list
    #if it is found we r entering it into another list
    #named word_matched

        if line  in word_list:
            word_matched.append(line)
    
    #here printing the mathed words 
    #clearing list word_matched and word_list
    #closing file also 
    #and done

    if word_matched:
       print 
       print "Matched found"
       print word_matched
    else:
       print 
       print " Matched not found"
       print "may by u would have enter a spache between" ,
       print "alpphabet , which is a space chaacter"
       print 
       print "or"
       print " it is not in the dictionary.txt  file"

    del word_matched[0:len(word_matched)]
    del word_list[0:len(word_list)]
    f.close()
    print 
    print 'DONE!'

if __name__=="__main__":
    
    #calculating number of argument from command line 
    length = len(sys.argv) 


    #if number of command line argumnet is not eqal to  2
    # than some suggstion for him
    if length != 2:
        print "you have to enter an argument not more",
        print "than that from command line as a set alphabet"
	print 
	print '''argument like  "epmalxe" '''
	print 
	exit(1)
    

    #else 
    #takes arument from command line 
    #measuring length of argument excluding name of programe 
    #calling function for generating possiblities word from given alphabet
    #passing argument as the given apphabet, length of alphabet and a number upto which 
    #we will make number of possible words
    else:
        alphabet = list(str(sys.argv[1]))
	length = len(str(sys.argv[1]))
        print 
        print "for matching , generating possible words............." 
        print 
	#maximum_combination = pow(length , length)   # open it if u want max_to_max words
	nu_max_comb = 8000                            # comant if you  opening the above line 
	word_generator(alphabet, length, nu_max_comb)


        
