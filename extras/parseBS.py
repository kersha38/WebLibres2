from bs4 import BeautifulSoup

# archivo html
arch=open('index.html','r')
contenido=arch.read()
soup = BeautifulSoup(contenido,"html.parser")


print (soup.title.string)
for tag in soup.find_all('meta'):

    try:
        if tag.get('name')=='author':
            print (tag.get('content'))
    except:
        pass

    try:
        if tag.get('name')=='description':
            print (tag.get('content'))
            break
    except:
        pass
