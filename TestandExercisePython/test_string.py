def reverse(text):
  Length = len (text)
  processed_text=text[-1]
  
  for num in range(2,Length+1):
    processed_text = processed_text + text[-num]
  print (processed_text)
  return  
