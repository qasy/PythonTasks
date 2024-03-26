def select(input_func):
    # *args - allow to use all args of input_func 
    def output_func(*args):
        print("***********")
        input_func(*args)
        print("***********")
    return output_func

def log(input_func):
    def output_func(*args):
        if args[1] < 0:
            print("Warning: ", end = "")
        else:            
            print("Log: ", end = "")
        is_adult = input_func(*args)
        if is_adult == True:
            print(f"Already adult, because is_adult = ", end="")
        return is_adult
        
    return output_func

@log
def print_person(name, age):
    print(f"Name = {name}, Age = {age}")
    if age > 18:
        return True
    else:
        return False
    
        

@select
def sum(a, b):
    print(a + b)

def main():
    # sum(2,7)
    res = print_person("Alex", 10)
    print(res)
        
main()