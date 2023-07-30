# Using https://www.dnsleaktest.com/

import requests

def parse_ip(text):
    ip_start = text.find('<p class="hello">')+23
    locate_start = text.find('<p>from')+8
    text_len = len(text)
    my_ip = ""
    my_location = ""

    for i in range(ip_start, text_len):
        if text[i] != '<':
            my_ip += text[i]
        else:
            break

    if text[locate_start] == ',':
        locate_start += 2

    for i in range(locate_start, text_len):
       if text[i] != '<':
            my_location += text[i]
       else:
            break

    print("IP\t\tLocation")
    print(f"{my_ip}\t{my_location}")

parse_ip(requests.get('https://www.dnsleaktest.com/').text)
