
import SphinxToFlask
import time
import sys


#argvs = sys.argv
#print argvs
doc = SphinxToFlask.SphinxToFlask()

now = ""
old = ""
doc.build()
doc.toflask()
"""
while 1 :

	now = doc.time_get()
	if(now != old):
		doc.build()
		
	old = now
	time.sleep(1)
	#print "HELLO"
"""
