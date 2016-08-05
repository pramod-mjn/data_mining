def cluster(nums, centers):
    while(1):
        clusters = {}
        for i, each in enumerate(centers):
            clusters[i] = []

        for num in nums:
            diff = []
            for i, center in enumerate(centers):
                diff.append(abs(center - num))
            clusters[diff.index(min(diff))].append(num)
        new_centers = []
        for i, each in enumerate(centers):
            if(clusters[i] == []):
                new_centers.append(each)
            else:
                new_centers.append(round(sum(clusters[i])/len(clusters[i])))

        for i, each in enumerate(clusters.values()):
            print("cluster ",i+1," : ",each)
        print("centers :", new_centers)
        print("\n")

        if(new_centers == centers):
            break
        centers = new_centers

def main():
    '''
    x = input("Enter numbers").split()
    y = input("Centers").split()
    x = [int(i) for i in x] 
    y = [int(i) for i in y]'''
    x = [11,8,13,10,13,5,4,12,6,10,11,6,7,13]
    x.sort()
    y = [1,2,3]
    cluster(x,y)

main()
