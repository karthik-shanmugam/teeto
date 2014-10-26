#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ShanmM01
#
# Created:     31/03/2014
# Copyright:   (c) ShanmM01 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def count(page,element):
    count=0
    size=len(element)
    if size==0:
        return 0
    readingIndex=0
    for char in page:
        if readingIndex==0:
            if char==element[0]:
                if readingIndex+1>=size:
                    count=count+1
                    readingIndex=0
                else:
                    readingIndex=readingIndex+1
        else:
            if char==element[readingIndex]:
                if readingIndex+1>=size:
                    count=count+1
                    readingIndex=0
                else:
                    readingIndex=readingIndex+1
            else:
                readingIndex=0
    return count

def countMany(page,elements):
    counts=[0]*len(elements)


def countTeemosInThread(url):
    print(url)
    pageData=str(urllib.request.urlopen(url).read())
    total=0
    page=1
    default=-1
    morePages=True
    if count(pageData,"Invalid Thread specified. The Thread might have been deleted.")>0:
        print("invalid")
        return default
    while morePages:
        #print (page)
        try:
         teemos=count(pageData.lower(),"nerf")
         #print(" "+str(teemos))
         total=total+teemos
         page=page+1
         if count(pageData,"page="+str(page))==0:
            morePages=False
         else:
            newAddress=url+"&page="+str(page)
            pageData=str(urllib.request.urlopen(newAddress).read())
        except:
           morePages=False
    return total

def countTeemos(url):
    pageData=str(urllib.request.urlopen(url).read())
    return count(pageData.lower(),"teemo")

def generateThreadID():
    return random.randint(1,4398516)

def countRealThreads(i):
    total=0
    while(i>0):
        temp=countTeemosInThread("http://forums.na.leagueoflegends.com/board/showthread.php?t="+str(generateThreadID()))
        if temp==-1:
            pass
        else:
            total=temp+total
            i=i-1
    return total








baseUrl='http://wikipedia.org'
import random
import time
import urllib.request
t1 = time.time()
count=countRealThreads(100)
print ("done")
print (str(count))
print (str(time.time()-t1))
