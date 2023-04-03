import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chockolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def start_requests(self):
        # GET request
        yield scrapy.Request("https://www.vinted.com/vetements?brand_id%5B%5D=53",
                             meta={"playwright": True})

    def parse(self, response):
        pass
        # yield {response: response.body}
        items = response.xpath('@class="feed-grid__item"')
        for item in items:
            yield {
                'price': item.xpath('.//h4[contains(@class,"web_ui__Text__text")]/text()').get()
            }
        # yield {
        #     headers:
        # }