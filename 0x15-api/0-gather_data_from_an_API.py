#!/usr/bin/python3
"""
 Python script that, using this REST API, given employee ID, returns inf
 """
import requests as r
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = r.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    
    done_tasks = [title.get("title") for title in to_do if
                 title.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(done_tasks),
                                                          len(to_do)))
    
    [print("\t {}".format(title)) for title in done_tasks]
