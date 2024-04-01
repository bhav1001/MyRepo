def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
    
def WaterJug(m,n,d):
    j1=0
    j2=0
    s=0 #Step Count
    print("(",j1,j2,")") #prints initial state
    j2=n
    s=s+1
    print("(",j1,j2,")")
  
    while(j1!=d or j2!=d):
        temp=min(j2,m-j1) ## Find the maximum amount that can be poured 
        j1=j1+temp
        j2=j2-temp
        print("(",j1,j2,")")
        s=s+1
        if(j1==m):
            j1=0
        if(j2==0):
            j2=n
        if(j1==d or j2==d):
            break
        print("(",j1,j2,")")
        s+=1
    
    print("Number Of steps ",s)

if __name__=="__main__":
        
    m=int(input("Enter Jug1 Capacity "))
    n=int(input("Enter Jug2 Capacity "))
    d=int(input("Enter Required Amount: "))

    if(d%gcd(m,n)==0 and (d<m or d<n)):#Condition whether Solution is possible or not
      
        WaterJug(m,n,d)
    
    else:
        print("NOT POSSIBLE")
 
