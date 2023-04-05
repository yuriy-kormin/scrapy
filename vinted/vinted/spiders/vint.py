import json
from urllib.parse import urlparse, urlunparse, urlencode, parse_qsl

import scrapy


class VintedSpider(scrapy.Spider):
    name = "vinted_spider"
    start_urls = ["https://www.vinted.com"]
    api_url = 'https://www.vinted.com/api/v2/catalog/items?'

    custom_settings = {
        'DOWNLOAD_DELAY': 2  # 2 seconds of delay
    }

    def parse(self, response):
        # api_url = 'https://www.vinted.com/api/v2/promoted_closets?closet_count=&item_count=1000&exclude_member_ids=&search_session_id=&screen_name=catalog&catalog_ids=&color_ids=&brand_ids=53&size_ids=&material_ids=&video_game_rating_ids=&status_ids='
        # api_url = 'https://www.vinted.com/api/v2/promoted_closets?closet_count=&item_count=1000&exclude_member_ids=&brand_ids=53'
        brands = {
            "Cyrillus": 53,
            # "Eden Park": 489,
            # "Lancaster": 11731,
            # "La Fee Maraboutee": 5493,
            # "Envie de Fraise": 4694147,
            # "Alpinestars": 34867,
            # "3 suisses": 212,
        }
        for brand in brands.values():
            api_url = f'{self.api_url}brand_ids={brand}&per_page=96&page=1'
            yield scrapy.Request(url=api_url,
                                 callback=self.parse_brand_page)

    def get_next_page_url(self, url, page_count):
        url_parsed = urlparse(url)
        qs_parsed = dict(
            parse_qsl(
                url_parsed.query, keep_blank_values=True
            )
        )
        page_num = qs_parsed.get('page')
        if page_num and int(page_num) < page_count:
            qs_parsed['page'] = str(int(qs_parsed['page']) + 1)
            return urlunparse(
                url_parsed._replace(query=urlencode(qs_parsed))
            )
        return False

    def parse_brand_page(self, response):
        brand_data = json.loads(response.body)
        page_count = brand_data['pagination']['total_pages']
        yield brand_data['pagination']
        for item in brand_data['items']:
            yield {
                i: item[i] for i in (
                    'brand_title',
                    'id',
                    'price',
                    'service_fee',
                    'total_item_price',
                    'currency',
                )
            }
        if next_url := self.get_next_page_url(response.url, page_count):
            yield response.follow(next_url, callback=self.parse_brand_page)
