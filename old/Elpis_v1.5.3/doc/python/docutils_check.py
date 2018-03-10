import datetime
import os
import subprocess 
from docutils.core import publish_cmdline, default_description

class docutils_check :
	def __init__(self,csspath,rstpath,htmlpath):
		self.csspath = csspath
		self.rstpath = rstpath
		self.htmlpath = htmlpath
		self.pypath = os.path.abspath(os.path.dirname(__file__))
		#print self.pypath
		pass
	def build(self):
		publish_cmdline(writer_name='html', argv=["--stylesheet",self.csspath,self.rstpath,self.htmlpath])		
		#subprocess.call(["sphinx-build","-b","html",self.pypath,self.pypath+"/templates"])
		print "build now."
	def time_get(self):
		dt = datetime.datetime.fromtimestamp(os.stat(self.rstpath).st_mtime)
		#print(dt.strftime("%Y-%m-%d %H:%M:%S"))  # Print 2011-05-30 17:48:12
		return dt.strftime("%H:%M:%S")

