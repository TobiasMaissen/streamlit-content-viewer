import json
import re
import csv

def load_blog_posts(json_file):
    """
    Liest die Blogbeiträge aus einer JSON-Datei.
    Erwartetes Format: Ein Dictionary mit dem Key "blog_posts", der eine Liste von Beiträgen enthält.
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data["blog_posts"]

def save_content(posts, output_file):
    """
    Speichert die Blog- und LinkedIn-Inhalte in einer JSON-Datei.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"blog_posts": posts}, f, indent=2, ensure_ascii=False)

def clean_blog_content(content: str) -> str:
    """
    Bereinigt den Blog-Text, indem unnötige Markdown-Elemente und Meta-Informationen entfernt werden.
    Schritte:
      1. Entferne Bild-Markdown (z.B. ![...](...))
      2. Ersetze Markdown-Links [Text](URL) durch nur den Linktext.
      3. Entferne Zeilen, die Navigationslinks oder typische Meta-Informationen enthalten.
      4. Entferne überflüssige Leerzeilen und trimme den Text.
    """
    # 1. Entferne Bild-Markdown
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    # 2. Ersetze Markdown-Links durch den Linktext
    content = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', content)
    # 3. Entferne unerwünschte Zeilen
    lines = content.splitlines()
    cleaned_lines = []
    skip_keywords = [
        "Vorherige", "Back Navigation", "Nächste",
        "min read", "AM", "PM", "Play", "AI-generated audio",
        "- Post Button", "- Teilen", "- Facebook", "Teilen0"
    ]
    for line in lines:
        if any(kw in line for kw in skip_keywords):
            continue
        if line.strip() == "":
            continue
        cleaned_lines.append(line.strip())
    # 4. Füge die bereinigten Zeilen wieder zusammen
    cleaned_content = "\n".join(cleaned_lines)
    return cleaned_content


if __name__ == "__main__":

    # Dateinamen definieren
    csv_datei = 'seo_dinotronic.csv'      # Hier steht der Name bzw. Pfad der Eingabe-CSV-Datei
    json_datei = 'seo_output.json'   # Hier wird die Ausgabe-JSON-Datei gespeichert

    # Zwischenspeicher: Gruppierung der Keywords anhand des main_keyword
    gruppen = {}

    # CSV-Datei einlesen (Delimiter ist ";" wegen deiner CSV-Struktur)
    with open(csv_datei, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        
        for row in reader:
            # Werte trimmen und in Kleinbuchstaben umwandeln
            main_keyword = row["main_keyword"].strip().lower() if row["main_keyword"] else ""
            secondary_keyword = row["secondary_keyword"].strip().lower() if row["secondary_keyword"] else ""
            language = row["language"].strip().lower() if row["language"] else ""
            
            # Falls main_keyword noch nicht existiert, neuen Eintrag anlegen
            if main_keyword not in gruppen:
                gruppen[main_keyword] = {
                    "main_keyword": main_keyword,
                    "language": language,
                    "secondary_keywords": []
                }
            
            # secondary_keyword hinzufügen, wenn vorhanden und nicht bereits in der Liste
            if secondary_keyword and secondary_keyword not in gruppen[main_keyword]["secondary_keywords"]:
                gruppen[main_keyword]["secondary_keywords"].append(secondary_keyword)

    # Umwandeln des Gruppierungs-Dictionaries in eine Liste von Objekten
    kontext_liste = list(gruppen.values())

    # Schreiben des Ergebnisses in die JSON-Datei
    with open(json_datei, 'w', encoding='utf-8') as jsonfile:
        json.dump(kontext_liste, jsonfile, indent=4)
