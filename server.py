from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from database.news import find_all_data, find_other_data
import uvicorn,os

load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f'{os.environ.get("URL")}'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return "Hi 歡迎來到 newBug"

@app.get('/all_news/{page}')
async def news(page: int):
    return find_all_data(page)

@app.get('/news/{news_name}')
async def other_news(news_name: str):
    return find_other_data(news_name)

if __name__ == '__main__':
    uvicorn.run("server:app", reload= True)