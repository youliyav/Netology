import json
import xml.etree.ElementTree as ET


def work_list(titles):
    titles_dict = dict()
    for title in set(titles):
        if len(title) > 6:
            titles_dict[title] = titles.count(title)

    titles_dict_new = dict()
    for title in titles_dict:
        if titles_dict[title] not in titles_dict_new.keys():
            titles_dict_new[titles_dict[title]] = list()
        titles_dict_new[titles_dict[title]].append({title})

    titles_list_sort = sorted(titles_dict_new.keys(), reverse=True)

    top_words = []
    for x in titles_list_sort:
        for i in titles_dict_new[x]:
            top_words.append(i)
    return top_words[:10]


print("10 самых часто встречающихся слов в xml:")
with open("newsafr.xml", encoding='utf8') as f:
    xml = f.read()
    tree = ET.XML(xml)
    titles = []
    xml_items = tree.findall("channel/item")
    for item in xml_items:
       title = item.find("description")
       titles += title.text.split(" ")
    result = work_list(titles)
    print(result)

print("10 самых часто встречающихся слов в json:")
with open("newsafr.json", encoding="utf8") as datafile:
    json_data = json.load(datafile)
    titles = []
    json_items = json_data["rss"]["channel"]["items"]
    for item in json_items:
        title = item["description"]
        titles += title.split(" ")
    result = work_list(titles)
    print(result)
