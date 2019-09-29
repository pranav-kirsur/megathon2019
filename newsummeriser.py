from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
 
import requests
"""
# getting text document from Internet
text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text
 
 
# getting text document from file
fname="C:\\Users\\TextRank-master\\wikipedia_deep_learning.txt"
with open(fname, 'r') as myfile:
      text=myfile.read()
"""    

text = """A few layers of cells beneath the epidermis are generally simple permanent tissue. Parenchyma is the most common simple permanent tissue. It consists of relatively unspecialised cells with thin cell walls. They are living cells. They are usually loosely arranged, thus large spaces between cells (intercellular  spaces) are found in this tissue (Fig. 6.4 a). This tissue generally stores food. In some situations, it contains chlorophyll and performs photosynthesis, and then it is called chlorenchyma. In aquatic plants, large air cavities are present in parenchyma to help them float. Such a parenchyma type is called aerenchyma.
The flexibility in plants is due to another permanent tissue, collenchyma. It allows bending of various parts of a plant like tendrils and stems of climbers without breaking. It also provides mechanical support. We can find this tissue in leaf stalks below the epidermis. The cells of this tissue are living, elongated and irregularly thickened at the corners. There is very little intercellular space"""


"""
#getting text document from web, below function based from 3
from bs4 import BeautifulSoup
from urllib.request import urlopen
 
def get_only_text(url):
  
  return the title and the text of the article
  at the specified url
 
 page = urlopen(url)
 soup = BeautifulSoup(page, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 return soup.title.text, text    
"""
  
print ('Summary:')
print (summarize(text, ratio=0.1))
 
print ('\nKeywords:')
print (keywords(text, ratio=0.01))
