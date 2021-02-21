import GetData
import ProcessData
import sys
import time

if len(sys.argv) != 4:
    print('Need id of three movies, just like "python main.py 114514 1919 810"')
    exit()

movie_ids = []
status = {1: 0b1001, 2: 0b1010, 3: 0b1100}  # 0b1 -> 计数器, 001 -> 代表种类

movie_ids.append(int(sys.argv[1]))
movie_ids.append(int(sys.argv[2]))
movie_ids.append(int(sys.argv[3]))

name = GetData.gerMovieName(movie_ids)

GetData.getMovieCmt(int(sys.argv[1]), status[1], tps=3)  # tps: 2 seconds
time.sleep(2)
GetData.getMovieCmt(int(sys.argv[2]), status[2], tps=3)
time.sleep(2)
GetData.getMovieCmt(int(sys.argv[3]), status[3], tps=3)

GetData.gerMovieName(movie_ids)

result = ProcessData.sortData(movie_ids)
ProcessData.drawVennGraph(result, name)
print('Analyse Venn graph generated successfully, please check ./out.png')
