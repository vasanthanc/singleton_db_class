from connect_db import ConnectDB as database


class Products (object):


    def __init__(self):
        self.table = "products"
        self.db = database ()
        self.default_limit = 20

    def product_list(self):
        # with database () as db:
            self.db.cursor.execute ("SELECT * FROM {}".format (self.table))
            columns = self.db.cursor.description
            result = [{columns[index][0]: column for index, column in enumerate (value)} for value in
                      self.db.cursor.fetchall ()]
            return result

    def number_of_products(self):
        # with database () as db:
            self.db.cursor.execute ("SELECT * FROM {}".format (self.table))
            return len(self.db.cursor.fetchall ())

    def offset_products(self,offset,limit = None):

        if not limit:
            limit = self.default_limit

        posts = "select * from {} LIMIT {} OFFSET {}".format(self.table,limit,offset)
        print(posts)
        self.db.cursor.execute (posts)
        columns = self.db.cursor.description
        result = [{columns[index][0]: column for index, column in enumerate (value)} for value in
                  self.db.cursor.fetchall ()]
        return result

if __name__ == "__main__":
    product = Products ()
    products = product.product_list ()

    for record in products:
        print (record)

    print(product.number_of_products())

    product_list = product.offset_products(100)
    print(len(product_list))
    for record in product_list:
        print(record)