import json
import product
import os.path

save_path = "../data"
file_name = "products.json"

complete_name = os.path.join(save_path, file_name)

def insert(product):
    all_products = []

    with open(complete_name, "w") as file:
        all_products = json.load(file)      # read file and store current contents in temp variable
    
        new_product = {"name": product.getName(), "start_price": product.getStartPrice(), "current_price": product.getCurrentPrice(),
                    "previous_price": product.getPreviousPrice(), "availability": product.getAvailability(),
                    "creation_date": product.getCreationDate(), "last_update": product.getLastUpdate(),
                    "is_lower_price": product.getIsLowerPrice()}        # create a dictionary for new product
        
        file.seek(0)    # go to beginning of file
    
        all_products["products"].append(new_product)    # add new product to product list

        json.dump(all_products, file, indent = 4)   # write to file using altered product list