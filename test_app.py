# test for app.py

#Import the functions methods that I want to test:
from app import get_available_products, get_product_by_id, get_all_categories

# Test the get available products function
def test_get_available_products():
    #verify that we can retrieve products
    #call the get_available_products function
    products = get_available_products()

    #Test using an assertion if three products are returned
    assert len(products) == 3
    # Test that the products have all of the required fields (price, description, category, etc.)
    assert all('id' in p and 'name' in p and 'description' in p and 
               'base_price' in p and 'image' in p and 'category' in products
               for p in products)
    #test that the number of products in the "funny" category is 2
    #more or less than 2, the test will fail
    assert len(get_available_products('funny')) == 2

""#test the get product by ID function
def test_get_products_by_id():
    #Get a product from teh collection of products with product id 1
    product = get_product_by_id(1)

    #test that the product exists and that the id is 1 and the name is "Meme Lord"
    assert product and product['id'] == 1 and product['name'] == 'Meme Lord'

    #test if we have an invalid product id is handled gracefully, instead of throwing an error
    assert get_product_by_id(999) is None

#test the get all categories function
def test_get_all_categories():
    #check that we have the correct number of categories of socks
    #check that 'funny' and 'school' are in the list of categories
    categories = get_all_categories()

    #test that there are 2 categories in the list
    assert len(categories) == 2

    #test that the two categories are "funny" and "school"
    assert 'funny' in categories and 'school' in categories