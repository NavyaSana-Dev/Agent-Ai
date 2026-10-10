# def merchant(l):
#     c=0
#     for i in l:
#         if i==1:
#             c+=1
#     return c    
# l=list(map(int,input().split(',')))
# print(merchant(l))    


# from math import comb

# def players(A,B,C):
#     total=0
#     for i in range(4,min(A,C)+1):
#         w=C-i
#         if w>=1 and w<=B:
#             total+=(comb(w,i)+comb(B,w))
#     return total
# A=4
# B=5
# C=6
# print(players(A,B,C))    



# def plants(n,c,p):
#     s=0
#     water=c
#     for i in range(n):
#         if p[i]<=water:
#             water-=p[i]
#             s+=1
#         else:
#             s+=2*i+1
#             water-=p[i]
#     return s
# n=6
# c=4
# p=[1,1,1,4,2,3]
# print(plants(n,c,p))


# n=int(input())
# l=list(map(int,input().split((' '))))
# sold=[]
# stock=[]
# for i in l:
#     if i==0:
#         sold.append(stock.pop(i))
#     else:
#         stock.append(i)
# for j in stock:
#     print(j)            


stack=[]
def push():
    limit=int(input("Enter the stack limit:"))
    if len(stack)==limit:
        print("Stack is Full")
    else:
        element=list(map(int,input("Enter the Number to be inserted:").split(',')))
        stack.append(element)
        print(stack)  
def pop():
    if not stack:
        print("Stack is empty try adding elements <'.'>")
    else:
        e=stack.pop()
        print(stack)      
while True:
    print("Chose a number 1:Push,2:Pop,3:Quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break        
    else:
        print("Enter valid Number:")