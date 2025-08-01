import time, sys

indent = 0 #how many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not

try:
    while True: #the main loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second.
        
        if indentIncreasing:
            #increase the number of spaces
            indent = indent + 1    
            
        if indent == 20:
            indentIncreasing = False # change direction
        
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
                
except KeyboardInterrupt:
    sys.exit()
   
    
    
    
    
    
    