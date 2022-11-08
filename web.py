import webbrowser
import os
'''
with open ("index.html", "r") as f:
	html = f.read()
'''
file = "index.html"
realpath = os.path.realpath(file)
browserpath = realpath.replace("#", "%23")
print(realpath, browserpath)
webbrowser.open('file:///' + browserpath)
