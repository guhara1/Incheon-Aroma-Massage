# 2026년 7월 1일 인천 행정체제 개편 대응 페이지 (제물포구·영종구·서해구·검단구)
# 개편 전에는 noindex(draft) 상태로 두고, 개편 이후 canonical·redirect·sitemap 을 재정리한다.

from ._helpers import page

_CRUMB = [("인천", "/incheon/"), ("2026 개편 대응", None)]


def _reform_body(name, current, future_desc, links):
    link_html = "".join(
        f'<li><a href="{h}">{l}</a></li>' for l, h in links
    )
    return f"""
<section>
<h2>{name} 개편 안내</h2>
<p>{name}는 2026년 7월 1일 시행 예정인 인천광역시 행정체제 개편으로 새로 설치되는 자치구입니다. 현재는 개편 전이므로 이 페이지는 준비 단계(noindex)로 운영되며, 실제 개편 이후 행정구역 기준에 맞춰 색인·내부링크·리디렉션을 재정리할 예정입니다.</p>
<p>{future_desc} 개편 전에는 아래 현행 구·군 페이지에서 동일 생활권을 먼저 확인하세요. 출장마사지·홈타이 방문 가능 지역과 예약 전 확인사항은 현행 페이지 기준으로 안내됩니다.</p>
</section>

<section>
<h2>현재 안내 기준</h2>
<p>{name} 예정 권역은 현재 다음 페이지에서 안내합니다.</p>
<ul>{link_html}</ul>
<p>정확한 행정구역 변동 일정은 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청</a> 공고를 함께 확인하시기 바랍니다. 개편 시행 후에는 본 페이지가 정식 안내 페이지로 전환됩니다.</p>
</section>
"""


PAGES = [
    page(
        path="incheon/jemulpo-gu/",
        title="제물포구 출장마사지 안내 (2026 개편 대응 준비)",
        desc="제물포구 출장마사지·홈타이는 개편 전 중구 내륙·동구 생활권 페이지에서 확인하세요.",
        h1="제물포구 출장마사지 (개편 대응 준비)",
        breadcrumb=_CRUMB,
        body=_reform_body(
            "제물포구", "중구 내륙·동구",
            "제물포구는 중구 내륙권과 동구를 중심으로 재편될 예정입니다.",
            [("중구", "/incheon/jung-gu/"), ("동구", "/incheon/dong-gu/"),
             ("동인천", "/incheon/jung-gu/dongincheon-area/")],
        ),
        noindex=True,
    ),
    page(
        path="incheon/yeongjong-gu/",
        title="영종구 출장마사지 안내 (2026 개편 대응 준비)",
        desc="영종구 출장마사지·홈타이는 개편 전 중구 영종·운서·공항 생활권에서 확인하세요.",
        h1="영종구 출장마사지 (개편 대응 준비)",
        breadcrumb=_CRUMB,
        body=_reform_body(
            "영종구", "영종·운서·공항권",
            "영종구는 영종·운서·인천공항 권역을 중심으로 재편될 예정입니다.",
            [("중구", "/incheon/jung-gu/"), ("영종", "/incheon/jung-gu/yeongjong-area/"),
             ("영종·운서 생활권", "/incheon/life/yeongjong-unseo/"),
             ("인천공항 생활권", "/incheon/life/incheon-airport/")],
        ),
        noindex=True,
    ),
    page(
        path="incheon/seohae-gu/",
        title="서해구 출장마사지 안내 (2026 개편 대응 준비)",
        desc="서해구 출장마사지·홈타이는 개편 전 서구 남부 청라·가정·석남 생활권에서 확인하세요.",
        h1="서해구 출장마사지 (개편 대응 준비)",
        breadcrumb=_CRUMB,
        body=_reform_body(
            "서해구", "서구 남부권",
            "서해구는 청라·가정·석남·가좌·루원 등 서구 남부권을 중심으로 재편될 예정입니다.",
            [("서구", "/incheon/seo-gu/"), ("청라", "/incheon/seo-gu/cheongna/"),
             ("청라국제도시 생활권", "/incheon/life/cheongna-international-city/")],
        ),
        noindex=True,
    ),
    page(
        path="incheon/geomdan-gu/",
        title="검단구 출장마사지 안내 (2026 개편 대응 준비)",
        desc="검단구 출장마사지·홈타이는 개편 전 서구 검단·원당·당하·마전 생활권에서 확인하세요.",
        h1="검단구 출장마사지 (개편 대응 준비)",
        breadcrumb=_CRUMB,
        body=_reform_body(
            "검단구", "검단·원당·당하·마전권",
            "검단구는 검단·원당·당하·마전 등 검단신도시 권역을 중심으로 재편될 예정입니다.",
            [("서구", "/incheon/seo-gu/"), ("검단", "/incheon/seo-gu/geomdan-area/"),
             ("검단신도시 생활권", "/incheon/life/geomdan-newtown/")],
        ),
        noindex=True,
    ),
]
