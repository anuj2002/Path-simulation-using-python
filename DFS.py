from pyamaze import maze,agent,textLabel,COLOR

def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

if __name__=='__main__':
    m=maze(25,25)
    # m.CreateMaze(5,4,loopPercent=100)
    m.CreateMaze(loopPercent=10,theme='light')
    bSearch,bfsPath,fwdPath=DFS(m)
    a=agent(m,footprints=True,color=COLOR.yellow,shape='square',filled=True)
    b=agent(m,footprints=True,color=COLOR.red,shape='square',filled=False)
    # c=agent(m,5,4,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    m.tracePath({a:bSearch},delay=5)
    m.tracePath({c:bfsPath},delay=5)
    m.tracePath({b:fwdPath},delay=5)

    m.run()