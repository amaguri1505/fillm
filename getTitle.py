from time import sleep
import bottlenose
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def error_handler(err):
    ex = err['exception']
    if isinstance(ex, HTTPError) and ex.code == 503:
        sleep(1)
        return True


def get_totalpages(amazon):
    response = amazon.ItemLookup(
        Service="AWSECommerceService",
        Operation="ItemSearch",
        Sort="date-desc-rank",
        BrowseNode="3535604051",
        SearchIndex="VideoDownload",
        ResponseGroup="BrowseNodes,Images,ItemAttributes,ItemIds,Offers",
        Keywords="映画",
    )

    soup = BeautifulSoup(response, "lxml")
    return soup.find('totalpages').string


def get_result(amazon, cnt):
    response = amazon.ItemLookup(
        Service="AWSECommerceService",
        Operation="ItemSearch",
        Sort="date-desc-rank",
        BrowseNode="3535604051",
        SearchIndex="VideoDownload",
        ResponseGroup="BrowseNodes,Images,ItemAttributes,ItemIds,Offers",
        Keywords="映画",
        ItemPage=str(cnt)
    )
    soup = BeautifulSoup(response, "lxml")

    output_file = "result" + str(cnt) + ".html"

    f = open(output_file, 'a', encoding='utf-8')
    f.write(soup.prettify())
    f.close()


def main():
    # access_key = "xxx"
    # secret_key = "xxx"
    # associate_tag = "xxx"


    amazon = bottlenose.Amazon(access_key, secret_key, associate_tag, Region="JP",  ErrorHandler=error_handler)

    totalpage = get_totalpages(amazon)

    for i in range(1, int(totalpage)):
        get_result(amazon, i)
        sleep(1)


if __name__ == '__main__':
    main()
    #test()
