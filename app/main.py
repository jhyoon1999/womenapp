from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import numpy as np
import uvicorn
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def home(request: Request):
    # (이전과 동일하게)
    AGE_LABELS = ["10대", "20대", "30대", "40대", "50대", "60대 이상"]
    AGE_VALUES = [120, 450, 390, 260, 150, 45]
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "age_labels": AGE_LABELS,
            "age_values": AGE_VALUES,
        }
    )

@app.get("/news")
async def news(request: Request):
    # Excel 파일에서 뉴스 데이터 읽기
    try:
        df_news = pd.read_excel("app/data/news_data.xlsx", sheet_name="뉴스")
        news_data = df_news.to_dict('records')
    except:
        news_data = []
    
    return templates.TemplateResponse("news.html", {"request": request, "news_data": news_data})

@app.get("/cases")
async def cases(request: Request):
    # Excel 파일에서 판례 데이터 읽기
    try:
        df_cases = pd.read_excel("app/data/news_data.xlsx", sheet_name="판례")
        cases_data = df_cases.to_dict('records')
    except:
        cases_data = []
    
    return templates.TemplateResponse("cases.html", {"request": request, "cases_data": cases_data})

@app.get("/resources")
async def resources(request: Request):
    return templates.TemplateResponse("resources.html", {"request": request})

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/statistics")
async def statistics(request: Request):
    # 연령대별 피해유형 데이터
    df_age = pd.read_csv("app/data/한국여성인권진흥원_디지털성범죄피해자지원센터 연령대별 세부 피해 유형 현황_20231231.csv", encoding="cp949")
    # 지원현황 데이터
    df_support = pd.read_csv("app/data/한국여성인권진흥원_디지털성범죄피해자지원센터 지원현황_20241231.csv", encoding="cp949")

    # 연령대별 피해유형 그래프용 데이터
    age_labels = df_age.iloc[:,0].tolist()
    age_types = df_age.columns[1:].tolist()
    age_type_values = [df_age[type].tolist() for type in age_types]

    # 연도별 지원현황 그래프용 데이터
    year_labels = df_support.iloc[1:,0].tolist()
    support_types = df_support.columns[1:].tolist()
    support_type_values = [df_support[type].iloc[1:].astype(int).tolist() for type in support_types]
    return templates.TemplateResponse(
        "statistics.html",
        {
            "request": request,
            "age_labels": age_labels,
            "age_types": age_types,
            "age_type_values": age_type_values,
            "year_labels": year_labels,
            "support_types": support_types,
            "support_type_values": support_type_values,
        }
    )

if __name__ == "__main__":
    # 환경변수에서 포트 가져오기 (cloudtype.io는 기본적으로 8080 사용)
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)