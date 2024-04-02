import scrapy


class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/" + "catalogue/page-1.html"]

    def parse(self, response):
        # Извлечение названия книг и цены с помощью селекторов XPath
        for book in response.xpath('//article[@class="product_pod"]'):
            yield {
                'title': book.xpath('h3/a/@title').get(),
                'price': book.xpath('div[@class="product_price"]/p[@class="price_color"]/text()').get()
            }

        # Пагинация на следующую страницу
        next_page = response.xpath('//a[text()="next"]/@href').get()
        print(next_page)
        url = "http://books.toscrape.com/" + "catalogue/" + next_page
        if next_page is not None:
            yield response.follow(url, self.parse)

#### при запуске паука в терминале вводится команда сохранения в JSON файл:
#### scrapy crawl book_spider -o books_data_gb_lesson_5.json