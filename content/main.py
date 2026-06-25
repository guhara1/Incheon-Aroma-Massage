import json
from .site import BRAND, BASE_URL, PHONE

_BASE = BASE_URL.rstrip("/")
_HOME = _BASE + "/"

# 메타 설명 (80자 이내)
DESC = "인천 출장마사지·홈타이 예약 전 송도, 부평, 구월, 청라, 검단, 영종, 주안 생활권을 확인하세요."

# 자주 묻는 질문 (FAQ 스키마)
_FAQ = [
    ("인천은 구·군별 페이지를 모두 만들어야 하나요?",
     "구·군별 페이지를 두는 것이 좋습니다. 다만 단순 반복이 아니라 대표 생활권, 가까운 역, 예약 기준이 구마다 다르게 안내되어야 합니다. 인천은 송도·연수의 국제도시 생활권, 구월·인천시청의 행정·상권, 부평·주안의 역세권, 청라·검단의 신도시 생활권이 뚜렷하게 구분됩니다."),

    ("송도와 연수구 페이지를 따로 봐도 되나요?",
     "가능합니다. 연수구 페이지는 송도·연수·동춘·원인재를 아우르는 구 전체 허브이고, 송도 페이지는 송도국제도시와 인천대입구역·센트럴파크역 중심의 생활권으로 좁혀 확인하실 수 있습니다."),

    ("부평역과 부평동은 어떻게 다른가요?",
     "부평역 페이지는 환승 역세권과 부평시장·부평구청 인접 동선을 기준으로, 부평동 페이지는 부평문화의거리와 주거 생활권을 기준으로 안내합니다. 위치에 따라 더 가까운 쪽을 확인하세요."),

    ("영종과 인천공항은 따로 확인해야 하나요?",
     "따로 보시는 것이 좋습니다. 영종은 운서·영종 주거 생활권 기준이고, 인천공항은 공항·숙소·차량 이동 기준 중심입니다. 공항 인근 숙소 방문은 출입 방식과 이동 시간을 먼저 확인하세요."),

    ("강화군과 옹진군도 방문이 되나요?",
     "강화군과 옹진군은 도심형이 아니라 사전 확인형 지역입니다. 차량 이동 기준, 추가 이동비, 방문 가능 주소, 사전 예약 가능 여부를 먼저 확인한 뒤 예약하시는 것이 좋습니다. 도서 지역은 이동 가능 시간을 반드시 확인하세요."),

    ("예약 전 꼭 확인해야 할 사항은 무엇인가요?",
     "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 자택·숙소·오피스텔 이용 기준, 결제 방식, 예약 변경 기준, 개인정보 처리 기준을 먼저 확인하세요. 불법·선정적 서비스는 어떤 경우에도 제공하지 않습니다."),
]

_faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "@id": f"#faq-{i+1}",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for i, (q, a) in enumerate(_FAQ)
    ],
}

# WebPage 스키마 (메인)
_webpage_schema = {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "인천 출장마사지｜송도·부평·구월·청라 홈타이 생활권 예약 안내",
    "description": DESC,
    "url": _HOME,
    "inLanguage": "ko",
    "isPartOf": {"@id": _BASE + "/#organization"},
    "publisher": {"@id": _BASE + "/#organization"},
    "primaryImageOfPage": {"@id": _HOME + "#primaryimage"},
}

# ImageObject 스키마 (선호 썸네일 지정 — schema.org + og:image 병행)
_image_schema = {
    "@context": "https://schema.org",
    "@type": "ImageObject",
    "@id": _HOME + "#primaryimage",
    "url": _BASE + "/assets/og-image.png",
    "contentUrl": _BASE + "/assets/og-image.png",
    "width": 1200,
    "height": 630,
    "caption": "인천 출장마사지·홈타이 지역별 예약 안내",
}

# BreadcrumbList 스키마 (메인)
_breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "홈", "item": _HOME},
    ],
}


def _ld(obj):
    return ('<script type="application/ld+json">\n'
            + json.dumps(obj, ensure_ascii=False, indent=2)
            + "\n</script>")


_EXTRA_HEAD = "\n".join(
    _ld(o) for o in (_webpage_schema, _image_schema, _breadcrumb_schema, _faq_schema)
)

_HERO = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">전지역 방문 관리 · 24시간 예약 상담</div>
    <h1 class="hero-title">인천 출장마사지<br><span class="hero-accent">홈타이</span><br>우리 동네 방문 예약 가이드</h1>
    <p class="hero-lead">송도·부평·구월·청라·검단·영종·주안 등 주요 생활권을 골라 방문 가능 지역과 예약 전 확인사항을 바로 확인하세요.</p>
    <div class="hero-cta">
      <a href="#districts" class="btn btn-primary">구·군별 안내</a>
      <a href="#areas" class="btn btn-secondary">지역별 안내</a>
      <a href="#stations" class="btn btn-secondary">지하철역 찾기</a>
      <a href="#lifestyle" class="btn btn-secondary">생활권 찾기</a>
      <a href="/incheon/reservation/" class="btn btn-secondary">예약 안내 보기</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat"><div class="stat-number">2군8구</div><div class="stat-label">구·군 안내</div></div>
    <div class="stat"><div class="stat-number">36</div><div class="stat-label">지역 생활권</div></div>
    <div class="stat"><div class="stat-number">31</div><div class="stat-label">역세권 안내</div></div>
    <div class="stat"><div class="stat-number">24H</div><div class="stat-label">상담 가능</div></div>
  </div>
</div>"""

PAGE = {
    "path": "",
    "title": "인천 출장마사지｜송도·부평·구월·청라 홈타이 생활권 예약 안내",
    "desc": DESC,
    "h1": "인천 출장마사지·홈타이 생활권별 방문 예약 가이드",
    "hero": _HERO,
    "breadcrumb": [],
    "extra_head": _EXTRA_HEAD,
    "body": """
<section id="criteria">
  <h2>인천에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
  <p>인천광역시는 구·군별 생활권 차이가 매우 큰 도시입니다. 출장마사지·홈타이를 예약하기 전에 자신의 위치가 어느 구의 어느 생활권에 속하는지 먼저 파악하면 방문 주소와 이동 시간을 정확히 정할 수 있습니다.</p>
  <p>송도와 연수는 국제도시·주거 중심의 생활권이고, 구월과 인천시청 주변은 행정·상권 중심입니다. 부평과 주안은 환승 역세권 검색 의도가 강하고, 청라와 검단은 신도시형 생활권 검색이 많습니다. 영종과 인천공항은 공항·숙소·차량 이동 기준이 중요하며, 강화와 옹진은 사전 방문 가능 여부와 추가 이동비 확인이 먼저 필요한 지역입니다.</p>
  <p>또한 인천은 2026년 7월 1일 행정체제 개편이 예정되어 있습니다. 중구·동구 내륙권은 제물포구로, 영종·운서·공항권은 영종구로, 서구 남부권은 서해구로, 검단권은 검단구로 재편될 예정이므로 관련 지역은 개편 이후 구조까지 고려하여 안내합니다. 행정구역 변동은 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청</a> 공고를 함께 확인하시면 정확합니다.</p>
</section>

<section id="districts">
  <h2>인천 구·군별 방문 가능 지역 안내</h2>
  <p>인천 2군 8구의 구·군별 대표 생활권과 가까운 역을 기준으로 방문 가능 지역을 안내합니다. 각 구를 눌러 상세 생활권을 확인하세요.</p>
  <div class="card-grid">
    <a href="/incheon/jung-gu/" class="card"><h3>중구</h3><p>동인천, 영종, 운서, 인천공항 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/dong-gu/" class="card"><h3>동구</h3><p>송림, 송현, 동인천 인접 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/michuhol-gu/" class="card"><h3>미추홀구</h3><p>주안, 도화, 용현, 학익 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/yeonsu-gu/" class="card"><h3>연수구</h3><p>송도, 연수, 동춘, 원인재 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/namdong-gu/" class="card"><h3>남동구</h3><p>구월, 간석, 논현, 소래 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/bupyeong-gu/" class="card"><h3>부평구</h3><p>부평역, 부평시장, 삼산, 산곡 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/gyeyang-gu/" class="card"><h3>계양구</h3><p>계산, 작전, 계양역, 귤현 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/seo-gu/" class="card"><h3>서구</h3><p>청라, 검단, 검암, 루원, 석남 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/ganghwa-gun/" class="card"><h3>강화군</h3><p>강화읍, 길상, 화도, 교동 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/ongjin-gun/" class="card"><h3>옹진군</h3><p>영흥, 자월, 백령, 대청 도서 생활권</p><span class="card-arrow">→</span></a>
  </div>
</section>

<section id="areas">
  <h2>인천 대표 지역별 방문 가능 지역 안내</h2>
  <div class="card-grid">
    <a href="/incheon/yeonsu-gu/songdo/" class="card"><h3>송도</h3><p>송도국제도시, 인천대입구역, 센트럴파크 생활권</p></a>
    <a href="/incheon/namdong-gu/guwol-dong/" class="card"><h3>구월동</h3><p>인천시청, 예술회관, 인천터미널 인접 생활권</p></a>
    <a href="/incheon/bupyeong-gu/bupyeong-dong/" class="card"><h3>부평동</h3><p>부평역, 부평시장, 부평구청 인접 생활권</p></a>
    <a href="/incheon/michuhol-gu/juan-dong/" class="card"><h3>주안동</h3><p>주안역, 도화동, 미추홀구 중심 생활권</p></a>
    <a href="/incheon/seo-gu/cheongna/" class="card"><h3>청라</h3><p>청라국제도시, 청라국제도시역, 루원 인접 생활권</p></a>
    <a href="/incheon/seo-gu/geomdan-area/" class="card"><h3>검단</h3><p>검단신도시, 검단사거리역, 완정역 생활권</p></a>
    <a href="/incheon/jung-gu/yeongjong-area/" class="card"><h3>영종</h3><p>운서역, 영종역, 인천공항 인접 생활권</p></a>
    <a href="/incheon/namdong-gu/nonhyeon-dong/" class="card"><h3>논현동</h3><p>인천논현역, 소래포구역, 남동공단 인접 생활권</p></a>
    <a href="/incheon/gyeyang-gu/gyesan-dong/" class="card"><h3>계산동</h3><p>계산역, 경인교대입구역, 작전동 인접 생활권</p></a>
    <a href="/incheon/jung-gu/dongincheon-area/" class="card"><h3>동인천</h3><p>동인천역, 신포, 제물포 인접 생활권</p></a>
  </div>
</section>

<section id="stations">
  <h2>인천 주요 지하철역별 홈타이 안내</h2>
  <p>인천 1·2호선, 수인분당선, 인천공항철도 주요 역을 기준으로 인접 생활권과 예약 전 확인사항을 안내합니다. 환승역은 역명 기준 한 페이지로만 안내합니다.</p>
  <div class="card-grid">
    <a href="/incheon/station/bupyeong-station/" class="card"><h3>부평역</h3><p>부평동, 부평시장, 부개동 인접</p></a>
    <a href="/incheon/station/juan-station/" class="card"><h3>주안역</h3><p>주안동, 도화동 인접</p></a>
    <a href="/incheon/station/incheon-cityhall-station/" class="card"><h3>인천시청역</h3><p>구월동, 간석동 인접</p></a>
    <a href="/incheon/station/songdo-moonlight-festival-park-station/" class="card"><h3>송도달빛축제공원역</h3><p>송도국제도시, 국제업무지구 인접</p></a>
    <a href="/incheon/station/incheon-national-univ-station/" class="card"><h3>인천대입구역</h3><p>송도, 센트럴파크 인접</p></a>
    <a href="/incheon/station/woninjae-station/" class="card"><h3>원인재역</h3><p>연수동, 동춘동 인접</p></a>
    <a href="/incheon/station/gyeyang-station/" class="card"><h3>계양역</h3><p>귤현, 박촌 인접</p></a>
    <a href="/incheon/station/geomam-station/" class="card"><h3>검암역</h3><p>검암동, 아라 인접</p></a>
    <a href="/incheon/station/cheongna-international-city-station/" class="card"><h3>청라국제도시역</h3><p>청라, 루원 인접</p></a>
    <a href="/incheon/station/geomdan-sageori-station/" class="card"><h3>검단사거리역</h3><p>검단, 마전 인접</p></a>
    <a href="/incheon/station/seongnam-station/" class="card"><h3>석남역</h3><p>석남동, 가좌 인접</p></a>
    <a href="/incheon/station/dongincheon-station/" class="card"><h3>동인천역</h3><p>신포, 중구 내륙 인접</p></a>
    <a href="/incheon/station/unseo-station/" class="card"><h3>운서역</h3><p>영종, 인천공항 인접</p></a>
    <a href="/incheon/station/incheon-airport-terminal-1-station/" class="card"><h3>인천공항1터미널역</h3><p>인천공항, 운서동 인접</p></a>
  </div>
</section>

<section id="lifestyle">
  <h2>인천 생활권별 예약 기준</h2>
  <p>생활권 페이지는 구·군 페이지와 역 페이지 사이를 연결하는 중간 허브입니다. 지역과 역을 함께 묶어 더 정확한 방문 주소와 이동 시간을 확인할 수 있습니다.</p>
  <div class="card-grid">
    <a href="/incheon/life/songdo-international-city/" class="card">송도국제도시</a>
    <a href="/incheon/life/guwol-incheon-cityhall/" class="card">구월·인천시청</a>
    <a href="/incheon/life/bupyeong-station-market/" class="card">부평역·부평시장</a>
    <a href="/incheon/life/juan-dohwa/" class="card">주안·도화</a>
    <a href="/incheon/life/cheongna-international-city/" class="card">청라국제도시</a>
    <a href="/incheon/life/geomdan-newtown/" class="card">검단신도시</a>
    <a href="/incheon/life/yeongjong-unseo/" class="card">영종·운서</a>
    <a href="/incheon/life/incheon-airport/" class="card">인천공항</a>
  </div>
</section>

<section id="check">
  <h2>인천 홈타이 예약 전 확인사항</h2>
  <p>예약을 진행하기 전에 다음 항목을 먼저 확인하면 예약 과정이 훨씬 수월합니다. 자세한 내용은 <a href="/incheon/check/">이용 전 확인사항</a> 페이지에서 확인하세요.</p>
  <ul>
    <li><strong>방문 가능 주소 확인</strong> — 자택·숙소·오피스텔 등 정확한 방문 주소와 건물 유형</li>
    <li><strong>예약 가능 시간 확인</strong> — 희망 시간대의 방문 가능 여부</li>
    <li><strong>추가 이동비 여부 확인</strong> — 기본 이동권 외 추가 이동비 발생 여부</li>
    <li><strong>건물 출입 방식 확인</strong> — 공동현관·자동문·경비 출입 방식</li>
    <li><strong>자택·숙소·오피스텔 이용 기준 확인</strong> — 방문 장소별 이용 기준</li>
    <li><strong>호텔·숙소 이용 기준 확인</strong> — 호텔·모텔·게스트하우스 방문 기준</li>
    <li><strong>공항·도서 지역 방문 가능 여부 확인</strong> — 인천공항·강화·옹진 방문 가능 여부</li>
    <li><strong>결제 방식 확인</strong> — 가능한 결제 수단</li>
    <li><strong>예약 변경·취소 기준 확인</strong> — 변경·취소 절차와 기준</li>
    <li><strong>개인정보 처리 기준 확인</strong> — 개인정보 수집·이용·보관 방식</li>
    <li><strong>불법·선정적 서비스 불가 안내</strong> — 건전한 방문 관리 서비스만 제공</li>
  </ul>
</section>

<section id="faq">
  <h2>인천 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
""" + "\n".join(
    f'    <dt id="faq-{i+1}">{q}</dt>\n    <dd>{a}</dd>'
    for i, (q, a) in enumerate(_FAQ)
) + """
  </dl>
</section>
"""
}
