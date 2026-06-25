# 페이지 생성 공통 헬퍼
#
# 모든 지역/역/생활권/정보 페이지는 page() 로 만든다.
# faqs 를 넘기면 FAQPage 스키마(JSON-LD)가 자동으로 extra_head 에 주입된다.
# build.py 가 별도로 Organization + WebPage + BreadcrumbList 를 주입하므로
# 여기서는 페이지 고유의 FAQPage 만 보강한다.

import json

from .site import PHONE, PHONE_DISPLAY

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
