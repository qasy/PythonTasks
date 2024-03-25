def sum_with(number1):
    def sum(number2):
        nonlocal number1
        print(number1 + number2)    
    return sum
    
    
    
def main():
    f = sum_with(5)
    f(2)
    f(4)
    
main()