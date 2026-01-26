from fastapi import FastAPI, Path, Query
from typing import Annotated
app = FastAPI()

# 문제 1. 사용자 조회 API
@app.get("/users/{user_id}")  # /items/숫자 형태의 요청을 처리
async def get_user_id(
        user_id : Annotated[
            int, Path(ge=1, le=10000, title="사용자 ID")
        ] #ge : 이상, le : 이하
):
    return {"user_id" : user_id}

# 문제 2. 상품 가격 조회 API
@app.get("/products/{product_id}")
async def get_product_id(
        product_id : Annotated[int, Path(ge=1, le=999)],
        min_price : Annotated[float | None, Query(ge=0)] = None,
        max_price : Annotated[float | None, Query(ge=1)] = None
):
    result = {"product_id": product_id}
    if min_price is not None:
        result["min_price"] = min_price
    if max_price is not None:
        result["max_price"] = max_price
    return result

# 문제 3. 페이지네이션 API
@app.get("/posts/page/{page_num}")
async def get_page_num(
        page_num : Annotated[int, Path(ge=1)],
        size : Annotated[int, Query(ge=1, le=100)] = 10,
):
    return {"page" : page_num, "size" : size}

# 도전 문제. 점수 범위 검증
@app.get("/scores/{subject_id}")
async def get_subject_id(
        subject_id : Annotated[int, Path(ge=1, le=10)],
        score : Annotated[float, Query(ge=0, le= 100)],
        bonus : Annotated[float | None, Query(ge=1, le=9)] = None,
):
    total = score + (bonus or 0)
    result = {
        "subject_id": subject_id,
        "score": score,
        "total": min(total, 100),
    }
    if bonus is not None:
        result["bonus"] = bonus
    return result