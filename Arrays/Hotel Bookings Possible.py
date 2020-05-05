# https://www.interviewbit.com/problems/hotel-bookings-possible/

def Bookings(arrive, depart, K):
	store = []
	for i in range(len(arrive)):
		store.append((arrive[i],1))
		store.append((depart[i],0))				

	store.sort()
	cur_book, max_book = 0, 0
	for i in range(len(store)):
		if store[i][1]==1:
			cur_book+=1
			max_book = max(max_book, cur_book)
		else:
			cur_book-=1
	return K>=max_book

arrive = [int(i) for i in input().split()]
depart = [int(i) for i in input().split()]
k = int(input())
print(Bookings(arrive, depart, k))