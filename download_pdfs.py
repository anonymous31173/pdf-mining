from requests import get
from urlparse import urljoin
from os import path, getcwd, system
from bs4 import BeautifulSoup as soup
from sys import argv

def get_all_links(html):
    bs= soup(html)
    system("rm mylinks.txt")
    system("lynx -cache=0 -dump -listonly " + str(url) + " | grep \".*\.pdf$\" | awk '{print $2}' | tee mylinks.txt")
    links = []
    with open('mylinks.txt', 'rb') as myfile:
        links = myfile.readlines()
    return links

def get_pdf(url):
    print(url)
    links = get_all_links(url)
    for link in links:
        system("wget " + str(link))

if __name__=='__main__':
    if len(argv) not in (2, 3):
        print 'Error! Invalid arguments'
        print __doc__
        exit(-1)
    arg= ''
    url = argv[1]
    print(argv[1])
    if len(argv)==3:
        arg= argv[2]
    base_dir= [getcwd(), arg][path.isdir(arg)]
    try:
        get_pdf(url)
    except Exception, e:
        print e
        exit(-1)

	
	