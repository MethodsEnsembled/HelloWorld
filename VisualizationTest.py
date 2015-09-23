
import nltk
import re
import string
`
# Create initial documents list

doc = [ ]
doc.append( 'It is a far, far better thing I do, than I have every done' )
doc.append( 'Call me Ishmael' )
doc.append( 'Is this a dagger I see before me?' )
doc.append( 'O happy dagger' )

print doc``
# Remove punctuation, then tokenize documents

punc = re.compile( '[%s]' % re.escape( string.punctuation ) )
term_vec = [ ]

for d in doc:
    d = d.lower()
    d = punc.sub( '', d )
    term_vec.append( nltk.word_tokenize( d ) )

# Print resulting term vectors

for vec in term_vec:
    print vec