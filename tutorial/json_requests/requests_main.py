import requests
import time

from requests.cookies import RequestsCookieJar

event_ids = []


def print_data(items):
    global event_ids

    for data in items:
        if data["id"] in event_ids:
            break

        print '{who} => {do} => {on}'.format(
            who=data["actor"]["display_login"],
            do=data["type"],
            on=data["repo"]["name"]
        )
        event_ids.append(data["id"])
        time.sleep(0.3)


def get_event_info():
    response = requests.get('https://api.github.com/events')
    return response.json()


def main():
    while True:
        print_data(get_event_info())
        time.sleep(3)


def run():
    print "https://www.baidu.com/s?wd=123"
    response = requests.get('https://www.baidu.com/s', params={'wd': 123})
    print response.url

    print "basic auth http://wiki.cubead.com/Home"
    print requests.get('http://wiki.cubead.com/Home').status_code
    print requests.get('http://wiki.cubead.com/Home', auth=('cubead', 'cubead')).status_code
    print requests.get(
        'http://wiki.cubead.com',
        headers={
            "Authorization": "Basic Y3ViZWFkOmN1YmVhZA=="
        },
        cookies={
            "hi": "hello"
        }
    ).status_code
    print requests.get('http://wiki.cubead.com', auth=('cubead', 'cubead'), ).status_code

    print 'keep common work like auth, header'
    session = requests.Session()
    session.auth = ('cubead', 'cubead')
    jar = RequestsCookieJar()
    jar.set("hi", "hello")
    session.cookies = jar
    session.headers = {"x-name", "smite"}
    print session.get('http://wiki.cubead.com/Home').status_code

    print "save to file"
    response = session.get('http://wiki.cubead.com/Home', stream=True)

    with open('wiki_home.html', 'r+') as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)

        fd.seek(0)
        print fd.read()

if __name__ == '__main__':
    main()
