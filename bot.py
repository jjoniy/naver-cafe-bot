import os
import requests

def send_discord_notification():
    webhook_url = os.environ.get('DISCORD_WEBHOOK_URL')
    print(f"Webhook URL Loaded: {'Yes' if webhook_url else 'No'}")

    url = "https://openapi.naver.com/v1/search/cafearticle.json?query=공지사항&display=1"
    headers = {
        "X-Naver-Client-Id": "mJdNXCs5Wz5tvav0AiUO",
        "X-Naver-Client-Secret": "meNyYrEmDx"
    }

    response = requests.get(url, headers=headers)
    print(f"Naver API Status Code: {response.status_code}")
    print(f"Naver API Response: {response.text}")

    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            item = data["items"][0]
            title = item["title"].replace("<b>", "").replace("</b>", "")
            link = item["link"]

            payload = {"content": f"**[네이버 카페 새 글]**\n{title}\n{link}"}
            discord_response = requests.post(webhook_url, json=payload)
            print(f"Discord API Status Code: {discord_response.status_code}")
        else:
            print("검색된 아이템(items)이 없습니다.")

if __name__ == "__main__":
    send_discord_notification()
