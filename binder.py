from bottle import route,run,request,template,get,post,static_file
import os
import sys
import shutil

directories = { 
	"WEB"          :["html5", "html", "htm", "xhtml","css","js","php","xml"], 
	"IMAGES"       :["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg", "heif", "psd"], 
	"DOCUMENTS"    :["text","in","out","pdf","ppt","oxps","epub","pages","docx","doc","fdf","ods",
				     "odt","pwi","xsn","xps","dotx","docm","dox","rvg","rtf","rtfd","wpd","xls",
                     "xlsx","ppt","pptx"], 
	"ARCHIVES"     :["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z","dmg", "rar", "xar","zip"], 
	"AUDIO"        :["aac","aa","aac","dvf","m4a","m4b","mp3","msv","ogg","oga","raw","vox",
	                 "wav","wma"],
    "VIDEOS"       :["avi","flv","wmv","mov","mp4","webm","vob","mng","qt","mpg","mpeg","3gp"],
	"EXE"          :["exe"], 
	"PROGRAMS"     :["py","java","ccp","c","class","o"],
	"SHELL"        :["sh"]
}

sub_directories = {
	"HTML"    :["html5", "html", "htm", "xhtml","css","js"],
	"PHP"     :["php"],
	"XML"     :["xml"],
    "PDF"     :["pdf"],
    "TEXT"    :["text","oxps", "epub", "pages", "docx", "doc", "fdf","pwi","ods","odt","xsn","xps",
    			"dotx","docm","dox","rvg","rtf","rtfd","wpd","xls","xlsx","ppt","pptx"],
    "PPT"     :["ppt"],
    "PYTHON"  :["py"],
    "C"       :["c","o"],
    "JAVA"    :["java","class"],
    "CPP"     :["cpp"],
}

ph = os.path.expanduser('~')
def classification():
	p = request.forms.get("c")
	pat = ph + "/" + p
	l = os.listdir(pat)
	for i in l:
		if os.path.isfile(pat + '/' + i):      # to check file or not
			for j in directories.keys():       # mapping file_format and dictionary keys
				if i.split('.')[-1] in directories[j]: # extracting file_format from file_name
					destination = pat + '/' + j
					if not os.path.exists(destination):
						os.mkdir(destination)
					else:
						pass
					if j in ["WEB","DOCUMENTS","PROGRAMS"]:  #to create sub_directories
						for k in sub_directories.keys():
							if i.split('.')[-1] in sub_directories[k]:
								destination = pat + '/' + j + '/' + k
								if not os.path.exists(destination):
									os.mkdir(destination)
								source = pat+'/'+i
								shutil.move(source,destination)
								t = 1
								break
					else:
						source = pat+'/'+i
						shutil.move(source,destination)
						break
					if t == 1:
						break
			else:
				destination = pat+"/others"
				if not os.path.exists(destination):
					os.mkdir(destination)
				source = pat + '/' + i
				shutil.move(source,destination)
					
	return 1
def undo_classification():
	p = request.forms.get("c1")      
	exc = request.forms.get("u")
	exception = [x for x in exc.split()]    #exception folders not to undo
	pat = ph + "/" + p	
	l = os.listdir(pat)
	for i in l:
		if os.path.isdir(pat+'/'+i):		#to check directory or not
			if i not in exception: 
				for j in os.listdir(pat+'/'+i):		# listing files in the folder
					source = pat+'/'+i+'/'+j
					destination = pat+'/' + j
					shutil.move(source,destination)
				os.rmdir(pat+'/'+i)
	return 1
				
@route("/")
def home():
    return template("classify")

@post("/page")
def classify():
	r = classification()
	return template("classify")
	
@post("/page1")
def undo():
	u = undo_classification()
	u = undo_classification()
	return template("classify")
	
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root = 'static/')


run(host = "localhost", reloader = "True", port = 1234)
