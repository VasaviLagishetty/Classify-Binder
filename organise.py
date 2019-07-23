import os 
from pathlib import Path

DIRECTORIES = { 
	"HTML": [".html5", ".html", ".htm", ".xhtml"], 
	"IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
			".heif", ".psd"], 
	"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
			".qt", ".mpg", ".mpeg", ".3gp"], 
	"DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
				"pptx"], 
	"ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
				".dmg", ".rar", ".xar", ".zip"], 
	"AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
	"PLAINTEXT": [".txt", ".in", ".out"], 
	"PDF": [".pdf"],  
	"XML": [".xml"], 
	"EXE": [".exe"], 
	"PYTHON":[".py"],
	"SHELL": [".sh"] 
} 

FILE_FORMATS = {file_format: directory 
				for directory, file_formats in DIRECTORIES.items() 
				for file_format in file_formats}
def organize_junk(directory_name): 
	for entry in os.listdir(directory_name):
		file_path = Path(directory_name).joinpath(Path(entry))
		if file_path.is_dir():
			continue
		print(file_path)
		file_format = file_path.suffix.lower()
		print(file_format)
		if file_format in FILE_FORMATS: 
			directory_path = Path(directory_name).joinpath(Path(FILE_FORMATS[file_format]))
			directory_path.mkdir(exist_ok=True)
			print(directory_path)
			file_path.rename(directory_path.joinpath(Path(entry)))
directory_name = input("enter path of directory which is to be organized:")
organize_junk(directory_name) 
