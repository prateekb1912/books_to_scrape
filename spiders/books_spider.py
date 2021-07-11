import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books_spider'

    def start_requests(self):
        url = "http://books.toscrape.com/index.html"

        yield scrapy.Request(url, callback=self.parse)
    
    def parse(self, response):

        books = response.css('article.product_pod')

        for b in books:
            title = b.css("h3 a::attr('title')").get()
            price = float(b.css('p.price_color::text').get()[1:])

            yield {
                'Title': title,
                'Price': price
            }