# megathon2019

Fill in the blank question generation from textbooks. Made for Megathon 2019 @ IIIT Hyderabad


## Pre-requisites
1. Removal of paragraphs from the text - Bhavyajeet / Jai
    - (i) and other bullet points
    - Split by \n\n
    - Remove Fig lines
    - 1.2.x are headings
    - Split by headings
    - Remove numerical lines (Later)
2. Removal of sentences from the paragraphs - Pranav / Jai
    - Using Simple split by "."
3. Grouping of the sentence and paras and relevant things such as Subsection Title, etc. - Pranav / Jai
    - Find last heading and subheading of the paragraph
  

## Sentence Selection 
1. Feature Extraction
    - Sentence Similarity - Ahish --> DONE
    - Common words to the title - Bhavyajeet --> DONE
    - Similar to summary - Bhavyajeet 
    - Superlative - Pranav --> DONE
    - Abbreviations - Pranav --> DONE
    - Number (Y/N) - Pranav --> DONE
    - Certain Keyword (later)
    - Sentence Position in Para - Already provided by preprocessing
    - Length of sentence - Already provided by preprocessing
    - Number of Nouns / Length - Pranav --> DONE
    - Number of Pronouns / Length - Pranav --> DONE
    - Discourse Connective - Jai
2. Neural Network Design - Ahish / Jai


## Keywords Selection
1. Feature Extraction
    - Parse Tree Height
    - Similarity to Title
    - Other Sequence Labelling things
2. Neural Network Design 
   
