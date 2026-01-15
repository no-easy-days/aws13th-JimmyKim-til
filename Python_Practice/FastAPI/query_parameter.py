from fastapi import FastAPI
from datetime import date
app = FastAPI()
# 문제 1: 상품 목록 API 만들기
@app.get("/products")
async def get_products(
        category : str | None = None,
        min_price : int = 0,
        max_price : int | None = None,
        page : int = 1
        ):
    return {
        "category" : category,
        "min_price" : min_price,
        "max_price" : max_price,
        "page" : page
    }

# 문제 2: 검색 API 만들기
@app.get("/search")
async def get_search(
        q : str,
        sort : str = "relevance",
        order : str = "desc",
        include_archived : bool = False
):
    return {
        "q" : q,
        "sort" : sort,
        "order" : order,
        "include_archived" : include_archived
    }

# 문제 3: 사용자 프로필 API 만들기
@app.get("/users/{user_id}/profile")
async def get_profile(
        user_id : str,
        include_posts : bool = True,
        include_comments : bool = False,
        limit : int = 10
):
    return {
        "user_id" : user_id,
        "include_posts" : include_posts,
        "include_comments" : include_comments,
        "limit" : limit
    }

# 문제 4: 통계 API 만들기
@app.get("/stats")
async def get_stats(
        metric : str,
        group_by : str = "day",
        start_date: date | None = None,
        end_date: date | None = None
):
    return {
        "start_date" : start_date,
        "end_date" : end_date,
        "metric" : metric,
        "group_by" : group_by
    }

# 문제 5: 종합 문제
# 과제에 써먹자. 페이지 네이션 - 1, 10으로 적용.
@app.get("/posts")
async def get_posts(
        page : int = 1,
        size : int = 10,
        sort_by : str = "likes",
        order : str = "desc",
        author : str = "Jimmy",
        tag : str = "Jimmy_tag",
        published: date | None = None,
        search : str | None = None
):
    return {
        page,
        size,
        sort_by,
        order,
        author,
        tag,
        published,
        search
    }