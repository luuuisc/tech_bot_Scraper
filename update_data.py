import json
from pathlib import Path

from scrapers.hackaday_scraper import scrape_hackaday
from scrapers.ieee_scraper import scrape_ieee_rss
from scrapers.techcrunch_scraper import scrape_techcrunch

def save_to_json(data, path):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Archivo JSON actualizado en: {path}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo JSON: {e}")

if __name__ == "__main__":
    print("Ejecutando scrapers de Hackaday, IEEE Spectrum y TechCrunch...\n")

    hackaday_data = scrape_hackaday()
    ieee_data = scrape_ieee_rss()
    techcrunch_data = scrape_techcrunch()

    # Combinar todos los artículos en una sola lista
    all_articles = hackaday_data + ieee_data + techcrunch_data

    # Definir ruta de salida
    output_path = Path("web/data.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Guardar archivo combinado
    save_to_json(all_articles, output_path)