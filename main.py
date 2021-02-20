import GetData

movie_ids = []

movie_id = 19944106  # 美人鱼
movie_ids.append(movie_id)
# status = 0b01001
# GetData.getMovieCmt(movie_id, status)

movie_id = 30163509  # 飞驰人生
movie_ids.append(movie_id)
# status = 0b01010
# GetData.getMovieCmt(movie_id, status)

movie_id = 26698897  # 唐人街探案2
movie_ids.append(movie_id)
# status = 0b01100
# GetData.getMovieCmt(movie_id, status)


def mergeDict(A, B):
    for key, value in B.items():
        if key in A:
            A[key] += value
        else:
            A[key] = value
    return dict(sorted(A.items(), key=lambda d: d[1]))


def parseData(movie_ids):
    import json

    total = {}

    for mid in movie_ids:
        try:
            with open(f'D3MA-SpiderLog/temp_cmtInfo_{mid}', 'r') as fio:
                temp = json.load(fio)
                if total:
                    mergeDict(total, temp)
                else:
                    total = temp
        except FileNotFoundError:
            print('SpiderLogNotExist: Please check dir "D3MA-SpiderLog" or delete it.')
            exit()
    return total


def sortData(movie_ids):
    total = parseData(movie_ids)
    res = {
        0b11111: 0,
        0b10110: 0,
        0b10101: 0,
        0b10011: 0,
        0b01100: 0,
        0b01010: 0,
        0b01001: 0
    }
    for v in total.values():
        res[v] += 1
    print(res)


sortData(movie_ids)
