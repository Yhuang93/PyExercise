question=['name','colour','shape']
answer=['apple','red','a circle']
for question, answer in zip (question,answer):
    print("What is your %s? I am %s" %(question,answer))
