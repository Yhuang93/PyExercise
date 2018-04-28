#Test whether **kwargs could be used with a list? Or just dictionary
def Take_and_t(**kwargs):
    for keys,values in kwargs.items():
        print(("%s=%.2f")%(keys,values))
    return
dict={"huang":1.878787,"yi":2.98989,"ning":3.12345}
Take_and_t(**dict)
