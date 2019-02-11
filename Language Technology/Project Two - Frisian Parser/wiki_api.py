import wikipedia
import json


def random_page():
    wikipedia.set_lang("fy")
    random = wikipedia.random(1)
    try:
        result = wikipedia.page(random).summary
    except wikipedia.exceptions.DisambiguationError as e:
        result = random_page()
    
    return result

def main():
    data = {} 
    data['wiki'] = []
    for i in range(0, 500):
        article = random_page()
        if not article == "":
            if len(article) >= 75:
                # print(title)
                # print(len(article))
                print(article)
                data['wiki'].append({  
                    'content': article
                })
            
    with open('frysk_data.json', 'w',  encoding="utf-8") as outfile:
         json.dump(data['wiki'], outfile, ensure_ascii=False)

if __name__ == "__main__":
    main()