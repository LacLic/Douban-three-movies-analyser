from urllib import parse, request
from http import cookiejar
import re
import json
import time


def log(id, page):
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


def get_html(id, start=0):
    # cookie
    opener = save_cookie()

    # url
    url = f'https://movie.douban.com/subject/{id}/reviews?sort=time&start={start}'

    # headers
    headers = {
        'User-Agent': 'Douban-movies-user-analyser Client/0.0.1',
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
    return parse_html(
        html, r'<a href="https://www.douban.com/people/([0-9]*)/" class="avator">')


def save_to_local(movie_id, dic=None):
    import os

    try:
        os.mkdir('D3MA-SpiderLog')
    except Exception:
        raise

    with open(f'D3MA-SpiderLog/temp_cmtInfo_{movie_id}', 'w') as fio:
        json.dump(dic, fio)
        print(dic)


def getMovieCmt(id, status):
    usr_dic = {}
    for page in range(1, 30000):
        # get comment user info
        usr_list = get_html(id=id, start=(page-1)*20)

        # roop condition
        if not usr_list:
            break

        for usr in usr_list:
            usr_dic[usr] = status

        # print log
        log(id, page)

        # wait to escape from spider-check
        time.sleep(1.5)
    save_to_local(id, usr_dic)
    # print(usr_dic)
