if __name__ == '__main__':
    list1 = []
    list2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
        list2.append(score)
            
    minScore = min(list2)
    while(minScore == min(list2)):
        del list1[(list2.index(min(list2)))]
        list2.remove(min(list2))
        
    newlist = []
    for i in list1:
        if(i[1] == min(list2)):
            newlist.append(i[0])
    print('\n'.join(sorted(newlist)))
