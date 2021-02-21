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
        0b01001: 0,
        0b01010: 0,
        0b10011: 0,
        0b01100: 0,
        0b10101: 0,
        0b10110: 0,
        0b11111: 0,
    }
    for v in total.values():
        res[v] += 1
    return list(res.values())


def drawVennGraph(result, name):
    # Import the library
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fmg
    from matplotlib.pylab import mpl
    from matplotlib_venn import venn3

    # set Chinese font env
    plt.rcParams['font.sans-serif'] = ['KaiTi']
    mpl.rcParams['axes.unicode_minus'] = False

    # Make the diagram
    graps = venn3(subsets=result, set_labels=name)
    plt.savefig('out.png')
