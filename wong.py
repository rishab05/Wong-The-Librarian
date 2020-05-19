from bs4 import BeautifulSoup as bs
import pyperclip as pc
import requests
import re
import webbrowser as wb
from search import menu


headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}

def search_book(query,limit):

    allbook=[]
    i=1
    url='https://b-ok.cc/s/'+query

    source=requests.get(url,headers=headers)

    soup=bs(source.text,'html.parser')
    if(soup.find_all('h3',itemprop="name")):

        for result,type in zip(soup.find_all('h3',itemprop="name"),soup.find_all('div',class_="bookProperty property__file")):
            if(i==limit):
                break

            else:
                name=result.text.replace('\n','')
                print(i,name+type.text)
                print()
                i+=1
                allbook.append(result.a.get('href'))


        ch=int(input("Select a book "))

        print("Hold on tight getting your link ..............................")


        url='https://b-ok.cc/'+allbook[ch-1]

        get_book(url)
    else:
        print("No book found...")
        menu()


def get_book(url):

    source=requests.get(url,headers=headers)
    soup=bs(source.text,'html.parser')
    dl=soup.find('a',class_="btn btn-primary dlButton addDownloadedBook")
    l="https://b-ok.cc"+dl.get('href')

    print("Here is your direct download link: ",l)
    print("try to opening it in your default web browser...............")
    wb.open_new_tab(l)
    print()
    print("\nThanks for using\nCreated with " + "\u2764"+ " by Rishabh Sharma")
    menu()
