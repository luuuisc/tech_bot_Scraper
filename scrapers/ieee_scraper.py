import feedparser
from bs4 import BeautifulSoup
import datetime

def scrape_ieee_rss():
    rss_url = "https://spectrum.ieee.org/rss/fulltext"
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
            "site": "IEEE Spectrum",
            "title": title,
            "url": link,
            "date": date,
            "summary": summary_text
        })

    print(f"✅ {len(data)} artículos extraídos desde el RSS.\n")

    for i, a in enumerate(data, 1):
        print(f"🧠 {i}. {a['title']} ({a['date']})")
        print(f"🔗 {a['url']}")
        print(f"📝 {a['summary'][:150]}...\n")

    return data

# Prueba directa
if __name__ == "__main__":
    scrape_ieee_rss()