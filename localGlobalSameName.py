def spam():
    eggs = 'spam local'
    print(eggs) # print spam local eggs
    
def bacon():
    eggs = 'bacon local'
    print(eggs) #print bacon local eggs
    spam()
    print(eggs)
    
eggs = 'global'
bacon()
print(eggs) #print global
    
    
