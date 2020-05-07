from appscript import app
from bs4 import BeautifulSoup

EVERNOTE = app('Evernote')
NEW_EXAMPLE = EVERNOTE.find_note('evernote:///view/490746/s5/797681af-aef3-4b21-8e87-1060e5a02a93/797681af-aef3-4b21-8e87-1060e5a02a93/')
OLD_EXAMPLE = EVERNOTE.find_note('evernote:///view/490746/s5/73cad0ba-e8aa-4428-a42b-c0a1ce36c8ba/73cad0ba-e8aa-4428-a42b-c0a1ce36c8ba/')

print("Text Styling Samples (ENML) from older notes…")
soup = BeautifulSoup(OLD_EXAMPLE.ENML_content(), 'html.parser')
for div in soup.find_all('div'):
    print(div)
print()

# <div>Lorem ipsum dolor sit amet</div>
# <div>Lorem ipsum <span style="font-weight: bold;">dolor sit amet</span></div>
# <div>Lorem ipsum <span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</span></div>
# <div>Lorem ipsum <span style="font-weight: bold; background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</span></div>
# <div><span style="font-weight: bold;">Lorem ipsum </span><span style="background-color: rgb(255, 250, 165); font-weight: bold;-evernote-highlight:true;">dolor sit amet</span></div>

print("Text Styling Samples (ENML) from newer notes…")
soup = BeautifulSoup(NEW_EXAMPLE.ENML_content(), 'html.parser')
for div in soup.find_all('div'):
    print(div)
print()

# <div>Lorem ipsum dolor sit amet</div>
# <div>Lorem ipsum <b>dolor sit amet</b></div>
# <div>Lorem ipsum <span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</span></div>
# <div>Lorem ipsum <b style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</b></div>
# <div><b>Lorem ipsum <span style="background-color: rgb(255, 250, 165);-evernote-highlight:true;">dolor sit amet</span></b></div>