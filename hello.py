#!/usr/bin/env python
def application(env, start_response):
    body = [bytes(i + '\n') for i in env['QUERY_STRING'].split('&')]
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)

    return body
