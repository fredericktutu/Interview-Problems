INF = 10000
def all_zero(lst):
    flag = 1
    for x in lst:
        if x > 0:
            flag = 0
        elif x < 0:
            return -1
    return flag

def do(lst, i, mode,rever):  #加牌或减牌
    if mode == 1:
        lst[i] += 1 *rever
    elif mode == 2:
        lst[i] += 2 *rever
    elif mode == 3:
        for j in range(5):
            lst[i+j] += 1*rever
    elif mode == 4:
        for j in range(3):
            lst[i+j] += 2* rever

res = []
realres = []
def dfs(lst, time, m):
    # lst保存各个牌的数量， time 记录 到目前为止出了几次牌
    # m记录之前已经搜索到尽头的最少出牌数
    if time >= m:      #当前已经超出了最少出牌数
        return m
    if all_zero(lst) == 1:  #牌全部出完了
        if(time < m):

            global realres
            realres = [x for x in res]
            return time
        else:
            return m
    elif all_zero(lst) == -1:   #牌中有负数
        return m
    else:
        n = m
        for i in range(6):
            do(lst,i,3,-1)
            res.append("顺子从"+ str(i + 1) + "开始")
            n = dfs(lst, time + 1, n)
            res.pop()
            do(lst,i,3,1)
        for i in range(8):
            do(lst,i,4,-1)
            res.append("连对从" + str(i + 1) +"开始")
            n = dfs(lst, time + 1, n)
            res.pop()
            do(lst,i,4,1)
        if n != INF:
            return n
        for i in range(10):
            do(lst,i,2,-1)
            res.append("一对"+ str(i+1))
            n = dfs(lst, time + 1, n)
            res.pop()
            do(lst,i,2,1)
        if n != INF:
            return n
        for i in range(10):
            do(lst,i,1,-1)
            res.append("单张"+str(i+1))
            n = dfs(lst, time + 1, n)
            res.pop()
            do(lst,i,1,1)
        return n
         

cards = list(map(int, input().split(" ")))
print(dfs(cards, 0, INF))
print(realres)
