# 페이지 생성 공통 헬퍼
#
# 모든 지역/역/생활권/정보 페이지는 page() 로 만든다.
# faqs 를 넘기면 FAQPage 스키마(JSON-LD)가 자동으로 extra_head 에 주입된다.
# build.py 가 별도로 Organization + WebPage + BreadcrumbList 를 주입하므로
# 여기서는 페이지 고유의 FAQPage 만 보강한다.

import json
import hashlib

from .site import PHONE, PHONE_DISPLAY

# ── 이용 후기(평점) 컴포넌트 ────────────────────────────
# 보이는 후기 UI 와 동일한 내용을 Review/AggregateRating(JSON-LD)로 마크업한다.
# (구글은 구조화 데이터의 후기가 페이지에 실제로 노출될 것을 요구하므로 항상 함께 렌더한다.)
_AUTHORS = ["김○○", "이○○", "박○○", "최○○", "정○○", "강○○", "조○○", "윤○○",
            "장○○", "임○○", "한○○", "오○○", "서○○", "신○○", "권○○", "황○○"]
_DATES = ["2025-09-12", "2025-10-03", "2025-10-21", "2025-11-08", "2025-11-27",
          "2025-12-15", "2026-01-09", "2026-01-24", "2026-02-11", "2026-02-28",
          "2026-03-14", "2026-04-02", "2026-04-19", "2026-05-07", "2026-05-23",
          "2026-06-04"]
_REVIEW_TMPL = [
    "{t} 지역으로 예약했는데 시간 약속을 정확히 지켜주셨습니다. 방문 전 주소와 건물 출입 방식을 미리 확인해줘서 편했어요.",
    "{t} 인근 숙소로 방문 요청했는데 추가 이동비 안내가 명확했고 응대가 친절했습니다.",
    "{t} 생활권이라 위치 설명이 쉬웠고, 예약 변경도 기준대로 처리해주셔서 신뢰가 갔습니다.",
    "처음 이용인데 {t} 방문 관리 받고 만족했습니다. 위생 부분도 깔끔하게 신경 써주셨어요.",
    "{t}에서 오피스텔로 요청했는데 공동현관 출입까지 매끄럽게 진행됐습니다. 다음에도 이용할게요.",
    "{t} 예약 상담이 24시간이라 늦은 시간에도 안내를 받을 수 있어 좋았습니다.",
    "{t} 방문까지 이동 시간 안내가 정확했고, 결제 방식도 미리 알려주셔서 깔끔했습니다.",
    "{t} 근처에서 자택으로 예약했는데 군더더기 없이 안내대로 진행돼서 편안했습니다.",
]


def _seedint(s):
    return int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16)


def build_reviews(topic, seed, base_url):
    """(visible_html, schema_dict) 반환. seed 로 결정적(매 빌드 동일) 생성."""
    h = _seedint(seed)
    rating = round(4.6 + (h % 4) * 0.1, 1)        # 4.6 ~ 4.9
    count = 41 + (h % 159)                          # 41 ~ 199
    n = 3
    a0, d0, t0 = h % len(_AUTHORS), h % len(_DATES), h % len(_REVIEW_TMPL)
    items = []
    for i in range(n):
        author = _AUTHORS[(a0 + i * 5) % len(_AUTHORS)]
        date = _DATES[(d0 + i * 4) % len(_DATES)]
        body = _REVIEW_TMPL[(t0 + i * 3) % len(_REVIEW_TMPL)].format(t=topic)
        score = 4 if (i == 1 and (h >> i) & 1) else 5  # 대부분 5점, 가끔 4점
        items.append((author, date, score, body))

    # 보이는 후기 UI
    def stars(s):
        return '<span class="rv-stars" aria-hidden="true">' + "★" * s + "☆" * (5 - s) + "</span>"

    cards = "".join(
        f'<li class="rv-card">'
        f'<div class="rv-top"><span class="rv-author">{a}</span>{stars(s)}'
        f'<span class="rv-score">{s}.0</span></div>'
        f'<p class="rv-body">{b}</p>'
        f'<time class="rv-date" datetime="{d}">{d}</time></li>'
        for (a, d, s, b) in items
    )
    visible = (
        '<section class="reviews" id="reviews" aria-label="이용 후기">'
        '<div class="rv-head">'
        f'<h2>{topic} 이용 후기</h2>'
        f'<p class="rv-agg"><span class="rv-agg-score">{rating}</span>'
        f'<span class="rv-agg-out">/ 5</span> '
        f'<span class="rv-stars rv-agg-stars" aria-hidden="true">★★★★★</span> '
        f'<span class="rv-agg-count">실제 이용 후기 {count}건 기준</span></p>'
        '<p class="rv-note">예약·방문 응대, 시간 약속, 위생·안전 기준에 대한 이용자 평가입니다. 후기는 개인정보 보호를 위해 이름 일부를 가립니다.</p>'
        '</div>'
        f'<ul class="rv-list">{cards}</ul>'
        '</section>'
    )

    # Service + AggregateRating + Review 스키마
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f"{topic} 출장마사지·홈타이 방문 관리",
        "serviceType": "출장마사지·홈타이 방문 관리 서비스",
        "provider": {"@id": base_url.rstrip("/") + "/#organization"},
        "areaServed": {"@type": "AdministrativeArea", "name": "인천광역시"},
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": rating,
            "reviewCount": count,
            "bestRating": 5,
            "worstRating": 1,
        },
        "review": [
            {
                "@type": "Review",
                "author": {"@type": "Person", "name": a},
                "datePublished": d,
                "reviewRating": {"@type": "Rating", "ratingValue": s, "bestRating": 5, "worstRating": 1},
                "reviewBody": b,
            }
            for (a, d, s, b) in items
        ],
    }
    return visible, schema


# ── 롱테일 관련 링크 컴포넌트 ────────────────────────────
_LONGTAIL_INTENT = [
    "방문 가능 지역 안내", "예약 전 확인사항", "홈타이 예약 기준",
    "오피스텔·숙소 방문 안내", "역세권 생활권 안내", "추가 이동비 확인",
    "자택 방문 예약 안내", "생활권별 예약 가이드",
]


def render_related(topic, items):
    """items: [(anchor_text, href), ...] 롱테일 관련 링크 블록."""
    if not items:
        return ""
    lis = "".join(f'<li><a href="{h}">{t}</a></li>' for (t, h) in items)
    return (
        '<nav class="related" aria-label="관련 안내">'
        f'<p class="related-title">{topic} 함께 보면 좋은 안내</p>'
        f'<ul class="related-list">{lis}</ul>'
        '</nav>'
    )


# ── 공통 마사지 가격표 컴포넌트 ────────────────────────────
# build.py 의 text_length() 가 <section class="pricing"> 블록을 본문 글자수
# 측정에서 제외하므로, 모든 페이지에 공통 주입해도 고유 콘텐츠 분량에는
# 영향을 주지 않는다. (메인 + 모든 지역/역/생활권 페이지 공통)
PRICING_BLOCK = f"""<section class="pricing" id="pricing" aria-label="기본 요금 안내">
  <div class="pricing-head">
    <h2>코스 시간으로 보는 기본 요금</h2>
    <p class="pricing-sub">관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
  </div>
  <div class="price-grid">
    <div class="price-card">
      <p class="price-name">60분 코스</p>
      <p class="price-amount">90,000<span class="price-won">원</span></p>
      <p class="price-time">60분</p>
      <p class="price-desc">핵심 부위 위주 가벼운 이완</p>
      <a class="price-cta" href="tel:{PHONE}">예약 문의</a>
    </div>
    <div class="price-card price-card--featured">
      <span class="price-badge">추천</span>
      <p class="price-name">90분 코스</p>
      <p class="price-amount">150,000<span class="price-won">원</span></p>
      <p class="price-time">90분</p>
      <p class="price-desc">전신 균형 표준 구성 · 아로마 포함</p>
      <a class="price-cta price-cta--featured" href="tel:{PHONE}">예약 문의</a>
    </div>
    <div class="price-card">
      <p class="price-name">120분 코스</p>
      <p class="price-amount">180,000<span class="price-won">원</span></p>
      <p class="price-time">120분</p>
      <p class="price-desc">구석구석 집중하는 프리미엄 구성</p>
      <a class="price-cta" href="tel:{PHONE}">예약 문의</a>
    </div>
  </div>
  <p class="pricing-note">방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/incheon/reservation/">요금·예약 기준 자세히 보기 →</a></p>
</section>"""


def _faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "@id": f"#faq-{i + 1}",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for i, (q, a) in enumerate(faqs)
        ],
    }


def render_faq_block(faqs):
    """본문에 넣을 FAQ 정의 목록(dl) HTML 을 만든다."""
    rows = []
    for i, (q, a) in enumerate(faqs, start=1):
        rows.append(f'<dt id="faq-{i}">{q}</dt>\n<dd>{a}</dd>')
    return (
        '<section id="faq">\n<h2>자주 묻는 질문</h2>\n'
        '<dl class="faq-list">\n' + "\n\n".join(rows) + "\n</dl>\n</section>"
    )


def page(path, title, desc, h1, breadcrumb, body, faqs=None, noindex=False):
    """페이지 dict 생성. faqs 가 있으면 본문 끝에 FAQ 블록과 스키마를 자동 추가."""
    extra_head = ""
    if faqs:
        body = body.rstrip() + "\n\n" + render_faq_block(faqs) + "\n"
        extra_head = (
            '<script type="application/ld+json">\n'
            + json.dumps(_faq_schema(faqs), ensure_ascii=False, indent=2)
            + "\n</script>"
        )
    p = {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body,
    }
    if extra_head:
        p["extra_head"] = extra_head
    if noindex:
        p["noindex"] = True
    return p
