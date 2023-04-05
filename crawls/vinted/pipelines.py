# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from web.scraper.scraper.vinted.models import Item

class VintedPipeline:
    def process_item(self, item, spider):
        # shop_id = item['shop_id']
        # shop = Shop.objects.get(id=shop_id)
        #
        # # Create a new Item instance
        # item_data = {
        #     'name': item['name'],
        #     'price': item['price'],
        #     'description': item['description'],
        #     'shop': shop
        # }
        # item_instance = Item(**item_data)
        # item_instance.save()

        # Return the processed item
        return item