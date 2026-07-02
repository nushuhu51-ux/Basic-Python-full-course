# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in
"""
## 1. local variable
def func1():
    a = 1
    print(a)
    
def func2():
    b = 2
    print(b)
    
func1()
func2()
"""

## 2. Global variable
def func1():
    x = 1
    
    def func2():
        x = 2
        print(x)
        
    func2()
func1()