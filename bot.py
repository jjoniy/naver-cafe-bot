Python
import os
import requests

def send_discord_notification():
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    
    # 네이버 오픈 API 또는 크롤링 로직 수행
    url = "https://openapi.naver.com/v1/search/cafearticle.json?query=공지사항 & 정보 소개&display=1"
    headers = {
        "X-Naver-Client-Id": "YOUR_CLIENT_ID",
        "X-Naver-Client-Secret": "YOUR_CLIENT_SECRET"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            item = data["items"][0]
            title = item["title"].replace("<b>", "").replace("</b>", "")
            link = item["link"]
            
            # 디스코드로 전송
            payload = {"content": f"**[네이버 카페 새 글]**\n{title}\n{link}"}
            requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    send_discord_notification()
