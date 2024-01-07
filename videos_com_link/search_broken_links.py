from csv import DictReader
from webbrowser import open as open_browser
MAX_TABS=10
with open('links.csv',mode='r') as file:
    links=[x['url'] for x in DictReader(file)]
for index,link in enumerate(links,start=1):
    open_browser(link)
    if index%MAX_TABS==0:
        print(f'Limit of {MAX_TABS} tabs reached')
        input('Type any key to continue')
