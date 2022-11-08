import requests
import bs4
from fake_useragent import UserAgent

# KEYWORDS = ['посадки', 'Минфина', 'web', 'поэтому']

# base_url = 'https://habr.com'
# url = base_url + '/ru/all/'
# ua = UserAgent()
# headers = {'User-Agent': ua.chrome}
# response = requests.get(url, headers=headers)
# text = response.text
# soup = bs4.BeautifulSoup(text, features='html.parser')
# articles = soup.find_all('article')
# for arlicle in articles:
#     tag_p = arlicle.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
#     tag_p = [text_p.text for text_p in tag_p]
#     # print(tag_p)
# Habr не отвечает, взял сайт https://russian.rt.com/tag/novosti-rossii. Структура похожая

if __name__ == "__main__":
    KEYWORDS = ['посадки', 'Минфина', 'семей', 'Заместитель']

    base_url = 'https://russian.rt.com'
    url = base_url + '/tag/novosti-rossii'
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}

    response = requests.get(url, headers=headers)
    text = response.text

    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all(class_="listing__column listing__column_all-new listing__column_js")
    for article in articles:
        list_article = [a.text.split() for a in article]
        for list_words in list_article:
            for word in list_words:
                if word in KEYWORDS:
                    href = article.find(class_="link link_color").attrs["href"]
                    link  = base_url+href
                    title = article.find(class_="card__heading card__heading_all-new").text.strip()
                    date_article = article.find(class_="date").text.strip()
                    print(f"Дата: {date_article} - Заголовок: {title} - Ссылка {link}")
                    
        
