import feedparser
from bs4 import BeautifulSoup
import datetime

def scrape_techcrunch():
    rss_url = "https://techcrunch.com/feed/"
    print(f"Conectando a RSS: {rss_url}...")

    feed = feedparser.parse(rss_url)

    if not feed.entries:
        print("❌ No se encontraron artículos.")
        return []

    data = []

    for entry in feed.entries[:10]:  # Limitar a 10 entradas
        title = entry.title
        link = entry.link
        summary_html = entry.summary
        summary_text = BeautifulSoup(summary_html, 'html.parser').get_text().strip()
        date = entry.published if 'published' in entry else str(datetime.date.today())

        data.append({
            "site": "TechCrunch",
            "title": title,
            "url": link,
            "date": date,
            "summary": summary_text
        })

    print(f"✅ {len(data)} artículos extraídos desde TechCrunch.")
    return data

# Prueba directa
if __name__ == "__main__":
    articles = scrape_techcrunch()
    for a in articles:
        print(f"\n📰 {a['title']} ({a['date']})")
        print(f"🔗 {a['url']}")
        print(f"📝 {a['summary'][:150]}...")