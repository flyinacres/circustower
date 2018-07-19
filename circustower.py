# circus tower
test =(65,100), (70, 150), (56, 90), (75, 190), (60, 95), (68,110)
#test = (1,1), (2,2), (3,3)


    
class towers:
    def __init__(self, specs):
        self.height, self.weight = specs
        self.bases = []
        self.noSmaller = True
        
    def findHeight(self, curHeight, maxHeight, best):
        if len(self.bases) == 0:
            if curHeight + 1 > maxHeight:
                best = best + "({0},{1})".format(self.height, self.weight)
            return curHeight + 1, best
        
        for n in self.bases:
            tHeight, tBest = n.findHeight(curHeight + 1, maxHeight, best)        
            print(best + "({0},{1})".format(self.height, self.weight))
            print(curHeight, tHeight, maxHeight)
            if tHeight > maxHeight:
                maxHeight = tHeight
                best = "({0},{1})".format(self.height, self.weight) + tBest
                
        return maxHeight, best
            
        
t = []

for p in test:
    n = towers(p);
    print("new person: (", n.height, ", ", n.weight, ")")    
    
    for tt in t:
        if tt.height < n.height and tt.weight < n.weight:
            print("   Existing smaller (", tt.height, ", ", tt.weight, ")")
            tt.bases.append(n)
            n.noSmaller = False
        elif tt.height > n.height and tt.weight > n.weight:
            print("   Existing bigger (", tt.height, ", ", tt.weight, ")")
            n.bases.append(tt)
            
    t.append(n)

        
for tt in t:
    
    
    if  tt.noSmaller:
       # print("For (", tt.height, ", ", tt.weight, ")")
       # for n in tt.bases:
       #     print("(", n.height, ", ", n.weight, "), ", end='')
       # print() 
        
        best = ''
        maxHeight = 0
        tHeight, tBest = tt.findHeight(0, 0, "")
        if tHeight > maxHeight:
            maxHeight = tHeight
            best = tBest
                                       
            
        print("the max height is ", maxHeight)
        print("the best is ", best)
