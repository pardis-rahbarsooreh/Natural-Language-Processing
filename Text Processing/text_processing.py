'''
import nltk
nltk.download()
'''

import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from part_of_Speech import get_part_of_speech


# removing noise from a text using Regular Expressions (import re)
text = "<p>    This is a paragraph</p>"
result1 = re.sub(r'<.?p>', '', text)     # remove HTML tags
result2 = re.sub(r'\s{4}', '', result1)   # remove spaces


bali_text = """
Bali is predominantly a Hindu country.
Bali is known for its elaborate, traditional dancing.
The dancing is inspired by its Hindi beliefs.
Most of the dancing portrays tales of good versus evil.
To watch the dancing is a breathtaking experience.
Lombok has some impressive points of interest – the majestic Gunung Rinjani is an active volcano.
It is the second highest peak in Indonesia. Art is a Balinese passion.
Batik paintings and carved statues make popular souvenirs.
Artists can be seen whittling and painting on the streets, particularly in Ubud.
It is easy to appreciate each island as an attractive tourist destination.
Majestic scenery; rich culture; white sands and warm, azure waters draw visitors like magnets every year.
Snorkelling and diving around the nearby Gili Islands is magnificent.
Marine fish, starfish, turtles and coral reef are present in abundance.
Bali and Lombok are part of the Indonesian archipelago. Bali has some spectacular temples.
The most significant is the Mother Temple, Besakih.
The inhabitants of Lombok are mostly Muslim with a Hindu minority.
Lombok remains the most understated of the two islands.
Lombok has several temples worthy of a visit, though they are less prolific.
Bali and Lombok are neighbouring islands.
"""

# tokenize word by word (from nltk.tokenize import word_tokenize)
word_tokenized = word_tokenize(bali_text)
# tokenize sentence by sentence (from nltk.tokenize import sent_tokenize)
sent_tokenized = sent_tokenize(bali_text)


# setting a list of stop words in english and delete them from tokenized word list (from nltk.corpus import stopwords)
stop_words = set(stopwords.words('english'))
word_tokenized_no_stopword = [word for word in word_tokenized if word not in stop_words]


# stemming a list of tokenized words (from nltk.stem import PorterStemmer)
stemmer = PorterStemmer()
word_stemmed = [stemmer.stem(token) for token in word_tokenized_no_stopword]


# lemmatizing a list of tokenized words (from nltk.stem import WordNetLemmatizer)
lemmatizer = WordNetLemmatizer()
word_lemmatized = [lemmatizer.lemmatize(token) for token in word_tokenized_no_stopword] # lemmatize() doesn't consider part pf speech, not useful!


# use a part-of-Speech function in lemmatize() (from part_of_Speech import get_part_of_speech)
word_lemmatized_with_pos = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in word_tokenized_no_stopword]












