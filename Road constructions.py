# In the famous city of Kyzylorda, where there are N centers,
# a certain count lives - Azamat.
# He wants to know the number of different road structures between them,
# if it is known that two centers can be
# connected in one of two directions or not connected at all.
# Input: the number of centers in the city, 2 ≤ N ≤ 100.
# Output: It is necessary to display the number of all possible road constructions.
# Solution: there are 3 road options between each two centers and there are (n * (n - 1)) / 2 possible pairs from centers, so number of different road constructions between n centers is pow(3, (n * (n - 1)) / 2).

n = int(input())
print(pow(3, ((n * (n - 1))//2))