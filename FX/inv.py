from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

pairs = [["usd-jpy", 3], ["aud-usd", 5], ["eur-usd", 1], ["gbp-usd", 2], ["xau-usd", 68],]  # noqa E501

for pair in pairs:
    site = f"https://www.investing.com/currencies/{pair[0]}"
    req = Request(site)
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")  # noqa E501
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36")  # noqa E501
    req.add_header("X-Requested-With", "XMLHttpRequest")

    html = urlopen(req)
    soup = BeautifulSoup(html.read(), "html.parser")
    high = soup.find("span", {"class": f"pid-{pair[1]}-high"}).get_text()
    low = soup.find("span", {"class": f"pid-{pair[1]}-low"}).get_text()
    print(f"---\n{pair[0].upper()} H - {high} | L - {low}")
