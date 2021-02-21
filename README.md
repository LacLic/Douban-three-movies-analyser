# Douban-three-movies-analyser

本项目旨在分析3个电影之间的用户分布，借以更好地分析三部电影的关系。

注：如果ip被封禁，重启路由器更换ip即可。

最后的结果在目录下的out.png中
# 算法

1. 爬取的时候，默认每1.6秒爬取一次评论内容（api限制一分钟内只能爬40次）
2. 爬取到的数据按用户id归并入字典（单id多次评论只算一次）
3. 不同影评分别存储到了不同temp文件中，方便后续项目调试修改
4. 不同影评归并的时候使用二进制状态码进行区别，最后直接通过字典序计数
5. 一开始考虑到遍历所有数据的时间复杂度，但是由于爬虫本身为了伪装，需要主动设置间隔时间，后续遍历字典花的时间其实相比之下不算什么，就没有进行额外的改动了

# Instruction

need install urllib, matplotlib, matplotlib_venn

## clone the repository

```
mkdir github_repo
cd github_repo
git pull https://github.com/LacLic/Douban-three-movies-analyser
cd Douban-three-movies-analyser
```

## run the project in command line at format like

```python .\main.py [movid_id1] [movid_id2] [movid_id3]```

May use ```python3``` instead of ```python``` if NoPythonCommand error occurs

## Example

```python .\main.py 19944106 30163509 26698897```

```python3 main.py 114514 1919 810```
