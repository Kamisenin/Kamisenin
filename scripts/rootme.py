import requests
from bs4 import BeautifulSoup

USERNAME = "Kami"

url = f"https://www.root-me.org/{USERNAME}?lang=en"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

challenges = []

for item in soup.select(".challenge-card-title"):
    challenges.append(item.text.strip())

# Limite pour README propre
challenges = challenges[:10]

output = "## 🧠 RootMe\n\n"

for c in challenges:
    output += f"- {c}\n"

# Remplacement dans README
with open("README.md", "r") as f:
    readme = f.read()

start = "<!--ROOTME_START-->"
end = "<!--ROOTME_END-->"

new_readme = readme.split(start)[0] + start + "\n" + output + "\n" + end + readme.split(end)[1]

with open("README.md", "w") as f:
    f.write(new_readme)
