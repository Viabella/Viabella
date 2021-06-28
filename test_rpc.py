import xmlrpc.client


url = 'url'
db = 'db'
username = 'username'
password = 'password'

# Logging in
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

# Calling Methos

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
orders = models.execute_kw(db, uid, password, 'sale.order', 'get_orders', [], {'state': 'on_hold'})
print (orders)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
orders = models.execute_kw(db, uid, password, 'sale.order', 'get_order_detail', [1], {'fields': ['name']})
print (orders)