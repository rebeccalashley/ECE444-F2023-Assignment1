class utils :

    def reversed(num):
        
        if num.isdigit(): 
            while num != 0: 
                unit = num % 10
                r_num = r_num * 10 + unit
                num //= 10

        else:
            print("input error: not an integer")

        

    def formatter(num):

        if num.isdigit():
            binary = bin(num)
            octal = oct(num)

        else:
            print("input error: not an integer")


