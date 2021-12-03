import webbrowser

f = open('webpage.html', 'w')
f.write('<html>'
        '<body>'
        '<h1>'
        'Stay tuned for our amazing summer sale!'
        '</h1>'
        '</body>'
        '</html>')
f.close()

filename = 'file:////Users/mikecrews/Documents/TechAcademy/GitHub/PythonProjects/Intermediate/' + 'webpage.html'
webbrowser.open_new_tab(filename)
