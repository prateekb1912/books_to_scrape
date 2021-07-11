import scrapy

def conv2Num(stars):
    if stars == 'One':
        stars = 1
    elif stars == 'Two':
        stars = 2
    elif stars == 'Three':
        stars = 3
    elif stars == 'Four':
        stars = 4
    elif stars == 'Five':
        stars = 5 
    else: 
        stars = 0 

    return stars  

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
            stars = b.css('p.star-rating').attrib['class'].split(' ')[1]

            numStars = int(conv2Num(stars))

            yield {
                'Title': title,
                'Price': price,
                'Stars': numStars
            }