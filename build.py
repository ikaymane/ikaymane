"""Generate the animated SVGs for the GitHub profile README.

Edit the CONFIG section, then run:  python build.py
Every asset is written twice (dark + light) into ./assets so the README can
switch with <picture> + prefers-color-scheme.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent / "assets"

# ───────────────────────────── CONFIG ─────────────────────────────

USERNAME = "ikaymane"
NAME = "Aymane Idrissi Khamlichi"
EYEBROW = "AI & Automation"
HEADLINE = ["Building AI systems.", "Automating real work."]
SUBLINE = "Agentic AI  ·  Workflow automation  ·  Digital business"
ROLE = "Data Science & AI @ ENSAF  ·  Founder @ Notorify  ·  Design Lead @ GDG on Campus ENSAF"
LOCATION = "Rabat, Morocco"

EXPERIENCE = [
    ("Founder", "Notorify", "Aug 2026 – Present",
     "Gets businesses covered in online news outlets. A journalist writes the story, the client "
     "approves it, and it goes live across news sites in their market, with a report on every placement."),
    ("Agentic AI Intern", "AiOO · Dubai, remote", "Aug 2026 – Oct 2026",
     ""),
    ("AI & ML · AI Automation Intern", "Devoteam · Rabat", "Jul 2025 – Aug 2025",
     "Shipped a multilingual AI medical assistant and a medication reminder engine on n8n and LLM pipelines."),
]
EDUCATION = [
    ("Data Science & AI", "ENSA Fès", "2026 – 2029"),
    ("Computer & Information Sciences", "ENSA Al Hoceima", "2024 – 2026"),
]
LEADERSHIP = [
    ("Lead Designer", "GDG on Campus ENSA Fès", "Oct 2026 – Present"),
    ("Designer", "01 Club ENSAH", "Sep 2025 – Mar 2026"),
    ("Sponsorship Coordinator", "Enactus ENSAH", "Mar 2025 – Jun 2025"),
]

PROJECTS = [
    {"slug": "operion", "kicker": "Oct 2026 · AMD Hackathon Act III", "title": "Operion",
     "desc": "Predictive maintenance copilot that flags equipment issues before they turn into downtime. Built in a team of four.",
     "tags": ["Python", "AI", "Hackathon"]},
    {"slug": "deflake", "kicker": "Sep 2026 · IBM Bob 2.0 Hackathon", "title": "Deflake",
     "desc": "Finds flaky pytest tests and fixes the root cause with AI agents. Took a demo suite from 10% to 100% green.",
     "tags": ["Python", "pytest", "AI agents"]},
    {"slug": "token-pulsar", "kicker": "Mar 2026 · Automation", "title": "Token Pulsar",
     "desc": "Autonomous crypto content engine. Four n8n workflows watch RSS, Reddit and news, then Claude writes and posts.",
     "tags": ["n8n", "Claude API", "Telegram"]},
    {"slug": "ika-tracker", "kicker": "Apr 2026 · Full-stack", "title": "IKA Tracker",
     "desc": "All-in-one personal tracker: tasks, AI planning, gym logging and nutrition in one mobile-first app.",
     "tags": ["TypeScript", "Claude", "Supabase"]},
    {"slug": "ai-medical-assistant", "kicker": "Jul 2025 · Devoteam", "title": "AI Medical Assistant",
     "desc": "Multilingual health assistant with a medication reminder engine, built on LLM pipelines in n8n.",
     "tags": ["n8n", "LLM", "Healthcare"]},
    {"slug": "luxiohome", "kicker": "2022 – 2026 · Web & SEO", "title": "LuxioHome",
     "desc": "Home design and lifestyle blog, built and run end to end on WordPress with a focus on SEO.",
     "tags": ["WordPress", "SEO", "Content"]},
    {"slug": "mario-rl-agent", "kicker": "2025 · Reinforcement learning", "title": "Mario RL Agent",
     "desc": "RL agent trained from scratch to play Super Mario Bros, using reward shaping and frame preprocessing.",
     "tags": ["PyTorch", "OpenAI Gym", "Python"]},
    {"slug": "foody-app", "kicker": "Product concept · Full-stack", "title": "Foody",
     "desc": "Asset-light food delivery platform with dashboards for owners, restaurants, clients and drivers.",
     "tags": ["React", "TypeScript", "Gemini"]},
]

STACK = [
    ("AI & Automation", ["n8n", "Claude API", "Claude Code", "LangGraph", "OpenAI", "Make", "Zapier"]),
    ("Code", ["Python", "TypeScript", "React", "FastAPI", "SQL", "pytest"]),
    ("Data & ML", ["PyTorch", "NumPy", "OpenAI Gym", "MATLAB"]),
    ("Cloud & Web", ["AWS", "Supabase", "WordPress", "SEO"]),
    ("Design", ["Photoshop", "Illustrator", "Canva"]),
]

# (title, issuer key, date, image slug, verify url). Images come from export_certs.py.
CERTS = [
    ("Introduction to Cybersecurity", "cisco", "Jul 2026", "cisco-cybersecurity", ""),
    ("The AI Filmmaking Pipeline", "higgsfield", "Jul 2026", "higgsfield-filmmaking", ""),
    ("Professional Foundations", "alx", "May 2026", "alx-professional-foundations",
     "https://savanna.alxafrica.com/certificates/z8YyH3ETne"),
    ("Introduction to Agent Skills", "anthropic", "May 2026", "anthropic-agent-skills", ""),
    ("Claude Code in Action", "anthropic", "Apr 2026", "anthropic-claude-code",
     "https://verify.skilljar.com/c/p9f796k6abmh"),
    ("Crash Course: AWS Basics", "kodekloud", "Feb 2026", "kodekloud-aws", ""),
    ("Git and GitHub", "365", "Nov 2025", "365-git-github", ""),
    ("ChatGPT for SQL Beginners", "365", "Nov 2025", "365-chatgpt-sql", ""),
    ("Google AI Essentials", "google", "Nov 2025", "google-ai-essentials",
     "https://coursera.org/verify/5XQ6B7K920MT"),
    ("Data Analysis with ChatGPT", "365", "Nov 2025", "365-data-analysis-chatgpt", ""),
    ("Understanding Data Science", "datacamp", "Nov 2025", "datacamp-understanding-ds", ""),
    ("AI Fundamentals", "datacamp", "Nov 2025", "datacamp-ai-fundamentals", ""),
    ("AI Career Essentials", "alx", "Aug 2024", "alx-ai-career-essentials",
     "https://intranet.alxswe.com/certificates/mnM38Y7BSf"),
    ("Master Adobe Illustrator", "udemy", "Mar 2024", "udemy-illustrator",
     "https://ude.my/UC-c4046809-ad0d-4c4f-ac72-a07e82c4d784"),
    ("Adobe Photoshop CC", "udemy", "Jun 2023", "udemy-photoshop",
     "https://ude.my/UC-ca4f5dd0-7a26-4ed1-9bd5-1b3168511c35"),
    ("Design Instagram Posts in Canva", "udemy", "Nov 2022", "udemy-canva",
     "https://ude.my/UC-91471415-ab04-40b6-a5a8-aa9b4e4fb4a9"),
]
CERTS_PAGE = "https://ikaymane.github.io/ikaymane/certificates/"
ISSUERS = {
    "anthropic": ("Anthropic", "A", "#D97757"),
    "cisco": ("Cisco", "C", "#049FD9"),
    "higgsfield": ("Higgsfield", "H", "#8DB600"),
    "alx": ("ALX", "alx", "#0BB07B"),
    "kodekloud": ("KodeKloud", "K", "#1E88E5"),
    "365": ("365 Data Science", "365", "#5B6B8C"),
    "google": ("Google", "G", "#4285F4"),
    "datacamp": ("DataCamp", "DC", "#05B85A"),
    "udemy": ("Udemy", "U", "#A435F0"),
}

# ───────────────────────────── THEMES ─────────────────────────────

THEMES = {
    "light": {
        "bg": "#ffffff", "card": "#f6f8fa", "border": "#d0d7de", "text": "#1f2328",
        "muted": "#59636e", "line": "#d0d7de", "node": "#afb8c1", "hub": "#1f2328",
        "accent": "#1f2328", "empty": "#eff2f5",
    },
    "dark": {
        "bg": "#0d1117", "card": "#151b23", "border": "#30363d", "text": "#f0f6fc",
        "muted": "#9198a1", "line": "#3d444d", "node": "#656c76", "hub": "#f0f6fc",
        "accent": "#f0f6fc", "empty": "#1c2128",
    },
}
SERIF = "Georgia, 'Iowan Old Style', 'Times New Roman', serif"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"

BASE_CSS = f"""
  .serif {{ font-family: {SERIF}; }}
  .sans {{ font-family: {SANS}; }}
  .mono {{ font-family: {MONO}; }}
  .up {{ opacity: 0; animation: up 1s cubic-bezier(.2,.7,.2,1) forwards; }}
  @keyframes up {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
  .draw {{ animation: draw 1.4s cubic-bezier(.4,0,.2,1) forwards; }}
  @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
  @media (prefers-reduced-motion: reduce) {{
    * {{ animation: none !important; opacity: 1 !important; stroke-dashoffset: 0 !important; }}
  }}
"""


def text_w(s, size, k=0.56):
    """Rough rendered width for a proportional string (k scales the average glyph)."""
    def g(c):
        if c in "il.,·'’|/ :": return 0.30
        if c in "mwMW": return 0.86
        if c.isupper() or c.isdigit(): return 0.66
        return 0.53
    return sum(g(c) for c in s) * size * (k / 0.56)


def wrap(s, max_px, size):
    lines, cur = [], ""
    for word in s.split():
        trial = f"{cur} {word}".strip()
        if cur and text_w(trial, size) > max_px:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + [cur] if cur else lines


def svg(W, H, label, css, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
            f'role="img" aria-label="{escape(label)}">\n  <title>{escape(label)}</title>\n'
            f'  <style>{BASE_CSS}{css}</style>\n{body}\n</svg>\n')


def frame(W, H, t, fill="bg"):
    return f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="{t[fill]}" stroke="{t["border"]}"/>'


def eyebrow(x, y, label, t, delay=0.0):
    return (f'<g class="up" style="animation-delay:{delay:.2f}s">'
            f'<line x1="{x}" y1="{y-4}" x2="{x+26}" y2="{y-4}" stroke="{t["muted"]}" stroke-width="1.2"/>'
            f'<text class="sans" x="{x+38}" y="{y}" font-size="12" letter-spacing="2.6" fill="{t["muted"]}">'
            f'{escape(label.upper())}</text></g>')


# ───────────────────────────── HEADER ─────────────────────────────

def header(t):
    W, H = 1200, 430
    hub = (968, 168)
    sats = [(842, 104, 7), (1112, 86, 7), (1104, 224, 7), (986, 290, 7), (880, 236, 5)]
    lines, nodes = [], []
    for i, (x, y, r) in enumerate(sats):
        length = ((x - hub[0]) ** 2 + (y - hub[1]) ** 2) ** 0.5
        lines.append(
            f'<path id="l{i}" d="M{hub[0]},{hub[1]} L{x},{y}" stroke="{t["line"]}" stroke-width="1.4" fill="none" '
            f'stroke-dasharray="{length:.0f}" stroke-dashoffset="{length:.0f}" class="draw" '
            f'style="animation-delay:{0.9 + i*0.12:.2f}s"/>'
        )
        nodes.append(
            f'<circle class="up" cx="{x}" cy="{y}" r="{r}" fill="{t["bg"]}" stroke="{t["node"]}" stroke-width="1.6" '
            f'style="animation-delay:{1.4 + i*0.12:.2f}s"/>'
        )
    # A quiet signal travelling out along each spoke in turn.
    pulses = "".join(
        f'<circle r="2.6" fill="{t["accent"]}" opacity="0">'
        f'<animateMotion dur="6s" begin="2.4s" repeatCount="indefinite" keyPoints="0;0;1;1" '
        f'keyTimes="0;{i*0.18:.2f};{i*0.18 + 0.14:.2f};1" calcMode="linear"><mpath href="#l{i}"/></animateMotion>'
        f'<animate attributeName="opacity" dur="6s" begin="2.4s" repeatCount="indefinite" values="0;0;.9;0;0" '
        f'keyTimes="0;{i*0.18:.2f};{i*0.18 + 0.04:.2f};{i*0.18 + 0.14:.2f};1"/></circle>'
        for i in range(len(sats))
    )
    head = "".join(
        f'<text class="serif up" x="70" y="{176 + i*66}" font-size="56" letter-spacing="-.8" fill="{t["text"]}" '
        f'style="animation-delay:{0.25 + i*0.18:.2f}s">{escape(line)}</text>'
        for i, line in enumerate(HEADLINE)
    )
    body = f"""  <defs><clipPath id="clip"><rect width="{W}" height="{H}" rx="16"/></clipPath></defs>
  {frame(W, H, t)}
  <g clip-path="url(#clip)">
    {eyebrow(72, 96, EYEBROW, t, 0.1)}
    {head}
    <text class="sans up" x="72" y="292" font-size="16" fill="{t["muted"]}" style="animation-delay:.7s">{escape(SUBLINE)}</text>

    <g>{"".join(lines)}{pulses}
      <circle cx="{hub[0]}" cy="{hub[1]}" r="13" fill="{t["hub"]}" class="up" style="animation-delay:1.2s"/>
      <circle cx="{hub[0]}" cy="{hub[1]}" r="13" fill="none" stroke="{t["hub"]}" class="ring"/>
      {"".join(nodes)}
    </g>

    <line x1="72" y1="338" x2="{W-72}" y2="338" stroke="{t["border"]}" stroke-dasharray="{W-144}" stroke-dashoffset="{W-144}" class="draw" style="animation-delay:.5s"/>
    <text class="sans up" x="72" y="381" font-size="19" font-weight="600" fill="{t["text"]}" style="animation-delay:1s">{escape(NAME)}</text>
    <text class="sans up" x="{W-72}" y="381" font-size="14" text-anchor="end" fill="{t["muted"]}" style="animation-delay:1.1s">{escape(ROLE)}</text>
  </g>"""
    css = f"""
  .ring {{ transform-origin: {hub[0]}px {hub[1]}px; opacity: 0; animation: ring 3.2s 2s ease-out infinite; }}
  @keyframes ring {{ 0% {{ transform: scale(1); opacity: .6 }} 100% {{ transform: scale(2.6); opacity: 0 }} }}"""
    return svg(W, H, f"{NAME} — {' '.join(HEADLINE)}", css, body)


# ──────────────────────────── EXPERIENCE ───────────────────────────

def experience(t):
    W = 1200
    lx, rx = 72, 760
    out, y = [eyebrow(lx, 64, "Experience", t)], 112
    k = 0
    for role, org, when, desc in EXPERIENCE:
        d = 0.15 + k * 0.15
        lines = wrap(desc, 560, 15)
        out.append(
            f'<g class="up" style="animation-delay:{d:.2f}s">'
            f'<circle cx="{lx+5}" cy="{y-6}" r="5" fill="{t["bg"]}" stroke="{t["accent"]}" stroke-width="1.6"/>'
            f'<text class="serif" x="{lx+28}" y="{y}" font-size="22" fill="{t["text"]}">{escape(role)}</text>'
            f'<text class="mono" x="{rx-56}" y="{y-2}" font-size="12.5" text-anchor="end" fill="{t["muted"]}">{escape(when)}</text>'
            f'<text class="sans" x="{lx+28}" y="{y+24}" font-size="14" font-weight="600" fill="{t["text"]}">{escape(org)}</text>'
            + "".join(f'<text class="sans" x="{lx+28}" y="{y+50 + i*22}" font-size="15" fill="{t["muted"]}">{escape(l)}</text>'
                      for i, l in enumerate(lines))
            + "</g>"
        )
        y += 50 + len(lines) * 22 + 34
        k += 1
    left_end = y - 34
    # Timeline spine, drawn in behind the dots.
    spine = left_end - 120
    out.insert(0, f'<line x1="{lx+5}" y1="{106}" x2="{lx+5}" y2="{106 + spine}" stroke="{t["line"]}" stroke-width="1.2" '
                  f'stroke-dasharray="{spine}" stroke-dashoffset="{spine}" class="draw" style="animation-delay:.1s"/>')

    def block(title, rows, y, k):
        out.append(eyebrow(rx, y, title, t, 0.2 + k * 0.1))
        y += 44
        for a, b, when in rows:
            d = 0.3 + k * 0.12
            out.append(
                f'<g class="up" style="animation-delay:{d:.2f}s">'
                f'<text class="serif" x="{rx}" y="{y}" font-size="18" fill="{t["text"]}">{escape(a)}</text>'
                f'<text class="mono" x="{W-72}" y="{y+22}" font-size="12.5" text-anchor="end" fill="{t["muted"]}">{escape(when)}</text>'
                f'<text class="sans" x="{rx}" y="{y+22}" font-size="14" fill="{t["muted"]}">{escape(b)}</text></g>'
            )
            y += 56
            k += 1
        return y, k

    ry, k2 = block("Education", EDUCATION, 64, 0)
    ry, k2 = block("Leadership", LEADERSHIP, ry + 22, k2)
    H = max(left_end, ry) + 30
    divider = f'<line x1="{rx-36}" y1="48" x2="{rx-36}" y2="{H-40}" stroke="{t["border"]}"/>'
    return svg(W, H, "Experience, education and leadership", "", f"  {frame(W, H, t)}\n  {divider}\n  " + "\n  ".join(out))


# ───────────────────────────── CARDS ──────────────────────────────

def card(p, t, idx):
    W, H = 580, 236
    d = (idx % 2) * 0.12
    lines = wrap(p["desc"], 500, 16)[:3]
    desc = "".join(
        f'<text class="sans" x="32" y="{126 + i*23}" font-size="16" fill="{t["muted"]}">{escape(l)}</text>'
        for i, l in enumerate(lines)
    )
    tags = f'<text class="mono" x="32" y="{H-30}" font-size="14" letter-spacing=".2" fill="{t["muted"]}">{escape("  ·  ".join(p["tags"]))}</text>'
    body = f"""  {frame(W, H, t, "card")}
  <line x1="32" y1="0.5" x2="{W-32}" y2="0.5" stroke="{t["accent"]}" stroke-width="2" stroke-dasharray="{W-64}" stroke-dashoffset="{W-64}" class="draw" style="animation-delay:{d + .3:.2f}s"/>
  <g class="up" style="animation-delay:{d:.2f}s">
    <text class="mono" x="32" y="48" font-size="13" letter-spacing="1.4" fill="{t["muted"]}">{escape(p["kicker"].upper())}</text>
    <text class="serif" x="31" y="88" font-size="30" letter-spacing="-.4" fill="{t["text"]}">{escape(p["title"])}</text>
    <g class="arrow"><path d="M{W-50},{52} L{W-34},{36} M{W-46},{36} H{W-34} V{48}" fill="none" stroke="{t["muted"]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></g>
    {desc}
    {tags}
  </g>"""
    css = f"""
  .arrow {{ animation: nudge 4s {1 + idx*0.3:.1f}s ease-in-out infinite; }}
  @keyframes nudge {{ 0%, 80%, 100% {{ transform: none }} 90% {{ transform: translate(3px, -3px) }} }}"""
    return svg(W, H, p["title"], css, body)


# ───────────────────────────── STACK ──────────────────────────────

def stack(t):
    W, lx, col = 1200, 72, 290
    out, y, k = [], 58, 0
    for cat, items in STACK:
        out.append(f'<text class="sans up" x="{lx}" y="{y}" font-size="12" letter-spacing="2.4" fill="{t["muted"]}" '
                   f'style="animation-delay:{k*0.03:.2f}s">{escape(cat.upper())}</text>')
        x = col
        for label in items:
            w = text_w(label, 15) + 30
            out.append(
                f'<g class="up" style="animation-delay:{0.1 + k*0.04:.2f}s">'
                f'<rect x="{x}" y="{y-21}" width="{w:.0f}" height="32" rx="16" fill="{t["card"]}" stroke="{t["border"]}"/>'
                f'<text class="sans" x="{x + w/2:.0f}" y="{y}" font-size="15" text-anchor="middle" fill="{t["text"]}">{escape(label)}</text></g>'
            )
            x += w + 10
            k += 1
        y += 52
    H = y - 6
    return svg(W, H, "Tech stack", "", f"  {frame(W, H, t)}\n  " + "\n  ".join(out))


# ───────────────────────────── CERTS ──────────────────────────────

def cert_card(title, key, when, t):
    """One small certificate, drawn at the origin (CW x CH)."""
    name, mono, _ = ISSUERS[key]
    lines = wrap(title, CW - 48, 17)[:2]
    ms = 11 if len(mono) <= 2 else 9.5
    return (
        f'<rect width="{CW}" height="{CH}" rx="10" fill="{t["card"]}" stroke="{t["border"]}" filter="url(#shadow)"/>'
        f'<rect x="7" y="7" width="{CW-14}" height="{CH-14}" rx="6" fill="none" stroke="{t["border"]}" stroke-opacity=".8"/>'
        f'<text class="mono" x="22" y="34" font-size="9.5" letter-spacing="2.2" fill="{t["muted"]}">CERTIFICATE</text>'
        f'<circle cx="{CW-32}" cy="30" r="13" fill="{t["bg"]}" stroke="{t["border"]}"/>'
        f'<text class="sans" x="{CW-32}" y="{30 + ms*0.36:.1f}" font-size="{ms}" font-weight="700" text-anchor="middle" fill="{t["text"]}">{escape(mono)}</text>'
        + "".join(f'<text class="serif" x="22" y="{70 + j*22}" font-size="17" fill="{t["text"]}">{escape(l)}</text>'
                  for j, l in enumerate(lines))
        + f'<line x1="22" y1="{CH-40}" x2="{CW-22}" y2="{CH-40}" stroke="{t["border"]}"/>'
        f'<text class="sans" x="22" y="{CH-20}" font-size="12.5" fill="{t["muted"]}">{escape(name)}</text>'
        f'<text class="mono" x="{CW-22}" y="{CH-20}" font-size="12" text-anchor="end" fill="{t["muted"]}">{escape(when)}</text>'
    )


CW, CH, CGAP = 236, 150, 18


def certs(t):
    """Two rows of small certificates that pop in, glide back and forth, and take turns zooming."""
    W, H = 1200, 470
    per_row = -(-len(CERTS) // 2)
    row_w = per_row * (CW + CGAP) - CGAP
    travel = row_w - W + 80          # how far a row slides to reveal every card
    rows_y = (112, 112 + CH + 30)
    step = 1.6                        # seconds between spotlight hops
    cycle = step * len(CERTS)
    issuers = list(dict.fromkeys(ISSUERS[c[1]][0] for c in CERTS))

    rows = []
    for r, ry in enumerate(rows_y):
        cards = []
        for j, (title, key, when, *_) in enumerate(CERTS[r * per_row:(r + 1) * per_row]):
            i = r * per_row + j
            # Spotlight alternates rows so it hops around the wall.
            order = j * 2 + r
            cards.append(
                f'<g transform="translate({j * (CW + CGAP)},0)">'
                f'<g class="pop" style="animation-delay:{0.2 + i*0.06:.2f}s">'
                f'<g class="focus" style="animation-delay:{2.2 + order*step:.2f}s">{cert_card(title, key, when, t)}</g></g></g>'
            )
        rows.append(f'<g transform="translate(40,{ry})"><g class="row{r}">{"".join(cards)}</g></g>')

    css = f"""
  .pop {{ opacity: 0; transform-box: fill-box; transform-origin: center; animation: pop .7s cubic-bezier(.2,.9,.25,1.25) forwards; }}
  @keyframes pop {{ from {{ opacity: 0; transform: translateY(14px) scale(.82); }} to {{ opacity: 1; transform: none; }} }}
  .focus {{ transform-box: fill-box; transform-origin: center; animation: focus {cycle:.1f}s ease-in-out infinite; }}
  @keyframes focus {{ 0% {{ transform: none; }}
    {100*0.35/cycle:.2f}%, {100*1.25/cycle:.2f}% {{ transform: translateY(-6px) scale(1.09); }}
    {100*1.6/cycle:.2f}%, 100% {{ transform: none; }} }}
  .row0 {{ animation: slideA 30s 1.2s ease-in-out infinite alternate; }}
  .row1 {{ animation: slideB 30s 1.2s ease-in-out infinite alternate; transform: translateX(-{travel}px); }}
  @keyframes slideA {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-{travel}px); }} }}
  @keyframes slideB {{ from {{ transform: translateX(-{travel}px); }} to {{ transform: translateX(0); }} }}"""
    defs = f"""<defs>
    <clipPath id="clip"><rect width="{W}" height="{H}" rx="16"/></clipPath>
    <linearGradient id="edge" x1="0" x2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".07" stop-color="#fff"/>
      <stop offset=".93" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="fade" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="url(#edge)"/></mask>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="160%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000" flood-opacity="{.35 if t["bg"] != "#ffffff" else .07}"/>
    </filter>
  </defs>"""
    body = f"""  {defs}
  {frame(W, H, t)}
  <text class="serif up" x="40" y="64" font-size="30" fill="{t["text"]}">{len(CERTS)} certificates</text>
  <text class="sans up" x="{W-40}" y="62" font-size="14" text-anchor="end" fill="{t["muted"]}" style="animation-delay:.1s">{escape(" · ".join(issuers))}</text>
  <g clip-path="url(#clip)"><g mask="url(#fade)">
  {"".join(rows)}
  </g></g>"""
    return svg(W, H, f"{len(CERTS)} certificates", css, body)


# ──────────────────────────── ACTIVITY ────────────────────────────

LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}
LEVEL_OP = [0, .3, .55, .8, 1]


def fetch_activity():
    """Contribution calendar via GraphQL. Needs GITHUB_TOKEN or a logged-in gh CLI."""
    import json, os, subprocess, urllib.request

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        try:
            token = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            return None
    query = """query($login: String!) { user(login: $login) {
      repositories(privacy: PUBLIC, ownerAffiliations: OWNER, isFork: false) { totalCount }
      contributionsCollection { contributionCalendar { totalContributions
        weeks { contributionDays { date contributionCount contributionLevel } } } } } }"""
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": {"login": USERNAME}}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-build"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        user = json.load(r)["data"]["user"]
    cal = user["contributionsCollection"]["contributionCalendar"]
    days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    return {"total": cal["totalContributions"], "weeks": cal["weeks"], "days": days,
            "repos": user["repositories"]["totalCount"]}


def streaks(days):
    longest = run = 0
    for d in days:
        run = run + 1 if d["contributionCount"] else 0
        longest = max(longest, run)
    current, tail = 0, list(reversed(days))
    if tail and not tail[0]["contributionCount"]:
        tail = tail[1:]  # today not counted yet
    for d in tail:
        if not d["contributionCount"]:
            break
        current += 1
    return current, longest


def activity(data, t):
    from datetime import date

    W, H = 1200, 250
    cell, gap = 12, 3
    gx, gy = 372, 64
    cur, best = streaks(data["days"])
    stats = [
        (f'{data["total"]:,}', "contributions, last 12 months"),
        (f"{cur} / {best}", "current / longest streak (days)"),
        (str(data["repos"]), "public repositories"),
    ]
    left = "".join(
        f'<g class="up" style="animation-delay:{i*0.12:.2f}s">'
        f'<text class="serif" x="56" y="{82 + i*58}" font-size="30" fill="{t["text"]}">{escape(v)}</text>'
        f'<text class="sans" x="56" y="{102 + i*58}" font-size="13" fill="{t["muted"]}">{escape(k)}</text></g>'
        for i, (v, k) in enumerate(stats)
    )

    def fill(lvl):
        return (f'fill="{t["accent"]}" fill-opacity="{LEVEL_OP[lvl]}"' if lvl else f'fill="{t["empty"]}"')

    cells, months, last_month = [], [], None
    for wi, w in enumerate(data["weeks"]):
        x = gx + wi * (cell + gap)
        first = date.fromisoformat(w["contributionDays"][0]["date"])
        if first.month != last_month and wi < len(data["weeks"]) - 2:
            if last_month is not None or first.day <= 7:
                months.append(f'<text class="mono" x="{x}" y="{gy - 12}" font-size="11" fill="{t["muted"]}">{first.strftime("%b")}</text>')
            last_month = first.month
        for d in w["contributionDays"]:
            wd = (date.fromisoformat(d["date"]).weekday() + 1) % 7  # Sunday = 0
            lvl = LEVELS.get(d["contributionLevel"], 0)
            cells.append(
                f'<rect class="c" x="{x}" y="{gy + wd * (cell + gap)}" width="{cell}" height="{cell}" rx="3" {fill(lvl)} '
                f'style="animation-delay:{0.3 + wi * 0.018:.3f}s"><title>{d["contributionCount"]} on {d["date"]}</title></rect>'
            )
    days_lbl = "".join(
        f'<text class="mono" x="{gx - 10}" y="{gy + i * (cell + gap) + 10}" font-size="10" text-anchor="end" fill="{t["muted"]}">{n}</text>'
        for i, n in ((1, "Mon"), (3, "Wed"), (5, "Fri"))
    )
    lx = gx + len(data["weeks"]) * (cell + gap) - 5 * (cell + gap)
    ly = gy + 7 * (cell + gap) + 14
    legend = "".join(f'<rect x="{lx + i*(cell+gap)}" y="{ly}" width="{cell}" height="{cell}" rx="3" {fill(i)}/>' for i in range(5))
    legend += (f'<text class="mono" x="{lx - 8}" y="{ly + 10}" font-size="11" text-anchor="end" fill="{t["muted"]}">Less</text>'
               f'<text class="mono" x="{lx + 5*(cell+gap) + 4}" y="{ly + 10}" font-size="11" fill="{t["muted"]}">More</text>')

    css = """
  .c { opacity: 0; animation: pop .5s cubic-bezier(.2,.7,.2,1) forwards; transform-box: fill-box; transform-origin: center; }
  @keyframes pop { from { opacity: 0; transform: scale(.4); } to { opacity: 1; transform: none; } }"""
    body = f"""  {frame(W, H, t)}
  <line x1="324" y1="40" x2="324" y2="{H-40}" stroke="{t["border"]}"/>
  {left}
  {"".join(months)}
  {days_lbl}
  {"".join(cells)}
  {legend}"""
    return svg(W, H, f'{data["total"]} contributions in the last year', css, body)


# ───────────────────────────── BUILD ──────────────────────────────

def main():
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.svg"):
        if not old.name.startswith("activity-"):
            old.unlink()
    try:
        data = fetch_activity()
    except Exception as e:  # keep building the rest if the API is unreachable
        print(f"activity skipped: {e}")
        data = None
    for name, t in THEMES.items():
        (OUT / f"header-{name}.svg").write_text(header(t), encoding="utf-8")
        (OUT / f"experience-{name}.svg").write_text(experience(t), encoding="utf-8")
        (OUT / f"stack-{name}.svg").write_text(stack(t), encoding="utf-8")
        (OUT / f"certs-{name}.svg").write_text(certs(t), encoding="utf-8")
        if data:
            (OUT / f"activity-{name}.svg").write_text(activity(data, t), encoding="utf-8")
        for i, p in enumerate(PROJECTS):
            (OUT / f"card-{p['slug']}-{name}.svg").write_text(card(p, t, i), encoding="utf-8")
    # Data for the interactive certificates page.
    import json
    page = Path(__file__).parent / "certificates"
    page.mkdir(exist_ok=True)
    (page / "data.json").write_text(json.dumps([
        {"title": title, "issuer": ISSUERS[key][0], "date": when, "img": f"img/{slug}.jpg", "verify": verify}
        for title, key, when, slug, verify in CERTS
    ], indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(list(OUT.glob('*.svg')))} svgs to {OUT}")


if __name__ == "__main__":
    main()
