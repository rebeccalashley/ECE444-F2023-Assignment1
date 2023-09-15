class utils:

    def reversed(num):
        
        r_num = None
        unit = None

        if num.isdigit(): 
            while num != 0: 
                unit = num % 10
                r_num = r_num * 10 + unit
                num //= 10

        else:
            print("input error: not an integer")

        return r_num

        

    def formatter(num):

        binary = None
        octal = None

        if num.isdigit():
            binary = bin(num)
            octal = oct(num)

        else:
            print("input error: not an integer")

        return binary, octal


