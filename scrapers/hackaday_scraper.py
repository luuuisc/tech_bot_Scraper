import requests
from bs4 import BeautifulSoup
import datetime

def scrape_hackaday():
    url = "https://hackaday.com/"
    print(f"Conectando a {url}...")
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Error al acceder a la página: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Buscar artículos recientes en la sección "recent_entries-list"
    article_list = soup.select('ul.recent_entries-list > li')
    print(f"📄 Se encontraron {len(article_list)} artículos.")

    articles = []

    for i, li in enumerate(article_list):
        try:
            h2 = li.find('h2')
            title = h2.text.strip() if h2 else 'Sin título'
            link = h2.find('a')['href'] if h2 and h2.find('a') else 'Sin enlace'

            date_tag = li.find('span', class_='post-date')
            date = date_tag.text.strip() if date_tag else str(datetime.date.today())

            paragraph = li.find('p')
            summary = paragraph.text.strip() if paragraph else 'Sin resumen'

            articles.append({
                "site": "Hackaday",
                "title": title,
                "url": link,
                "date": date,
                "summary": summary
            })

        except Exception as e:
            print(f"⚠️ Error al procesar artículo {i+1}: {e}")
    
    return articles

# Prueba directa
if __name__ == "__main__":
    articles = scrape_hackaday()
    for a in articles:
        print(f"\n📰 {a['title']} ({a['date']})")
        print(f"🔗 {a['url']}")
        print(f"📝 {a['summary']}")