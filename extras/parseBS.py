from bs4 import BeautifulSoup

# archivo html
arch=open('prueba.html','r')
contenido=arch.read()


soup = BeautifulSoup(contenido, "lxml")

for tag in soup.find_all('string'):

    print (tag)

print (soup.title)

