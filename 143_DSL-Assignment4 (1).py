#!/usr/bin/env python
# coding: utf-8

# In[1]:


def accept_array(arr):
    n=int(input("Enter no. of elements to be entered :"))
    print("Enter the elements")
    for i in range (n):
        arr.append(int(input()))
        
        
        
def show_array(arr):
    print("The array formed is :",arr)
    
    
def ternary_search(arr,l,h,k):
    while(h>=1):
        m1=int(l+(h-l)/3)
        m2=int(h-(h-l)/3)
        
        if(k==arr[m1]):
            return m1
        elif(k==arr[m2]):
            return m2
        elif(k<arr[m1]):
            h=m1-1
        elif(k>arr[m2]):
            l=m2+1
        else:
            l=m1+1
            h=m2-1
    return -1



def main():
    arr=[]
    while(True):
        print("""
              1.Accept elements for array
              2.Display Array
              3.Ternary Search
              4.Exit from the program""")
        choice=int(input("Enter your choice"))
        if(choice==1):
            accept_array(arr)
        elif(choice==2):
            show_array(arr)
        elif(choice==3):
            k=int(input("Enter the elements which are to be searched:-"))
            l=0
            h=len(arr)-1
            print("The element to be searched is:- ",k)
            res=ternary_search(arr,l,h,k)
            if(res==-1):
                print("The value entered is not present in array")
            else:
                print("Element has been found at index:- ",res)
        elif(choice==4):
            print("You have exited the program")
            break
        
        else:
            print("Invalid Choice")
            
            
main()
    
        


# In[ ]:





# In[ ]:




