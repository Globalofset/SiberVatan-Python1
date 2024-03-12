# def palindrom(metin):
#     return metin == metin[::-1]
# kelime_girin = input("bir kelime girin")
# if  palindrom(kelime_girin):
#     print (f"{kelime_girin}palindromdur")
# else:
#     print(f"{kelime_girin}  palindrom değildir")


# liste1 = [1,2,3,4,5]
# liste2 = [3,4,5,6,7]

# ortak=[]
# for eleman in liste1:
#     if eleman in liste2:
#         ortak.append(eleman)

# print(ortak)


# liste = [1,2,3,4,5,6,7]
 
# frekans = {}

# for eleman in liste:
#     if eleman in frekans:
#         frekans [eleman] +=1
#     else:
#         frekans [eleman] =1

# for eleman , frekans in  frekans.items():
#     print(f"{eleman}: {frekans}")


# def fibonacci(n):
#     a , b  = 0 , 1
#     result = []
#     for i in  range (n):
#         result.append(a)
#         a , b = b , a + b
#     return result

# print(fibonacci(9))

def fibonacci(n):
    fib = [0,1]
    for i in range(2 , n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(10))











 



 










