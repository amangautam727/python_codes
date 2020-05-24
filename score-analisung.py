#fint the second lowest score
if __name__ == '__main__':
    result=[]
    marks=[]

    for i in range(int(input())):
        name = input()
        score = float(input())
        result+=[[name,score]]
        marks+=[score]
    t=sorted(set(marks))[1]
    for i,j in sorted(result):
        if j==t:
            print(i)
           