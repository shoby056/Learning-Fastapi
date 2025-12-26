Path Parameters & Query Parameters

In FastAPI, there are two main ways to pass data in routes:

Path Parameters → Part of the URL

Query Parameters → Passed in the URL using ?key=value format

1️⃣ Concept: Path Parameters

A path parameter is data that is directly included in the URL path.

Example:
/user/1

Here, 1 is the user ID.

In FastAPI, this is handled like this:

@app.get("/user/{user_id}")


{user_id} is the path parameter

It is usually required

2️⃣ Concept: Query Parameters

A query parameter is data passed at the end of the URL using ?.

Example:
/search?name=shoaib&age=20


name and age are query parameters

Query parameters can be optional or required

3️⃣ Real-World Example
E-commerce Application Example:

Path Parameter

/product/123


→ Shows details of a specific product

Query Parameter

/products?category=shoes&price=1000


→ Filters products by category and price