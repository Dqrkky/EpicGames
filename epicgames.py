from selenium import webdriver
import json, urllib

keywords = input("What do you want to search on EpicGames : ")

params = urllib.parse.urlencode(
    query={
        "operationName": "searchStoreQuery",
        "variables": json.dumps(
            obj={
                "allowCountries": "GR",
                "category": "games/edition/base|bundles/games|games/edition|editors|addons|games/demo|software/edition/base",
                "count": 40,
                "country": "GR",
                "keywords": keywords,
                "locale": "en-US",
                "sortBy": "relevancy,viewableDate",
                "sortDir": "DESC,DESC",
                "tag": "",
                "withPrice": True
            }
        ),
        "extensions": json.dumps(
            obj={
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "7d58e12d9dd8cb14c84a3ff18d360bf9f0caa96bf218f2c5fda68ba88d68a437"
                }
            }
        )
    }
)
url = f"https://store.epicgames.com/graphql?{params}"

driver = webdriver.Chrome(executable_path="<path-to-chrome-driver.exe>")
driver.get(url)

a = None
for ii in driver.page_source.replace("\n", "").split(">"):
    if ii.startswith("{"):
        a = ii
if a != None:
    for ii in a.split("<"):
        if ii.endswith("}"):
            a = ii

if a != None:
    epic = json.loads(
        s=a
    )
    elements = epic["data"]["Catalog"]["searchStore"]["elements"]
    #for element in elements:
    #    print(element)
    #    print("\n\n")
    print(elements[0])
    #https://store.epicgames.com/en-US/p/{productSlug}
