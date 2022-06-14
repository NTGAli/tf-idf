import codecs
import io
import sys
from urllib import request

import app as app

import br
import main

def makeHtml(query):
    if query is None:
        return
    titles, urls, txts, cosines = main.getList(query)
    print(f'{query} Query:')
    with codecs.open('helloworld.html', 'w', "utf-8") as f:
        f.write(f"""
            <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>computer engineering mutex concept - Google Search</title>
        <link rel="shortcut icon" type="image" href="assets/" />
        <link rel="stylesheet" type="text/css" href="style.css" />
        <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
    </head>

    <body>
        <div id="header">
            <div id="topbar">
                <img id="searchbarimage" src="assets/google_logo.png" />
                <div id="searchbar" type="text">
                    <input id="searchbartext" type="text" value="{query}" disabled />
                    <button id="searchbarmic">
                        <img src="images/googlemic.png" />
                    </button>
                    <button id="searchbarbutton">
                        <svg focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path
                                d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z">
                            </path>
                        </svg>
                    </button>
                </div>

                <div id="boxesicon"></div>
                <div id="bellicon"></div>
                <img id="profileimage" src="images/photo.png" />
            </div>
            <div id="optionsbar">
                <ul id="optionsmenu1">
                    <li id="optionsmenuactive">All</li>
                    <li>News</li>
                    <li>Videos</li>
                    <li>Images</li>
                    <li>Maps</li>
                    <li>More</li>
                </ul>

                <ul id="optionsmenu2">
                    <li>Settings</li>
                    <li>Tools</li>
                </ul>
            </div>
        </div>
        <div id="searchresultsarea">
            <p id="searchresultsnumber">About 155,000 results (0.56 seconds) </p>
            """)
        for i in range(10):
            f.write(f"""
                <div class="searchresult">
                    <a href="{urls[i]}">
                        <h2>{titles[i]}</h2>
                    </a>
                    
                   <a>{urls[i]}</a> <button></button>
                    <p>{txts[i][0:100]}</p>
                    <p> {cosines[i]}</p>
                </div>
                """)

        f.write("""


            <div class="pagebar">
                <ul class="pagelist">
                    <li class="pagelistprevious">Previous</li>
                    <li class="pagelistfirst">1</li>
                    <li class="pagelistnumber">2</li>
                    <li class="pagelistnumber">3</li>
                    <li class="pagelistnumber">4</li>
                    <li class="pagelistnumber">5</li>
                    <li class="pagelistnumber">6</li>
                    <li class="pagelistnumber">7</li>
                    <li class="pagelistnumber">8</li>
                    <li class="pagelistnumber">9</li>
                    <li class="pagelistnumber">10</li>
                    <li class="pagelistnext">Next</li>
                </ul>
            </div>
        </div>

        <div id="footer">
            <div id="footerlocation">
                <p>Somewhere, Moon </p>
                <p> - From your phone (Location History) - Use precise location - Learn more</p>
            </div>

            <ul id="footermenu">
                <li>Help</li>
                <li>Send feedback</li>
                <li>Privacy</li>
                <li>Terms</li>
            </ul>
        </div>
    </body>

    </html>
    """)
    message = "aaa"
    # f.write(message)
    f.close()


# if __name__ == "__main__":
#     makeHtml("متاورس")