def check_lenght(x:str):

    if len(x) > 10:
        print(f"{x} bigger than 10")
    elif len(x) < 10:
        print(f"{x} smaller than 10")
    else :
        print(f"{x} equal 10")

check_lenght("ciao caro")