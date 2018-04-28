def censor(text,word):
    #Length_text=len(text)
    Length_word=len(word)
    #for tenum in range(0,(Length_text+1)):
     #   if text[tenum:(tenum+Length_word+1)] == word:
    print(text.replace(word,("*"*Length_word)))
    
    return None
    
