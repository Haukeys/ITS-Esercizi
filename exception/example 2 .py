def linux_interaction(a:int ,b:int)->int:
            a+b>0
            try:
                linux_interaction(a,b)
            except RuntimeError as error:
                print(error)
            else:
                print("doing even more linux thing")

print(linux_interaction(9,8))