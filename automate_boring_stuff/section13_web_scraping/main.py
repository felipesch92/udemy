import webbrowser
import sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = input('Digite o endereço que deseja visualizar: ')
# https://www.google.com.br/maps/place/R.+Aurora,+1250+-+Mal.+Rondon,+Canoas+-+RS,+92020-510/@-29.9099024,-51.1663399,17z/data=!3m1!4b1!4m5!3m4!1s0x9519701ae5eb0d6f:0xe543d4184fa7cbd1!8m2!3d-29.9099024!4d-51.1663399
webbrowser.open('https://www.google.com.br/maps/place/' + address)
