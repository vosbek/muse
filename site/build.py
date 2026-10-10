#!/usr/bin/env python3
"""Build the static GitHub Pages site into docs/ from the repo's markdown."""
import os, re, json, shutil, sys, html as htmlmod, datetime
sys.path.insert(0, os.path.expanduser("~/workspace/.pylibs"))
import markdown

REPO = os.path.expanduser("~/workspace/ai-skills-playbook")
OUT = os.path.join(REPO, "docs")
SITE_TITLE = "AI Skills Playbook"
SITE_URL = "https://vosbek.github.io/muse/"

SECTIONS = [
    ("start", "Start here", ["tokenomics-playbook.md", "COMBINED.md", "README.md"]),
    ("talks", "AI Engineer talks", ["ai-engineer-talks"]),
    ("deep-dives", "Deep dives", ["deep-dives"]),
    ("maps", "Storage & memory maps", [
        "08-tools-apis/vscode-storage-memory-map.md",
        "01-claude-code-agents/github-copilot-storage-memory-map.md",
        "03-agent-memory/reddit-claude-storage-memory-map.md",
    ]),
    ("categories", "Categories", ["01-claude-code-agents", "02-jev-context-economics",
        "03-agent-memory", "04-automation", "05-prompts-evals", "06-design-vibe-coding",
        "07-ai-news", "08-tools-apis", "09-learn"]),
    ("resources", "Resources", ["templates", "setups"]),
    ("repos", "GitHub Repos", ["github-repos.md"]),
]

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#141414;--panel:#1c1c1c;--line:#2e2e2e;--txt:#e8e8e8;--mut:#a8a8a8;--dim:#8f8f8f;--grn:#2e9e77;--amb:#d49036}
body{background:var(--bg);color:var(--txt);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.65}
a{color:var(--grn);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:960px;margin:0 auto;padding:0 24px}
header.top{border-bottom:1px solid var(--line);padding:18px 0;position:sticky;top:0;background:rgba(20,20,20,.96);z-index:10}
header.top .wrap{display:flex;align-items:center;gap:26px}
.brand{font-weight:700;font-size:20px;color:#fff;white-space:nowrap}.brand b{color:var(--grn)}
nav.main{display:flex;gap:18px;flex-wrap:wrap;font-size:15px}
nav.main a{color:var(--mut)}nav.main a:hover{color:#fff}
.hero{padding:64px 0 40px;text-align:center}
.hero h1{font-size:44px;color:#fff;letter-spacing:-.5px}.hero h1 .g{color:var(--grn)}.hero h1 .a{color:var(--amb)}
.hero p{color:var(--mut);font-size:18px;max-width:640px;margin:16px auto 0}
.searchbox{margin:28px auto 0;max-width:560px}
.searchbox input{width:100%;padding:14px 18px;font-size:17px;border-radius:10px;border:1px solid var(--line);background:var(--panel);color:var(--txt)}
#results{max-width:560px;margin:8px auto 0;text-align:left}
#results a{display:block;padding:10px 14px;border-bottom:1px solid var(--line);color:var(--txt)}
#results a small{color:var(--dim);display:block}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px;margin:36px 0}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:20px}
.card h3{font-size:18px;color:#fff;margin-bottom:6px}.card p{font-size:14px;color:var(--mut)}
.card .n{font-size:13px;color:var(--amb)}
.card h3 a{color:#fff;text-decoration:none}.card h3 a:hover{color:var(--grn)}
.card-preview{list-style:none;margin:12px 0 0;padding:0}
.card-preview li{font-size:13px;margin:7px 0;line-height:1.35}
.card-preview a{color:var(--mut);text-decoration:none}.card-preview a:hover{color:var(--grn)}
.card .more{margin:12px 0 0;font-size:13px}.card .more a{color:var(--grn);text-decoration:none}
h2.band{font-size:20px;margin:34px 0 4px;color:#fff}h2.band small{font-size:13px;font-weight:normal}
.latest{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px;margin:16px 0 6px}
.latest-item{display:block;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px;text-decoration:none}
.latest-item:hover{border-color:var(--grn)}
.latest-item b{display:block;color:#fff;font-size:14px;margin-bottom:4px;line-height:1.35}
.latest-item span{font-size:12px;color:var(--dim)}
.vstrip{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin:16px 0 6px}
.strip-item{display:block;text-decoration:none}
.strip-item img{width:100%;border-radius:8px;border:1px solid var(--line);aspect-ratio:1;object-fit:cover}
.strip-item span{display:block;font-size:12px;color:var(--dim);margin-top:6px;line-height:1.3}
@media(max-width:640px){.vstrip{grid-template-columns:repeat(2,1fr)}}
h2.sec{font-size:26px;color:#fff;margin:44px 0 6px}h2.sec small{color:var(--dim);font-weight:400;font-size:16px}
ul.idx{list-style:none;margin:12px 0 30px}
ul.idx li{padding:9px 0;border-bottom:1px solid var(--line);font-size:16px}
ul.idx li small{color:var(--dim)}
article.doc{padding:36px 0 60px}
article.doc h1{font-size:34px;color:#fff;margin-bottom:6px}
article.doc h2{font-size:25px;color:#fff;margin:34px 0 10px;padding-top:10px;border-top:1px solid var(--line)}
article.doc h3{font-size:20px;color:#fff;margin:24px 0 8px}
article.doc p{margin:12px 0;color:#d5d5d5}
article.doc ul,article.doc ol{margin:10px 0 10px 26px;color:#d5d5d5}
article.doc li{margin:6px 0}
article.doc table{border-collapse:collapse;width:100%;margin:16px 0;font-size:14px}
article.doc table{display:block;width:max-content;min-width:100%;max-width:100%;overflow-x:auto}
article.doc th,article.doc td{border:1px solid var(--line);padding:8px 10px;text-align:left}
article.doc th{background:var(--panel);color:#fff}
article.doc img{max-width:100%;border-radius:10px;margin:14px 0}
article.doc code{background:#262626;padding:2px 7px;border-radius:6px;font-size:14px}
article.doc pre{background:#1a1a1a;border:1px solid var(--line);border-radius:10px;padding:16px;overflow:auto;margin:14px 0}
article.doc pre.mermaid{background:#141414;text-align:center}
article.doc pre.mermaid svg{max-width:100%;height:auto}
.hero-visual{margin:20px 0;text-align:center}
.hero-visual img{max-width:100%;border-radius:12px;border:1px solid var(--line)}
.hero-visual .mermaid{display:inline-block;max-width:100%}
details.sec{border:1px solid var(--line);border-radius:10px;margin:12px 0;background:#181818}
details.sec summary{cursor:pointer;padding:14px 16px;font-weight:700;font-size:18px;list-style:none}
details.sec summary::-webkit-details-marker{display:none}
details.sec summary::before{content:"▸ ";color:var(--amb)}
details.sec[open] summary::before{content:"▾ "}
details.sec .sec-body{padding:0 16px 14px}
.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:22px;margin-top:18px}
.gallery figure{margin:0}
.gallery img{width:100%;border-radius:12px;border:1px solid var(--line)}
.gallery figcaption{padding:10px 4px;color:var(--mut)}
.gallery figcaption b{color:var(--txt)}
.lede{color:var(--mut);font-size:19px}
article.doc pre code{background:none;padding:0}
article.doc blockquote{border-left:3px solid var(--grn);padding:4px 16px;color:var(--mut);margin:14px 0}
.crumb{font-size:14px;color:var(--dim);margin:26px 0 0}.crumb a{color:var(--dim)}
footer{border-top:1px solid var(--line);padding:26px 0 40px;color:var(--dim);font-size:14px}
footer .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
.badge{display:inline-block;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--dim);margin-bottom:10px}
"""

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · """ + SITE_TITLE + """</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} · """ + SITE_TITLE + """">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="{root}assets/style.css"></head>
<body><header class="top"><div class="wrap"><a class="brand" href="{root}"><b>AI</b> Skills Playbook</a>
<nav class="main">{nav}</nav></div></header><div class="wrap">{body}</div>
<footer><div class="wrap"><span>Distilled from public talks, posts & docs. For learning — verify before deploying.</span><span>ai-skills-playbook</span></div></footer>
<script>var ROOT="{root}";</script><script src="{root}assets/search.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad:true,theme:"dark",securityLevel:"loose"}});</script></body></html>"""

SEARCH_JS = """
(function(){
var box=document.getElementById("q"),res=document.getElementById("results");
if(!box||!res)return;
var IDX=null;
box.addEventListener("input",function(){
  var q=box.value.trim().toLowerCase();
  if(q.length<2){res.innerHTML="";return;}
  function go(){
    var hits=IDX.filter(function(e){return (e.t+" "+e.s+" "+e.x).toLowerCase().indexOf(q)>=0;}).slice(0,12);
    res.innerHTML=hits.map(function(h){return '<a href="'+ROOT+h.u+'">'+h.t+'<small>'+h.s+'</small></a>';}).join("");
  }
  if(IDX){go();}else{fetch(ROOT+"search.json").then(function(r){return r.json();}).then(function(j){IDX=j;go();});}
});
})();
"""


def mermaid_blocks(html):
    """Convert ```mermaid fenced blocks into mermaid render targets."""
    def rep(m):
        code = m.group(1)
        code = code.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
        return '<pre class="mermaid">' + code.strip() + "</pre>"
    return re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>', rep, html, flags=re.S)


OPEN_SECTIONS = {"thesis", "the-mental-model", "decision-framework", "how-to-apply-it"}


def hero_visual(html):
    """Pull the first image or mermaid diagram out to feature at the top of the page."""
    m = re.search(r'<p><img[^>]*></p>|<pre class="mermaid">.*?</pre>', html, re.S)
    if not m:
        return "", html
    return f'<div class="hero-visual">{m.group(0)}</div>', html[:m.start()] + html[m.end():]


def collapsible_sections(html):
    """Keep lead sections open; wrap the rest in <details> so long pages aren't walls of text."""
    parts = re.split(r'(?=<h2 )', html)
    out = [parts[0]]
    for part in parts[1:]:
        m = re.match(r'<h2 id="([^"]+)">', part)
        sid = m.group(1) if m else ""
        h2end = part.find("</h2>") + len("</h2>")
        if h2end <= len("</h2>") - 1:
            out.append(part)
            continue
        title = re.sub(r"<[^>]+>", "", part[:h2end]).strip()
        content = part[h2end:]
        if sid in OPEN_SECTIONS:
            out.append(part)
        else:
            out.append(f'<details class="sec"><summary>{title}</summary><div class="sec-body">{content}</div></details>')
    return "".join(out)


def rewrite_md_links(html, rel, page_rels):
    """Rewrite relative .md links to their generated page URLs (relative)."""
    curdir = os.path.dirname(out_url(rel))  # e.g. p/deep-dives

    def rep(m):
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        path, anchor = (href.split("#", 1) + [""])[:2]
        anchor = "#" + anchor if anchor else ""
        target = os.path.normpath(os.path.join(os.path.dirname(rel), path))
        if path.endswith(".md"):
            cands = [target]
        elif path.endswith("/"):
            # directory link -> that dir's README page
            cands = [os.path.join(target, "README.md")]
        else:
            return m.group(0)
        for prel in page_rels:
            if prel in cands or prel.lower() in [c.lower() for c in cands]:
                new = os.path.relpath(out_url(prel), curdir) + anchor
                return 'href="' + new + '"'
        return m.group(0)

    return re.sub(r'href="([^"]+)"', rep, html)


def title_of(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    base = os.path.basename(path)
    if base.lower() == "readme.md":
        base = os.path.basename(os.path.dirname(path))
    base = re.sub(r"\.md$", "", base).replace("-", " ").replace("_", " ")
    return base.title()


def collect():
    pages = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "docs", "site", ".pylibs")]
        for fn in files:
            if fn.endswith(".md"):
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, REPO)
                pages.append((rel, full))
    return sorted(pages)


def section_of(rel):
    for sid, sname, members in SECTIONS:
        for m in members:
            if rel == m or rel.startswith(m.rstrip("/") + "/"):
                return sid, sname
    return "categories", "Categories"


def out_url(rel):
    if rel == "README.md":
        return "p/about/"
    noext = rel[:-3]
    if os.path.basename(noext).lower() == "readme":
        noext = os.path.dirname(noext)
    return "p/" + noext + "/"


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT + "/assets")
    with open(OUT + "/assets/style.css", "w") as f:
        f.write(CSS)
    with open(OUT + "/assets/search.js", "w") as f:
        f.write(SEARCH_JS)

    pages = collect()
    page_rels = [rel for rel, _ in pages]
    # nav is built per-page with correct relative root; placeholder replaced in TEMPLATE loop
    nav_tpl = "".join('<a href="{root}#' + sid + '">' + sname + "</a>" for sid, sname, _ in SECTIONS)

    # copy only images actually referenced by each page
    for rel, full in pages:
        with open(full, encoding="utf-8") as f:
            src = f.read()
        refs = set(re.findall(r"!\[[^\]]*\]\(([^)]+)\)", src))
        # also catch raw-HTML <img> tags (e.g. gallery grids in READMEs)
        refs |= set(re.findall(r'<img\s+[^>]*src="([^"]+)"', src))
        # and image files linked (not embedded) cross-folder, e.g. [infographic](../02-.../x.jpg)
        refs |= set(r for r in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", src)
                    if r.lower().split("?")[0].split("#")[0].endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg")))
        # also copy linked PDFs (e.g. hosted whitepapers)
        refs |= set(r for r in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", src) if r.lower().endswith(".pdf"))
        destdir = os.path.join(OUT, out_url(rel))
        os.makedirs(destdir, exist_ok=True)
        srcdir = os.path.dirname(full)
        for ref in refs:
            if ref.startswith(("http://", "https://", "data:")):
                continue
            imgpath = os.path.normpath(os.path.join(srcdir, ref))
            if os.path.isfile(imgpath):
                dest = os.path.join(destdir, os.path.normpath(ref))
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy(imgpath, dest)

    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    index = []
    rendered = {}
    for rel, full in pages:
        with open(full, encoding="utf-8") as f:
            src = f.read()
        # strip provenance bold lines? keep as-is
        html = md.convert(src)
        md.reset()
        html = rewrite_md_links(html, rel, page_rels)
        html = re.sub(r'<img (?![^>]*loading=)', '<img loading="lazy" ', html)
        html = mermaid_blocks(html)
        hero, html = hero_visual(html)
        html = collapsible_sections(html)
        title = title_of(full)
        sid, sname = section_of(rel)
        url = out_url(rel)
        # fix root-relative asset paths for depth
        depth = url.count("/")
        root = "../" * depth
        crumb = f"<div class='crumb'><a href='{root}'>Home</a> · <a href='{root}#{sid}'>{sname}</a></div>"
        inner = hero + html
        if not src.lstrip().startswith("#"):
            inner = f"<h1>{title}</h1>" + inner
        body = crumb + f"<article class='doc'><div class='badge'>{sname}</div>" + inner + "</article>"
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text).strip()
        desc = htmlmod.escape(text[:157].rsplit(" ", 1)[0] + "…" if len(text) > 160 else text)
        page = TEMPLATE.format(title=title, root=root, nav=nav_tpl.format(root=root), body=body, desc=desc)
        dest = os.path.join(OUT, url, "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(page)
        index.append({"t": title, "s": sname, "u": url, "x": text[:600]})
        rendered[rel] = (title, sid, sname, url)

    build_visual_index(nav_tpl, index, rendered)

    with open(OUT + "/search.json", "w") as f:
        json.dump(index, f)

    # home page
    def rel_date(ts):
        days = (datetime.date.today() - datetime.date.fromtimestamp(ts)).days
        if days <= 0:
            return "today"
        if days == 1:
            return "yesterday"
        if days < 14:
            return f"{days} days ago"
        return datetime.date.fromtimestamp(ts).strftime("%b %-d")

    # recency per page from source-file mtime (section READMEs get touched on every new entry)
    page_meta = []  # (mtime, rel, title, sid, sname, url)
    for rel, (t, s, sn, u) in rendered.items():
        try:
            mt = os.path.getmtime(os.path.join(REPO, rel))
        except OSError:
            mt = 0
        page_meta.append((mt, rel, t, s, sn, u))
    page_meta.sort(reverse=True)

    # "latest additions" band: 6 freshest pages across the site
    latest = "".join(
        f"<a class='latest-item' href='{u}'><b>{htmlmod.escape(t)}</b>"
        f"<span>{sn} · {rel_date(mt)}</span></a>"
        for mt, rel, t, s, sn, u in page_meta[:6])

    # section cards: each links to its index and previews its 3 freshest entries
    cards = ""
    sec_lists = ""
    for sid, sname, members in SECTIONS:
        items = [(mt, t, u) for mt, rel, t, s, sn, u in page_meta if s == sid]
        items.sort(reverse=True)
        preview = "".join(
            f"<li><a href='{u}'>{htmlmod.escape(t)}</a></li>" for mt, t, u in items[:3])
        cards += (f"<div class='card'><h3><a href='#{sid}'>{sname}</a></h3>"
                  f"<p class='n'>{len(items)} pages</p><p>{blurb(sid)}</p>"
                  f"<ul class='card-preview'>{preview}</ul>"
                  f"<p class='more'><a href='#{sid}'>All {len(items)} pages →</a></p></div>")
        full = sorted([(t, u) for _, t, u in items],
                      key=lambda x: (0 if "readme" in x[1].lower() or x[1].endswith("/ai-engineer-talks/") else 1, x[0]))
        lis = "".join(f"<li><a href='{u}'>{htmlmod.escape(t)}</a></li>" for t, u in full)
        sec_lists += f"<h2 class='sec' id='{sid}'>{sname} <small>{len(items)}</small></h2><ul class='idx'>{lis}</ul>"

    # visual strip: infographics from the freshest pages, one per section, max 6
    groups = scan_figures(rendered)
    strip = ""
    for mt, rel, t, s, sn, u in page_meta:
        if strip.count("strip-item") >= 6:
            break
        figs = groups.get(s)
        if not figs:
            continue
        rel_src, page_href, alt, ptitle = figs.pop(0)
        # scan_figures paths are relative to p/visual-index/; homepage sits at root
        strip += (f"<a class='strip-item' href='p/{page_href[3:]}'>"
                  f"<img src='p/{rel_src[3:]}' alt='{htmlmod.escape(alt)}' loading='lazy'>"
                  f"<span>{htmlmod.escape(alt)}</span></a>")

    hero = """<div class="hero"><h1><span class="g">AI</span> Skills <span class="a">Playbook</span></h1>
<p>Distilled talks, posts and docs on AI engineering — agents, context economics, memory, evals and tooling. Every entry keeps its thesis, key points and sources.</p>
<div class="searchbox"><input id="q" placeholder="Search the playbook…"></div><div id="results"></div></div>
<h2 class="band">Latest additions</h2><div class="latest">""" + latest + """</div>
<h2 class="band">Browse by section</h2>
<div class="cards">""" + cards + """</div>
<h2 class="band">From the visual index <small><a href="p/visual-index/">all →</a></small></h2>
<div class="vstrip">""" + strip + """</div>
<h2 class="band">Full index</h2>""" + sec_lists
    home_desc = "Distilled talks, posts and docs on AI engineering — agents, context economics, memory, evals and tooling. Every entry keeps its thesis, key points and sources."
    home = TEMPLATE.format(title="Home", root="", nav=nav_tpl.format(root=""), body=hero, desc=home_desc)
    with open(OUT + "/index.html", "w") as f:
        f.write(home)

    # sitemap.xml for crawlers
    urls = [SITE_URL] + [SITE_URL + e["u"] for e in index] + [SITE_URL + "p/visual-index/"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{htmlmod.escape(u)}</loc></url>")
    sm.append("</urlset>")
    with open(OUT + "/sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(sm))
    # search.js needs ROOT var per depth; patch: use relative fetch
    print(f"built {len(pages)} pages -> {OUT}")


def scan_figures(rendered):
    """Scan built pages for <img> tags; return {sid: [(rel_src, page_href, alt, title)]}.

    Paths are relative to p/visual-index/ (the gallery page). Shared by the
    visual-index page and the homepage strip so both stay in sync.
    """
    # rendered: rel -> (title, sid, sname, url); url looks like "p/02-jev-context-economics/"
    groups = {}
    for rel, (title, sid, sname, url) in rendered.items():
        page_file = os.path.join(OUT, url, "index.html")
        if not os.path.isfile(page_file):
            continue
        with open(page_file, encoding="utf-8") as f:
            phtml = f.read()
        seen = set()
        for m in re.finditer(r'<img\s+[^>]*src="([^"]+)"[^>]*>', phtml):
            src = m.group(1)
            if src.startswith(("http://", "https://", "data:")):
                continue
            if (url, src) in seen:
                continue
            seen.add((url, src))
            altm = re.search(r'alt="([^"]*)"', m.group(0))
            alt = (altm.group(1) if altm else "").strip()
            # generic alt text -> fall back to the page title for a useful caption
            if not alt or alt.lower() in ("visual one-pager", "image", "img", "picture", "photo"):
                alt = title
            # visual-index lives at p/visual-index/; images are relative to their page
            rel_src = "../" + url[len("p/"):] + src
            page_href = "../" + url[len("p/"):]
            groups.setdefault(sid, []).append((rel_src, page_href, alt, title))
    return groups


def build_visual_index(nav_tpl, index, rendered):
    """Gallery page: every infographic across the playbook, each linking to its page.

    Auto-generated by scanning the built pages for <img> tags, so it never goes
    stale when new infographics are added. Grouped by section, in SECTIONS order.
    """
    groups = scan_figures(rendered)
    sid_order = [sid for sid, _, _ in SECTIONS]
    destdir = os.path.join(OUT, "p", "visual-index")
    os.makedirs(destdir, exist_ok=True)
    body_parts = []
    total = 0
    for sid in sid_order:
        items = groups.get(sid)
        if not items:
            continue
        sname = next(s for i, s, _ in SECTIONS if i == sid)
        figs = ""
        for rel_src, page_href, alt, ptitle in items:
            total += 1
            figs += (f"<figure><a href='{page_href}'>"
                     f"<img src='{rel_src}' alt='{alt}' loading='lazy'></a>"
                     f"<figcaption><b>{alt}</b><br><span>{ptitle}</span></figcaption></figure>")
        body_parts.append(f"<h2 class='sec'>{sname} <small>{len(items)}</small></h2>"
                          f"<div class='gallery'>{figs}</div>")
    body = (f"<div class='crumb'><a href='../../'>Home</a></div>"
            f"<article class='doc'><div class='badge'>Visual index</div>"
            f"<h1>Visual index</h1>"
            f"<p class='lede'>Every infographic in the playbook ({total}), full-size. "
            f"Tap one to open its page.</p>"
            + "".join(body_parts) + "</article>")
    page = TEMPLATE.format(title="Visual index", root="../../",
                           nav=nav_tpl.format(root="../../"), body=body,
                           desc="Every infographic in the AI Skills Playbook, full-size. Browse all diagrams and result cards by section.")
    with open(os.path.join(destdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    index.append({"t": "Visual index", "s": "Galleries",
                  "u": "p/visual-index/", "x": "all infographics visual gallery"})


def blurb(sid):
    return {
        "start": "The fastest on-ramp: tokenomics, cross-item patterns, and what this collection is.",
        "talks": "37 talks from the AI Engineer World's Fair 2026, each distilled with a tokenomics angle.",
        "deep-dives": "Long-form dossiers with mechanisms, numbers and local-deploy steps.",
        "maps": "What's local vs cloud, in the bensimon.dev visual language.",
        "categories": "Distilled Instagram reels and X bookmarks, organized by topic.",
        "resources": "Reusable templates and project setups.",
        "repos": "36 open-source repos scored /10 on his tokenomics remit — routing, RAG, memory, evals.",
    }.get(sid, "")


if __name__ == "__main__":
    main()
