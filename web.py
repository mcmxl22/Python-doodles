import webbrowser

new = 2

choice = raw_input('Type site name:\n> ')
site = choice
url1 = 'www..com'

url = url1[:4] + site + url1[4:]

webbrowser.open(url,new=new)