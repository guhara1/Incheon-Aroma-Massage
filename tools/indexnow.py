#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스에 URL을 한 번에 알린다.

사용법:
  # 전체 URL 일괄 통보 (sitemap.xml 기준)
  python3 tools/indexnow.py

  # 특정 URL만 통보 (글 올릴 때마다)
  python3 tools/indexnow.py https://incheon-aroma-massage.pages.dev/incheon/seo-gu/cheongna/

표준 라이브러리만 사용한다(추가 설치 불필요).
IndexNow 참여 검색엔진(Bing·Naver·Yandex·Seznam)은 한 곳에 통보해도 서로 공유하지만,
확실한 전달을 위해 대표 엔드포인트 여러 곳에 함께 제출한다.
"""
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = BASE.split("://", 1)[-1]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# IndexNow 엔드포인트 (참여 검색엔진끼리 공유되지만 직접 제출이 가장 빠름)
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://yandex.com/indexnow",
]


def urls_from_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(path)
    return [loc.text.strip() for loc in tree.findall(".//s:loc", ns)]


def submit(urls):
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    headers = {"Content-Type": "application/json; charset=utf-8"}
    for ep in ENDPOINTS:
        req = urllib.request.Request(ep, data=payload, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                print(f"  [{resp.status}] {ep}")
        except urllib.error.HTTPError as e:
            # 200/202 가 정상. 일부 엔드포인트는 키 위치 검증 후 처리.
            print(f"  [{e.code}] {ep} — {e.reason}")
        except Exception as e:  # noqa: BLE001
            print(f"  [ERR] {ep} — {e}")


def main():
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    urls = args if args else urls_from_sitemap()
    if not urls:
        sys.exit("통보할 URL이 없습니다.")
    print(f"IndexNow 통보 대상 {len(urls)}개 URL → host={HOST}, key={INDEXNOW_KEY}")
    for u in urls[:5]:
        print("   -", u)
    if len(urls) > 5:
        print(f"   … 외 {len(urls) - 5}개")
    submit(urls)
    print("완료. 빙·네이버 서치어드바이저에서 색인 상태를 확인하세요.")


if __name__ == "__main__":
    main()
