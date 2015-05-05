# -*- coding: utf-8 -*-
##########################################################################################
#
#  Creator: Tae Kim 
#
#  my_running_median.py 
#  May 5,2015
#
#   Running Median - which keeps track of the median for a stream of numbers, 
#   updating the median for each new number.  
#
#  Please let me know if this is does not work or does not meet your coding standard. 
#  Since I am going through final, I spent very little time coding for this
#  I can spend more time next week to make the code cleaner and robust
#
##########################################################################################
import math
import glob


def txtReader(thisfile):
    '''
    Reads txt file, and save
    '''
    thisList={}
    with open(thisfile,'r')  as f:
         thisList[thisfile]=[]
         for line in f:
             thisNum= float(len(line.strip("\n").split(" ")))
             thisList[thisfile].append(thisNum)
       
             #print thisNum
         #print ""
         #med =  sum(thisList)/len(thisList)
      
    return thisList

          

if __name__ == '__main__': 
      thisList={}
      for thisFile in sorted(glob.glob("wc_input/*.txt")):
          thisList[thisFile]=txtReader(thisFile)
      
      thisL=[]
      for v in thisList.values():
          for i in v.values():
              for z in i:
                  thisL.append(z)
                  
      med = sum(thisL)/float(len(thisL))      
      with open('wc_output/med_result.txt', 'w') as outfile:
             [outfile.write("{0}\n".format(i)) for i in thisL]
             outfile.seek(0,2)
             outfile.writelines("\n%.1f" %med)
   