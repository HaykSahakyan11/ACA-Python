from bs4 import BeautifulSoup
import requests
import re
from collections import Counter


# Spider class helps to find inner links in a link by customized parameters such as depth and limits.
# Main execution - "run" method, which calls other methods consequently
# Also has method "get_links_Counter" which shows how many times inner link appears.

class Spider:
    # Initialize main data accumulator, which will be updated when main method "run" runs
    def __init__(self, url):
        self.base_url = "https://en.wikipedia.org"
        self.main_url = url
        self.links_Counter = Counter()
        self.depth = None  # will be updated when "run" method runs and gets attribute

    # Depends on depth value (0 or other) method returns url's or tag's soup consequently using bs4
    def soup_from_url_or_tag(self, tag_link=None, depth=0):
        # if depth = 0 means that we are creating main dict for url
        if depth == 0:
            url = self.main_url

        # else : means that we are creating sub dict for tag
        else:
            new_url = tag_link.attrs["href"]
            url = f"{self.base_url}{new_url}"
        source = requests.get(url=url).text
        soup = BeautifulSoup(source, 'lxml')
        return soup

    # Creates main dictionary. Value of key "links" which is a list, can be updated by dictionaries of inner links.
    def main_dict_constructor(self):
        url = self.main_url
        soup = self.soup_from_url_or_tag(url)
        title = soup.title.text
        self.links_Counter.update([title])
        main_dict = {
            "title": f"{title}",
            "links": []
        }
        return main_dict

    # Finds inner links for sub links  of main link and
    # creates sub dictionaries for main dictionary calling this method recursively.
    # Method checks links that has been appeared and skips them, but keeps count of appearance.
    def sub_dict_constructor(self, tag_link, depth=0):
        new_url = tag_link.attrs["href"]
        soup = self.soup_from_url_or_tag(tag_link, depth)
        title = soup.title.text
        url_dict = {
            new_url: {
                "title": f"{title}",
                "links": []
            }
        }
        if depth <= 3:
            if new_url not in self.links_Counter:
                depth += 1
                self.links_Counter.update([new_url])
                for tag_link in soup.find_all("a", {"href": True,
                                                    "title": True,
                                                    "class": False}, href=re.compile("^[\/]wiki"), limit=self.depth):
                    url_dict[new_url]["links"].append(self.sub_dict_constructor(tag_link, depth))
            else:
                self.links_Counter.update([new_url])
        return url_dict

    def run(self, depth):
        self.depth = depth
        soup = self.soup_from_url_or_tag()
        current_depth = 0
        main_dict = self.main_dict_constructor()
        current_depth += 1
        for tag_link in soup.find_all("a", {"href": True, "title": True, "class": False}, href=re.compile("^[\/]wiki"),
                                      limit=depth + 1):  # Data is too big, so use limits
            tag_reference = tag_link.attrs["href"]
            if tag_reference not in self.links_Counter:
                main_dict["links"].append(self.sub_dict_constructor(tag_link, current_depth))
        return main_dict

    def get_links_Counter(self):
        return self.links_Counter


def Spider_test():
    full_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    spider = Spider(full_url)
    depth = 3
    finale_dict = spider.run(depth)
    for value in finale_dict.values():
        print(len(value))
        for i in value:
            print(i)

    print(spider.get_links_Counter())


if __name__ == "__main__":
    Spider_test()
