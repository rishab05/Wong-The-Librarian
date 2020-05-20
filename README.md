![GitHub](https://img.shields.io/github/license/rishab05/Wong-The-Librarian?color=blue&style=plastic)
# Wong-The-Librarian
Your personal Librarian for searching PDF and epub of Books and give you direct download link.
Wong can open your default browser too and your book start downloading immediately for you.

### Getting Started
To run this repository clone or download using above link.

### Prerequisites
 * Python-3.6 or above
 * BeautifulSoup
 * requests
 * webbrowser

### Run
For run "Wong", first install all the requirements. You can install with ```pip install requirements.txt``` after that run
```python search.py```

### Important Note

The website changing download link for each request so for using best of this program you have to do these things
* Go to wong.py and search for variable headers, you will find it on 9 or 10 line
* Update it with your default browser headers. Don't know what are your headers, don't worry.
* Simply Go to https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending from your default browser
scroll down and copy all the content of User agents.
* Remove value of headers in file wong.py and Paste the content you copy like this headers={'User-Agent':' the content you copy'}

#### Note:
If you do not want to update and do all above steps still the program will work. Now it will opening a link of web page where your book are present simply click on download and your download will start.


### Features
* Wong can download your book directly using your browser and print the link also so that you can share it with others
* Wong give you long serach result( upto 15 with option s and upto 40 with option l)
* Wong show the name of the book, type of file(pdf or epub) and size of the book.

### Screenshots

![](Screenshots/result1.png?raw=true "Start-Wong")
![](Screenshots/result2.png?raw=true "search result")
![](Screenshots/out.png?raw=true "link of book")
![](Screenshots/browser.png?raw=true "Open your browser,start download")






Created with :heart: by Rishabh Sharma

