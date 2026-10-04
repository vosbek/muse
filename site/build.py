#!/usr/bin/env python3
"""Build the static GitHub Pages site into docs/ from the repo's markdown."""
import os, re, json, shutil, sys
sys.path.insert(0, os.path.expanduser("~/workspace/.pylibs"))
import markdown

REPO = os.path.expanduser("~/workspace/ai-skills-playbook")
OUT = os.path.join(REPO, "docs")
SITE_TITLE = "AI Skills Playbook"

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
article.doc th,article.doc td{border:1px solid var(--line);padding:8px 10px;text-align:left}
article.doc th{background:var(--panel);color:#fff}
article.doc img{max-width:100%;border-radius:10px;margin:14px 0}
article.doc code{background:#262626;padding:2px 7px;border-radius:6px;font-size:14px}
article.doc pre{background:#1a1a1a;border:1px solid var(--line);border-radius:10px;padding:16px;overflow:auto;margin:14px 0}
article.doc pre.mermaid{background:#141414;text-align:center}
article.doc pre.mermaid svg{max-width:100%;height:auto}
article.doc pre code{background:none;padding:0}
article.doc blockquote{border-left:3px solid var(--grn);padding:4px 16px;color:var(--mut);margin:14px 0}
.crumb{font-size:14px;color:var(--dim);margin:26px 0 0}.crumb a{color:var(--dim)}
footer{border-top:1px solid var(--line);padding:26px 0 40px;color:var(--dim);font-size:14px}
footer .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
.badge{display:inline-block;font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--dim);margin-bottom:10px}
"""

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · """ + SITE_TITLE + """</title><link rel="stylesheet" href="{root}assets/style.css"></head>
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
        html = mermaid_blocks(html)
        title = title_of(full)
        sid, sname = section_of(rel)
        url = out_url(rel)
        # fix root-relative asset paths for depth
        depth = url.count("/")
        root = "../" * depth
        crumb = f"<div class='crumb'><a href='{root}'>Home</a> · <a href='{root}#{sid}'>{sname}</a></div>"
        inner = html
        if not src.lstrip().startswith("#"):
            inner = f"<h1>{title}</h1>" + inner
        body = crumb + f"<article class='doc'><div class='badge'>{sname}</div>" + inner + "</article>"
        page = TEMPLATE.format(title=title, root=root, nav=nav_tpl.format(root=root), body=body)
        dest = os.path.join(OUT, url, "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(page)
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text)[:600]
        index.append({"t": title, "s": sname, "u": url, "x": text})
        rendered[rel] = (title, sid, sname, url)

    with open(OUT + "/search.json", "w") as f:
        json.dump(index, f)

    # home page
    cards = ""
    sec_lists = ""
    for sid, sname, members in SECTIONS:
        items = [(t, u) for rel, (t, s, sn, u) in rendered.items() if s == sid]
        # order: keep repo order (sorted), but put section index first
        items.sort(key=lambda x: (0 if "readme" in x[1].lower() or x[1].endswith("/ai-engineer-talks/") else 1, x[0]))
        cards += f"<div class='card'><h3>{sname}</h3><p class='n'>{len(items)} pages</p><p>{blurb(sid)}</p></div>"
        lis = "".join(f"<li><a href='{u}'>{t}</a></li>" for t, u in items)
        sec_lists += f"<h2 class='sec' id='{sid}'>{sname} <small>{len(items)}</small></h2><ul class='idx'>{lis}</ul>"

    hero = """<div class="hero"><h1><span class="g">AI</span> Skills <span class="a">Playbook</span></h1>
<p>Distilled talks, posts and docs on AI engineering — agents, context economics, memory, evals and tooling. Every entry keeps its thesis, key points and sources.</p>
<div class="searchbox"><input id="q" placeholder="Search the playbook…"></div><div id="results"></div></div>
<div class="cards">""" + cards + "</div>" + sec_lists
    home = TEMPLATE.format(title="Home", root="", nav=nav_tpl.format(root=""), body=hero)
    with open(OUT + "/index.html", "w") as f:
        f.write(home)
    # search.js needs ROOT var per depth; patch: use relative fetch
    print(f"built {len(pages)} pages -> {OUT}")


def blurb(sid):
    return {
        "start": "The fastest on-ramp: tokenomics, cross-item patterns, and what this collection is.",
        "talks": "37 talks from the AI Engineer World's Fair 2026, each distilled with a tokenomics angle.",
        "deep-dives": "Long-form dossiers with mechanisms, numbers and local-deploy steps.",
        "maps": "What's local vs cloud, in the bensimon.dev visual language.",
        "categories": "Distilled Instagram reels and X bookmarks, organized by topic.",
        "resources": "Reusable templates and project setups.",
    }.get(sid, "")


if __name__ == "__main__":
    main()
