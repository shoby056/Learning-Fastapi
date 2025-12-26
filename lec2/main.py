from fastapi import FastAPI
app=FastAPI()

# path parameter
@app.get("/product/{product_id}")
def get_product(product_id : int):
    return {"Product": {product_id} , "message":f"laptop is good {product_id}"}

# Query Parameters
@app.get("/filter")
def filter_item(price:int =None  , category:str="all"):
    return{"price":price, "category":category}
