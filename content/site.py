# 인천시 출장마사지 사이트 공통 설정

BASE_URL = "https://incheon-aroma-massage.pages.dev"

BRAND = "바로 GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 외부 문의 채널 (텔레그램)
TELEGRAM_URL = "https://t.me/googleseolab"

# 헤더/푸터 공통 문구
HOME_URL = "/"
TAGLINE = "인천 전지역 방문 관리"
SERVICE_AREA = "인천광역시 전지역"
FOOTER_DESC = (
    "인천 전지역 방문 출장마사지·홈타이 안내 사이트입니다. 모든 서비스는 "
    "안내된 관리 범위와 위생·안전 기준 안에서만 제공됩니다."
)

# 푸터 — 서비스 안내 링크
FOOTER_SERVICE = [
    ("인천 출장마사지", "/"),
    ("구·군별 안내", "/incheon/yeonsu-gu/"),
    ("지역별 안내", "/incheon/yeonsu-gu/songdo/"),
    ("역세권 안내", "/incheon/station/bupyeong-station/"),
    ("생활권 안내", "/incheon/life/songdo-international-city/"),
]

# 푸터 — 이용 안내 링크
FOOTER_INFO = [
    ("예약 안내", "/incheon/reservation/"),
    ("이용 전 확인사항", "/incheon/check/"),
    ("고객센터", "/incheon/support/"),
]

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시
NAV = [
    ("인천 홈", "/", []),
    ("구·군별 안내", "/incheon/yeonsu-gu/", [
        ("중구", "/incheon/jung-gu/"),
        ("동구", "/incheon/dong-gu/"),
        ("미추홀구", "/incheon/michuhol-gu/"),
        ("연수구", "/incheon/yeonsu-gu/"),
        ("남동구", "/incheon/namdong-gu/"),
        ("부평구", "/incheon/bupyeong-gu/"),
        ("계양구", "/incheon/gyeyang-gu/"),
        ("서구", "/incheon/seo-gu/"),
        ("강화군", "/incheon/ganghwa-gun/"),
        ("옹진군", "/incheon/ongjin-gun/"),
    ]),
    ("지역별 안내", "/incheon/yeonsu-gu/songdo/", [
        ("송도", "/incheon/yeonsu-gu/songdo/"),
        ("구월동", "/incheon/namdong-gu/guwol-dong/"),
        ("부평동", "/incheon/bupyeong-gu/bupyeong-dong/"),
        ("주안동", "/incheon/michuhol-gu/juan-dong/"),
        ("청라", "/incheon/seo-gu/cheongna/"),
        ("검단", "/incheon/seo-gu/geomdan-area/"),
        ("영종", "/incheon/jung-gu/yeongjong-area/"),
        ("논현동", "/incheon/namdong-gu/nonhyeon-dong/"),
        ("계산동", "/incheon/gyeyang-gu/gyesan-dong/"),
        ("동인천", "/incheon/jung-gu/dongincheon-area/"),
    ]),
    ("역세권 안내", "/incheon/station/bupyeong-station/", [
        ("부평역", "/incheon/station/bupyeong-station/"),
        ("주안역", "/incheon/station/juan-station/"),
        ("인천시청역", "/incheon/station/incheon-cityhall-station/"),
        ("송도달빛축제공원역", "/incheon/station/songdo-moonlight-festival-park-station/"),
        ("인천대입구역", "/incheon/station/incheon-national-univ-station/"),
        ("원인재역", "/incheon/station/woninjae-station/"),
        ("계양역", "/incheon/station/gyeyang-station/"),
        ("검암역", "/incheon/station/geomam-station/"),
        ("청라국제도시역", "/incheon/station/cheongna-international-city-station/"),
        ("검단사거리역", "/incheon/station/geomdan-sageori-station/"),
        ("석남역", "/incheon/station/seongnam-station/"),
        ("동인천역", "/incheon/station/dongincheon-station/"),
        ("운서역", "/incheon/station/unseo-station/"),
        ("인천공항1터미널역", "/incheon/station/incheon-airport-terminal-1-station/"),
    ]),
    ("생활권 안내", "/incheon/life/songdo-international-city/", [
        ("송도국제도시", "/incheon/life/songdo-international-city/"),
        ("구월·인천시청", "/incheon/life/guwol-incheon-cityhall/"),
        ("부평역·부평시장", "/incheon/life/bupyeong-station-market/"),
        ("주안·도화", "/incheon/life/juan-dohwa/"),
        ("청라국제도시", "/incheon/life/cheongna-international-city/"),
        ("검단신도시", "/incheon/life/geomdan-newtown/"),
        ("영종·운서", "/incheon/life/yeongjong-unseo/"),
        ("인천공항", "/incheon/life/incheon-airport/"),
    ]),
    ("예약 안내", "/incheon/reservation/", []),
    ("이용 전 확인사항", "/incheon/check/", []),
    ("고객센터", "/incheon/support/", [
        ("홈타이 이용 가이드", "/incheon/guide/"),
        ("호텔·숙소 이용 안내", "/incheon/hotel/"),
        ("오피스텔 이용 안내", "/incheon/officetel/"),
        ("개인정보처리방침", "/incheon/support/privacy/"),
    ]),
]
