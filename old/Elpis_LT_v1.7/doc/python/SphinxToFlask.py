import datetime
import os
import subprocess 
from docutils.core import publish_cmdline, default_description

# sphinx-build -b html -d _build/doctrees . _build/html


class SphinxToFlask :
	def __init__(self):
		self.pypath = os.path.abspath(os.path.dirname(__file__))
		self.rstdir =  self.pypath.replace("/"+ os.path.basename(self.pypath),"")
		self.elpisdir =  self.rstdir.replace("/"+ os.path.basename(self.rstdir),"")
		print self.elpisdir
	def build(self):
		from sphinx import main
		from sphinx import cmdline
		cmdline.main(['','--version'])
		cmdline.main(['','-b','html',self.rstdir,self.rstdir+'/_build/html'])

		#publish_cmdline(writer_name='html', argv=["--stylesheet",self.csspath,self.rstpath,self.htmlpath])		
		#subprocess.call(["sphinx-build","-b","html",self.pypath,self.pypath+"/templates"])
		print "build now."
	def toflask(self):
		import shutil
		shutil.copy(self.rstdir+'/_build/html/document.html', self.elpisdir+"/templates")
		#shutil.copy("../_build/html/document.html", "../../templates")
		#shutil.copy("../_build/html/document.html", "../../templates")
		
		try:
			shutil.copytree(self.rstdir+"/_build/html/_static", self.elpisdir+"/static/_static")
		except OSError:		
			shutil.rmtree(self.elpisdir+"/static/_static")
			shutil.copytree(self.rstdir+"/_build/html/_static", self.elpisdir+"/static/_static")
		try:
			shutil.copytree(self.rstdir+"/_build/html/_sources", self.elpisdir+"/static/_sources")
		except OSError:		
			shutil.rmtree(self.elpisdir+"/static/_sources")
			shutil.copytree(self.rstdir+"/_build/html/_sources", self.elpisdir+"/static/_sources")
		
		


	def time_get(self):
		pass
		#dt = datetime.datetime.fromtimestamp(os.stat(self.rstpath).st_mtime)
		#print(dt.strftime("%Y-%m-%d %H:%M:%S"))  # Print 2011-05-30 17:48:12
		#return dt.strftime("%H:%M:%S")

