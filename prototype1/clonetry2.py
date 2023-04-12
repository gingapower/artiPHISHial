from pywebcopy import save_webpage

def clone_webpage(furl):
    print(furl)
    download_folder = 'C:/Users/Fabian Huber/Desktop/ArtiPHISHial/artiPHISHial/Login-Scraper/downloads'    
    kwargs = {'bypass_robots': True, 'project_name': "clone", 'open_in_browser':True, 'delay':None,'threaded':False,}
    save_webpage(furl, download_folder, **kwargs)
#     save_webpage(
#       url=furl,
#       project_folder=download_folder,
#       project_name= furl,
#       bypass_robots=True,
#       debug=True,
#       open_in_browser=True,
#       delay=None,
#       threaded=False,
# )
#clone_webpage(url)
