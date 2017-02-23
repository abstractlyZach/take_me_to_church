# server_startup.py

# runs a single time when the server starts

divider = '=' * 20

print(divider)
print('running startup script!')
print(divider)

# download the punkt library so that I can use the tokenizer
import nltk
nltk.download('punkt')

print(divider)
print('startup script is ending.')
print(divider)