def check_if_palindrome(n):
    aux=n
    inv=0
    while aux:
        inv=inv*10+int(aux%10)
        aux=int(aux/10)
    if n==inv:
        return True
    else:
        return False
def check_if_power(n,k):
    for d in range(1,n//2+1):
        if d**k==n:
            return True
    return False
def get_longest_all_palindromes(list):
    largest = 0
    temp_largest = 0
    location = 0
    for count, value in enumerate(list):
        if check_if_palindrome(value)==True:
            temp_largest += 1
        else:
            temp_largest = 0
        if temp_largest >= largest:
            largest = temp_largest
            location = count + 1 - temp_largest
    rezultat = []
    for i in range(location,location+largest):
        rezultat.append(list[i])
    
    return rezultat


def get_longest_powers_of_k(list,k):
    largest = 0
    temp_largest = 0
    location = 0
    for count, value in enumerate(list):
        if check_if_power(value,k)==True:
            temp_largest += 1
        else:
            temp_largest = 0
        if temp_largest >= largest:
            largest = temp_largest
            location = count + 1 - temp_largest
    rezultat= []
    for i in range(location,location+largest):
        rezultat.append(list[i])
    return rezultat
        

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([1,111,333,222,54,23])==[1,111,333,222]

test_get_longest_all_palindromes()

def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([8,27,64,5,23,11],3)==[8,27,64]

test_get_longest_powers_of_k()

def citire_afisare_get_longest_all_palindromes():
    list=[]
    while True:
        element=input("Element: ")
        if element=="x":
            break
        else:
            list.append(int(element))
    print(get_longest_all_palindromes(list))

def citire_afisare_get_longest_powers_of_k():
    list=[]
    while True:
        element=input("Element: ")
        if element=="x":
            break
        else:
            list.append(int(element))
    k=int(input("Puterea: "))
    print(get_longest_powers_of_k(list,k))

def main():
    # interfata de tip consola aici
    secventa=input("Secventa: ")
    if secventa=="1":
        citire_afisare_get_longest_all_palindromes()
    if secventa=="2":
        citire_afisare_get_longest_powers_of_k()

    
main()
exit(0)