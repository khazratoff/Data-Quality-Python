import random

#task 1
def create_random_list():
    l = []
    for _ in range(100):
        l.append(random.randint(1, 100))
    return l

#task 2
def sort_min_max(l:list):
    #bubble sort
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

#task 3
def even_odd(l:list):
    #even numbers
    even = list(filter(lambda x:x if x%2==0 else None,l))
    #odd numbers
    odd = list(filter(lambda x: x if x not in even else None,l))
    #avarages
    print(sum(even)/len(even),sum(odd)/len(odd))


def main():
    create_random_list()
    sort_min_max([1,2,12,33,4,5,6,7,8,9,1])
    even_odd([1,2,3,4,5,6,7,8,9,10])

if __name__ == '__main__':
    main()