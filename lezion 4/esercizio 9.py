def ccomputePi(approximation_value:float, decimal_digits) -> int :
    #terms of the pi series to compute
    terms:int = 0

    #value of pi to compute for every iteration
    pi:float = 0

    #counter for while loop
    i:int =0

    #compute needed terms to obtain approximation_value of pi
    while round(pi, decimal_digits) != approximation_value:
        #compute each term of pi series for every iteration
        #if i is even, the term of pi series is positive
        if i%2==0 :
            pi = pi +4/(2*i+1)
        #if i is odd, the term of the pi series is negative
        else:
            pi = pi - 4/(2*i +1)
        
        #incrementing terms by 1
        terms += 1
        #incrementing i by 1
        i += 1

    return terms


# calling ccomputePi function to determine how many terms are needed to obtain 3.14 ( 152 terms)
print(f"{ccomputePi(3.14, 2)} terms are needed to compute a value of pi approximated to 3.14!")
# calling ccomputePi function to determine how many terms are needed to obtain 3.141 ( 916 terms)
print(f"{ccomputePi(3.141, 3)} terms are needed to compute a value of pi approximated to 3.141!")
# calling ccomputePi function to determine how many terms are needed to obtain 3.145 ( 7010 terms)
print(f"{ccomputePi(3.1415, 4)} terms are needed to compute a value of pi approximated to 3.1415!")
# calling ccomputePi function to determine how many terms are needed to obtain 3.1459 ( 130'658 terms)
print(f"{ccomputePi(3.14159, 5)} terms are needed to compute a value of pi approximated to 3.14159!")
