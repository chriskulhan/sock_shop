# test for app.py

#Import the functions methods that I want to test:
from app import get_available_products, get_product_by_id, get_all_categories

# Test the get available products function
def test_get_available_products():
    #Dr. Mary's notes from the assignment:

    """

    This test verifies our product retrieval functionality:

    - Checks that we have the correct number of products (3)

    - Ensures each product contains all required data fields

    - Tests that category filtering works correctly (2 'funny' products)

    

    If this test fails, it could mean:

    - Products are missing from the database

    - Products are missing required fields

    - The category filtering logic is broken

    """
    #my notes from class:
    #verify that we can retrieve products
    #call the get_available_products function
    products = get_available_products()

    #Test using an assertion if three products are returned
    assert len(products) == 3
    # Test that the products have all of the required fields (price, description, category, etc.)
    assert all('id' in p and 'name' in p and 'description' in p and 
               'base_price' in p and 'image' in p and 'category' in p
               for p in products)
    #test that the number of products in the "funny" category is 2
    #more or less than 2, the test will fail
    assert len(get_available_products('funny')) == 2

""#test the get product by ID function
def test_get_products_by_id():
    #Dr. Mary's notes from the assignment:

    """

    This test checks our product lookup functionality:

    - Verifies we can retrieve a product using its ID

    - Confirms the product data is correct

    - Tests that invalid IDs return None instead of causing errors

    

    If this test fails, it could mean:

    - The product with ID 1 is missing or has incorrect data

    - The function isn't handling invalid IDs properly

    """

    #my notes from class:
    #Get a product from teh collection of products with product id 1
    product = get_product_by_id(1)

    #test that the product exists and that the id is 1 and the name is "Meme Lord"
    assert product and product['id'] == 1 and product['name'] == 'Meme Lord'

    #test if we have an invalid product id is handled gracefully, instead of throwing an error
    assert get_product_by_id(999) is None

#test the get all categories function
def test_get_all_categories():
    #Dr. Mary's notes from the assignment:

    """

    This test examines our category management:

    - Checks that we have the expected number of categories (2)

    - Verifies that all expected categories exist ('funny' and 'school')

    

    If this test fails, it could mean:

    - Categories are missing from the database

    - The category retrieval logic is broken

    """
    
    #my notes from class:
    #check that we have the correct number of categories of socks
    #check that 'funny' and 'school' are in the list of categories
    categories = get_all_categories()

    #test that there are 2 categories in the list
    assert len(categories) == 2

    #test that the two categories are "funny" and "school"
    assert 'funny' in categories and 'school' in categories