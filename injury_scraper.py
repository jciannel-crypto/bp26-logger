import requests
from bs4 import BeautifulSoup
import pdfplumber
import io
import re

url = "https://official.nba.com/nba-injury-report-2025-26-season/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

print("Fetching latest injury report...")
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

pdf_links = [a["href"] for a in soup.find_all("a", href=True)
             if "Injury-Report" in a["href"] and ".pdf" in a["href"]]

latest_pdf_url = pdf_links[-1]
print(f"Report: {latest_pdf_url}\n")

pdf_response = requests.get(latest_pdf_url, headers=headers)

statuses = ["Out", "Available", "Questionable", "Doubtful", "Probable"]

# Known team names for clean extraction
nba_teams = [
    "AtlantaHawks","BostonCeltics","BrooklynNets","CharlotteHornets",
    "ChicagoBulls","ClevelandCavaliers","DallasMavericks","DenverNuggets",
    "DetroitPistons","GoldenStateWarriors","HoustonRockets","IndianaPacers",
    "LAClippers","LosAngelesLakers","MemphisGrizzlies","MiamiHeat",
    "MilwaukeeBucks","MinnesotaTimberwolves","NewOrleansPelicans","NewYorkKnicks",
    "OklahomaCityThunder","OrlandoMagic","Philadelphia76ers","PhoenixSuns",
    "PortlandTrailBlazers","SacramentoKings","SanAntonioSpurs","TorontoRaptors",
    "UtahJazz","WashingtonWizards"
]

def add_spaces(name):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', name)

current_date = ""
current_game = ""
current_team = ""

with pdfplumber.open(io.BytesIO(pdf_response.content)) as pdf:
    for page in pdf.pages:
        words = page.extract_words()
        rows = {}
        for word in words:
            y = round(word["top"] / 5) * 5
            if y not in rows:
                rows[y] = []
            rows[y].append(word)

        for y in sorted(rows.keys()):
            row_words = sorted(rows[y], key=lambda w: w["x0"])
            line = " ".join(w["text"] for w in row_words)

            # Date header
            date_match = re.search(r'(\d{2}/\d{2}/\d{4})', line)
            if date_match and "Injury Report" not in line and "GameDate" not in line:
                date = date_match.group(1)
                if date != current_date:
                    current_date = date
                    print(f"\n{'='*65}")
                    print(f"  {current_date}")
                    print(f"{'='*65}")

            # Game header
            game_match = re.search(r'(\d{2}:\d{2}\(ET\))\s+([A-Z]{2,3}@[A-Z]{2,3})', line)
            if game_match:
                game_str = f"{game_match.group(1)}  {game_match.group(2)}"
                if game_str != current_game:
                    current_game = game_str
                    current_team = ""
                    print(f"\n  {current_game}")

            # Team detection — only match known teams
            for team in nba_teams:
                if team in line:
                    if team != current_team:
                        current_team = team
                        print(f"\n    [{add_spaces(team)}]")
                    break

            # Player/status detection
            status_found = None
            for s in statuses:
                if s in line:
                    status_found = s
                    break

            if not status_found:
                continue

            parts = line.split(status_found)
            pre = parts[0].strip().split()
            reason = parts[1].strip() if len(parts) > 1 else ""

            player = ""
            for w in pre:
                if "," in w:
                    player = w
                    break

            if player:
                print(f"      {player:<28} {status_found:<14} {reason}")
