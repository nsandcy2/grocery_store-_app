from sql_connection import get_sql_connection
def get_all_products(connection):

    cursor = connection.cursor()
    res=[]
    query = ("SELECT products.product_id,products.name,products.uom_id,products.price_per_unit,uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    for (i,j,k,l,m ) in cursor:
        res.append({
                'product_id':i,
                'name':j,
                'uom_id':k,
                'price_per_unit':l,
                'uom_name':m
            }
        )

    return res

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid
# def query(connection):
#     cursor = connection.cursor()
#     query=("SELECT * FROM order_details WHERE order_id = 17")
#     red=cursor.execute(query)
#     for r in res:
#         print(r,end=" ")
#         print()
    







if __name__=='__main__':
    connection = get_sql_connection()
    # print(delete_product(connection,10))
    ans=get_all_products(connection)
    
    
    # print(insert_new_product(connection, {
    #     'product_name': 'califlower',
    #     'uom_id': '1',
    #     'price_per_unit': 60
    # }))
