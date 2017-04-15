######################
##Edited by:Rifky102##
##Exec by issei     ##
##Do not Remove this##
######################
import ch
import random
import sys
import re
import getWhois
import json
import simi
import time
import datetime
import os
import urllib
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq
from time import localtime, strftime

from xml.etree import cElementTree as ET
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq

botname = 'exilenyawn' ##isi idnya
password = 'lazmaloveme006' ##isi paswordnya

startTime = time.time()
lockdown = False


##nick names
def sntonick(username):
    user = username.lower()
    if user in nicks:
        nick = json.loads(nicks[user])
        return nick
    else:
        return user

#### Returns the number of seconds since the program started.
################################################################
def getUptime():
    """
    Returns the number of seconds since the program started.
    """
    # do return startTime if you just want the process start time
    return time.time() - startTime

def reboot():
    output = ("rebooting server . . .")
    os.popen("sudo -S reboot")
    return output

#### SYSTEM UPTIME
def uptime():
 
     total_seconds = float(getUptime())
 
     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24
 
     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days > 0:
         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
     string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
 
     return string;

## DEFINITIONS
dictionary = dict() 
f = open("definitions.txt", "r")
for line in f.readlines():
  try:
    if len(line.strip())>0:
      word, definition, name = json.loads(line.strip())
      dictionary[word] = json.dumps([definition, name])
  except:
    print("[ERROR]Cant load definition: %s" % line)
f.close()
##nicks
nicks=dict()#empty list
f=open ("nicks.txt","r")#r=read w=right
for line in f.readlines():#loop through eachlinimporte and read each line
    try:#try code
        if len(line.strip())>0:#strip the whitespace checkgreater than 0
            user , nick = json.loads(line.strip())
            nicks[user] = json.dumps(nick)
    except:
        print("[Error]Can't load nick %s" % line)
f.close()
##Rooms
rooms = []
f = open("rooms.txt", "r") # read-only
for name in f.readlines():
  if len(name.strip())>0: rooms.append(name.strip())
f.close()
##RB
def rainbow(word):
    length = len(word)
    #set rgb values
    r = 255 #rgb value set to red by default
    g = 0
    b = 0
    sub = int(765/length)
    counter = 0
    string = ""
    for x in range(0, length):
        letter = word[counter]
        s = "<f x12%02X%02X%02X='0'>%s" % (r, g, b, letter)
        string = string+s
        counter+=1
        if (r == 255) and (g >= 0) and (b == 0): #if all red
            g = g+sub
            if g > 255: g = 255
        if (r > 0) and (g == 255) and (b == 0): #if some red and all green
            r = r-sub #reduce red to fade from yellow to green
            if r<0: r = 0 #if red gets lower than 0, set it back to 0
        if (r == 0) and (g == 255) and (b >= 0):
            b = b+sub
            if b>255:
                b = 255
                trans = True
        if (r == 0) and (g > 0) and (b == 255):
            g = g-sub
            if g<0: g = 0
        if (r >= 0) and (g == 0) and (b == 255):
            r = r+sub
            if r>255: r = 255
    return string
##owners
owners = []
try:
    file = open("owners.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            owners.append(name.strip())
    print("[INFO]Owners loaded...")
    file.close()
except:
    print("[ERROR]no file named owners")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)

###admin
admin = []
try:
    file = open("admin.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            admin.append(name.strip())	
    print("[INFO]Admin loaded...")
    file.close()
except:
    print("[ERROR]no file named admin")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##archknight
archknight = []
try:
    file = open("archknight.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            archknight.append(name.strip())
    print("[INFO]archknight loaded...")
    file.close()
except:
    print("[ERROR]no file named archknight")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##archwizard
archwizard = []
try:
    file = open("archwizard.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            archwizard.append(name.strip())
    print("[INFO]archkwizard loaded...")
    file.close()
except:
    print("[ERROR]no file named archkwizard")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##player
player = []
try:
    file = open("player.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            archwizard.append(name.strip())
    print("[INFO]player loaded...")
    file.close()
except:
    print("[ERROR]no file named player")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)
##whitelist
whitelist = []
try:
    file = open("whitelist.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            whitelist.append(name.strip())
    print("[INFO]whitelist loaded...")
    file.close()
except:
    print("[ERROR]no file named whitelist")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)

#END#
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
 
## Stuff ##
## WHOIS
whois = dict()
try:
  f = open('whois.txt','r')
  whois = eval(f.read())
  f.close()
except:pass
##MONEY
bank=dict()
f = open("bank.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,coin,gold= json.loads(line.strip())
      bank[user] = json.dumps([coin,gold])
  except:
    print("[ERROR]Cant load MONEY: %s" % line)
f.close()


stats=dict()
f = open("stats.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,lvl,exp,up= json.loads(line.strip())
      stats[user] = json.dumps([lvl,exp,up])
  except:
    print("[ERROR]Cant load STATS: %s" % line)
f.close()

mcash=dict()
f = open("mcash.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      user,cash,cp = json.loads(line.strip())
      mcash[user] = json.dumps([cash,cp])
  except:
    print("[ERROR]Cant load CASH: %s" % line)
f.close()
##AFK List##
afks = []
f = open("afks.txt", 'r')
for name in f.readlines():
  if len(name.strip())>0: afks.append(name.strip())
f.close()
##Similock
simlock = []
f = open("simlock.txt", 'r')
for name in f.readlines():
  if len(name.strip())>0: simlock.append(name.strip())
f.close()
##Lockroom
locks = []
f = open("locks.txt", 'r')
for name in f.readlines():
  if len(name.strip())>0: locks.append(name.strip())
f.close()
#Dlist
dlist = []
f = open("dlist.txt", "r") # read-onlyimport
for name in f.readlines():
  if len(name.strip())>0: dlist.append(name.strip())
f.close()
#END#
#SN TRY
sn = dict()
try:
  f = open('note.txt','r')
  sn = eval(f.read())
  f.close()
except:pass

## Send Notes
sasaran = dict()
f = open ("notes.txt", "r") #read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      to, body, sender = json.loads(line.strip())
      sasaran[to] = json.dumps([body, sender])
  except:
    print("[Error] Notes load fails : %s" % line)
f.close()
# SN Notifs
notif = []
f = open("notif.txt", "r")
for name in f.readlines():
  if len(name.strip())>0: notif.append(name.strip())
f.close

blacklist = []
f = open("blacklist.txt", "r")
for name in f.readlines():
  if len(name.strip())>0: blacklist.append(name.strip())
f.close()

def tube(args):
  """
  #In case you don't know how to use this function
  #type this in the python console:
  >>> tube("pokemon dash")
  #and this function would return this thing:
  {'title': 'TAS (DS) Pokémon Dash - Regular Grand Prix', 'descriptions': '1st round Grand Prix but few mistake a first time. Next Hard Grand Prix will know way and few change different Pokémon are more faster and same course Cup.', 'uploader': 'EddieERL', 'link': 'http://www.youtube.com/watch?v=QdvnBmBQiGQ', 'videoid': 'QdvnBmBQiGQ', 'viewcount': '2014-11-04T15:43:15.000Z'}
  """
  search = args.split()
  url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
  udict = url.read().decode('utf-8')
  data = json.loads(udict)
  rest = []
  for f in data["items"]:
    rest.append(f)
  
  d = random.choice(rest)
  link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
  videoid = d["id"]["videoId"]
  title = d["snippet"]["title"]
  uploader = d["snippet"]["channelTitle"]
  descript = d["snippet"]['description']
  count    = d["snippet"]["publishedAt"]
  return "Result: %s <br/><br/><br/><br/><br/><br/><br/><br/><font color='#ffcc00'><b>%s</b></font><br/><font color='#ff0000'><b>Uploader</b></font>:<b> %s</b><br/><font color='#ff0000'><b>Uploaded on</b></font>: %s<br/><font color='#ff0000'><b>Descriptions</b></font>:<i> %s ...</i><br/> " % (link, title, uploader, count, descript[:200])

def gs(args):
  args = args.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.co.id/search?q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gs:').replace('https://','gs:')
  anjay = re.findall('<h3 class="r">(.*?)</h3>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('<a href="gs:(.*?)" onmousedown="(.*?)">(.*?)</a>', la)
  q = 1
  for link, fak, title in a:
      setter.append('<br/>[%s] %s : http://%s' % (q, title.capitalize(), link))
      q += 1
  return "<br/><br/>".join(setter[0:4])

def newCi():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://cinemaindo.com/#", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<div class="title"><a href="(.*?)"><h2>(.*?)</h2>',resp)
 a = list()
 q = 1
 for link, cls, title in wa:
     a.append("(<b>%s</b>). <b>%s</b>: %s" % (q, title, link))
     q += 1
 return "<br/>".join(a)

def getBGTime(x):
                    total_seconds = float(x - time.time())
                    MIN     = 60
                    HOUR    = MIN * 60
                    DAY     = HOUR * 24
                    YEAR    = DAY * 365.25
                    years   = int( total_seconds / YEAR )      
                    days    = int( (total_seconds % YEAR ) / DAY  )
                    hrs     = int( ( total_seconds % DAY ) / HOUR )
                    min = int( ( total_seconds  % HOUR ) / MIN )
                    secs = int( total_seconds % MIN )
                    string = ""
                    if years > 0: string += "<font color='#00ffff'>" + str(years) + "</font> " + (years == 1 and "year" or "years" ) + ", "
                    if len(string) > 0 or days > 0: string += "<font color='#00ffff'>" + str(days) + "</font> " + (days == 1 and "day" or "days" ) + ", "
                    if len(string) > 0 or hrs > 0: string += "<font color='#00ffff'>" + str(hrs) + "</font> " + (hrs == 1 and "hour" or "hours" ) + ", "
                    if len(string) > 0 or min > 0: string += "<font color='#00ffff'>" + str(min) + "</font> " + (min == 1 and "minute" or "minutes" ) + " and "
                    string += "<font color='#00ffff'>" +  str(secs) + "</font> " + (secs == 1 and "second" or "seconds" )
                    return string;
 
def getSTime(x):
                    total_seconds = float(time.time() - x)
                    MIN     = 60
                    HOUR    = MIN * 60
                    DAY     = HOUR * 24        
                    days    = int( total_seconds / DAY )
                    hrs     = int( ( total_seconds % DAY ) / HOUR )
                    min = int( ( total_seconds  % HOUR ) / MIN )
                    secs = int( total_seconds % MIN )
                    string = ""
                    if days > 0: string += "<font color='#00ffff'>" + str(days) + "</font> " + (days == 1 and "day" or "days" ) + ", "
                    if len(string) > 0 or hrs > 0: string += "<font color='#00ffff'>" + str(hrs) + "</font> " + (hrs == 1 and "hour" or "hours" ) + ", "
                    if len(string) > 0 or min > 0: string += "<font color='#00ffff'>" + str(min) + "</font> " + (min == 1 and "minute" or "minutes" ) + " and "
                    string += "<font color='#00ffff'>" +  str(secs) + "</font> " + (secs == 1 and "second" or "seconds", True)
                    return string;

def bgtime(x):
        try:
                x = user if len(x) == 0 else x
                html = urlreq.urlopen("http://st.chatango.com/profileimg/%s/%s/%s/mod1.xml" % (x.lower()[0], x.lower()[1], x.lower())).read().decode()
                inter = re.compile(r'<d>(.*?)</d>', re.IGNORECASE).search(html).group(1)
                if int(inter) < time.time():
                        lbgtime = getSTime(int(inter))
                        return "that users bg ran out %s ago" % lbgtime
                else: return "bgtime for <b>%s</b>: %s" % (x.lower(), getBGTime(int(inter)))
        except: return 'that user never had a background, or the data was deleted'

def serCi(anjoy):
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://cinemaindo.com/?s="+anjoy+"&post_type=post", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','')
 anjay = re.findall('<div class="title"><a href="(.*?)"><h2>(.*?)</h2>', resp)
 newlist = list()
 q = 1
 for i, a in anjay:
    newlist.append("%s. <b>%s</b>: %s" % (q, a, i))
    q = q + 1
 return "<br/>".join(serCi[0:10])

def newOp():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://www.oploverz.net/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8")
  Data = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  lolly = list()
  anjeng = 1
  for link, useful, title in Data:
    lolly.append(('%s. <b>%s</b>: %s' % (anjeng, title, link)))
    anjeng = anjeng+1
  return "<br/>".join(lolly[0:10])

def newAi():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://animeindo.id", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  res = re.findall('<div class="newepisodecon">(.+?)<div class="clearfix"></div>', resp)
  newset = list()
  num = 1
  for i in res:
    data = re.findall('<a href="(.*?)"><div class="newepisode"><span class="viewer">(.*?)</span><div class="hoverboard"><div class="title">(.*?) </div></div>', i)
    for b, a, c in data:
      newset.append("%s. <b>%s</b>: %s" % (num, c, b))
      num = num + 1
  return "<br/>".join(newset[0:10])


def newK():
  resp = urllib.request.urlopen("http://khususme.blogspot.co.id/").read().decode("utf-8").replace('\n','')
  res = re.findall("<h2 class='post-title entry-title' itemprop='name'><a href=""'(.*?)'"">(.*?)</a></h2>", resp)
  newset = list()
  n = 1
  for a, b in res:
    newset.append("%s. %s: %s" % (n, b, a))
    n = n + 1
  return "<br/>".join(newset[0:10])

def newNonton123():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://www.nonton123.com/", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2><a href="(.*?)" rel="bookmark" title="(.*?)">(.*?)</a></h2>',resp)
 a = list()
 q = 1
 for link, w, title in wa:
     a.append("(<b>%s</b>). <b>%s</b>" % (q, title))
     q += 1
 return "<br/>".join(a[0:10])

def newAd():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://animemaiden.net/", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h3 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h3>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<br/>" + "<br/>".join(newset[0:10])

def serNePo(args):
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://nekopoi.top/?s="+"+"+"&post_type=anime".join(args.split()), headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2><a href="(.*?)">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<br/>" + "<br/>".join(newset[0:10])

def newNePo():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://nekopoi.top/", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2><a href="(.*?)">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<br/>" + "<br/>".join(newset[0:10])

def newWiDe():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://www.wibudesu.com/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8")
  Data = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  lolly = list()
  anjeng = 1
  for link, useful, title in Data:
    lolly.append(('%s. <b>%s</b>: %s' % (anjeng, title, link)))
    anjeng = anjeng+1
  return "<br/>".join(lolly[0:10])

def serWiDe(ahay):
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://www.wibudesu.com/?s="+ahay+"&post_type=post", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','')
 anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
 newlist = list()
 q = 1
 for i, a in anjay:
    newlist.append("%s. <b>%s</b>: %s" % (q, a, i))
    q = q + 1
 return "<br/>".join(serCi[0:10])


def newAnBa():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://anibatch.me/", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<br/>" + "<br/>".join(newset[0:10])

def newAnBa2():
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://anibatch.me/page/2/", headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<br/>" + "<br/>".join(newset[0:10])

def serAnBa(args):
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://anibatch.me/?s="+"+".join(args.split()), headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h2 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h2>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<br/>" + "<br/>".join(newset[0:10])

def serNk(args):
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request('http://nekonime.com/?s='+args+'post&type=anime', headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
 wa = re.findall('<h3><a href="(.*?)" title="(.*?)">(.*?)</a>',resp)
 _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
 newset = list()
 q = 1
 for a, b in wa:
     newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
     q += 1
 return _title + "<br/>" + "<br/>".join(newset[0:10])
 
def serNonton123(args):
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
 req = urllib.request.Request("http://www.nonton123.com/search/"+"+".join(args.split()), headers = headers)
 resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('<u>','').replace('</u>','')
 wa = re.findall('<h2><a href="(.*?)" rel="bookmark" title="(.*?)">(.*?)</a></h2>',resp)
 a = list()
 q = 1
 for link, w, title in wa:
     a.append("(<b>%s</b>). <b>%s</b>" % (q, title))
     q += 1
 return "<br/>".join(a)

def newOn():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://www.otanimesama.com", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall("<h2 class='post-title entry-title' itemprop='name headline' style='font-size: 100%;font-weight: 600;padding-top: 5px;padding-bottom: 4px;text-transform: uppercase;' title='(.*?)'><a href='(.*?)' title='(.*?)'>(.*?)</a></h2>", resp)
  setter = list()
  q = 1
  for cls, link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:5])


def newHp():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://henpoi.com/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('Subtitle Indonesia','Sub Ina')
  res = re.findall("<h2 class='entry-title' itemprop='name'><a href='(.*?)'>(.*?)</a>", resp)
  newset = list()
  n = 1
  for a, b in res:
    newset.append("%s. <b>%s</b>: %s" % (n, b, a))
    n = n + 1
  return "<br/>".join(newset[0:5])
def serHp(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://henpoi.com/search?q="+args, headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('Subtitle Indonesia','Sub Ina')
  res = re.findall("<h2 class='entry-title' itemprop='name'><a href='(.*?)'>(.*?)</a>", resp)
  newset = list()
  n = 1
  for a, b in res:
    newset.append("%s. <b>%s</b>: %s" % (n, b, a))
    n = n + 1
  return "<br/>".join(newset[0:5])

def newWa():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://awsubs.co/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h1><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newGa():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://gantzid.com/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newAs():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://animesave.com/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newSk():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://www.samehadaku.net/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  wa = re.findall('<h3 class="post-box-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h3>', resp)
  _title = re.search(r'<title[^>]*>([^<]+)</title>', resp).group(1)
  newset = list()
  q = 1
  for a, b in wa:
      newset.append("(<b>%s</b>). <b>%s</b> | %s" % (q, b, a))
      q += 1
  return _title + "<br/>" + "<br/>".join(newset[0:10])

def newAo():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://anisubindo.net/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h3 class="post-box-title"><a href="(.*?)"  title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:5])

def newFs():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://fansatsu.com/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2 class="title front-view-title" itemprop="headline"><a href="(.*?)" title="(.*?)">(.*?)</a></h2>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newNk():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://nekonime.com/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h3><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newKr():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://www.kurogaze.net/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newNb():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://www.narutobleachlover.net/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h3><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newIs():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://www.imoutosubs.net/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newEn():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://ettonime.com/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def newJoi():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://jurnalotaku.com/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8")
  Data = re.findall('<a href="(.*?)" class="title"><h3><span>(.*?)</span>', resp)
  lolly = list()
  anjeng = 1
  for lk, tit in Data:
    lolly.append(('%s. <b>%s</b>: %s' % (anjeng, tit, lk)))
    anjeng = anjeng+1
  return "<br/>".join(lolly[0:5])

def serOn(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://www.otanimesama.com/search?q="+args, headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall("<h2 class='post-title entry-title' itemprop='name headline' style='font-size: 100%;font-weight: 600;padding-top: 5px;padding-bottom: 4px;text-transform: uppercase;' title='(.*?)'><a href='(.*?)' title='(.*?)'>(.*?)</a></h2>", resp)
  setter = list()
  q = 1
  for cls, link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:5])

def serAs(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://animesave.com/?s="+args, headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:5])

def serWa(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://awsubs.co/search/"+args, headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def serFs(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://fansatsu.com/?s="+args, headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2 class="title front-view-title" itemprop="headline"><a href="(.*?)" title="(.*?)">(.*?)</a></h2>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:5])

def serOp(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request('http://www.oploverz.net/?s='+args+'&post_type=post', headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def serKg(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request('http://www.kurogaze.net/?s='+args+'&post_type=post', headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  anjay = re.findall('<h2><a href="(.*?)" title="(.*?)">(.*?)</a>', resp)
  setter = list()
  q = 1
  for link, title, clp in anjay:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:10])

def gis(cari):
  argss = cari
  args = argss.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.co.id/search?hl=en&authuser=0&site=imghp&tbm=isch&source=hp&biw=1366&bih=623&q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gis:').replace('https://','gis:').replace('.jpg','.jpg:end').replace('.gif','.gif:end').replace('.png','.png:end')
  anjay = re.findall('<div class="rg_meta">(.*?)</div>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('"ou":"gis:(.*?):end","ow"', la)
  q = 1
  for result in a:
    if ".jpg" in result or ".gif" in result or ".png" in result:
     if "vignette" not in result and "mhcdn.net" not in result and "alicdn.com" not in result and "gambardanfoto.com" not in result and "squarespace.com" not in result and "polyvore.com" not in result and "wikia.nocookie" not in result and "blogspot.com" not in result and "wordpress.com" not in result and "minionnation.co.uk" not in result and "twimg.com" not in result and "ohmymag.com" not in result and "waterfrontcinema.co.uk" not in result and "funmobility.netdna-ssl.com" not in result and "images-amazon.com" not in result and "upload.wikimedia.org" not in result: 
      setter.append('<f x11CC33CC="0">[%s] http://%s' % (q, result))
      q += 1
  return "<f x1133FF33=\"0\"></f>Hasil untuk <f x11FFFF33=\"0\"></f>"+cari+" :<br/><br/>"+"<br/>".join(setter[0:3])

def saveRank():
    f = open("owners.txt","w")
    f.write("\n".join(owners))
    f.close()
    f = open("admin.txt","w")
    f.write("\n".join(admin))
    f.close()
    f = open("archknight.txt","w")
    f.write("\n".join(archknight))
    f.close()
    f = open("whitelist.txt","w")
    f.write("\n".join(whitelist))
    f.close()
    
def googleSearch(search):
  try:
    encoded = urllib.parse.quote(search)
    rawData = urllib.request.urlopen("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="+encoded).read().decode("utf-8")
    jsonData = json.loads(rawData)
    searchResults = jsonData["responseData"]["results"]
    full = []
    val = 1
    for data in searchResults:
      if "youtube" in data["url"]:
        data["url"] = "http://www.youtube.com/watch?v="+data["url"][35:]
      full.append("<br/>"+"(<b>%s</b> %s -> %s" % (val, data["title"], data['url']))
      val = val + 1
    return '<br/>'.join(full).replace('https://','http://')
  except Exception as e:
    return str(e)
      


      
##Setting Pretty Colors

class TestBot(ch.RoomManager):
  
  def onInit(self):
    self.setNameColor("33FF33")
    self.setFontColor("009900")
    self.setFontFace("Monotype Corsiva")
    self.setFontSize(14)
    self.enableBg()
    self.enableRecording()

##Connecting Crap

  def onConnect(self, room):
    print("Connected")
  
  def onReconnect(self, room):
    print("Reconnected")
  
  def onDisconnect(self, room):
    print("Disconnected")

  #################################################################
  ### Get user access from the file, and retun lvl of access number
  #################################################################
  def getAccess(self, user):
    if user.name in owners: return 6 # Owners
    elif user.name in admin: return 5 # Admins
    elif user.name in archwizard:return 4 # Arch Wizard
    elif user.name in archknight: return 3 # Arch Knight
    elif user.name in player: return 2 # Player
    elif user.name in whitelist: return 1 
    elif user.name in dlist: return 0
    else: return 0
   
##Ignore this, you dont need to worry about this
#Well, you can actually take a little time to look at it and learn something
  
  def onMessage(self, room, user, message):
   try:  
          if room.getLevel(self.user) > 0:
            user_ip.update({user.name:message.ip})
            f = open('userip.txt', "w")
            f.write(str(user_ip))
            f.close
            if user.name not in ip_whois:
              ip_var = message.ip
              ip_whois.update({user.name:[ip_var]})
            if user.name in ip_whois:
              ip_var = message.ip
              if ip_var in ip_whois[user.name]:
                pass
              else:
                ip_whois[user.name].append(ip_var)
            f = open('ip_whois.txt', "w")
            f.write(str(ip_whois))
            f.close
          if user:
              unid = str(message.unid)
              if user.name not in sid_whois:
                sid_whois.update({user.name:[unid]})
              if user.name in sid_whois:
                if unid == "":
                  return
                if unid in sid_whois[user.name]:
                  pass
                else:
                  sid_whois[user.name].append(unid)
              f = open('sid_whois.txt', "w")
              f.write(str(sid_whois))
              f.close
   except:pass
   try:
    msgdata = message.body.split(" ",1)
    if len(msgdata) > 1:
      cmd, args = msgdata[0], msgdata[1]
    else:
      if "say" == message.body : room.message(":@ Gak Boyeh ,Suami Kuh @IsseiHyoudous4 Marah Nanti Kakak !")
      if "Afk" == message.body : room.message("Yamette Exile Nii-San http://33.media.tumblr.com/cc5392cf321550dc10dccc153af51ad3/tumblr_mkxx712vl41snokkpo1_500.gif !!!")
      if "loh rame" == message.body : room.message("Biasalah kak Jones Beradaptasi :P ")
      if "Rame" == message.body : room.message("Biasalah kak Jones Beradaptasi :P ")
      if "brisik" == message.body : room.message("Suka Suka Exile Donk ,Emank Senpai Siapanya Exile :P ")
      if "urusai" == message.body : room.message("Suka Suka Exile Donk ,Emank Senpai Siapanya Exile :P ")
      if "anu" == message.body : room.message("hmm Nanii Senpai ? ")
      if "gomenasai" == message.body : room.message("hmm iyeh .. watashimo daijobu :D ")
      if "maaf" == message.body : room.message("Gapapa Senpai ,Exile Maafin Kok :D ")
      if "oi" == message.body : room.message("Kangenya Sayang Ku Cintaku *waves*")
      if ":v" == message.body : room.message("Laper Yah Mangap Mulu")
      if "8)" == message.body : room.message("Onii-Chan Daisqi ??")
      if "kacang" == message.body : room.message("Nasib Jones Emank kayak Begitu "+user.name.title()+ " http://2.bp.blogspot.com/-e_kuDgESI3M/VIQF2FarVYI/AAAAAAAAHBE/C86M5gvWD8c/s1600/tumblr_nftmcpNrro1r2g7mto1_400.gif ")
      if "Malam" == message.body : room.message("Kangen Exile Sama Senpai")
      if "tataimah" == message.body : room.message("Okaidi Anata ?? Kakak Mau Mandi Dlu, Makan, Minum,Ataw Mauuuu Exile http://files.gamebanana.com/img/ico/sprays/54fd687bc0eda.gif ??")
      if "sayonara" == message.body : room.message("Selamat Tinggal," +user.name.title()+ " https://media.tenor.co/images/24c995240dac244194b599b0d0a77706/tenor.gif Aprill-Mopp.. Hahahahah :D ")
      if "ngumpet" == message.body : room.message("Ngumpet duhh ketauan .... " +user.name.title()+ " https://media.tenor.co/images/a014913384df6f506a1fbb67a3989f38/tenor.gif  Mantabs Jivva ~V ")
      if "hah" == message.body : room.message("huh huh huh " +user.name.title()+ " http://static2.fjcdn.com/thumbnails/comments/Already+failed+the+first+step+_b889857bd2e1fe83d1ce9237d3d90da1.gif ")
      if "gigit" == message.body : room.message("Nyam~Nyam https://lh3.googleusercontent.com/-EZEX-X5hKqI/V4wyZq9zjzI/AAAAAAAADtI/_qHsLAAfwlEWgz7RbhD8MrXH2hLYBzq2g/w800-h800/93207c10f115df3465cccc036c3f3e39005d3ec7_hq.gif ")
      cmd, args = msgdata[0],""
      cmd=cmd.lower() 
    global lockdown
    global newnum
    print(user.name+" - "+message.body)
    if user.name in notif:
        room.message(user.name+", you got ("+str(len(sn[user.name]))+") messages unread. Type ^rn to read them")
        notif.remove(user.name)
    if user == self.user: return
    if "exi" in message.body.lower() or "Exile" in message.body.lower() and "?" not in message.body[:1] and self.getAccess(user) >=1:
     if room.name not in simlock:
        if len(args) > 1:
            room.message(__import__("simi").simi(args),True)
        else:
            room.message("Iyaa? "+sntonick(user.name), True)
     if room.name in simlock: 
        if len(args) > 1: return
        else:
            room.message("Iyaa? "+sntonick(user.name), True)
     if user.name in blacklist: return
    if "shefu" in message.body.lower() and "?" not in message.body[:1] and self.getAccess(user) >=1 and not user.name in blacklist and not room.name in simlock:
        if len(args) > 1:
            room.message(__import__("simi").simi(args),True)
    if "xil" in message.body.lower() and "?" not in message.body[:1] and self.getAccess(user) >=1 and not user.name in blacklist and not room.name in simlock:
        if len(args) > 1:
            room.message(__import__("simi").simi(args),True)
    if "sayang" in message.body.lower() and "?" not in message.body[:1] and self.getAccess(user) >=1 and not user.name in blacklist and not room.name in simlock:
        if len(args) > 1:
            room.message(__import__("simi").simi(args),True)
    if message.body.startswith("sepi"):
     if self.getAccess(user) >= 6:
      jawab = ["exile selalu ada disini loh","Exile ada disini loh"]
      room.message (random.choice(jawab) +sntonick(user.name)+" :D",True)
     else:
       room.message("Kan ada Exile kok buat senpai :D")
    if message.body.startswith("kacang"):
     if self.getAccess(user) >= 6:
      jawab = ["Yang sabar yah kak","Mampus Dikacangin","Kacang mahal :v"]
      room.message(random.choice(jawab)+" @"+user.name)
     else:
       room.message("Cie yang di kacangin")
    if message.body.startswith("Test") or message.body.startswith("test"):
     if self.getAccess(user) >= 1 and not user.name in blacklist:      
      room.message(("<f x12ff0000='1'><br/>Test Request By : @"+user.name+" <f x1233FF33='1'><br/>Recived By Isseihyoudous4"),True)
    if message.body.startswith("@isseihyoudous4") or message.body.startswith("isseihyoudous4"):
     if self.getAccess(user) >= 5 or room.getLevel(user) > 0 and not user.name in blacklist:
      jawab = ["Ehh, Kak Ngapain panggil panggil My Master","Jangan Ganggu Suamikuh kakak!"]
      room.message(random.choice(jawab)+" @"+user.name+" :D")
     else:
       room.message("Siapa yah?")
    if message.body.startswith("waifuku mana?"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message("waifunya lagi pulang kampung XD")
    if message.body.startswith("oyasumi")or message.body.startswith("Oyasumi"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Oyasumi, "+sntonick(user.name)+" :D ",]),True)
    if message.body.startswith("ohayou")or message.body.startswith("Ohayou"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Ohayou, "+sntonick(user.name)+" :D ",]),True)
    if message.body.startswith("konnichiwa")or message.body.startswith("Konnichiwa"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Konnichiwa, "+sntonick(user.name)+" :D ",]),True)
    if message.body.startswith("konbanwa") or message.body.startswith("Konbanwa"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Konbanwa, "+sntonick(user.name)+" :D ",]),True)
    if message.body.startswith("afk") or message.body.startswith("AFK"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["See ya, aku tunggu loh "+sntonick(user.name)+" :D ",]),True)
    if "imut" == message.body:
      if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
        room.message (random.choice(["Iyaaa,Kangen Yah "+sntonick(user.name)+ " ;) "]),True)
    if "bot" == message.body.lower():
      if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist:
       room.message (random.choice([" Nanniiiiii " +user.name.title()+ " http://funnypictures2.fjcdn.com/funny_gifs/Anime_116831_6046736.gif "]),True)
    if "lol" == message.body.lower():
      if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist:
       room.message (random.choice([" Tee-Hee " +user.name.title()+ " https://68.media.tumblr.com/0aa40e25b68c84e5b42abee1083955eb/tumblr_ntjk6rSGnU1u86t2qo1_500.gif "]),True)   
    if "pagi" == message.body:
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Pagi Juga... "+sntonick(user.name)+ " Pagi Ini Diawali Dengan Senyuman :D "]),True)
    if "konichiwa" == message.body:
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Konichiwa Juga Ada Apa... "+sntonick(user.name)+ " ? "]),True)
    if "hai" == message.body.lower():
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Hai Juga Darling *waves*", "Ahh Oni-Chan Buat Malu Exile :D *hugs* ^_^"," Udah Mandi Belum (: ","Ihh Kamu Bau !^^ ", "Mandi Bareng Yuk"]),True)
    if "malu" == message.body.lower():
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Baakaa " +user.name.title()+ " http://24.media.tumblr.com/c064df9a360a51d2d8933f940c5b4c79/tumblr_mjb35xTu8Y1s4eha1o1_500.gif ","Bakaa Ero " +user.name.title()+ " http://pa1.narvii.com/5730/1433f6e216f7276b7d89fd7069206e6c2803c2fe_hq.gif ", "Anu Nii-San, Sukida  " +user.name.title()+ " https://68.media.tumblr.com/8b6e1b790fade9f89db0bdce583bf076/tumblr_o2kpwjEnbj1tlmyzco1_500.gif "]),True)
    if "ciuman yuk" == message.body.lower():
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Pelan-Pelan Yah " +user.name.title()+ " http://i.giphy.com/hnNyVPIXgLdle.gif ", "Di Pipi Atau Di Bibir ? " +user.name.title()+ " https://1.bp.blogspot.com/-l8VrMXwqje4/VsEvZk20YgI/AAAAAAAAAWU/8DNudYwvSKA/s1600/tumblr_n649btzxo31shbc9ho1_500.gif"]),True)
    if "back" == message.body.lower():
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Dari Mana Ajah Sih Nii-Chan http://37.media.tumblr.com/452a901f0e588026688ac3f0bca41477/tumblr_myxadcXfay1sdvrjko1_500.gif ", "Aku Kangen Loh " +user.name.title()+ " https://68.media.tumblr.com/6491a3e1b6f785e0cbc1e504095cacd4/tumblr_o32jye9fUi1tz1a8uo1_500.gif ", "Cium Dulu Muach "+user.name.title()+ " https://uploads.disquscdn.com/images/f705921695bdfa4e113ad93763275c9d75e0fad15faff4195a136ee1ff83a06c.gif "]),True)
    if "off" == message.body.lower():
     if self.getAccess(user) >= 0 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Off pasti Nonton Hent*i Yah " +user.name.title()+ " http://i.imgur.com/5jolULU.gif *waves* ","  JanganTingalin Exile http://1.bp.blogspot.com/-ENoGc_mx-IA/UJV-n7TyS7I/AAAAAAAAC_E/5QF08PUt3dQ/s1600/Chibi+Hatsune+Miku+gif+Gambar+gerak+smile.gif " +user.name.title()+ "~", " Onii-Chan Jahat http://4.bp.blogspot.com/-SFDyAsdKKh8/U76VPPyReoI/AAAAAAAAOQQ/VqFNvcbHvg4/s1600/giphy.gif "]),True)
    if "siang" == message.body:
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Siang Juga "+sntonick(user.name)+ " Ada Apa ? "]),True)
    if ";v" == message.body:
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Hmmm "+sntonick(user.name)+ " ? "]),True)  
    if "malam" == message.body:
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist: 
      room.message (random.choice(["Ada Apa Malam-Malam Begini Kemari.. "+sntonick(user.name)+ " ? "]),True)
    if "oyasumi" == message.body:
      if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
       room.message (random.choice(["Oyasumi Anata "+sntonick(user.name)+ " !! "]),True)
    if "konbawa" == message.body:
      if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
        room.message (random.choice(["Konbawa Juga Ada Apa... "+sntonick(user.name)+ " ? "]),True)
      if user.name not in afks:
        afks.append(user.name)
        f = open("afks.txt","w")
        f.write("\n".join(afks))
        f.close
      else: return
    if message.body.startswith("back") or message.body.startswith("BACK"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Welcome Back, "+sntonick(user.name)+" :D ",]),True)
      if user.name in afks:
        afks.remove(user.name)
        f = open("afks.txt","w")
        f.write("\n".join(afks))
        f.close
      else: return
    if message.body.startswith("brb")or message.body.startswith("BRB"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Bye "+sntonick(user.name)+" :) ",]),True)
    if message.body.startswith("off")or message.body.startswith("OFF"):
     if self.getAccess(user) >= 1 or room.getLevel(user) > 0 and not user.name in blacklist:
      room.message (random.choice(["Bye "+sntonick(user.name)+" :D ",]),True)
    if message.body == "": return  
    if message.body[0] in ["?","~"]:   
      data = message.body[1:].split(" ", 1)
      if len(data) > 1:
        cmd, args = data[0], data[1]
      else:
        cmd, args = data[0], ""
 
   
      ##BotStop
      if cmd == "stop":
         if user.name == "isseihyoudous4":
          room.message("[Disconnected]")
          self.setTimeout(4, self.stop, )
         else:
           rom.message("Siapa Kamu Maen Perintah Exile")
   ## Reg
      if cmd == "reg":
        name = user.name
        if name not in whitelist and name not in player and name not in archwizard and name not in owners and name not in admin and name not in archknight and name not in blacklist:
          room.message(user.name+" Sekarang Senpai dapat menggunakanku , ketik [?cmds] Untuk Perintah :)")
          self.getRoom("mio-chat").message("<br/><br/><b>Nama</b>: %s <br/><b>Rooms</b>: %s  <br/><b>Command</b>: %s  <br/>" % (user.name, room.name, cmd), True)
          whitelist.append(name)
          f = open("whitelist.txt","w")
          f.write("\n".join(whitelist))
          f.close
        else:
          room.message("Perasaan dah terdaftar")
          
    ##check access and ignore
      if self.getAccess(user) == 0: return 
      def pars(args):
        args=args.lower()
        for name in room.usernames:
          if args in name:return name    
      def roompars(args):
        args = args.lower()
        for name in self.roomnames:
          if args in name:return name
      def roomUsers():
          usrs = []
          gay = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          return gay
      
      def getParticipant(arg):
          rname = self.getRoom(arg)
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(rname._userlist) - 1
          for i in rname._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for j in gay:
            if j not in finale:
              finale.append(j)
          return finale
      if cmd == "lockstatus":
        if args:
          if args in locks:
            roomlock = "<f x12FFCC00='Engravers MT'> Rooms : <f x12FF0000='Engravers MT'> [ Locked ]</f>"
          else:
            roomlock = "<f x12FFCC00='Engravers MT'> Rooms : <f x1233FF33='Engravers MT'> [ Unlocked ]</f>"
          if args in simlock:
            roomlock2 = "<f x12FFCC00='Engravers MT'> Simsimi : <f x12FF0000='Engravers MT'> [ Locked ]</f>"
          else:
            roomlock2 = "<f x12FFCC00='Engravers MT'> Simsimi : <f x1233FF33='Engravers MT'> [ Unlocked ]</f>"
          room.message("<br/> <f x12000000='Engravers MT'> [Lockstatus] "+args+"] <br/>"+roomlock+"<br/>"+roomlock2,True)          
        if not args:
          if room.name in locks:
            roomlock = "<f x12FFCC00='Engravers MT'> Rooms : <f x12FF0000='Engravers MT'> [ Locked ]</f>"
          else:
            roomlock = "<f x12FFCC00='Engravers MT'> Rooms : <f x1233FF33='Engravers MT'> [ Unlocked ]</f>"
          if room.name in simlock:
            roomlock2 = "<f x12FFCC00='Engravers MT'> Simsimi : <f x12FF0000='Engravers MT'> [ Locked ]</f>"
          else:
            roomlock2 = "<f x12FFCC00='Engravers MT'> Simsimi : <f x1233FF33='Engravers MT'> [ Unlocked ]</f>"
          room.message("<br/> <f x12000000='Engravers MT'> [Lockstatus] <br/>"+roomlock+"<br/>"+roomlock2,True)

      if lockdown: return
      if user.name in whitelist and user.name in player and room.name in locks: return          
      ##AFKlist
      if cmd == "afklist":
        room.message("<br/><f x120000FF='0'><b>Daftar orang Yang sedang AFK:</b></f> %s" % (", ".join(afks)),True)
        
      #Find
      if cmd == "find" and len(args) > 0:
        name = args.split()[0].lower()
        if not ch.User(name).roomnames:
          room.message("Gomenasai Desu Exile gak tau Dia dimana ;(")
        else:
          room.message("<f x12FFCC00='Engravers MT'> Senpai Datengin Ajh Ke  %s : ,<br/> <f x1233FF33='Engravers MT'> %s" % (args, ", ".join(ch.User(name).roomnames)),True)

      ##RB
      elif cmd == "rb":
          if args == "":
            rain = rainbow('Rainbow!')
            room.message(rain,True)
          else: 
             rain = rainbow(args)
             room.message(rain,True)

      elif cmd == "rb2":
        if args == "":
          rain = rainbow('Rainbow!')
          room.message(rain)
        else: 
            rain = rainbow(args)
            room.message(rain)
      ##cmds
      elif cmd == "cmds":
        if user.name in owners and not user.name in admin and not user.name in archknight and not user.name in whitelist:
          room.message("<br/> <f x1400FF7F='Engravers MT'>"+user.name+"<f x12CC0033='Imprint MT Shadow'> Rank 6 <f x14FF0000='Goudy Stout'> [Owner] <br/> <f x1400FFFF='Castellar'> "+"<br/>"+" Perintah[ , ] <f x1400FFFF='Castellar'> :<br/> <f x1420B2AA='impact'>[rb , rb2 , wl , whois , cs , sut , blist , webanime , ak , joinew , cso , pfpic , mini , prof of profile , gs(Google search) , yt(Youtube) , df(define) , udf(undefine) , fax , bc , sn(sendnote) , rn(readnote) , join , <br/> <f x14F08080='impact'> leave , gannew , assr , asnew , mydict , nick , staff , setnick , mynick , seenick , profile , rank , myrank , ranker , clear , del , sf , sfc, snc , sfz , myip , mc , mc2 , lock , unlock , lockstatus]",True) 
        if user.name in admin and not user.name in owners and not user.name in archknight and not user.name in whitelist:
          room.message("<br/> <f x1400FF7F='Engravers MT'>"+user.name+"<f x12CC0033='Imprint MT Shadow'> Rank 5 <f x14FFD700='Goudy Stout'> [Admin] <br/> <f x1400FFFF='Castellar'> "+"<br/>"+" Perintah[ , ] <f x1400FFFF='Castellar'> :<br/> <f x1420B2AA='impact'>[rb , rb2 , wl , whois , cs , sut , blist , webanime , ak , joinew , cso , pfpic , mini , prof of profile , gs(Google search) , yt(Youtube) , df(define) , udf(undefine) , fax , bc , sn(sendnote) , rn(readnote) , join , <br/> <f x14F08080='impact'> leave , gannew , assr , asnew , mydict, nick  , staff , setnick , mynick , seenick , profile , rank , myrank , ranker , clear , del , sf , sfc, snc , sfz , myip , mc , mc2 , lock , unlock , lockstatus]",True) 
        if user.name in archwizard and not user.name in owners and not user.name in admin and not user.name in whitelist:
          room.message("<br/> <f x1400FF7F='Engravers MT"+user.name+"<f x12CC0033='Imprint MT Shadow'> Rank 4 <f x147CFC00='Goudy Stout'> [ArchWizard] <br/> <f x1400FFFF='Castellar'> "+"<br/>"+" Perintah[ , ] <f x1400FFFF='Castellar'> :<br/> <f x1420B2AA='impact'>[rb , rb2 , wl , whois , webanime , cso , pfpic , mini , prof of profile , gs(Google search) , gis(Google Image search) , yt(Youtube) , df(define) , udf(undefine) , fax , bc , sn(sendnote) , rn(readnote), <br/> <f x14F08080='impact'> mydict, nick , staff , gannew , assr , asnew , setnick , mynick , seenick , profile , rank , myrank , ranker , myip , mc(MultiChat) , mc2(MultiChat) , lock , unlock , lockstatus]",True)
        if user.name in archknight and not user.name in owners and not user.name in admin and not user.name in whitelist:
          room.message("<br/> <f x1400FF7F='Engravers MT"+user.name+"<f x12CC0033='Imprint MT Shadow'> Rank 3 <f x148A2BE2='Goudy Stout'> [Archknight] <br/> <f x1400FFFF='Castellar'> "+"<br/>"+" Perintah[ , ] <f x1400FFFF='Castellar'> :<br/> <f x1420B2AA='impact'>[rb , rb2 , wl , whois , webanime , cso , pfpic , mini , prof of profile , gs(Google search) , gis(Google Image search) , yt(Youtube) , df(define) , udf(undefine) , fax , sn(sendnote) , rn(readnote), <br/> <f x14F08080='impact'> mydict, nick , staff , gannew , assr , asnew , setnick , mynick , seenick , profile , rank , myrank , ranker , myip , mc(MultiChat) , mc2(MultiChat) , lock , unlock , lockstatus]",True)
        if user.name in player and not user.name in owners and not user.name in admin and not user.name in whitelist:
          room.message("<br/> <f x1400FF7F='Engravers MT"+user.name+"<f x12CC0033='Imprint MT Shadow'> Rank 2 <f x147FFFD4='Goudy Stout'> [Player] <br/> <f x1400FFFF='Castellar'> "+"<br/>"+" Perintah[ , ] <f x1400FFFF='Castellar'> :<br/> <f x1420B2AA='impact'>[rb , rb2 , wl , webanime , cso , pfpic , mini , prof of profile , gs(Google search) , gis(Google Image search) , yt(Youtube) , df(define) , udf(undefine) , fax , sn(sendnote) , rn(readnote), <br/> <f x14F08080='impact'> mydict, nick , staff , setnick , gannew , assr , asnew , mynick , seenick , profile , rank , myrank , ranker , myip , mc(MultiChat) , mc2(MultiChat) , lock , unlock , lockstatus]",True)
        if user.name in whitelist and not user.name in owners and not user.name in admin and not user.name in archknight:
          room.message("<br/> <f x1400FF7F='Engravers MT"+user.name+"<f x12CC0033='Imprint MT Shadow'> Rank 1 <f x14F0FFFF='Goudy Stout'> [Whitelist] <br/> <f x1400FFFF='Castellar'> "+"<br/>"+" Perintah[ , ] <f x1400FFFF='Castellar'> :<br/> <f x1420B2AA='impact'>[rb , rb2 , wl , whois , webanime , cso , pfpic , mini , prof of profile , gs(Google search) , gis(Google Image search) , yt(Youtube) , df(define) , udf(undefine) , sn(sendnote) , rn(readnote), <br/> <f x14F08080='impact'> mydict , nick , staff , gannew , assr , asnew , setnick , mynick , seenick , profile , rank , myrank , ranker , myip , mc(MultiChat) , mc2(MultiChat) , lockstatus]",True)
      ### MultiChat
      elif cmd == "multichat" or cmd == "mc" or cmd == "MultiChat" or cmd == "Mc":
        if args == "":
            room.message("My Default room : www.mio-chat.chatango.com")
        else:
            room.message("Done ! , This is your Room : http://ch.besaba.com/chat/flash/?".join(args.split())+"!,")
      elif cmd == "multichat2" or cmd == "mc2":
        if args == "":
            room.message("My Default room : http://ch.besaba.com/chat/html5/?anibatch!,mio-chat!,dhikas-blog!,eksperimen!,ladiessplay!,momotarosatsu!,natsurubasecamp!,nosobafansubs!,poru-chat!")
        else:
            room.message("Done : http://ch.besaba.com/chat/html5/?"+(args)+"!")
      #### MyIp
      elif cmd =="myip" or cmd == "MyIp" or cmd == "MyIP" or cmd == "My IP Adress":
        try:
         room.message("IP address kamu adalah : "+message.ip)
        except:
         room.message("Gagal melihat IP address, Aku bukan mods disini.")
      #### CurrentStats
      if cmd == "cs" or cmd =="currentstats":
        a = len(self.roomnames)
        b = len(whitelist)
        c = len(owners)
        d = len(admin)
        e = len(nicks)
        f = len(archknight)
        g = len(blacklist)
        room.message("List Data : <br/> <f x1400FF7F='Engravers MT'>Rooms: "+str(a)+" <br/> <f x14ADE8E6='Engravers MT'>Whitelist: "+str(b)+" <br/> <f x14FFD700='Engravers MT'>Owners: "+str(c)+" <br/> <f x14DC143C='Engravers MT'>Admin: "+str(d)+" <br/> <f x14D8BFD8='Engravers MT'>Nick: "+str(e)+" <br/> <f x14ADFF2F='Engravers MT'>Moderator: "+str(f)+" <br/> <f x14000000='Engravers MT'>Blacklist: "+str(g)+"",True)
      ##testcmd
      if cmd == "webanime":
        room.message("<f x12F00='1'>Web Anime Untuk Sekarang:<f x12334433='1'><br/>1. Animeindo.id : ainew(new update on animeindo.id).<br/>2. Imoutosubs.com : isnew(new update on imoutosubs).<br/>3. Narutobleachlover.net : nbnew(new update on narutobleachlover).<br/>4. Kurogoze.net : krnew(new update on kurogaze) , krsr(kurogaze search).<br/>5. Nekonime.com : nknew(new update on nekonime).<br/>6. Animesave.com : asnew(new update on animesave.com) , assr(animesave.com search).<br/>7. Wardhanime.net : wanew(new update on wardhanime) , wasr(wardhanime search).<br/>8. Otanimesama : otnew(new update on otanimesama) , otsr(otanime search).<br/>9. Oploverz.net : opnew(new update on oploverz) , opsr(oploverz search).<br/>10. Fasatsu.com : fsnew(new update on fansatsu) , fssr(search fansatsu movie or anime).<br/>11. Samehadaku.net : sknew(new update on samehadaku).<br/>12.Anisubindo.net : aonew (new update on anisubindo.<br/>13.Anibatch.net : abnew, abnew2 (new update on anibatch) absr (anibatch search) ", True)
      if cmd == "cari":
       if room.name == "anibatch":
         room.message(serAnBa(args), True)
       if room.name == "hentaipoi":
         room.message(serNePo(args), True)
      if cmd == "opnew": room.message(newOp(), True)
      if cmd == "abnew": room.message(newAnBa(), True)
      if cmd == "abnew2": room.message(newAnBa2(), True)
      if cmd == "wbnew": room.mesage(newWiDe(), True)
      if cmd == "npnew":
       if room.name == "mio-chat":
         room.message(newNePo(), True)
       else: room.message("I Can't")
      if cmd == "otnew": room.message(newOn(), True)
      if cmd == "otsr": room.message(serOn(args), True)
      if cmd == "wanew": room.message(newWa(), True)
      if cmd == "gannew": room.message(newGa(), True)
      if cmd == "sknew": room.message(newSk(), True)
      if cmd == "asnew": room.message(newAs(), True)
      if cmd == "annew": room.message(newAn(), True)
      if cmd == "aonew": room.message(newAo(), True)
      if cmd == "nknew": room.message(newNk(), True)
      if cmd == "krnew": room.message(newKr(), True)
      if cmd == "nbnew": room.message(newNb(), True)
      if cmd == "wasr": room.message(serWa(args), True)
      if cmd == "joinew": room.message(newJoi(), True)
      if cmd == "ennew": room.message(newEn(), True)
      if cmd == "ainew": room.message(newAi(), True)
      if cmd == "fsnew": room.message(newFs(), True)
      if cmd == "fssr": room.message(serFs(args), True)
      if cmd == "absr": room.message(serAnBa(args), True)
      if cmd == "npsr":
       if room.name == "mio-chat" and room.name == "anibatch":
         room.message(serNePo(args), True)
       else: room.message("I Can't")
      if cmd == "bgtime": room.message(bgtime(args), True)
      if cmd == "n123": room.message(newNonton123(), True)
      if cmd == "n123sr": room.message(serNonton123(args), True)
      if cmd == "hpsr": room.message(serHp(), True)
      if cmd == "opsr": room.message(serOp(args), True)
      if cmd == "krsr": room.message(serKg(args), True)
      if cmd == "assr": room.message(serAs(args), True)
      if cmd == "ak":
                  sss = args
                  data = urlreq.Request("http://animeku.tv/?s=", headers = {'User-Agent': 'Mozilla/5.0'})
                  asu = urlreq.urlopen(data)
                  udict = asu.read().decode('utf-8')
                  data = re.findall('<h2><a href="(.*?)">(.*?)</a>', udict)
                  newset = list()
                  num = 1
                  for link, title in data:
                      newset.append(("(%s) <b>%s</b> - %s") % (num, title, link))
                      num = num+1
                  room.message("<br/>New episode on Animeku.tv:<br/>"+"<br/>".join(newset[0:5]),True) 

      ##List Mods
        #List of Mods and Owner name in the current room you're in
      elif cmd == "mods" or cmd == "Mods":
        args = args.lower()
        if not args:
           room.message("<br/><font color='#9999FF'><b>Owner</b></font>:  <u><b>"+(room.ownername)+"</b></u>  <br/><font color='#9999FF'><b>Mods</b></font>: "+", ".join(room.modnames), True)
           return
        if args in self.roomnames:
           moda = self.getRoom(args).modname
           own = self.getRoom(args).ownername
           room.message("<br/><font color='#9999FF'><b>Owner</b></font>:  <b><u>"+(own)+"</u></b>  <br/><font color='#9999FF'><b>Mods</b></font>:  "+",  ".join(moda), True)
        else:
           self.joinRoom(args)
           cek_mods[user.name] = json.dumps([room.name,args])
      ##Join Player
      elif (cmd == "register" or cmd == "reg" or cmd == "regist"):
          if self.getAccess(user) == 1 and not user.name in owners and not user.name in admin and not user.name in archwizard and not user.name in archknight:
            player.append(user.name)
            room.message(user.name+" has registered as a Player. ^^")
      #### Ban / Unban
      if cmd == "ban":
          if room.getLevel(user) > 0:
            if room.getLevel(self.user) > 0 :
              room.banUser(ch.User(args))
              room.message(args.title()+" is Banned ╭∩╮ ")
              self.pm.message(ch.User(args.lower()), "You have been banned from %s by %s." % (room.name, user.name))
             
      if cmd == "unban":
          if room.getLevel(user) > 0:
            if room.getLevel(self.user) > 0:
              room.unban(ch.User(args))
              room.message(args.title()+" is UnBanned ╭∩╮ ")
              self.pm.message(ch.User(args.lower()), "You have been unbanned from %s by %s." % (room.name, user.name))
       #### Restart
      elif cmd =="restart" or cmd == "Restart" or cmd == "Reconnect" or cmd == "reconnect" and self.getAccess(user) >= 3:
         if user.name in owners:
           room.reconnect()
         else:
           room.message("Ce ??? *lol*")
      ## Ban List
      if cmd == "banlist" and self.getAccess(user) >= 1:
        room.message("Banlist Exile ╭∩╮: "+str(room.banlist))
        
  
      ##Setnick
      if cmd == "setnick":
        if self.getAccess(user) < 5:return
        try:
          if args:
            user, nick = args.split(" ",1)
            nicks[user]=json.dumps(nick)
            room.message("Sukses")
            f = open("nicks.txt","w")
            for user in nicks:
              nick = json.loads(nicks[user])
              f.write(json.dumps([user,nick])+"\n")
            f.close()
          else:
            room.message("Daree? Namaewa?")
        except:
          room.message("Tolong Nick Nya Senpaii (?setnick (nama users) nama yang diinginkan)")

              
      ##Setrank
      if cmd == "setrank": 
        if self.getAccess(user) < 6:return
        try:
          if len(args) >= 3:
            name = args
            if pars(name) == None:
                name = name
            elif pars(name) != None:
                name = pars(name)
            name, rank = args.lower().split(" ", 1)
            if rank == "6":
              owners.append(name)
              f = open("owners.txt", "w")
              f.write("\n".join(owners))
              f.close()
              room.message("Berhasil Master")
              if name in admin:
                admin.remove(name)
                f = open("admin.txt", "w")
                f.write("\n".join(admin))
                f.close()
              if name in archwizard:
                archwizard.remove(name)
                f = open("archwizard.txt", "w")
                f.write("\n".join(archwizard))
                f.close()
              if name in archknight:
                archknight.remove(name)
                f = open("archknight.txt", "w")
                f.write("\n".join(archknight))
                f.close()
              if name in player:
                player.remove(name)
                f = open("player.txt", "w")
                f.write("\n".join(player))
                f.close()
              if name in whitelist:
                whitelist.remove(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
            if rank == "5":
              admin.append(name)
              f = open("admin.txt", "w")
              f.write("\n".join(admin))
              f.close()
              room.message("Youkaii set5")
              if name in archwizard:
                archwizard.remove(name)
                f = open("archwizard.txt", "w")
                f.write("\n".join(archwizard))
                f.close()
              if name in archknight:
                archknight.remove(name)
                f = open("archknight.txt", "w")
                f.write("\n".join(archknight))
                f.close()
              if name in player:
                player.remove(name)
                f = open("player.txt", "w")
                f.write("\n".join(player))
                f.close()
              if name in whitelist:
                whitelist.remove(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
            if rank == "4":
               archwizard.append(name)
               f = open("archwizard.txt", "w")
               f.write("\n".join(archwizard))
               f.close()
               room.message("Youkaii set4")
               if name in admin:
                 admin.remove(name)
                 f = open("admin.txt", "w")
                 f.write("\n".join(admin))
                 f.close()
               if name in archknight:
                 archknight.remove(name)
                 f = open("archknight.txt", "w")
                 f.write("\n".join(archknight))
                 f.close()
               if name in player:
                 player.remove(name)
                 f = open("player.txt", "w")
                 f.write("\n".join(player))
                 f.close()
               if name in whitelist:
                 whitelist.remove(name)
                 f = open("whitelist.txt", "w")
                 f.write("\n".join(whitelist))
                 f.close()
            if rank == "3":
                archknight.append(name)
                f = open("archknight.txt", "w")
                f.write("\n".join(archknight))
                f.close()
                room.message("Youkaii set3")
                if name in admin:
                  admin.remove(name)
                  f = open("admin.txt", "w")
                  f.write("\n".join(admin))
                  f.close()
                if name in archwizard:
                  archwizard.remove(name)
                  f = open("archkwizard.txt", "w")
                  f.write("\n".join(archwizard))
                  f.close()
                if name in player:
                  player.remove(name)
                  f = open("player.txt", "w")
                  f.write("\n".join(player))
                  f.close()
                if name in whitelist:
                  whitelist.remove(name)
                  f = open("whitelist.txt", "w")
                  f.write("\n".join(whitelist))
                  f.close()
            if rank == "2":
                player.append(name)
                f = open("player.txt", "w")
                f.write("\n".join(player))
                f.close()
                room.message("Youkaii set2")
                if name in admin:
                  admin.remove(name)
                  f = open("admin.txt", "w")
                  f.write("\n".join(admin))
                  f.close()
                if name in archwizard:
                  archwizard.remove(name)
                  f = open("archwizard.txt", "w")
                  f.write("\n".join(archwizard))
                  f.close()
                if name in archknight:
                  archknight.remove(name)
                  f = open("archknight.txt", "w")
                  f.write("\n".join(archknight))
                  f.close()
                if name in whitelist:
                  whitelist.remove(name)
                  f = open("whitelist.txt", "w")
                  f.write("\n".join(whitelist))
                  f.close()
            if rank == "1":
                whitelist.append(name)
                f = open("whitelist.txt", "w")
                f.write("\n".join(whitelist))
                f.close()
                room.message("Youkaii set1")
                if name in admin:
                  admin.remove(name)
                  f = open("admin.txt", "w")
                  f.write("\n".join(admin))
                  f.close()
                if name in archwizard:
                  archwizard.remove(name)
                  f = open("archwizard.txt", "w")
                  f.write("\n".join(archwizard))
                  f.close()
                if name in archknight:
                  archknight.remove(name)
                  f = open("archknight.txt", "w")
                  f.write("\n".join(archknight))
                  f.close()
                  
        except:
              room.message("something wrong")

     # clear
      elif cmd == "clear":
          if room.getLevel(self.user) > 0:
            if self.getAccess(user) >= 6 or room.getLevel(user) == 2:
              room.clearall(),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
              room.clearUser(ch.User(random.choice(room.usernames))),
            else: room.message("Only rank 6+ or the room owner can do this")
          else:
            room.message("aku bukan mods disini :|")
      ##delete chat  
      elif (cmd == "delete" or cmd == "dl" or cmd == "del"):
          if room.getLevel(self.user) > 0:
            if self.getAccess(user) >= 1 or room.getLevel(user) > 0:
              name = args.split()[0].lower()
              room.clearUser(ch.User(name))
            else:room.message("kamu tidak bisa melakukannya!!")
          else:
            room.message("aku bukan mods disini :|")

      ##Yuri-test Spook
      if cmd == "syt":
        if self.getAccess(user) > 2:
          self.getRoom("yuri-test").message(args)
          room.message("_shhh ")
        else:
          room.message("Can't XD")
      ##Anibatch Spook
      if cmd == "sab":
        if self.getAccess(user) > 2:
          self.getRoom("anibatch").message(args)
          room.message("_shhh ")
        else:
          room.message("Can't XD")
      ##Spook
      if cmd == "whois" or cmd == "who" or cmd == "w":
          if not args :
            room.message("FAIL!! Do 'w<space>nick");return
          args = args.lower()
          if args[0] == "+":
            args = args[1:]
          elif pars(args) != None and not args[0] == "+":
            args = pars(args)
          try:
            f = open("ip_whois.txt", "r")
            ip_whois = eval(f.read())
            f.close()
          except:pass
          try:
            f = open("sid_whois.txt", "r")
            sid_whois = eval(f.read())
            f.close()
          except:pass
          ip_ver = getWhois.whois(ip_whois, args)
          sid_ver = getWhois.whois(sid_whois, args)
          if ip_ver == None and sid_ver == None:
            room.message("No alias found.")
            return
          room.message("Currently known alias(es) of %s:<br/>%s: %s.<br/>%s: %s."% (args.title(), "UnID Version", sid_ver, "IP Version", ip_ver), True)

      if cmd == "spook" or cmd == "sp":
        try:
          name, body = args.split(" ", 1)
          if name in self.roomnames :
            self.getRoom(name).message(body)
            room.message("_shhh ")
          else:
            room.message("Aku tidak ada di room itu")
        except:room.message("error")
      ##fax
      if cmd == "fax" or cmd == "Fax":
        try:
          name, body = args.split(" ", 1)
          l = "http://ch.besaba.com/mty.htm?"+room.name+"!"
          if name in self.roomnames :
            self.getRoom(name).message('[<font color="#6699CC"><b>Message</b></font> - %s ] in <a href=\"%s" target=\"_blank\"><u>%s</u></a> : <font color="#66FFFF"><i> %s <i></font>' % (sntonick(user.name), l, room.name, body),True)
            room.message("Sent")
          else:
            room.message("I haven't joined that room")
        except:room.message("error")    
          


      ##Ranker
      if cmd == "ranker":
        room.message("<br/> <f x12FF0000='0'> ╭∩╮（︶︿︶）╭∩╮||*R<f x12FF4500='Engravers MT'>A<f x12FF8A00='Engravers MT'>N<f x12FFCF00='Engravers MT'>K<f x12BAFF00='Engravers MT'>E<f x1275FF00='Engravers MT'>R<f x1230FF00='Engravers MT'>B<f x1200FF45='Engravers MT'>O<f x1200FF8A='Engravers MT'>A<f x1200FFCF='Engravers MT'>R<f x1200BAFF='Engravers MT'>D*||╭∩╮（︶︿︶）╭∩╮ <br/><f x120000FF='Engravers MT'><b>{Owner}:</b></f> %s<br/><f x12FF0000='Engravers MT'><b>{Admin}:</b></f> %s<br/><f x12216BF5='Engravers MT'><b>{ArchWizard}:</b></f> %s<br/><f x12FF00FF='Engravers MT'><b>{ArchKnight}: </b></f>%s" % (", ".join(owners), ", ".join(admin), ", ".join(archwizard), ", ".join(archknight)),True)
      ##RankBoard
      if cmd == "rankboard":
        room.message("<br/><f x120000FF='0'><b>My Rank Board</b></f><br/><f x120000FF='0'><b>Owner:</b></f> %s<br/><f x12FF0000='0'><b>Admin:</b></f> %s<br/><f x12216BF5='0'><b>ArchWizard:</b></f> %s<br/><f x12FF00FF='0'><b>ArchKnight:</b></f> %s<br/><<f x121BFF00='0'><b>Whitelist:</b></f> %s</br><f x1200FF98><b>Player:</b></f> %s<br/><f x12FF00FF='0'><b>Blacklist:</b></f> %s" % (", ".join(owners), ", ".join(admin), ", ".join(archwizard), ", ".join(archknight), ", ".join(whitelist), ", ".join(player), ", ".join(blacklist)),True)
      ##staff
      if cmd == "staff":
        room.message("<br/><f x120000FF='0'><b>Owner:</b></f> %s<br/><f x12FF0000='0'><b>Admin:</b></f> %s" % (", ".join(owners), ", ".join(admin)),True)

      ##GIS
      if cmd == "gis": 
        room.message(gis(args),True)
      ##GS
      if cmd == "gs": 
        room.message(gs(args),True)    

      if cmd == "pfpic":
                link = "http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg" % (args[0], args[1], args)
                room.message("<br/>"+"User ID : "+args+""+"<br/>Profile Picture :<br/>"+link,True)    
    ##Eval
      if cmd == "ev" or cmd == "eval" or cmd == "e":
        if self.getAccess(user) == 6:
          ret = eval(args)
          if ret == None:
            room.message("Done.")
            return
          room.message(str(ret))

     ##Smack
      elif cmd =="smack":
          if args:
            room.message("*I want To kill You @"+args+"* Finish Him! :@",True)
            self.setTimeout(int(4),room.message,"Ciattt!! Wataw,Wataw 8)!!")             
            self.setTimeout(int(8),room.message,"Diee :@+99")
          else:
            room.message("*Kisama https://media.tenor.co/images/45ae6ec607d359f6baee7731e26e365f/tenor.gif @"+random.choice(room.usernames)+" Kau Sepertinya Ingin Mati https://media.tenor.co/images/dcab299b237dafe5fce2508f44eb9e48/tenor.gif ")
            self.setTimeout(int(4),room.message,"Ciattt!! Wataw,Wataw 8)!! https://media.tenor.co/images/459a7d57a94598f1869a741c5773b5ca/tenor.gif ")
            self.setTimeout(int(8),room.message,"Diee https://media.tenor.co/images/a6f2a9402b2cda3ba7fbfd312e294fb6/tenor.gif :@+99")

      ##Say
      if cmd == "say":
        room.message(args)

      ##Random User
      if cmd == "randomuser":
        room.message(random.choice(room.usernames))
      
      ##Blacklist
      if cmd == "blist":
        a = ", ".join(blacklist)
        room.message("<f x13BAFF00='Engravers MT'>List Exile Benci <f x13FF0000='impact'> ╭∩╮ : "+str(a)+"",True)
          
        ##Check if Mod
	#not really important
      elif cmd == "ismod":
        user = ch.User(args)
        if room.getLevel(user) > 0:
          room.message("yesh")
        else:
          room.message("nope")

      ## Youtube
      elif cmd == "youtube" or cmd == "yt":
        if args:
          room.message(tube(args),True)
      ##simi Lock
      if cmd == "simlock" and self.getAccess(user) >= 3:
        if args:
          if args in simlock:
            room.message("Bahkan sudah DiLocked Simsimi Nya senpai :@")
          if args in self.roomnames:
            simlock.append(args)
            f = open("simlock.txt", "w")
            f.write("\n".join(simlock))
            f.close()
            room.message("<f x12FF0000='Engravers MT'>Locked Simsimi: <b>%s</b> <f x12000000='Engravers MT'>" % args, True)
          else: room.message("Only rank 2+ can do that")
        if not args:
          if room.name not in simlock:
             simlock.append(room.name)
             f = open("simlock.txt", "w")
             f.write("\n".join(simlock))
             f.close()
             room.message("<f x12FF0000='Engravers MT'>Locked Simsimi: <b>%s</b> <f x12000000='Engravers MT'>" % room.name,True)
          else:
             room.message("Bahkan sudah DiLocked Simsimi Nya senpai :@")
      ##Simi unlock
      if cmd == "simunlock" and self.getAccess(user) >= 3:
        if args:
          if args in simlock and args in self.roomnames:
            simlock.remove(args)
            f = open("simlock.txt", "w")
            f.write("\n".join(simlock))
            f.close()
            room.message("<f x1233FF33='Engravers MT'>Unlocked Simsimi: <b>%s</b> <f x12000000='Engravers MT'>" % args, True)
          if args not in simlock:
            room.message("Bahkan sudah DiUnlock Simsimi Nya senpai :@")
        if not args:
          if room.name in simlock:
             simlock.remove(room.name)
             f = open("simlock.txt", "w")
             f.write("\n".join(simlock))
             f.close()
             room.message("<f x1233FF33='Engravers MT'>Unlocked Simsimi: <b>%s</b> <f x12000000='Engravers MT'>" % room.name,True)
          else:
             room.message("Bahkan sudah DiUnlock Simsimi Nya senpai :@")
      ##Ping
      if cmd == "ping":
       if cmd == "ping":
         if args == "":
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for i in gay:
            if i not in finale:
              finale.append(i)
          if len(finale) > 40:
            room.message("@%s"% (" @".join(finale[:41])), True)
                
          if len(finale) <=40 :
            room.message("<f x1233FF33='Engravers MT'>@%s"% (" @".join(finale)), True)
                
         if args != "":
           if args not in self.roomnames:
             room.message("I'm not there.")
      ## cso
      if cmd=="cso":
       if len(args)>0:
          offline = None
          url = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
          if not "buyer" in url:
            room.message(args+" does not exist on chatango.")
          else:
            url2 = urlreq.urlopen("http://"+args+".chatango.com").readlines()
            for line in url2:
              line = line.decode('utf-8')
              if "leave a message for" in line.lower():
                print(line)
                offline = True
            if offline:
              room.message(args+" sedang <f x11FF0000='8'>Offline</f>",True)
            if not offline:
              room.message(args+" sedang <f x1133FF33='8'>Online</f>",True)
       else:
          room.message("<f x11FF6600='8'>I need the username of target :)</f>", True)
     ## upTime
      elif cmd == "uptime" or cmd == "ut" and self.getAccess(user) >= 2:
          room.message("Server uptime: %s" % uptime())
      ## Broadcast
      elif cmd=="bc" and self.getAccess(user) >= 4:
          r = room.name
          l = "http://ch.besaba.com/mty.htm?"+r+"+"
          for room in self.rooms:
            room.message("[<font color='#6699CC'><b>Broadcast</b></font>] from - "+sntonick(user.name)+ " : <font color='#33FF33'><i>"+args+"<i></font>", True)              
      elif cmd == "mads" and self.getAccess(user) >= 4:
          r = room.name
          l = "http://ch.besaba.com/mty.htm?"+r+"+"
          for room in self.rooms:
            room.message(args, True)
    ###### Define            
      elif cmd == "define" or cmd == "df" and len(args) > 0:
          try:
            try:
              word, definition = args.split(" as ",1)
              word = word.lower()
            except:
              word = args
              definition = ""
            if len(word.split()) > 4:
              room.message("gagal senpai")
              return
            elif len(definition) > 0:
              if word in dictionary:
                room.message("%s defined ini sudah ada yang Punya" % user.name.capitalize())
              else:
                dictionary[word] = json.dumps([definition, user.name])
                f =open("definitions.txt", "w")
                for word in dictionary:
                  definition, name = json.loads(dictionary[word])
                  f.write(json.dumps([word, definition, name])+"\n")
                f.close
                room.message("Definition Exile Simpan :D")
            else:
              if word in dictionary:
                definition, name = json.loads(dictionary[word])
                room.message("<br/>ID : %s<br/>Keyword : %s<br/>Definition:<br/>%s" % (name, word, definition),True)
              else:
                room.message(args+" Senpai Belum Punya Definitions Di Exile")
          except:
            room.message("ada sesuatu yang salah senpai")
                
      elif cmd == "rank":
        if not args:
            if user.name in owners and not user.name in whitelist:
              room.message("<br/> <f x1400FF7F='Engravers MT'>"+user.name+"<f x12CC0033='Imprint MT Shadow'> Kamu Rank 6 <f x14FF0000='Goudy Stout'> [Owner] ",True)
            elif user.name in admin and not user.name in archwizard and not user.name in player and not user.name in whitelist and not user.name in archknight and not user.name in owners:
              room.message("<br/> <f x1400FF7F='Engravers MT'>"+user.name+"<f x12CC0033='Imprint MT Shadow'> Kamu Rank 5 <f x14FFD700='Goudy Stout'> [Admin] ",True)
            elif user.name in archwizard and not user.name in player and not user.name in archknight and not user.name in whitelist and not user.name in owners and not user.name in admin:  
              room.message("<br/> <f x1400FF7F='Engravers MT'>"+user.name+"<f x12CC0033='Imprint MT Shadow'> Kamu Rank 4 <f x147CFC00='Goudy Stout'> [ArchWizard]",True)
            elif user.name in archknight and not user.name in whitelist and not user.name in owners and not user.name in admin:  
              room.message("<br/> <f x1400FF7F='Engravers MT'>"+user.name+"<f x12CC0033='Imprint MT Shadow'> Kamu Rank 3 <f x148A2BE2='Goudy Stout'> [ArchKnight]",True)
            elif user.name in player and not user.name in archwizard and not user.name in archknight and not user.name in whitelist and not user.name in owners and not user.name in admin:  
              room.message("<br/> <f x1400FF7F='Engravers MT'>"+user.name+"<f x12CC0033='Imprint MT Shadow'> Kamu Rank 2 <f x147FFFD4='Goudy Stout'> [Player]",True)
            elif user.name in whitelist and not user.name in owners:
              room.message("<br/> <f x1400FF7F='Engravers MT'>"+user.name+"<f x12CC0033='Imprint MT Shadow'> Kamu Rank 1 <f x14F0FFFF='Goudy Stout'> [Whitelist]",True)
            elif user.name not in whitelist and not user.name not in archknight and user.name not in admin and user.name not in owners and user.name not in archwizard and user.name not in player:
              room.message(user.name+" Kamu Belum terdaftar",True)
        if args:
              sss = args
              if sss in owners:
                  room.message("<br/> <f x1400FF7F='Engravers MT'>"+sss.title()+" <f x12CC0033='Imprint MT Shadow'> Rank Dia 6 <f x14FF0000='Goudy Stout'> [Owner] ",True)
              if sss in admin:
                  room.message("<br/> <f x1400FF7F='Engravers MT'>"+sss.title()+" <f x12CC0033='Imprint MT Shadow'> Rank Dia 5 <f x14FFD700='Goudy Stout'> [Admin] ",True)
              if sss in archwizard:
                  room.message("<br/> <f x1400FF7F='Engravers MT'>"+sss.title()+" <f x12CC0033='Imprint MT Shadow'> Rank Dia 4 <f x147CFC00='Goudy Stout'> [ArchWizard] ",True)
              if sss in archknight:
                  room.message("<br/> <f x1400FF7F='Engravers MT'>"+sss.title()+" <f x12CC0033='Imprint MT Shadow'> Rank Dia 3 <f x148A2BE2='Goudy Stout'> [ArchKnight] ",True)
              if sss in player:
                  room.message("<br/> <f x1400FF7F='Engravers MT'>"+sss.title()+" <f x12CC0033='Imprint MT Shadow'> Rank Dia 2 <f x147FFFD4='Goudy Stout'> [Player] ",True)
              if sss in whitelist:
                  room.message("<br/> <f x1400FF7F='Engravers MT'>"+sss.title()+" <f x12CC0033='Imprint MT Shadow'> rank Dia 1 <f x14F0FFFF='Goudy Stout'> [Whitelist] ",True)   
              if sss not in owners and sss not in admin and sss not in archknight and sss not in whitelist and sss not in archwizard and sss not in player:
                  room.message(sss.title()+" Tidak ada rank :) ")

      ### Lock/Unlock

                  


      ###lock
      if cmd == "lock" and self.getAccess(user) > 2:
          try:
           if user.name in whitelist or user.name in player:
            room.message("Jangan Perintah Exile , Exile Lagi BadMood :@+77")
            return
           if args in locks:
            room.message("Udah Di Lock loh dari Tadi :)")
            return
           if args in self.roomnames:
            if user.name in owners or user.name in admin or user.name in archknight or user.name in archwizard:
              locks.append(args)
              f.close()
              f = open("locks.txt", "w")
              f.write("\n".join(locks))
              f.close()
              room.message("<f x12FF0000='Engravers MT'>Locked: <b>%s</b> <f x12000000='Engravers MT'>" % args, True)
            else: room.message("Only rank 3+ can do that")
           if args == "":
            if room.name in locks:
              room.message("Udah Di Lock loh dari Tadi :)")
              return
            locks.append(room.name)
            room.message("<f x12FF0000='Engravers MT'>Locked: <b>%s</b> <f x12000000='Engravers MT'>" % room.name, True)
           if args not in self.roomnames:
            if args == "": return
            room.message("Exile Gak maen Di sini :|")
            return
          except:
            room.message("<f x12FF0000='Engravers MT'>Locked: <b>%s</b> <f x12000000='Engravers MT'>" % room.name, True)
            
      ##unlock      
      if cmd == "unlock" and self.getAccess(user) > 2:
          try:
           if not args:
             rnm = room.name
             if rnm in locks:
               locks.remove(rnm)
               f = open("locks.txt","w")
               f.write("\n".join(locks))
               f.close()
               room.message("<f x1233FF33='Engravers MT'>Unlocked <b>%s</b> <f x12000000='Engravers MT'>" % room.name,True)
             else:
               room.message("bahkan sudah diunlock dari tadi senpai :@")
           if args:
             ar = args
             if ar in locks:
               locks.remove(ar)
               f = open("locks.txt","w")
               f.write("\n".join(locks))
               f.close()
               room.message("<f x1233FF33='Engravers MT'>Unlocked <b>%s</b> <f x12000000='Engravers MT'>" % room.name,True)
             else:
               room.message("udah di unlock lohh dari tadi :@")
          except:
           room.message("UNLOCK ROOM",True)


         

    ##### Whitelist
      elif cmd == "wl" and self.getAccess(user) >= 1:
        name = args
        if name not in whitelist and name not in archwizard and name not in player and name not in owners and name not in admin and name not in archknight and name not in blacklist:
          room.message("Senpai Sekarang "+args+" dapat menggunakan exi,Exile (Prefix [?]Ok Senpai) :P")
          whitelist.append(name)
          f = open("whitelist.txt","w")
          f.write("\n".join(whitelist))
          f.close
        else:
          room.message("Dia Udah Ada Di Hati Exile :D")

     ###blacklist
      elif cmd == "bl" and self.getAccess(user) >= 5:
        name = args
        if name not in whitelist and name not in owners and name not in admin and name not in archknight:
          room.message("Youkaii")
          blacklist.append(name)
          f = open("blacklist.txt","w")
          f.write("\n".join(blacklist))
          f.close
        else:
          room.message("Dia Udah Exile Hapus Dari Hatikuh Selamanya :@")

      ##ubl
      if cmd == "ubl" and self.getAccess(user) >= 5:
        try:
          if args in blacklist:
            blacklist.remove(args)
            f = open("blacklist.txt","w")
            f.write("\n".join(blacklist))
            f.close()
            room.message("Sukses Senpai")
        except:
          room.message("Gagal Desu")
            
      ##uwl
      if cmd == "uwl" and self.getAccess(user) >= 5:
        try:
          if args in owners:
            room.message("Gomene Senpai Exile Gak Bisa")
          if args in admin:
            admin.remove(args)
            f = open("admin.txt","w")
            f.write("\n".join(admin))
            f.close()
            room.message("Youkaii")
          if args in archwizard:
            archwizard.remove(args)
            f = open("archwizard.txt","w")
            f.write("\n".join(archwizard))
            f.close()
            room.message("Youkaii")
          if args in archknight:
            archknight.remove(args)
            f = open("archknight.txt","w")
            f.write("\n".join(archknight))
            f.close()
            room.message("Youkaii")
          if args in archwizard:
            archwizard.remove(args)
            f = open("archwizard.txt","w")
            f.write("\n".join(archwizard))
            f.close()
            room.message("Youkaii")
          if args in player:
            player.remove(args)
            f = open("player.txt","w")
            f.write("\n".join(player))
            f.close()
            room.message("Youkaii")
          if args in whitelist:
            whitelist.remove(args)
            f = open("whitelist.txt","w")
            f.write("\n".join(whitelist))
            f.close()
            room.message("Sukses")  
        except:
          room.message("Gagal")
        
      if cmd== "sbg":
            if self.getAccess(user) >= 5:
              if len(args) > 0:
                  if args == "on":
                    room.setBgMode(1)
                    room.message("Background On")
                    return
                  if args == "off":
                    room.setBgMode(0)
                    room.message("Background Off")
      if cmd== "sf":
            if self.getAccess(user) >= 5:
                  if args:
                    self.setFontFace(args)
                    room.message("Done")

      if cmd== "sfc":
            if self.getAccess(user) >= 5:
                  if args:
                    self.setFontColor(args)
                    room.message("Done")
                    
      if cmd== "sfz":
            if self.getAccess(user) >= 5:
                  if args:
                    self.setFontSize(int(args))
                    room.message("Done")

      if cmd== "snc":
            if self.getAccess(user) >= 5:
                  if args:
                    self.setNameColor(args)
                    room.message("Done")
      elif cmd == "mydict" or cmd == "mydf":
          arr = []
          for i in dictionary:
            if user.name in dictionary[i]:
              arr.append(i)
          if len(arr) > 0:
            room.message("<f x1300FF7F='impact'> Senpai Punya Defined <b>"+str(len(arr))+"</b> Didalam Dictionary : <br/> <f x12FF0000='Engravers MT'> %s"% (', '.join(sorted(arr))), True)
          else:
            room.message("Dictionary Senpai Kosong.")



      if cmd == "udf" and len(args) > 0:
          try:
            word = args
            if word in dictionary:
              definition, name = json.loads(dictionary[word])
              if name == user.name or self.getAccess(user) >= 3:
                del dictionary[word]
                f =open("definitions.txt", "w")
                for word in dictionary:
                  definition, name = json.loads(dictionary[word])
                  f.write(json.dumps([word, definition, name])+"\n")
                f.close
                room.message(args+" Defined di hapus dari hati Exile")
                return
              else:
                room.message("<b>%s</b> you can not remove this define only masters or the person who defined the word may remove definitions" % user.name, True)
                return
            else:
               room.message("<b>%s</b> is not yet defined you can define it by typing <b>define %s: meaning</b>" % args, True)
          except:
            room.message("Gagal")
            return
            
      elif cmd == "sdf" or cmd == "seedict":
          if not args:
            room.message("Whose dict do you want to see ?")
            return
          args = args.lower()
          if pars(args) == None:
            args = args.lower()
          if pars(args) != None:
            args = pars(args)
          arr = []
          for i in dictionary:
            if args in dictionary[i]:
              arr.append(i)
          if len(arr) > 0:
            room.message("<b>"+args.title()+"</b> punya defined <b>"+str(len(arr))+"</b> didalam Dictionary :<i> %s"% (', '.join(sorted(arr))), True)
          else:
            room.message(args.title()+" defined kosong senpai.")

      if cmd == "seenick":
            try:
              if args in nicks:
                room.message(args+" Nick Dia : "+sntonick(args)+"", True)
              else:
                room.message(args+" Senpai itu belum membuat nama panggilan di exile :|")
            except:
              return      

      elif cmd=="prof" or cmd == "profile":
        try:
          args=args.lower()
          stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
          crap, age = stuff.split('<span class="profile_text"><strong>Age:</strong></span></td><td><span class="profile_text">', 1)
          age, crap = age.split('<br /></span>', 1)
          crap, gender = stuff.split('<span class="profile_text"><strong>Gender:</strong></span></td><td><span class="profile_text">', 1)
          gender, crap = gender.split(' <br /></span>', 1)
          if gender == 'M':
              gender = 'Laki-Laki'
          elif gender == 'F':
              gender = 'Perempuan'
          else:
              gender = '?'
          crap, location = stuff.split('<span class="profile_text"><strong>Location:</strong></span></td><td><span class="profile_text">', 1)
          location, crap = location.split(' <br /></span>', 1)
          crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
          mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
          mini=mini.replace("<img","<!")
          picture = '<a href="http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg</a>'
          prodata = '<br/> <a href="http://chatango.com/fullpix?' + args + '" target="_blank">' + picture + '<br/><br/> Age: '+ age + ' <br/> Gender: ' + gender +  ' <br/> Location: ' +  location + '' '<br/> <a href="http://' + args + '.chatango.com" target="_blank"><u>Chat With User</u></a> ' "<br/><br/> "+ mini 
          room.message(prodata.replace("\n","<br/>"),True)
        except:
          room.message(""+args+" doesn't exist o.o ")
      elif cmd=="mini":
        try:
          args=args.lower()
          stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
          crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
          mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
          mini=mini.replace("<img","<!")
          prodata = '<br/>'+mini
          room.message(prodata,True)
        except:
          room.message(""+args+" doesn't exist o.o ")

      if cmd == "bgimg":
        try:
          args=args.lower()
          picture = '<a href="http://st.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/msgbg.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/msgbg.jpg</a>'
          prodata = '<br/>'+picture
          room.message("<br/>"+"User ID : "+args+"<br/>Background :"+prodata,True)
        except:
          room.message(""+args+" doesn't exist:'v")
    

   

    ### Private Messages
      elif cmd=="pm":
        data = args.split(" ", 1)
        if len(data) > 1:
          name , args = data[0], data[1]
          self.pm.message(ch.User(name), "[Private.Message] By - "+user.name+" : "+args+" ")
          room.message("Sent to "+name+"")
    ### Sentnote
      elif cmd == "inbox":
          if user.name in sn:
            mesg = len(sn[user.name])
            room.message("["+str(mesg)+"] Pesan pada inbox Senpai")
          else:
            sn.update({user.name:[]})
            mesg = len(sn[user.name])
            room.message("["+str(mesg)+"] Pesan pada inbox Senpai")


        #send notes
      elif cmd == "sn" or cmd == "sendnote":
          args.lower()
          untuk, pesan = args.split(" ", 1)
          if untuk[0] == "+":
                  untuk = untuk[1:]
          else:
                  if pars(untuk) == None:
                    room.message("Who is "+untuk+" ??")
                    return
                  untuk = pars(untuk)
          if untuk in sn:
            sn[untuk].append([user.name, pesan, time.time()])
            if untuk not in notif:
              notif.append(untuk)
            else:pass
          else:
            sn.update({untuk:[]})
            sn[untuk].append([user.name, pesan, time.time()])
            if untuk not in notif:
              notif.append(untuk)
            else:pass
          room.message('Sent to %s'% (untuk)+"'s inbox" , True)
				


        #Read Notes
      elif cmd =="rn" or cmd =="readnote":
          if user.name not in sn:
            sn.update({user.name:[]})
          user=user.name.lower()
          if len(sn[user]) > 0:
            messg = sn[user][0]
            dari, pesen, timey = messg
            timey = time.time() - int(timey)
            minute = 60
            hour = minute * 60
            day = hour * 24
            days =  int(timey / day)
            hours = int((timey % day) / hour)
            minutes = int((timey % hour) / minute)
            seconds = int(timey % minute)
            string = ""
            if days > 0:
              string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
            if len(string) > 0 or hours > 0:
              string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
            if len(string) > 0 or minutes > 0:
              string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
            string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
            room.message("[<font color='#6699CC'><b>Private Message</b></font>] from - "+sntonick(dari)+" : "+pesen+"  (<font color='#9999FF'>"+string+" ago </font>)", True)
            try:
              del sn[user][0]
              notif.remove(user)
            except:pass
          else:room.message('%s'%(user)+" you don't have any messages in your inbox" , True)
   ###### leave + room 
      elif cmd == "leave"  and self.getAccess(user) >=5:
        if not args:args=room.name
        self.leaveRoom(args)
        room.message("<f x1233FF33='Engravers MT'>Youkaii <b></b>  Exile Leave dari: <f x14FFCC00='impact'> "+args+" ...",True)
        print("[SAVE] SAVING Rooms...")
        f = open("rooms.txt", "w")
        f.write("\n".join(self.roomnames))
        f.close()

    ###### join room + roomname

      if cmd == "join" and len(args) > 1:
          if self.getAccess (user) >= 5:
              if args not in self.roomnames:
                room.message("<f x1233FF33='Engravers MT'>Youkaii <b></b> Exile Join Ke: <f x14FFCC00='impact'> "+args+" ...", True)
                self.joinRoom(args)
              else:
                room.message("exile sudah ada disana ...")
              print("[SAVE] SAVING Rooms...")
              f = open("rooms.txt", "w")
              f.write("\n".join(self.roomnames))
              f.close()
      elif cmd == "userlist" or cmd == "ul":
         if args == "":
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for i in gay:
            if i not in finale:
              finale.append(i)
          if len(finale) > 40:
            room.message("<font color='#9999FF'><b>40</b></font> of <b>%s</b> users in this room: %s"% (len(finale), ", ".join(finale[:41])), True)
          if len(finale) <=40 :
            room.message("<f x1233FF33='Engravers MT'>Pemain <b>%s</b> Pada Room Ini: <f x14FFCC00='impact'>%s"% (len(finale),", ".join(finale)), True)
         if args != "":
           if args not in self.roomnames:
             room.message("I'm not there.")
             return
           users = getParticipant(str(args))
           if len(users) > 40:
             room.message("<font color='#9999FF'><b>40</b></font> of <b>%s</b> current users in <b>%s</b>: %s"% (len(users), args.title(), ", ".join(users[:41])), True)
           if len(users) <=40:
             room.message("<f x1233FF33='Engravers MT'>Pemain <b>%s</b> Pada Room  <f x12FF0000='Engravers MT'> <b>[%s]</b>: <f x14FFCC00='impact'>%s"% (len(users), args.title(), ", ".join(users)), True) 
    ##### bot rooms
      elif cmd == "rooms" : 
        j = [] 
        for i in self.roomnames: 
          j.append(i+'[%s]' % str(self.getRoom(i).usercount)) 
          j.sort() 
        room.message("<f x1233FF33='Engravers MT'>Exile bermain Di "+'[%s] rooms: <f x12FF0000="comic"> '%(len(self.roomnames))+", ".join(j),True)
      ## Mods
      elif cmd == "mods":
          args = args.lower()
          if args == "":
            room.message("<font color='#ffffff'><b>Room</b>: "+room.name+" <br/><b>Owner</b>: <u>"+ (room.ownername) +"</u> <br/><b>Mods</b>: "+", ".join(room.modnames), True)
            return
          if args in self.roomnames:
              modask = self.getRoom(args).modnames
              owner = self.getRoom(args).ownername
              room.message("<font color='#ffffff'><b>Room</b>: "+args+" <br/><b>Owner</b>: <u>"+ (owner) +"</u> <br/><b>Mods</b>: "+", ".join(modask), True)

      ####nick
      elif cmd == "nick":
        ## if user.name in reg or user.name in friends or user.name in trusted or user.name in owners:
            if args:
                nick = args 
                user = user.name 
                nicks[user] = json.dumps(nick)
                room.message(user +' Oke, mulai sekarang aku panggil '+str(args)+'', True)
                try: 
                    print("[SAVING] NICKS...")
                    f = open("nicks.txt", "w")
                    for user in nicks:
                        nick = json.loads(nicks[user])
                        f.write(json.dumps([user,nick]) + "\n")
                except:
                       room.message("Gagal membuat Nick baru..");return
            else:
              room.message('Ketik >nick <spasi> nama yang di inginkan', True)

    
    ##mynick
      elif cmd == "mynick" :
          user=user.name.lower()
          if user in nicks :
            nick = json.loads(nicks[user])
            room.message(user+" Nama panggilan kamu : "+nick,True)
          else:
            room.message("buat nick dulu yah?! :D ", True)


   except Exception as e:
      try:
        et, ev, tb = sys.exc_info()
        lineno = tb.tb_lineno
        fn = tb.tb_frame.f_code.co_filename
        room.message("[Expectation Failed] %s Line %i - %s"% (fn, lineno, str(e)))
        return
      except:
        room.message("Undescribeable error detected !!")
        return


  ##Other Crap here, Dont worry about it
  
  def onFloodWarning(self, room):
    room.reconnect()
  
  def onJoin(self, room, user):
    if room.name == "ujicobasaya": room.message("Welcome in This Room @"+user.name+ " Having Fun Yeah... XD")
    print(user.name + " joined the chat!")
  
  def onLeave(self, room, user):
    if room.name == "ujicobasaya": room.message("@"+user.name+ "Left This Room :(")
    print(user.name + " left the chat!")
  def onPMMessage(self, pm, user, body):
    print("PM - "+user.name+" :"+body)
    import simi
    response = simi.simi(body)
    pm.message(user, response)
    self.pm.message(ch.User("isseihyoudous4"), "Incoming PM From ["+user.name+"] - "+body)
    self.setTimout(int(1), self.getRoom("ujicobasaya").message, "Incoming PM From ["+user.name+"] - "+body)
                  
  def onUserCountChange(self, room):
    print("users: " + str(room.usercount))
  

        

if __name__ == "__main__":
  TestBot.easy_start(rooms, botname, password)
