import requests
#from selenium import webdriver

headers = {
    'User-Agent' : "Mobile"
}

#url = input("Enter the URL:")
url = input("What is the website link")
r = requests.get(url, headers=headers)
print(r.text)


print("Status code:")
print("\t'*",r.status_code)
h = requests.head(url)
print("Header:")
print("**********")

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

#headers = {
#    'User-Agent' : "Mobile"
#}

#url2 = 'http://www.wikipedia.org'
#rh = requests.get(url2, headers=headers)
#print(rh.text)
