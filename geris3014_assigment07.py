#1
# O(n^3) siden den har høyest vekst

#2
# O(nlogn) siden den første for loopen gir n ganger også dobbles j
# som gir den andre loopen logN ganger

#3
# O(n^2) for loop gir n ganger også enda for loop som gir n som gir n * n

#4
def solve_problem(S):
    A = []
    sum = 0
    for i in range(len(S)):
        sum += S[i]
        average = sum / (i + 1)
        A.append(average)
    return A

print(solve_problem([1,2,3]))
# One for loop makes O(n) notation