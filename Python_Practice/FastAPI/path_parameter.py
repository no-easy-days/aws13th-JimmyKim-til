from fastapi import FastAPI
from enum import Enum

# 문제 4 : Enum 활용을 위한 클래스 생성
class Category(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    food = "food"
# 도전 3 : Enum과 타입 결합을 위한 클래스 생성
class Status(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
app = FastAPI()
# 문제 1: 기본 Path Parameter
@app.get("/products/{product_id}")
async def read_product_id(product_id):
    return {"product_id" : product_id}

# 문제 2: 타입이 있는 Path Parameter
@app.get("/orders/{order_id}")
async def read_order_id(order_id : int):
    return {"order_id" : order_id, "double_order_id" : order_id*2}

# 문제 3: Path Operation 순서
@app.get("/users/me")
async def read_users_me():
    return {"user_id": "current_user", "name": "jeff"}
@app.get("/users/admin")
async def read_users_admin():
    return {"user_id": "admin", "role": "administrator"}
@app.get("/users/{user_id}")
async def read_userid(user_id : int):
    return {"user_id" : user_id}

# 문제 4: Enum을 사용한 값 제한
@app.get("/categories/{category_name}")
async def get_category(category_name: Category):
    if category_name is Category.electronics:
        return {"Category" : category_name, "message" : "Enum! 전자제품 카테고리입니다... "}
    if category_name.value == "clothing":
        return {"Category" : category_name, "message" : "Enum인데 2번째! 의류 카테고리입니다... "}
    return {"Category" : category_name, "message" : "Enum에서 걸러지긴했음. 식품입니다. "}

# 문제 5: 경로를 포함하는 Path Parameter
@app.get("/files/{file_path:path}")
async def get_file_path(file_path : str):
    return {
        "full_path":file_path,
        "directory":file_path.rsplit("/", 1)[0],#오른쪽부터 자르기.
        "filename":file_path.split("/")[2]
    }

# 추가 도전 1 : 여러 Path Parameter 사용하기
@app.get("/stores/{store_id}/products/{product_id}")
async def get_product_id(store_id : int, product_id : int):
    return {"store_id": store_id, "product_id": product_id}

# 추가 도전 2 : 조건부 응답
@app.get("/numbers/{number}")
async def get_number(number : int):
    if number == int(0):
        return {"number" : "zero"}
    elif number % 2 == 0:
        return {"number" : "even"}
    else:
        return {"number" : "odd"}

# 추가 도전 3 : Enum과 타입 결합
@app.get("/requests/{request_id}/status/{status_name}")
async def get_status(request_id : int, status_name : Status):
    if status_name is Status.pending:
        return {
            "request_id" : request_id,
            "status" : status_name
        }
    if status_name is Status.approved:
        return {
            "request_id" : request_id,
            "status" : status_name
        }
    return {
        "request_id" : request_id,
        "status" : status_name
    }
