'''
Pastebin Scrapper

Requirements: Python3, requests package

Usage: 
The words in KEYWORDS will be shortlisted for in each paste.
If keyword is found it will the paste will be further refined using 
the list BLACKLIST.
If no keywords are entered, the script will simply display the text of
every paste.
'''

import os
import re
import sys
import time
import requests
from datetime import datetime

KEYWORDS = ['Keyword1', 'Keyword2', 'Keyword3']

BLACKLIST = ['Keyword3','Keyword4', 'Keyword5']

def get_data(url):
    try:
        content = requests.get(url)
    except Exception as e:
        print ("\n[!] Error: {}".format(e))
        sys.exit(0)

    return content

def get_recent_pastes():
    content = get_data('http://pastebin.com/archive')
    print ("\nGetting Data, code: {}\n".format(content))
    pastes = re.findall('" /><a href=\"\/(.+?)\">', content.text)
    return pastes
    
def get_paste(paste_id):
    return get_data('http://pastebin.com/raw.php?i=' + paste_id).text

def check_paste(paste_text, paste_id):
    paste_text = paste_text.lower()

    if len(KEYWORDS) == 0:
        print (paste_text)

    for word in KEYWORDS:
        if word in paste_text:
            if any(w in paste_text for w in BLACKLIST):
                continue
            else:
                print ("Keyword '{}' found at http://pastebin.com/raw.php?i={}"
                            .format(word, paste_id))
                index = paste_text.index(word)
                print (paste_text[index:index+30].replace('\n', '-'))
                print ('')

def main():
    print ('\nInitializing...\n')
    recent_pastes = []
    try:
        while True:
            new_pastes = get_recent_pastes()

            if len(new_pastes) == 0:
                print("[!] Blocked, retry later. {}.\n"
                        .format(datetime.now()
                        .strftime('%Y-%m-%d %H:%M:%S')))
                sys.exit(0)

            for paste_id in new_pastes:
                time.sleep(0.5)
                if paste_id not in recent_pastes:
                    recent_pastes.append(paste_id)
                    paste_text = get_paste(paste_id)

                    if paste_text == '':
                        continue
                    else:
                        check_paste(paste_text, paste_id)
                    
        print ('\nChecking For New pastes.....\n')
        time.sleep(46)

    except KeyboardInterrupt:
        print ("\n[!] Keyboard Interrupt, Exiting...")
        sys.exit(0)
        
if __name__ == '__main__':
    main()
