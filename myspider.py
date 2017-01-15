import scrapy

class HaikuSpider(scrapy.Spider):
		name = 'haikuspider'
		start_urls = ['https://haiku.mannlib.cornell.edu']

		def parse(self, response):
			haikus = []
			for entry in response.css('div.entry'):
				haiku = {'haiku': entry.css('p').extract_first()}
				haikus.append(haiku)

				next_page = response.css('div.alignleft > a ::attr(href)').extract_first()
				if next_page:
					yield scrapy.Request(response.urljoin(next_page), callback=self.parse)