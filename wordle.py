from pyquery import PyQuery
from random import choice
import requests

text_url = "https://www.mit.edu/~ecprice/wordlist.10000"
# text_url = "https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/"
text_response = requests.get(text_url)
# print(text_response)
text_html = PyQuery(text_url)

text = str(choice(text_html.text().split()))

while len(text) != 5:
    text = str(choice(text_html.text().split()))
    
# print(text)
# print(list(text))

ans_word = []
play_time = 0
while True:
    word = str(input("請輸入一個由5個英文字母組成的英文單字：").lower())
    if len(word) == 5 and word in text_html.text().split():
        
        if list(text) == list(word):
            print("🟩🟩🟩🟩🟩")
            ans_word.append("🟩🟩🟩🟩🟩")
            play_time += 1
            break
        else:
            nums = [0, 1, 2, 3, 4]
            res_word = []         
            for n in nums:
                if list(word)[n] in list(text) and list(word)[n] == list(text)[n]:
                    res_word.append("🟩")
                elif list(word)[n] in list(text) and list(word)[n] != list(text)[n]:
                    res_word.append("🟨")
                else:
                    res_word.append("🟫")
            space = ""
            print(space.join(res_word))
            ans_word.append(space.join(res_word))
            play_time += 1
            continue
        break
    elif len(word) !=5 and word in text_html.text().split():
        print("輸入的單字須由5個英文字母組成")
        continue
    elif len(word) ==5 and word not in text_html.text().split():
        print("請確認輸入的是否為英文單字")
        continue
    else:
        print("請確認輸入的是否為英文單字且須由5個英文字母組成")
        continue

        
print("---RESULT---")
print(f"答題次數：{play_time}次")
for time in ans_word:
    print(time)