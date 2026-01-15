from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import AfterValidator
app = FastAPI()
# 문제 1: 기본 검증 적용하기
@app.get("/search/")
async def get_search(
        keyword : Annotated[str | None, Query(min_length=2, max_length=100)] = None
    ):
    if keyword:
        return {"searching_for" : keyword}
    return {"message" : "검색어를 제대로 입력하셔야 합니다."}

# 문제 2: 정규표현식 패턴 적용하기
@app.get("/products/")
async def get_product(
        code: Annotated[str, Query(pattern="^PRD-[0-9]{4}$")]
):
    # ^PRD- : PRD-로 시작해야한다.
    # [0-9]{4} : 숫자 4개가 와야한다.
    # $ : 여기서 끝이 난다.
    return {"product code" : code}

# 문제 3: 여러 값 받기
@app.get("/articles/")
async def get_articles(
        tags: Annotated[list[str], Query()] = ["general"]
):
    # 리스트 타입은 반드시!!! Query()를 명시. 안그러면 Request Body로 읽힘!
    return {"tags" : tags}

# 문제 4: Alias와 메타데이터
# Python에서는 하이픈을 코드에 쓸 수 없기때문에, alias를 활용한다.
@app.get("/users/")
async def get_users(
        user_id : Annotated[
            str | None, Query(alias="user-id", title="사용자 ID", description="조회할 사용자 고유 식별자")
        ] = None
):
    return {"user-id" : user_id}

# 문제 5: 커스텀 검증 함수

def using_after_validator(email_address : str):
    if not email_address in ["@company.com", "@company.co.kr"]:
        raise ValueError(f"도메인 명이 이상합니다.")
    return email_address

@app.get("/register/")
async def get_register(
        email : Annotated[
            str, AfterValidator(using_after_validator)
        ]
):
    return {"email_address" : email}

# 도전 문제 : 복합 검증
@app.get("/orders/")
async def get_orders(
        order_id : Annotated[str | None, Query(pattern="^ORD-[0-9]{8}$")] = None,
        status : Annotated[list[str], Query()] = None,
        customer_name : Annotated[str | None, Query(min_length=2, max_length=50)] = None,
        page : Annotated[int, Query(ge=1)] = 1
):
    filters = {}
    if order_id:
        filters["order_id"] = order_id
    if status:
        filters["status"] = status
    if customer_name:
        filters["customer_name"] = customer_name

    return {
        "filters": filters,
        "page": page,
        "message": "검색 결과가 여기에 표시돼요"
    }
