
#define a function which takes a string as input
def anti_vowel(text):
    Length = len (text)
    new_list=[]
    for num in range(0, Length):
        if (text[num]!="a")and(text[num]!="e")and(text[num]!="i")and(text[num]!="o")and(text[num]!="u")and(text[num]!="A")and(text[num]!="E")and(text[num]!="I")and(text[num]!="O")and(text[num]!="U"):
            new_list.append(text[num])
    print(new_list)
    new_strline=new_list[0]
    for i in range(1,len(new_list)):
        new_strline = new_strline + new_list[i]
            
    print(new_strline)
    return new_strline
    
                
      
