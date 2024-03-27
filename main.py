from langdetect import detect 
# try to enter full text and not only words, language model is not 100% accurate always
text = input("Enter any text in any language: ")
print(detect(text))
