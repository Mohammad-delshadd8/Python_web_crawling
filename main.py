import requests as rqs
from bs4 import BeautifulSoup


site = rqs.get("https://liliome.ir/shop/")

sop = BeautifulSoup(site.text, "html.parser")

tag1_number = sop.find_all("a", {"class": "page-number"})
tag2_category = sop.find_all("p", {"class": "category uppercase is-smaller no-text-overflow product-cat op-7"})
tag3_Name = sop.find_all("a", {"class": "woocommerce-LoopProduct-link woocommerce-loop-product__link"})
tag4_price = sop.find_all("bdi")
tag5_sale = sop.find_all("span", {"class": "onsale"})
tag6_PageElements_counter = sop.find_all("div", {"class": "product-small box "})



# max_page_num = tag1_number[0].text
# print(tag3_Name[0].text)
# print(tag3_Name[0].text.split("|")[0])
# print(tag4_price[1].text.split("ت")[0])
# print(tag5_sale[1].text.split("-")[1].split("%")[0])
# print(tag5_sale.text[1].split("-")[1].split("%")[0])
# print(len(tag6_PageElements_counter))

i = 1
for i in range(int(tag1_number[5].text)):
    ste = f"https://liliome.ir/shop/{i}"
    for j in range(20):
        with open("result/perfumes.csv", 'a', encoding="utf-8") as result:
            result.write(tag2_category[j].text)
            result.write(",")
            result.write(tag3_Name[j].text.split("|")[0])
            result.write(",")
            result.write(tag3_Name[j].text.split("|")[1])
            result.write(",")
            result.write(str(tag4_price[1].text.split("ت")[0]).replace(",", "/"))
            result.write(",")
            result.write(tag5_sale[1].text.split("-")[1].split("%")[0])





