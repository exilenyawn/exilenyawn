import os
import re
import random
##IP Whois
ip_whois = dict()
try:
  f = open("ip_whois.txt", "r")
  ip_whois = eval(f.read())
  f.close()
except:pass
 
##SessionId Whois
sid_whois = dict()
try:
  f = open("sid_whois.txt", "r")
  sid_whois = eval(f.read())
  f.close()
except:pass
 
 
 
def whois(term, args):
    uid = term
    if len(uid) > 0:
        pair = []
        args = str(args)
        if args not in uid: return None
        for i in uid:
          if i == args:
            pass
          else:
            for z in uid[i]:
              for g in uid[args]:
                if g == z and g != '':
                  if i not in pair:
                    pair.append(i)
        if len(pair) > 0:
          return (", ".join(pair))
        else:
          return None
    else:
      return None
 
#uid = {'orx':[44554455, 44334433, 33443344, 44334433], 'moth':[44334433, 22332233, 33223322], 'cole':[22332233,11221122], 'leo':[33443344, 44554455, 88778877], 'abs':[44554455, 88778877, 22332233]}
#def getAlias(args):
#    print("Currently known alias
