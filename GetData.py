from urllib import parse, request
from http import cookiejar
import re
import json
import time


def log(id, page):  # print log
    print(f"Now spidering {id} at page {page}.")


def parse_html(html, regex):
    pattern = re.compile(  # Regex
        regex, re.S)
    items = re.findall(pattern, html)
    return items


def save_cookie():
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    return opener


def get_info(url, regex):  # get http response
    # cookie
    opener = save_cookie()

    # headers
    headers = {
        'User-Agent': 'Douban-movies-user-analyser Client/0.1.0',
        'Referer': '',
    }

    # POST-need
    dic = {}

    # encode the data
    data = bytes(parse.urlencode(dic), encoding='utf-8',)

    # send req to web
    req = request.Request(  # make request
        url=url, data=data, headers=headers, method='GET',)
    response = opener.open(req)  # open the page / send the request

    # get response
    html = response.read().decode('utf-8', 'ignore')

    # parse html and get comment
    return parse_html(html, regex), response.status


def save_to_local(movie_id, dic=None):
    import os

    # try to get dir
    try:
        os.mkdir('D3MA-SpiderLog')
    except Exception:
        pass

    # open file and write context
    with open(f'D3MA-SpiderLog/temp_cmtInfo_{movie_id}', 'w') as fio:
        json.dump(dic, fio)
        print(f"Successfully got {movie_id} info.")
        print(f"It'is saved at 'D3MA-SpiderLog/temp_cmtInfo_{movie_id}.'")


def getMovieCmt(id, status, tps=1.6):  # tps: Time Per Spidering
    usr_dic = {}
    for page in range(1, 30000):
        # get comment user info
        usr_list, status_code = get_info(
            url=f'https://movie.douban.com/subject/{id}/reviews?sort=time&start={(page-1)*20}',
            regex=r'<a href="https://www.douban.com/people/([0-9]*)/" class="avator">')

        # roop condition
        if not usr_list:
            break

        for usr in usr_list:
            usr_dic[usr] = status

        # print log
        log(id, page)

        # wait to escape from spider-check
        time.sleep(tps)
    save_to_local(id, usr_dic)
    # print(usr_dic)


def gerMovieName(movie_ids, tps=1.6):
    code = 0b001
    movie_names = {}
    for movie_id in movie_ids:
        temp_list, status = get_info(
            f'https://movie.douban.com/subject/{movie_id}/',
            r'<title>\s*(.*) \(豆瓣\)\s*</title>')
        try:
            movie_names[code] = temp_list[0]
        except IndexError:
            print(
                "Maybe your IP was banned, please check spider speed and restart your router.")
            exit()
        print(f"{movie_id}'s name is {movie_names[code]}.")
        code <<= 1
        time.sleep(tps)
    return list(movie_names.values())
