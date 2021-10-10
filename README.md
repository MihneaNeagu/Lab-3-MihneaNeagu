# Laborator 3 - Săptămâna 3

Instalați PyCharm sau alt editor.

Predați rezolvările în săptămâna 3 într-un fișier `main.py` comis în repository-ul vostru.

Scrieți un program care determină cea mai lungă subsecvență cu o anumită proprietate a unei liste de numere. Fiecare student primește două proprietăți: prima dintre `1-10`, a doua dintre `11-20`.

Rezolvați problema folosind: 
-	Minim trei funcții: una pentru calcule, specificată, o funcție de test cu assert pentru cea de calcul și alta care citește, afișează și apelează funcția pentru calcule. Nu aveți voie să folosiți cod în afara unei funcții: fără variabile globale.  
-	O interfață cu utilizatorul care are un meniu de genul:
1. Citire date.
2. Determinare cea mai lungă subsecvență cu proprietatea 1.
3. Determinare cea mai lungă subsecvență cu proprietatea 2.
4. Ieșire.

**Funcțiile trebuie să aibă denumirile date în enunț și să fie specificate. Funcția de test trebuie să aibă prefixul test_ urmat de denumirea funcției testate**. 

Proprietățile:

1. Toate numerele sunt pătrate perfecte.
  - Funcția de calcul: **get_longest_all_perfect_squares(lst: list[int]) -> list[int]**
2. Toate numerele sunt prime.
  - Funcția de calcul: **get_longest_all_primes(lst: list[int]) -> list[int]**
3. Numerele au semne alternante.
  - Funcția de calcul: **get_longest_alternating_signs(lst: list[int]) -> list[int]**
4. Numerele sunt ordonate crescător.
  - Funcția de calcul: **get_longest_sorted_asc(lst: list[int]) -> list[int]**
5. Toate numerele sunt palindroame.
  - Funcția de calcul: **get_longest_all_palindromes(lst: list[int]) -> list[int]**
6. Toate numerele sunt divizibile cu k (citit).
  - Funcția de calcul: **get_longest_div_k(lst: list[int], k: int) -> list[int]**
7. Toate numerele sunt neprime.
  - Funcția de calcul: **get_longest_all_not_prime(lst: list[int]) -> list[int]**
8. Suma numerelor este număr prim.
  - Funcția de calcul: **get_longest_sum_is_prime(lst: list[int]) -> list[int]**
9. Produsul numerelor este impar.
  - Funcția de calcul: **get_longest_product_is_odd(lst: list[int]) -> list[int]**
10.	Toate numerele sunt pare.
  - Funcția de calcul: **get_longest_all_even(lst: list[int]) -> list[int]**
11.	Toate numerele au același număr de biți de 1 în reprezentarea binară.
  - Funcția de calcul: **get_longest_same_bit_counts(lst: list[int]) -> list[int]**
12.	Toate numerele același număr de divizori.
  - Funcția de calcul: **get_longest_same_div_count(lst: list[int]) -> list[int]**
13.	Toate numerele sunt formate din cifre prime.
  - Funcția de calcul: **get_longest_prime_digits(lst: list[int]) -> list[int]**
14.	Toate numerele au partea întreagă egală cu partea fracționară.
  - Funcția de calcul: **get_longest_equal_int_real(lst: list[float]) -> list[float]**
15.	Toate numerele se pot scrie ca `x**k`, `k` citit, `x` întreg pozitiv.
  - Funcția de calcul: **get_longest_powers_of_k(lst: list[int], k: int) -> list[int]**
16.	Toate numerele sunt în progresie aritmetică.
  - Funcția de calcul: **get_longest_arithmetic_progression(lst: list[int]) -> list[int]**
17.	Media numerelor nu depășește o valoare citită.
  - Funcția de calcul: **get_longest_average_below(lst: list[int], average: float) -> list[int]**
18.	Numărul de cifre este în ordine descrescătoare.
  - Funcția de calcul: **get_longest_digit_count_desc(lst: list[int]) -> list[int]**
19.	Concatenarea numerelor din subsecvență are cifrele în ordine crescătoare.
  - Funcția de calcul: **get_longest_concat_digits_asc(lst: list[int]) -> list[int]**
20.	Concatenarea numerelor din subsecvență este număr prim.
  - Funcția de calcul: **get_longest_concat_is_prime(lst: list[int]) -> list[int]**
