# -*- coding: utf-8 -*-
##########################################################################################
#
#  Creator: Tae Kim 
#
#  my_word_count.py 
#  May 5,2015
#
#   Word Count, which takes in a text file or set of text files from a directory
#    and outputs the number of occurrences for each word
#
#  Please let me know if this is does not work or does not meet your coding standard. 
#  Since I am going through final, I spent very little time coding for this
#  I can spend more time next week to make the code cleaner and robust
#  
#
##########################################################################################



def txtReader(thisfile):
    '''
    Reads txt file, and save
    '''
    thisDictionary={}
    with open(thisfile,'r')  as f:
         for line in f:
             for item in line.strip('\n').replace(",","").split(" "):
               item=item.lower()   #make it lower case
               item=item.strip().replace(".","")    #remove period
           
               if item in thisDictionary:
                    thisDictionary[item]+=1
               else:
                    thisDictionary[item]=1

    with open('wc_output/wc_result.txt', 'w') as outfile:
        [outfile.write("{0}\t\t{1}\n".format(k,v)) for k,v in sorted(thisDictionary.iteritems(), key=lambda x:x[0])]


if __name__ == '__main__': 
      thisfile ="wc_input/input.txt"
      thisReader =  txtReader(thisfile)
   