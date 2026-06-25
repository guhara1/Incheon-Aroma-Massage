#!/usr/bin/env python3
"""(선택) 구글 Indexing API 즉시 통보 — 구글은 IndexNow 미참여이므로 별도 처리.

구글 Indexing API는 공식적으로 JobPosting·BroadcastEvent 용도로 안내되지만,
URL 업데이트/삭제 통보(urlNotifications.publish)는 일반 페이지에도 실무상 사용된다.
빠른 색인이 필요하면 Search Console sitemap 제출과 병행한다.

사전 준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 발급 (service_account.json)
  3) Search Console 속성에 해당 서비스 계정 이메일을 "소유자"로 추가
  4) 라이브러리 설치: pip install google-auth requests

사용법:
  python3 tools/google_indexing.py service_account.json \
      https://incheon-aroma-massage.pages.dev/incheon/seo-gu/cheongna/
  # URL 미지정 시 sitemap.xml 전체 통보 (일일 쿼터 200건 주의)
"""
import os
import sys
import xml.etree.ElementTree as ET

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def urls_from_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [loc.text.strip() for loc in ET.parse(path).findall(".//s:loc", ns)]


def main():
    if len(sys.argv) < 2:
        sys.exit("사용법: python3 tools/google_indexing.py <service_account.json> [URL ...]")
    sa_file = sys.argv[1]
    urls = [a for a in sys.argv[2:] if a.startswith("http")] or urls_from_sitemap()

    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성 필요: pip install google-auth requests")

    creds = service_account.Credentials.from_service_account_file(sa_file, scopes=SCOPES)
    session = AuthorizedSession(creds)

    print(f"구글 Indexing API 통보 {len(urls)}개 URL")
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        print(f"  [{r.status_code}] {u}")
    print("완료. (일일 쿼터 기본 200건)")


if __name__ == "__main__":
    main()
