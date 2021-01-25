import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))
print(res.text[:500])
play_file = open('romeoandjuliet.txt', 'wb')
