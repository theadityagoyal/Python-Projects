# Python program to illustrate 
# nested functions 
def outerFunction(text): 
    text = text 

    def innerFunction(): 
        print(text) 

    innerFunction() 


outerFunction('Hey!') 
