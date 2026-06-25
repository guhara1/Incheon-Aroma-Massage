# 색인(인덱싱) 가속 도구

빌드(`python3 build.py`)는 다음을 자동 생성합니다.

| 파일 | 용도 |
|---|---|
| `sitemap.xml` | 색인 가능한 전 페이지 + `lastmod`·`changefreq`·`priority` |
| `rss.xml` | 네이버 서치어드바이저 RSS 제출용 피드 |
| `robots.txt` | 모든 봇 허용 + `sitemap.xml`·`rss.xml` 명시 |
| `<INDEXNOW_KEY>.txt` | IndexNow 소유확인 키 파일(루트 노출) |
| `<head>` 내 `naver-site-verification` | 네이버 사이트 소유확인 메타 |

## 1) 검색엔진 등록 (최초 1회)

- **구글 Search Console**: 속성 등록 → `sitemap.xml` 제출
- **네이버 서치어드바이저**: 사이트 등록(메타태그는 이미 적용됨) → `sitemap.xml` + `rss.xml` 제출
- **빙 웹마스터**: 사이트 등록 → `sitemap.xml` 제출 (Search Console 가져오기 가능)

## 2) IndexNow — 빙·네이버·얀덱스 즉시 통보

추가 설치 없이 표준 라이브러리만 사용합니다.

```bash
# 전체 URL 일괄 통보 (배포 후 1회)
python3 tools/indexnow.py

# 글/페이지 추가·수정 시 해당 URL만 즉시 통보
python3 tools/indexnow.py https://incheon-aroma-massage.pages.dev/incheon/seo-gu/cheongna/
```

키 파일(`<key>.txt`)이 배포 도메인 루트에 실제로 노출된 뒤 실행해야 검증됩니다.

## 3) (선택) 구글 Indexing API — 구글 즉시 통보

구글은 IndexNow에 참여하지 않으므로 별도 API를 씁니다. 서비스 계정 준비가 필요합니다.

```bash
pip install google-auth requests
python3 tools/google_indexing.py service_account.json \
    https://incheon-aroma-massage.pages.dev/incheon/seo-gu/cheongna/
```

준비: GCP에서 Indexing API 사용 설정 → 서비스 계정 JSON 키 → 그 계정 이메일을
Search Console 속성에 "소유자"로 추가. (일일 쿼터 기본 200건)

## sitemap ping 관련 참고

구글·빙은 2023년에 sitemap **ping 엔드포인트를 폐지**했습니다. 따라서 자동 ping
대신 위의 **IndexNow(빙·네이버)** + **Search Console/서치어드바이저 sitemap 제출**이
현재 가장 빠른 색인 경로입니다.

## 배포 자동화 팁

배포(예: Cloudflare Pages) 후 한 줄로 즉시 통보하도록 연결할 수 있습니다.

```bash
python3 build.py && python3 tools/indexnow.py
```
