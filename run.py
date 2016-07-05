#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib

count=1
def extract_post(rurl):
    global count
    r = urllib.urlopen(rurl).read()
    soup = BeautifulSoup(r, "html.parser")
    
    print "<br> <br> <div class=\"container\"> <button type=\"button\" class=\"btn btn-success\" data-toggle=\"collapse\" data-target=\"#post{}\"> <span class=\"glyphicon glyphicon-collapse-down\"></span>".format(count)
    for header in soup.findAll(attrs={'class' : 'entry-header'}):
            print header.text.encode('utf8')
    print "</button> <div id=\"post{}\" class=\"collapse\">".format(count)
    print header.encode('utf8')
    for content in soup.findAll(attrs={'class' : 'entry-content'}):
            print content.encode('utf8')
    print "</div> </div>"
    count = count + 1


page_number=5
while(page_number>0):
#    print 'http://www.geeksforgeeks.org/category/c-arrays/page/{}/'.format(page_number)
#    post_list = BeautifulSoup(urllib.urlopen('http://www.geeksforgeeks.org/category/c-arrays/page/{}/'.format(page_number)).read(),"html.parser")
    post_list = BeautifulSoup(urllib.urlopen('http://www.geeksforgeeks.org/category/c-strings/page/{}/'.format(page_number)).read(),"html.parser")

    for links in post_list.findAll(attrs={'class' : 'entry-title'}):
        extract_post(links.find('a').get('href'))
    page_number = page_number - 1

