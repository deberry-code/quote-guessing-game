import requests
from bs4 import BeautifulSoup
import random

everyquote=[]
baseurl='http://quotes.toscrape.com'
page='/page/'


def nextpg():
  num=1
  while True: #while true when ready to be infinite
      currentpage=f'{baseurl}{page}{num}'
      response=requests.get(currentpage) #making requests to the url
      soup=BeautifulSoup(response.text, 'html.parser') #instance of beautifulsoup object. here is where the html is
      # print(currentpage)
      resp=response.text
      quotes=soup.find_all(class_='quote') #extracting every element inthe page with the html class 'quote'
      # print(quotes)
      num=num+1
      if "No quotes found!" in str(soup):
        print(f'ended at{currentpage}.')
        break
      else:
        for i in quotes:
          everyquote.append({'Quote': i.find(class_='text').get_text(), 'Author': i.find(class_='author').get_text(), 'Bio link:': f"{baseurl}{i.find('a')['href']}"})


def game():
  tries=4
  guessthis=random.choice(everyquote)
  print(guessthis['Quote'])
  for i in range(0, tries+1):
    if i ==tries:
      print(f"Wrong! It was {guessthis['Author']}. You lost. :(")
      break
    else:
      yourguess=input("Who do you think said this quote? ")
      if yourguess.lower()==guessthis['Author'].lower():
        print("Congratulations! You win!")
        break
      else:
        if i>=tries-1:
          continue
        else:
          print("Wrong! Try again.")
          continue

game()
