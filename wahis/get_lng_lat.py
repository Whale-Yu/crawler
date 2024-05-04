from lxml import etree


def get_lng_lat(country):
    # country = 'Belgium'
    country = country
    parser = etree.HTMLParser(encoding="utf-8")
    html = etree.parse('tableConvert.com_akw5r4.html', parser=parser)
    tr_list = html.xpath('/html/body/table/tbody/tr')
    try:
        for i in tr_list:
            id = i.xpath('./td[1]/text()')[0]
            county_eng = i.xpath('./td[2]/text()')[0]
            county_ch = i.xpath('./td[3]/text()')[0]
            lng = i.xpath('./td[4]/text()')[0]
            lat = i.xpath('./td[5]/text()')[0]

            if country == county_eng:
                print(id, county_eng, county_ch, lng, lat)
                return lng, lat, county_ch
    except:
        print('\033[31mnull\033[0m')
        return '', '', ''


if __name__ == '__main__':
    lng, lat, county_ch = get_lng_lat('china')
