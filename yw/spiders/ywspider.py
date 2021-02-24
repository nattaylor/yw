import scrapy


class YwspiderSpider(scrapy.Spider):
    name = 'ywspider'
    start_urls = [
        'https://www.yachtworld.com/boats-for-sale/condition-used/type-sail/sort-price:asc/?page=1',
    ]

    def parse(self, response):
        # Stop when there are no more results
        if response.status != 200:
            return True
        for listing in response.css(".listings-container .listing-card"):
            yield {
                'name': listing.css('.listing-card-title::text').getall(),
                'price': listing.css('.price span::text').get(),
                'length': listing.css('.listing-card-length-year::text').getall(),
                'location': listing.css('.listing-card-location::text').getall(),
            }

        page, num = response.url.split("=")
        next_page = page +"="+ str(int(num)+1)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
