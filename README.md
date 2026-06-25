# 인천 출장마사지 사이트

인천광역시 전지역 방문 관리 서비스(출장마사지·홈타이) 안내 정적 사이트입니다.

**상호**: 바로 GO
**예약전화**: 0508-202-4719
**메인 키워드**: 출장마사지 / **보조 키워드**: 홈타이

## 구조

- **정적 HTML 사이트** — 어느 호스팅(Cloudflare Pages, GitHub Pages, 웹서버)에서든 그대로 서빙
- **build.py** + **content/** — 페이지를 Python으로 정의하고 정적 HTML 생성
- **생성물** — 각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`

```
build.py                 # 빌드 스크립트 (가격표·스키마·푸터 공통 주입)
content/
  site.py                # 상호·전화·도메인·상단/하단 메뉴
  _helpers.py            # page() 헬퍼 + 공통 마사지 가격표(PRICING_BLOCK)
  root.py                # 루트(/) → /incheon/ 리다이렉트
  main.py                # 인천 메인 페이지 (/incheon/)
  districts.py           # 구·군 페이지 10개
  reform.py              # 2026 개편 대응 4개 (제물포·영종·서해·검단, noindex)
  areas.py               # 대표 지역 페이지
  stations.py            # 역세권 페이지
  life.py                # 생활권 페이지 (구↔역 연결 허브)
  info.py                # 예약·확인사항·가이드·호텔·오피스텔·고객센터·개인정보
data/incheon/            # 지역·역 메타데이터(JSON) — 지시서 18번 데이터 구조
assets/
  style.css              # 프리미엄 옵시디언 + 샴페인 골드 + 오렌지 / Pretendard
  nav.js                 # 모바일 네비게이션
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙

- 본문 **2,000자 미만 페이지는 자동 `noindex`** (가격표 블록은 글자수 측정에서 제외)
- 메뉴명·URL에 “출장마사지” 키워드를 반복하지 않음 (Title·H1·첫 문단에서만 자연스럽게)
- 환승역은 역명 기준 1개 URL (노선·출구별로 쪼개지 않음)
- 번호 동(송도1·2동 등)을 얇게 대량 생성하지 않음
- 모든 페이지 본문은 고유 작성 (지역명만 바꾼 복붙 금지)
- 강화군·옹진군은 도심형이 아닌 **사전 확인형 안내** 페이지
- 모든 페이지 메타 디스크립션 **80자 이내**

## 스키마(JSON-LD)

- 전역: **Organization** (방문형 — 오프라인 주소 없는 사이트이므로 LocalBusiness 미사용)
- 메인: WebPage · BreadcrumbList · Organization · **ImageObject**(선호 썸네일) · **FAQPage**
- 하위 페이지: Organization · WebPage · BreadcrumbList (+ 페이지별 FAQPage 자동 주입)

## 2026 행정체제 개편 대응

- 현행 2군 8구 기준으로 색인, `제물포구·영종구·서해구·검단구`는 `draft/noindex` 준비
- 개편(2026-07-01) 이후 canonical · 내부링크 · sitemap · redirect 재정리
- 데이터 그룹 분리: 영종·운서·공항 → 영종구 / 청라·가정·석남·가좌·루원 → 서해구 / 검단·원당·당하·마전 → 검단구 / 중구 내륙·동구 → 제물포구

## 컴포넌트

- **마사지 가격표**: 60분 90,000원 / 90분 150,000원(추천) / 120분 180,000원 — 메인 및 모든 지역 페이지 공통 주입
- **푸터**: 웹사이트 제작문의·제휴문의 오렌지 버튼 + 텔레그램 링크
- **부동 전화 버튼(FAB)**: 모바일 즉시 통화

## 배포 전 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `assets/og-image.png` (1200×630) 제작하여 추가 (OG·ImageObject 썸네일)
3. `python3 build.py` 재실행
4. Google Search Console에 `sitemap.xml` 제출
