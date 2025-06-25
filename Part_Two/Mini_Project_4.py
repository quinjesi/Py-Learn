import webbrowser

file = open('new.html', 'w')
msg = '<!DOCTYPE html> \n<html>\n<head>\n<title>My Web Page</title>\n</head>\n<body>\n<h1>Welcome to My Web Page</h1>\n<p>This is a simple web page created using Python.</p>\n</body>\n</html>'

file.write(msg)
file.close()

webbrowser.open_new_tab('new.html')