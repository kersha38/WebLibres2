from bs4 import BeautifulSoup
# archivo html
arch=open('prueba.html','r')
contenido=arch.read()
soup = BeautifulSoup(contenido)

for tag in soup.find_all('meta'):

    print (tag)

print (soup.title)

