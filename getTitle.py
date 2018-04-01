from time import sleep
import bottlenose
from bs4 import BeautifulSoup


def get_result(access_key, secret_key, associate_tag, cnt):
    amazon = bottlenose.Amazon(access_key, secret_key, associate_tag, Region="JP")
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
    f = open('result.xml', 'a')
    f.write(soup.find('item').prettify())
    f.close()


def main():
    access_key = "xxx"
    secret_key = "xxx"
    associate_tag = "xxx"

    for i in range(1, 201):
        get_result(access_key, secret_key, associate_tag, i)
        sleep(60)


if __name__ == '__main__':
    main()
