with open('C:/Users/Nirajan/Desktop/python 30 days/http_proxies.txt', 'r') as infile, open('C:/Users/Nirajan/Desktop/python 30 days/proxy_list.txt', 'w') as outfile:
    for line in infile:
        outfile.write("http://" + line)
