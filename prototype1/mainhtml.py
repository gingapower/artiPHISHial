import itertools
import re


def find_links(document, list):
    for a in document.find_all('a', href=True): 
        if a.text: 
            list.append(a['href'])
    a = document.find_all('a')

def find_links_title(document, list, outputlist):
    for link in document.find_all('a'):
        title = link.get('title')
        if title is not None and any(var.lower() in title.lower() for var in list):
            href = link.get('href')
            outputlist.append(href)
            return True

def check_form(document, list1, list2):
    for var1, var2 in itertools.product(list1, list2):
        if document.find('input', {'name'.lower(): var1}) and document.find('input', {'name'.lower(): var2}):
            return True
                 
def check_links(linklist, file, outputlist):
    found_var = False
    for var in file:
        for x in linklist:
            if var in x.lower():
                outputlist.append(x)
                found_var = True
    if found_var:
        return True
    else:return False
        
def check_html(outputlist,file):
    file_path = 'output.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "href" in line:
                matches = re.findall(r'href="(.+?)"', line)
                check_links(matches, file, outputlist)
                                          
            if "login" in line:
                for url in re.findall('"(/[^"]*)"', line):
                    if url.startswith('/'):
                        outputlist.append(url)
                        return True
                       
def check_google_login():
    file_path = 'output.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "https://accounts.google.com/" in line:
                return True
    return False
                
def buildurl(linklist, url):
    for index, element in enumerate(linklist):
        if element.startswith("/"):
            if url.endswith("/"):
                url = url[:-1]
            newurl = url + element
            linklist[index] = newurl

def sortlinks(linklist, unique_strings):
    updated_links = []
    for link in linklist:
        updated_link = link.split('?')[0]
        updated_links.append(updated_link)

    for string in updated_links:
        if string not in unique_strings:
            unique_strings.append(string)
    updated_links[:] = unique_strings

def filter_links(links, list):
    keyword_list = ["signup", "login", "signin"]
    
    for link in links:
        for keyword in keyword_list:
            if keyword in link:
                list.append(link)
                #break  # Stop checking other keywords for this link

    return list