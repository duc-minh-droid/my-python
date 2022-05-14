
def pos(a,/,b,c,**args):
    print(args)
    print(a, b,c)

x = {
    'name':'Minh',
    'age':19
}
pos(1,c=1,b='is',**x)













