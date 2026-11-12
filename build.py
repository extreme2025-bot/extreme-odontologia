# -*- coding: utf-8 -*-
"""Gera o site estático da Extreme Odontologia em ./site"""
import os, html, json, datetime, shutil

SITE_URL = os.environ.get("SITE_URL", "https://www.extremeodonto.com.br")
CRO_PJ = os.environ.get("CRO_PJ", "").strip()  # ex.: "CRO-MT-CLM-1234" (inserir quando o Rafael confirmar)
WHATS = "5566996641307"
WHATS_FMT = "(66) 99664-1307"
IG = "https://www.instagram.com/extreme_odontologia/"
ADDR = "Rua dos Cedros, 478 – Sala 05 – Jardim Botânico"
CITY = "Sinop – MT, 78556-046"
MAPS_Q = "Rua dos Cedros, 478 - Jardim Botânico, Sinop - MT, 78556-046"
PROMO_END = "31/12/2026"
TODAY = datetime.date.today().isoformat()

def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WHATS}?text={quote(msg)}"

WA_DEFAULT = wa("Olá! Vim pelo site da Extreme Odontologia e quero agendar uma avaliação.")
WA_PROMO = wa("Olá! Vim pelo site e quero agendar minha primeira visita com o presente de fim de ano (10% em limpeza, clareamento ou canal).")

OUT = os.path.join(os.path.dirname(__file__), "site")

CSS = r"""
:root{
  --g900:#17261e; --g800:#1f3328; --g700:#2f4135; --g600:#3b5346;
  --gold:#c9a35b; --gold2:#e3cb8f; --gold3:#f1e2b8; --gold-ink:#2a2008;
  --ivory:#f6f1e7; --sand:#ece4d4; --line:#d9cfbc; --ink:#17201b; --muted:#66706a;
  --serif:"Cormorant Garamond","Times New Roman",serif; --sans:"Inter","Segoe UI",system-ui,sans-serif;
  --r:18px; --max:1180px;
}
*{box-sizing:border-box} html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--ivory);color:var(--ink);font-family:var(--sans);font-size:17px;line-height:1.6}
img{max-width:100%;display:block} a{color:inherit}
.wrap{max-width:var(--max);margin:0 auto;padding:0 22px}
h1,h2,h3{font-family:var(--serif);font-weight:600;line-height:1.12;margin:0 0 .4em;letter-spacing:.005em}
h1{font-size:clamp(40px,6vw,66px)} h2{font-size:clamp(32px,4.2vw,46px)} h3{font-size:26px}
p{margin:0 0 1em} .lead{font-size:20px;color:#2b3630}
.eyebrow{font-family:var(--sans);font-size:12.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:600;margin-bottom:14px}
.btn{display:inline-flex;align-items:center;gap:10px;padding:15px 24px;border-radius:999px;font-weight:600;text-decoration:none;font-size:16px;transition:.18s;border:1px solid transparent}
.btn-gold{background:var(--gold);color:var(--gold-ink)} .btn-gold:hover{background:var(--gold2)}
.btn-ghost{border-color:rgba(255,255,255,.35);color:#fff} .btn-ghost:hover{border-color:var(--gold2);color:var(--gold3)}
.btn-dark{background:var(--g800);color:#fff} .btn-dark:hover{background:var(--g700)}
.btn-line{border-color:var(--g800);color:var(--g800)} .btn-line:hover{background:var(--g800);color:#fff}
.ico{width:20px;height:20px;flex:none}
/* header */
.top{position:sticky;top:0;z-index:50;background:rgba(23,38,30,.92);backdrop-filter:blur(10px);color:#fff;border-bottom:1px solid rgba(201,163,91,.25)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;height:74px;gap:18px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:#fff}
.brand img{width:44px;height:44px;border-radius:50%} .brand b{font-family:var(--serif);font-weight:600;font-size:21px;letter-spacing:.14em}
.brand small{display:block;font-size:10px;letter-spacing:.3em;color:var(--gold2);font-weight:600;margin-top:-2px}
nav.menu{display:flex;gap:26px;font-size:15px} nav.menu a{text-decoration:none;color:#e8e3d8;padding:6px 0;border-bottom:1px solid transparent} nav.menu a:hover,nav.menu a[aria-current]{border-color:var(--gold);color:#fff}
.top .btn{padding:11px 18px;font-size:14.5px}
.burger{display:none;background:none;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:10px;padding:8px 10px}
@media(max-width:900px){nav.menu{display:none} .top .btn span{display:none} .top .btn{padding:11px 13px} .burger{display:block}
 nav.menu.open{display:flex;position:absolute;left:0;right:0;top:74px;background:var(--g900);flex-direction:column;padding:16px 22px 22px;gap:14px;border-bottom:1px solid rgba(201,163,91,.3)}}
/* hero */
.hero{background:radial-gradient(1200px 600px at 80% -10%,#2b4a3b 0%,var(--g900) 55%);color:#fff;padding:72px 0 64px;position:relative;overflow:hidden}
.hero .grid{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}
.hero h1{color:#fff} .hero h1 em{font-style:italic;color:var(--gold2)}
.hero .lead{color:#d7d2c6}
.hero .cta{display:flex;gap:14px;flex-wrap:wrap;margin:26px 0 22px}
.hero .trust{display:flex;gap:22px;flex-wrap:wrap;color:#cfc9bb;font-size:14px}
.hero .trust span{display:flex;align-items:center;gap:8px}
.hero .photo{position:relative} .hero .photo img{border-radius:28px;box-shadow:0 30px 60px rgba(0,0,0,.45);aspect-ratio:4/5;object-fit:cover;width:100%}
.hero .photo::before{content:"";position:absolute;inset:-14px;border:1px solid rgba(201,163,91,.45);border-radius:36px;pointer-events:none}
.hero .tag{position:absolute;left:-10px;bottom:28px;background:var(--ivory);color:var(--ink);padding:14px 18px;border-radius:14px;box-shadow:0 20px 40px rgba(0,0,0,.35);font-size:14px;max-width:260px}
.hero .tag b{display:block;font-family:var(--serif);font-size:19px;color:var(--g800)}
@media(max-width:900px){.hero{padding:48px 0 40px}.hero .grid{grid-template-columns:1fr;gap:34px}.hero .photo{max-width:420px;margin:0 auto}.hero .tag{left:10px}}
/* promo band */
.promo{background:linear-gradient(90deg,var(--gold) 0%,var(--gold2) 100%);color:var(--gold-ink)}
.promo .wrap{display:grid;grid-template-columns:auto 1fr auto;gap:28px;align-items:center;padding:26px 22px}
.promo .k{font-size:12px;letter-spacing:.22em;text-transform:uppercase;font-weight:700}
.promo h2{font-size:30px;margin:2px 0 4px}
.promo p{margin:0;font-size:15px;max-width:720px}
.promo .btn{background:var(--g900);color:#fff}
@media(max-width:900px){.promo .wrap{grid-template-columns:1fr;gap:14px}}
/* sections */
section{padding:84px 0} section.tight{padding:56px 0}
.sec-head{max-width:760px;margin-bottom:44px} .center{text-align:center;margin-left:auto;margin-right:auto}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:30px 28px;transition:.2s;display:flex;flex-direction:column}
.card:hover{transform:translateY(-3px);box-shadow:0 20px 40px rgba(23,38,30,.12);border-color:var(--gold)}
.card h3{margin-top:14px} .card p{color:#3d4742;font-size:16px;flex:1}
.card .more{color:var(--g800);font-weight:600;text-decoration:none;display:inline-flex;gap:8px;align-items:center}
.card .num{font-family:var(--serif);font-size:15px;letter-spacing:.2em;color:var(--gold)}
.card .glyph{width:52px;height:52px;border-radius:14px;background:var(--g800);display:grid;place-items:center;color:var(--gold2)}
@media(max-width:900px){.cards{grid-template-columns:1fr}}
.dark{background:var(--g900);color:#fff} .dark h2,.dark h3{color:#fff} .dark p{color:#d3cfc4}
.dark .card{background:rgba(255,255,255,.04);border-color:rgba(201,163,91,.25)} .dark .card p{color:#cfcabf} .dark .card .more{color:var(--gold2)}
.split{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.split img{border-radius:24px;box-shadow:0 26px 50px rgba(23,38,30,.22)}
@media(max-width:900px){.split{grid-template-columns:1fr;gap:28px}}
.list{list-style:none;padding:0;margin:0 0 20px} .list li{padding:12px 0 12px 34px;position:relative;border-bottom:1px solid var(--line)}
.list li::before{content:"";position:absolute;left:0;top:19px;width:18px;height:18px;border-radius:50%;background:var(--gold);mask:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path fill='black' d='M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z'/></svg>") center/contain no-repeat}
.dark .list li{border-color:rgba(255,255,255,.12)}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;counter-reset:s}
.step{padding:26px 22px;border:1px solid var(--line);border-radius:var(--r);background:#fff}
.step::before{counter-increment:s;content:"0" counter(s);font-family:var(--serif);font-size:34px;color:var(--gold);display:block;line-height:1;margin-bottom:12px}
.step h3{font-size:21px} .step p{font-size:15px;color:#3d4742;margin:0}
@media(max-width:900px){.steps{grid-template-columns:1fr 1fr}} @media(max-width:560px){.steps{grid-template-columns:1fr}}
.ig{display:grid;grid-template-columns:repeat(3,1fr);gap:18px} .ig iframe{width:100%;height:560px;border:0;border-radius:16px;background:#fff}
@media(max-width:900px){.ig{grid-template-columns:1fr}}
.faq details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:4px 22px;margin-bottom:12px}
.faq summary{cursor:pointer;font-family:var(--serif);font-size:22px;font-weight:600;padding:14px 0;list-style:none;display:flex;justify-content:space-between;gap:16px;align-items:center}
.faq summary::after{content:"+";font-size:28px;color:var(--gold);font-weight:300} .faq details[open] summary::after{content:"–"}
.faq details p{color:#3d4742;padding-bottom:12px;margin:0}
.cta-final{background:var(--g800);color:#fff;border-radius:28px;padding:58px 48px;display:grid;grid-template-columns:1.3fr 1fr;gap:30px;align-items:center;position:relative;overflow:hidden}
.cta-final::after{content:"";position:absolute;right:-120px;top:-120px;width:380px;height:380px;border-radius:50%;border:1px solid rgba(201,163,91,.35)}
.cta-final h2{color:#fff} .cta-final p{color:#d3cfc4}
.cta-final .acts{display:flex;flex-direction:column;gap:12px;align-items:flex-start}
@media(max-width:900px){.cta-final{grid-template-columns:1fr;padding:38px 26px}}
/* article */
.article{max-width:760px;margin:0 auto} .article h2{font-size:32px;margin-top:40px} .article p,.article li{font-size:18px;color:#2b3630}
.article .meta{color:var(--muted);font-size:14px;margin-bottom:28px} .article blockquote{border-left:3px solid var(--gold);margin:28px 0;padding:6px 22px;font-family:var(--serif);font-size:24px;color:var(--g800)}
.note{background:var(--sand);border-radius:14px;padding:18px 22px;font-size:15px;color:#3d4742}
.crumbs{font-size:14px;color:var(--muted);margin-bottom:22px} .crumbs a{color:var(--muted);text-decoration:none} .crumbs a:hover{color:var(--g800)}
.page-head{background:var(--g900);color:#fff;padding:64px 0 54px} .page-head h1{color:#fff;font-size:clamp(36px,5vw,56px)} .page-head p{color:#d3cfc4;font-size:19px;max-width:720px;margin:0}
.info{display:grid;grid-template-columns:1fr 1fr;gap:40px} .info .box{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:30px}
.info .box h3{font-size:22px} .info dl{margin:0} .info dt{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:16px} .info dd{margin:4px 0 0;font-size:17px}
.map{border:0;width:100%;height:420px;border-radius:var(--r)}
@media(max-width:900px){.info{grid-template-columns:1fr}}
/* footer */
footer{background:#10190f;color:#cfcabf;padding:56px 0 30px;font-size:14.5px}
footer .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:34px;margin-bottom:34px} footer h4{color:#fff;font-family:var(--serif);font-size:20px;margin:0 0 12px}
footer a{color:#e6e1d6;text-decoration:none} footer a:hover{color:var(--gold2)} footer ul{list-style:none;padding:0;margin:0} footer li{margin:7px 0}
footer .legal{border-top:1px solid rgba(255,255,255,.12);padding-top:22px;font-size:13px;color:#a7a397;line-height:1.7}
footer .legal b{color:#e6e1d6;font-weight:600}
@media(max-width:900px){footer .cols{grid-template-columns:1fr}}
.fab{position:fixed;right:18px;bottom:18px;z-index:60;display:flex;align-items:center;gap:10px;background:#25d366;color:#0b2d19;font-weight:700;padding:13px 18px;border-radius:999px;text-decoration:none;box-shadow:0 14px 30px rgba(0,0,0,.25);font-size:15px}
.fab svg{width:22px;height:22px} @media(max-width:560px){.fab span{display:none}.fab{padding:14px}}
.pill{display:inline-block;background:rgba(201,163,91,.15);color:var(--g800);border:1px solid rgba(201,163,91,.5);border-radius:999px;padding:5px 12px;font-size:12.5px;font-weight:600;letter-spacing:.06em}
.dark .pill{color:var(--gold2)}
.small{font-size:13.5px;color:var(--muted)}
"""

WA_SVG = '<svg class="ico" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c.6.3 1.1.4 1.5.5a3.6 3.6 0 0 0 1.7.1c.5-.1 1.5-.6 1.7-1.2s.2-1.1.2-1.2-.3-.2-.5-.3Z"/></svg>'
PIN_SVG = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.6"/></svg>'
CLOCK_SVG = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
STAR_SVG = '<svg class="ico" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2 3 6.6 7 .8-5.2 4.8 1.4 7L12 17.6 5.8 21.2l1.4-7L2 9.4l7-.8z"/></svg>'
ARROW = '<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

NAV = [("tratamentos/", "Tratamentos"), ("duvidas.html", "Dúvidas"), ("artigos/", "Artigos"), ("contato.html", "Contato")]

# Tag do Google (Google Ads): mede clique no WhatsApp como conversao; personalizacao de anuncios desligada.
GADS_ID = "AW-10880997164"
GADS_WHATS_LABEL = "_hWmCJPtq7cdEKyuu8Qo"
GTAG = f"""<!-- Google tag (gtag.js): mede cliques no WhatsApp vindos de anuncios do Google Ads; sem publicidade personalizada -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GADS_ID}"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('set','allow_ad_personalization_signals',false);gtag('js',new Date());gtag('config','{GADS_ID}');
document.addEventListener('click',function(e){{var a=e.target&&e.target.closest?e.target.closest('a[href*="wa.me/"],a[href*="api.whatsapp.com"]'):null;if(!a)return;gtag('event','conversion',{{'send_to':'{GADS_ID}/{GADS_WHATS_LABEL}','value':1.0,'currency':'BRL','transport_type':'beacon'}});}},true);
</script>"""

def head(title, desc, root, path, extra_ld=None, ogimg="img/hero.jpg"):
    canonical = f"{SITE_URL}/{path}".rstrip("/") + ("/" if path.endswith("/") or path == "" else "")
    if path == "": canonical = SITE_URL + "/"
    ld = [{
        "@context": "https://schema.org", "@type": "Dentist", "@id": SITE_URL + "/#clinica",
        "name": "Extreme Odontologia", "legalName": "Extreme Odontologia Ltda", "url": SITE_URL + "/",
        "image": f"{SITE_URL}/img/dra-luana.jpg", "logo": f"{SITE_URL}/img/logo.png",
        "telephone": "+55 66 99664-1307", "priceRange": "$$",
        "address": {"@type": "PostalAddress", "streetAddress": "Rua dos Cedros, 478, Sala 05", "addressLocality": "Sinop", "addressRegion": "MT", "postalCode": "78556-046", "addressCountry": "BR"},
        "geo": {"@type": "GeoCoordinates", "latitude": -11.8673913, "longitude": -55.5075806},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "18:00"}],
        "sameAs": [IG], "areaServed": "Sinop e região",
        "employee": {"@type": "Person", "name": "Dra. Luana Alves de Andrade", "jobTitle": "Cirurgiã-dentista, responsável técnica", "identifier": "CRO-MT 11238"},
        "availableService": [{"@type": "MedicalProcedure", "name": n} for n in ["Limpeza dental (profilaxia)", "Clareamento dental", "Tratamento de canal (endodontia)", "Reabilitação oral", "Facetas", "Próteses"]]
    }]
    if extra_ld: ld.append(extra_ld)
    ldjson = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#17261e">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{SITE_URL}/{ogimg}"><meta property="og:site_name" content="Extreme Odontologia">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{root}img/favicon-32.png"><link rel="icon" type="image/png" sizes="64x64" href="{root}img/favicon-64.png"><link rel="apple-touch-icon" href="{root}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/site.css">
{ldjson}
{GTAG}
</head>
<body>
"""

def header(root, current):
    links = "".join(f'<a href="{root}{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="top"><div class="wrap">
  <a class="brand" href="{root}"><img src="{root}img/logo.png" alt="Extreme Odontologia" width="44" height="44"><span><b>EXTREME</b><small>ODONTOLOGIA</small></span></a>
  <nav class="menu" id="menu" aria-label="Principal">{links}</nav>
  <div style="display:flex;gap:10px;align-items:center">
    <a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">{WA_SVG}<span>Agendar no WhatsApp</span></a>
    <button class="burger" aria-label="Abrir menu" onclick="document.getElementById('menu').classList.toggle('open')">☰</button>
  </div>
</div></header>
"""

def footer(root):
    cro_pj = f" · Inscrição de pessoa jurídica no CRO-MT: <b>{html.escape(CRO_PJ)}</b>" if CRO_PJ else ""
    return f"""<footer><div class="wrap">
  <div class="cols">
    <div><h4>Extreme Odontologia</h4><p>Clínica odontológica de alto padrão em Sinop – MT. Planejamento, transparência e cuidado com cada detalhe do seu sorriso.</p>
      <p>{ADDR}<br>{CITY}<br>Segunda a sexta, 8h às 18h</p></div>
    <div><h4>Tratamentos</h4><ul>
      <li><a href="{root}tratamentos/limpeza-dental-sinop.html">Limpeza dental</a></li>
      <li><a href="{root}tratamentos/clareamento-dental-sinop.html">Clareamento dental</a></li>
      <li><a href="{root}tratamentos/tratamento-de-canal-sinop.html">Tratamento de canal</a></li>
      <li><a href="{root}tratamentos/">Reabilitação, facetas e próteses</a></li></ul></div>
    <div><h4>Contato</h4><ul>
      <li><a href="{WA_DEFAULT}" target="_blank" rel="noopener">WhatsApp {WHATS_FMT}</a></li>
      <li><a href="{IG}" target="_blank" rel="noopener">Instagram @extreme_odontologia</a></li>
      <li><a href="{root}contato.html">Como chegar</a></li>
      <li><a href="{root}duvidas.html">Dúvidas frequentes</a></li>
      <li><a href="{root}artigos/">Artigos</a></li></ul></div>
  </div>
  <div class="legal">
    <b>Extreme Odontologia Ltda</b> · CNPJ 54.410.614/0001-70{cro_pj}<br>
    Responsável técnica: <b>Dra. Luana Alves de Andrade – Cirurgiã-dentista – CRO-MT 11238</b><br>
    Este site tem caráter informativo e não substitui a avaliação clínica. Resultados variam de pessoa para pessoa. © {datetime.date.today().year} Extreme Odontologia.<br>
    Este site usa a tag do Google para medir cliques no WhatsApp vindos de anúncios, sem publicidade personalizada.
  </div>
</div></footer>
<a class="fab" href="{WA_DEFAULT}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{WA_SVG}<span>Agendar</span></a>
</body></html>
"""

def promo_band(root):
    return f"""<div class="promo"><div class="wrap">
  <div><div class="k">Presente de fim de ano</div><h2>10% na sua primeira visita</h2></div>
  <p>Para novos pacientes, em <b>limpeza dental, clareamento dental ou tratamento de canal</b>. Agende até <b>{PROMO_END}</b>. Mediante avaliação clínica; não cumulativo com outras condições.</p>
  <a class="btn" href="{WA_PROMO}" target="_blank" rel="noopener">{WA_SVG} Quero meu presente</a>
</div></div>
"""

def cta_final(root, title="Pronto para cuidar do seu sorriso com quem planeja cada detalhe?", text="Fale com a nossa equipe no WhatsApp, tire suas dúvidas e agende sua avaliação. Atendimento de segunda a sexta, das 8h às 18h, no Jardim Botânico, em Sinop."):
    return f"""<section class="tight"><div class="wrap"><div class="cta-final">
  <div><div class="eyebrow">Agendamento</div><h2>{title}</h2><p>{text}</p></div>
  <div class="acts"><a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">{WA_SVG} Agendar pelo WhatsApp</a>
  <a class="btn btn-ghost" href="{root}contato.html">{PIN_SVG} Ver endereço e horários</a></div>
</div></div></section>
"""

TRATAMENTOS = [
    dict(slug="limpeza-dental-sinop", nome="Limpeza dental", num="01", kicker="Profilaxia profissional",
         resumo="Remoção de placa e tártaro, polimento e orientação de higiene. A base de qualquer sorriso saudável — e o ponto de partida do seu plano de cuidado.",
         titulo="Limpeza dental em Sinop", desc_seo="Limpeza dental (profilaxia) em Sinop – MT na Extreme Odontologia: remoção de tártaro, polimento e orientação de higiene com a Dra. Luana Alves, CRO-MT 11238. Agende pelo WhatsApp.",
         intro="A limpeza profissional remove o que a escova e o fio não alcançam: placa endurecida (tártaro), manchas superficiais e biofilme abaixo da linha da gengiva. É um procedimento rápido, confortável e preventivo — evita cáries, gengivite e mau hálito, e protege o investimento em qualquer outro tratamento.",
         como=[("Avaliação", "Conferimos gengiva, dentes e restaurações e explicamos o que foi encontrado, com imagens quando necessário."),
               ("Remoção do tártaro", "Com ultrassom e instrumentos manuais, removemos os depósitos acima e abaixo da gengiva."),
               ("Polimento", "Pasta profilática e jato de bicarbonato para remover manchas e deixar a superfície lisa, o que dificulta a nova formação de placa."),
               ("Orientação", "Técnica de escovação, fio dental e produtos adequados ao seu caso. Combinamos o intervalo ideal de retorno.")],
         para=["Quem não faz limpeza há mais de 6 meses", "Gengiva que sangra ao escovar ou passar o fio", "Manchas de café, chá, vinho ou cigarro", "Antes de clareamento, próteses ou tratamentos estéticos", "Gestantes (com liberação do obstetra) e pacientes em tratamento ortodôntico"],
         faq=[("Limpeza dói?", "Na maioria dos casos não. Em gengivas inflamadas pode haver sensibilidade; usamos técnica cuidadosa e, se necessário, anestesia tópica."),
              ("De quanto em quanto tempo devo fazer?", "Em geral a cada 6 meses. Quem tem tendência a tártaro, gengivite ou usa aparelho pode precisar de intervalos menores — definimos isso na avaliação."),
              ("Limpeza clareia os dentes?", "Ela remove manchas superficiais e devolve a cor natural do dente, mas não clareia a estrutura. Para clarear, o procedimento indicado é o clareamento dental.")]),
    dict(slug="clareamento-dental-sinop", nome="Clareamento dental", num="02", kicker="Clareamento profissional",
         resumo="Protocolos de consultório e supervisionados em casa, com gel de concentração profissional e proteção da gengiva. Resultado natural, sem exageros.",
         titulo="Clareamento dental em Sinop", desc_seo="Clareamento dental profissional em Sinop – MT: protocolo de consultório ou supervisionado, com avaliação prévia e proteção gengival. Extreme Odontologia, Dra. Luana Alves, CRO-MT 11238.",
         intro="O clareamento dental profissional usa géis de peróxido em concentração controlada, aplicados com proteção da gengiva e acompanhamento da dentista. Diferente de produtos de prateleira, ele parte de uma avaliação: cor inicial, presença de restaurações, sensibilidade e expectativa realista para o seu caso.",
         como=[("Avaliação e registro da cor", "Verificamos saúde gengival, cáries, restaurações visíveis (que não clareiam) e registramos a cor inicial."),
               ("Preparo", "Limpeza prévia quando necessária e proteção dos tecidos moles. Em casos de sensibilidade, usamos dessensibilizantes."),
               ("Clareamento", "No consultório, sessões com gel de alta concentração ativado conforme o protocolo; ou moldeiras individuais para uso em casa com gel supervisionado — ou a combinação dos dois."),
               ("Manutenção", "Orientação sobre alimentação nas primeiras 48h e cuidados para prolongar o resultado.")],
         para=["Dentes amarelados ou escurecidos pelo tempo, café, chá e cigarro", "Quem busca um sorriso mais claro para um evento ou para o dia a dia", "Antes de facetas ou restaurações estéticas, para definir a cor final", "Maiores de 18 anos com gengiva e dentes saudáveis (avaliação obrigatória)"],
         faq=[("Clareamento estraga o esmalte?", "Feito com produto profissional, na concentração e no tempo corretos e com supervisão, o clareamento é seguro para o esmalte. O risco está no uso sem orientação."),
              ("Quanto tempo dura o resultado?", "Varia com hábitos: em média de 1 a 3 anos, com manutenções simples. Café, vinho, refrigerantes escuros e cigarro reduzem a duração."),
              ("Restaurações e próteses clareiam?", "Não. Por isso avaliamos antes: às vezes é preciso trocar uma restauração visível depois do clareamento para igualar a cor."),
              ("Dá sensibilidade?", "Pode ocorrer sensibilidade leve e passageira durante o tratamento. Ajustamos protocolo e usamos dessensibilizantes para manter o conforto.")]),
    dict(slug="tratamento-de-canal-sinop", nome="Tratamento de canal", num="03", kicker="Endodontia",
         resumo="Quando a dor chega ao nervo, o canal salva o dente. Diagnóstico preciso, anestesia eficiente e técnica atual para você sair da dor e preservar o seu dente.",
         titulo="Tratamento de canal em Sinop", desc_seo="Tratamento de canal (endodontia) em Sinop – MT: diagnóstico preciso, anestesia confortável e técnica atual para preservar o dente. Extreme Odontologia, Dra. Luana Alves, CRO-MT 11238.",
         intro="O tratamento de canal (endodontia) remove a polpa inflamada ou infectada de dentro do dente, limpa e sela os canais, eliminando a dor e preservando o dente natural. Com anestesia adequada e técnica atual, é um procedimento muito mais confortável do que a fama sugere — e quase sempre melhor do que extrair.",
         como=[("Diagnóstico", "Exame clínico, testes de sensibilidade e radiografia para confirmar o que está acontecendo e se o dente pode ser preservado."),
               ("Anestesia e isolamento", "Anestesia local eficiente e isolamento absoluto, que protege o dente de contaminação durante o procedimento."),
               ("Limpeza e modelagem dos canais", "Instrumentos rotatórios e soluções irrigadoras removem o tecido comprometido e desinfetam o interior do dente."),
               ("Selamento e restauração", "Os canais são preenchidos e selados; em seguida o dente recebe a restauração ou coroa definitiva para voltar a funcionar com segurança.")],
         para=["Dor de dente intensa ou que piora à noite", "Sensibilidade prolongada ao quente ou ao frio", "Dente escurecido após trauma", "Inchaço na gengiva, fístula (bolinha de pus) ou dor ao morder", "Cárie profunda que alcançou a polpa"],
         faq=[("Canal dói?", "Com anestesia adequada, o procedimento é confortável. A dor que a maioria sente é a de antes do tratamento — o canal existe justamente para acabar com ela."),
              ("Quantas sessões são necessárias?", "Muitos casos são resolvidos em uma sessão; dentes com infecção ou anatomia complexa podem precisar de duas ou mais. Explicamos o plano antes de começar."),
              ("E depois do canal?", "O dente fica mais frágil e precisa de uma restauração definitiva — às vezes uma coroa — para não fraturar. Esse passo faz parte do plano de tratamento."),
              ("Não é melhor extrair?", "Preservar o dente natural costuma ser a melhor escolha para mastigação, estética e para os dentes vizinhos. A extração é indicada apenas quando não há condição de salvar o dente.")]),
]

OUTROS = [
    ("Reabilitação oral", "Devolver função e estética a quem perdeu dentes ou tem desgastes extensos, com planejamento digital e etapas bem definidas."),
    ("Facetas", "Lâminas em porcelana ou resina para corrigir cor, forma e pequenos desalinhamentos, com prova do planejamento (mock-up) antes de executar."),
    ("Próteses fixas em porcelana", "Coroas e próteses com estética natural e precisão de adaptação, para dentes tratados ou muito destruídos."),
    ("Planejamento digital do sorriso", "Fotos, escaneamento e simulação para você ver o resultado proposto antes de qualquer procedimento."),
]

def card(t, root):
    return f"""<article class="card"><span class="num">{t['num']}</span><h3>{t['nome']}</h3><p>{t['resumo']}</p><a class="more" href="{root}tratamentos/{t['slug']}.html">Saiba mais {ARROW}</a></article>"""

def page_index():
    root = ""
    faq_ld = None
    body = head("Extreme Odontologia | Clínica odontológica de alto padrão em Sinop – MT", "Clínica odontológica em Sinop – MT: limpeza, clareamento, tratamento de canal, facetas e reabilitação com planejamento digital. Dra. Luana Alves, CRO-MT 11238. Agende pelo WhatsApp.", root, "")
    body += header(root, None)
    body += f"""<section class="hero"><div class="wrap grid">
  <div>
    <div class="eyebrow">Clínica odontológica · Sinop – MT</div>
    <h1>Um sorriso planejado <em>em cada detalhe.</em></h1>
    <p class="lead">Odontologia de alto padrão no Jardim Botânico: diagnóstico preciso, planejamento digital e um atendimento que explica cada etapa antes de começar.</p>
    <div class="cta"><a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">{WA_SVG} Agendar avaliação</a><a class="btn btn-ghost" href="{root}tratamentos/">Conhecer os tratamentos {ARROW}</a></div>
    <div class="trust"><span>{PIN_SVG} Rua dos Cedros, 478 · Sala 05</span><span>{CLOCK_SVG} Seg a sex, 8h às 18h</span><span>{STAR_SVG} Dra. Luana Alves · CRO-MT 11238</span></div>
  </div>
  <div class="photo"><img src="{root}img/dra-luana.jpg" alt="Dra. Luana Alves na recepção da Extreme Odontologia, em Sinop" width="788" height="978" fetchpriority="high"><div class="tag"><b>Transparência do início ao fim</b>Você vê o plano, entende as etapas e decide com calma.</div></div>
</div></section>
{promo_band(root)}
<section><div class="wrap">
  <div class="sec-head"><div class="eyebrow">Tratamentos</div><h2>O que fazemos por você</h2><p class="lead">Do cuidado de rotina à reabilitação completa, com a mesma exigência de qualidade.</p></div>
  <div class="cards">{''.join(card(t, root) for t in TRATAMENTOS)}</div>
  <p style="margin-top:26px"><a class="btn btn-line" href="{root}tratamentos/">Reabilitação, facetas, próteses e planejamento digital {ARROW}</a></p>
</div></section>
<section class="dark"><div class="wrap split">
  <div><div class="eyebrow">Por que a Extreme</div><h2>Excelência técnica, com a calma de quem explica.</h2>
    <p>Na Extreme Odontologia cada atendimento é conduzido pela Dra. Luana Alves com planejamento, responsabilidade e respeito à história de cada paciente. Nada é feito sem que você entenda o porquê.</p>
    <ul class="list"><li>Planejamento digital e prova do resultado (mock-up) nos casos estéticos</li><li>Materiais e protocolos atuais, com biossegurança rigorosa</li><li>Ambiente reservado, silencioso e confortável — consulta com hora marcada</li><li>Orçamento claro e etapas definidas antes de começar</li></ul>
    <a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">{WA_SVG} Falar com a clínica</a></div>
  <div><img src="{root}img/ambiente.jpg?v=2" alt="Recepção da Extreme Odontologia em Sinop, com o logotipo dourado na parede verde" loading="lazy" width="960" height="1200" style="aspect-ratio:4/5;object-fit:cover"></div>
</div></section>
<section><div class="wrap">
  <div class="sec-head center"><div class="eyebrow">Como funciona</div><h2>Sua primeira visita, passo a passo</h2></div>
  <div class="steps">
    <div class="step"><h3>Contato</h3><p>Você chama no WhatsApp, conta o que precisa e escolhe o melhor horário.</p></div>
    <div class="step"><h3>Avaliação</h3><p>Exame clínico completo, imagens quando necessário e uma conversa franca sobre o que encontramos.</p></div>
    <div class="step"><h3>Plano</h3><p>Opções, etapas, prazos e investimento apresentados com clareza — você decide sem pressa.</p></div>
    <div class="step"><h3>Tratamento</h3><p>Execução com hora marcada, conforto e acompanhamento até o resultado final.</p></div>
  </div>
</div></section>
<section class="tight" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><div class="eyebrow">Instagram</div><h2>Bastidores e informação de qualidade</h2><p class="lead">Acompanhe <a href="{IG}" target="_blank" rel="noopener">@extreme_odontologia</a>.</p></div>
  <div class="ig">
    <iframe src="https://www.instagram.com/p/Ddgy2txu0nA/embed/" loading="lazy" title="Post do Instagram da Extreme Odontologia"></iframe>
    <iframe src="https://www.instagram.com/p/DdMj5ntNfYr/embed/" loading="lazy" title="Post do Instagram da Extreme Odontologia"></iframe>
    <iframe src="https://www.instagram.com/p/DfXqjnWt6am/embed/" loading="lazy" title="Post do Instagram da Extreme Odontologia"></iframe>
  </div>
</div></section>
{cta_final(root)}
"""
    body += footer(root)
    return body

def page_tratamentos_index():
    root = "../"
    body = head("Tratamentos | Extreme Odontologia – Sinop", "Tratamentos da Extreme Odontologia em Sinop – MT: limpeza, clareamento, tratamento de canal, reabilitação oral, facetas, próteses em porcelana e planejamento digital do sorriso.", root, "tratamentos/")
    body += header(root, "tratamentos/")
    outros = "".join(f'<article class="card"><span class="num">{i+4:02d}</span><h3>{n}</h3><p>{d}</p><a class="more" href="{WA_DEFAULT}" target="_blank" rel="noopener">Perguntar no WhatsApp {ARROW}</a></article>' for i, (n, d) in enumerate(OUTROS))
    body += f"""<div class="page-head"><div class="wrap"><div class="crumbs" style="color:#bdb8ac"><a href="{root}" style="color:#bdb8ac">Início</a> › Tratamentos</div><h1>Tratamentos</h1><p>Da prevenção à reabilitação completa. Cada caso começa por uma avaliação criteriosa e um plano explicado com clareza.</p></div></div>
<section><div class="wrap"><div class="sec-head"><div class="eyebrow">Mais procurados</div><h2>Cuidado essencial</h2></div><div class="cards">{''.join(card(t, root) for t in TRATAMENTOS)}</div></div></section>
<section class="dark"><div class="wrap"><div class="sec-head"><div class="eyebrow">Estética e reabilitação</div><h2>Para transformar o sorriso com segurança</h2><p>Casos estéticos e de reabilitação são planejados digitalmente e provados antes de executar. Você vê o resultado proposto e participa das decisões.</p></div><div class="cards" style="grid-template-columns:repeat(2,1fr)">{outros}</div></div></section>
{promo_band(root)}
{cta_final(root)}
"""
    body += footer(root)
    return body

def page_tratamento(t):
    root = "../"
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    body = head(f"{t['titulo']} | Extreme Odontologia", t["desc_seo"], root, f"tratamentos/{t['slug']}.html", faq_ld)
    body += header(root, "tratamentos/")
    steps = "".join(f'<div class="step"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["como"])
    para = "".join(f"<li>{x}</li>" for x in t["para"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    promo_item = t["nome"].lower()
    body += f"""<div class="page-head"><div class="wrap"><div class="crumbs" style="color:#bdb8ac"><a href="{root}" style="color:#bdb8ac">Início</a> › <a href="{root}tratamentos/" style="color:#bdb8ac">Tratamentos</a> › {t['nome']}</div><div class="eyebrow">{t['kicker']}</div><h1>{t['titulo']}</h1><p>{t['intro']}</p>
<p style="margin-top:22px"><a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">{WA_SVG} Agendar {t['nome'].lower()}</a></p></div></div>
<section><div class="wrap"><div class="sec-head"><div class="eyebrow">Como é feito</div><h2>Etapas do {t['nome'].lower()} na Extreme</h2></div><div class="steps">{steps}</div></div></section>
<section class="dark"><div class="wrap split"><div><div class="eyebrow">Indicações</div><h2>Para quem é indicado</h2><ul class="list">{para}</ul><p class="small" style="color:#bdb8ac">A indicação definitiva depende de avaliação clínica. Resultados variam de pessoa para pessoa.</p></div>
<div><div class="card" style="background:rgba(255,255,255,.04)"><span class="pill">Presente de fim de ano</span><h3 style="margin-top:14px">10% na primeira visita</h3><p>Novos pacientes têm 10% de desconto no {promo_item} agendado até {PROMO_END}. Mediante avaliação; não cumulativo.</p><a class="btn btn-gold" href="{WA_PROMO}" target="_blank" rel="noopener">{WA_SVG} Quero agendar</a></div></div></div></section>
<section><div class="wrap"><div class="sec-head"><div class="eyebrow">Dúvidas</div><h2>Perguntas frequentes sobre {t['nome'].lower()}</h2></div><div class="faq">{faq}</div><p style="margin-top:20px"><a href="{root}duvidas.html">Ver todas as dúvidas {ARROW}</a></p></div></section>
{cta_final(root)}
"""
    body += footer(root)
    return body

FAQ_GERAL = [
    ("Como agendar uma consulta na Extreme Odontologia?", f"Pelo WhatsApp {WHATS_FMT}. Você conta o que precisa, escolhe o horário e recebe a confirmação. Atendemos com hora marcada, de segunda a sexta, das 8h às 18h."),
    ("Onde fica a clínica?", f"{ADDR}, {CITY} — no mesmo prédio de outras empresas do Jardim Botânico, com estacionamento na rua. Veja o mapa na página de contato."),
    ("Quem é a responsável técnica?", "A Dra. Luana Alves de Andrade, cirurgiã-dentista, CRO-MT 11238. Ela conduz pessoalmente os atendimentos e o planejamento de cada caso."),
    ("Como funciona a primeira consulta?", "É uma avaliação completa: exame clínico, imagens quando necessário e uma conversa sobre o que encontramos, as opções de tratamento, etapas e investimento. Você sai com um plano claro, sem compromisso de fechar na hora."),
    ("O que é o presente de fim de ano?", f"Novos pacientes que agendarem até {PROMO_END} têm 10% de desconto na primeira visita em limpeza dental, clareamento dental ou tratamento de canal. Vale mediante avaliação clínica e não é cumulativo com outras condições."),
    ("Vocês atendem convênios odontológicos?", "Nosso atendimento é particular, com planejamento individual. Fale conosco no WhatsApp para conhecer as formas de pagamento disponíveis."),
    ("Atendem urgência e dor de dente?", "Sim, dentro do horário de funcionamento. Chame no WhatsApp descrevendo o que sente — dor intensa, inchaço ou trauma têm prioridade de encaixe."),
    ("Atendem crianças?", "Atendemos adultos e adolescentes. Para crianças pequenas, indicamos avaliação prévia pelo WhatsApp para orientar o melhor encaminhamento."),
    ("De quanto em quanto tempo devo ir ao dentista?", "Para a maioria das pessoas, a cada 6 meses para limpeza e revisão. Quem tem gengivite, tendência a tártaro ou usa aparelho pode precisar de intervalos menores."),
    ("O que levar na primeira consulta?", "Documento com foto, exames ou radiografias recentes (se tiver) e a lista de medicamentos em uso. Se já tiver um orçamento de outra clínica, traga também — ajudamos a entender as opções."),
    ("Clareamento, limpeza e canal: por onde começo?", "Pela avaliação. Normalmente a sequência é tratar o que dói ou infecciona primeiro (canal, cáries), depois saúde da gengiva (limpeza) e, por fim, a estética (clareamento, facetas)."),
    ("Vocês fazem planejamento digital do sorriso?", "Sim. Em casos estéticos e de reabilitação usamos fotos, escaneamento e simulação para você ver o resultado proposto — e, quando indicado, a prova em boca (mock-up) antes de executar."),
]

def page_duvidas():
    root = ""
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ_GERAL]}
    body = head("Dúvidas frequentes | Extreme Odontologia – Sinop", "Respostas às dúvidas mais comuns sobre consultas, agendamento, limpeza, clareamento, canal e a primeira visita na Extreme Odontologia, em Sinop – MT.", root, "duvidas.html", faq_ld)
    body += header(root, "duvidas.html")
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ_GERAL)
    body += f"""<div class="page-head"><div class="wrap"><div class="crumbs" style="color:#bdb8ac"><a href="{root}" style="color:#bdb8ac">Início</a> › Dúvidas</div><h1>Dúvidas frequentes</h1><p>O que as pessoas mais perguntam antes da primeira visita. Não achou sua resposta? Chame no WhatsApp.</p></div></div>
<section><div class="wrap" style="max-width:860px"><div class="faq">{faq}</div></div></section>
{cta_final(root, "Ficou alguma dúvida?", "Mande uma mensagem no WhatsApp. Respondemos em horário comercial, com atenção e sem pressa.")}
"""
    body += footer(root)
    return body

ARTIGOS = [
    dict(slug="clareamento-dental-como-funciona", titulo="Clareamento dental: como funciona, o que esperar e como manter o resultado", data="2026-11-08", tempo="5 min",
         desc="Entenda como o clareamento dental profissional funciona, quem pode fazer, por que a avaliação vem antes e o que fazer para o resultado durar mais.",
         corpo="""
<p>Poucos procedimentos mudam tanto a percepção de um sorriso quanto o clareamento — e poucos geram tantas dúvidas. Vale entender o que acontece de verdade no dente antes de decidir.</p>
<h2>O que o clareamento faz</h2>
<p>Os géis clareadores (peróxido de hidrogênio ou de carbamida) penetram no esmalte e quebram as moléculas de pigmento acumuladas na dentina ao longo dos anos. O dente não é “pintado”: ele volta a um tom mais claro da sua própria cor. Por isso o resultado é natural quando o protocolo é respeitado.</p>
<h2>Consultório, casa ou os dois?</h2>
<p>No consultório, o gel em concentração mais alta é aplicado com proteção da gengiva e sessões controladas — resultado mais rápido. Em casa, moldeiras feitas sob medida recebem um gel de concentração menor por alguns dias, sob supervisão. Muitos casos combinam os dois para unir velocidade e estabilidade da cor.</p>
<h2>Por que a avaliação vem antes</h2>
<ul><li><b>Restaurações e próteses não clareiam.</b> Se houver uma restauração visível, ela pode precisar ser trocada depois para igualar a cor.</li><li><b>Gengiva inflamada e cáries</b> precisam ser tratadas antes.</li><li><b>Sensibilidade</b> prévia muda o protocolo: menor concentração, dessensibilizantes e intervalos maiores.</li><li><b>Expectativa:</b> dentes com manchas por tetraciclina ou fluorose respondem de forma diferente, e é melhor saber disso antes.</li></ul>
<blockquote>Clareamento seguro é clareamento supervisionado: produto certo, tempo certo e gengiva protegida.</blockquote>
<h2>O resultado dura quanto tempo?</h2>
<p>Em média de um a três anos, dependendo dos hábitos. Café, chá preto, vinho tinto, refrigerantes escuros e cigarro aceleram o retorno da cor. Uma manutenção simples, combinada com a dentista, prolonga o efeito.</p>
<h2>Cuidados nas primeiras 48 horas</h2>
<p>Evite alimentos e bebidas com corante forte, cigarro e batom escuro. Sensibilidade leve é esperada e passa; se for intensa, avise a clínica para ajustar o protocolo.</p>
<div class="note">Este conteúdo é informativo e não substitui a avaliação clínica. A indicação do clareamento, o protocolo e o número de sessões dependem de cada caso.</div>
"""),
    dict(slug="tratamento-de-canal-doi", titulo="Tratamento de canal dói? O que acontece na consulta, passo a passo", data="2026-11-08", tempo="5 min",
         desc="Como é feito o tratamento de canal hoje, por que a anestesia resolve o medo da dor e o que esperar depois do procedimento.",
         corpo="""
<p>“Canal” é a palavra que mais assusta no consultório — e, na prática, é o procedimento que tira a pessoa da dor. A fama vem de outra época; a técnica de hoje é outra.</p>
<h2>Quando o canal é necessário</h2>
<p>Quando uma cárie profunda, uma trinca ou um trauma atingem a polpa (o “nervo” do dente), ela inflama ou infecciona. Os sinais clássicos: dor espontânea que piora à noite, sensibilidade prolongada ao quente, dor ao morder, inchaço na gengiva ou uma pequena fístula. Em alguns casos não há dor nenhuma e o problema aparece na radiografia.</p>
<h2>O que acontece na consulta</h2>
<ol><li><b>Diagnóstico:</b> testes de sensibilidade e radiografia confirmam o dente envolvido e se ele pode ser preservado.</li><li><b>Anestesia:</b> local, eficiente. Em dentes muito inflamados pode ser preciso complementar — e é feito até você não sentir nada.</li><li><b>Isolamento absoluto:</b> uma lâmina de borracha isola o dente, protegendo de saliva e bactérias.</li><li><b>Limpeza dos canais:</b> instrumentos finos e rotatórios, com irrigação desinfetante, removem o tecido comprometido e modelam o interior do dente.</li><li><b>Selamento:</b> os canais são preenchidos e selados. O dente recebe então a restauração definitiva — às vezes uma coroa — para não fraturar.</li></ol>
<blockquote>A dor do canal é a dor de antes. Durante o procedimento, com anestesia adequada, o normal é sentir apenas pressão e vibração.</blockquote>
<h2>E depois?</h2>
<p>É comum um incômodo leve ao morder por alguns dias, controlado com analgésico comum. O passo mais negligenciado — e mais importante — é concluir a restauração definitiva: um dente tratado e não restaurado pode fraturar e aí sim ser perdido.</p>
<h2>Canal ou extração?</h2>
<p>Preservar o dente natural costuma ser melhor para a mastigação, para a estética e para os dentes vizinhos, que não precisam ser desgastados ou substituídos por implante. A extração fica para quando não há estrutura suficiente para salvar o dente.</p>
<div class="note">Conteúdo informativo. Só a avaliação clínica, com exame e radiografia, define a necessidade e o número de sessões do tratamento.</div>
"""),
    dict(slug="limpeza-dental-a-cada-6-meses", titulo="Limpeza dental a cada 6 meses: o que ela previne e por que vale a pena", data="2026-11-08", tempo="4 min",
         desc="Por que a limpeza profissional periódica é o cuidado com melhor custo-benefício da odontologia e o que acontece quando ela é adiada.",
         corpo="""
<p>A limpeza profissional é o procedimento mais simples do consultório e, ao mesmo tempo, o que mais evita problemas caros. Entenda o que ela faz que a escovação não consegue.</p>
<h2>Placa, tártaro e gengiva</h2>
<p>A placa bacteriana se forma todos os dias. Onde a escova e o fio não chegam, ela endurece em poucos dias e vira tártaro — que só sai com instrumentos profissionais. O tártaro irrita a gengiva (gengivite: sangramento, vermelhidão) e, se persistir, avança para o osso que segura o dente (periodontite), uma das principais causas de perda dentária em adultos.</p>
<h2>O que acontece na limpeza</h2>
<ul><li>Remoção do tártaro com ultrassom e instrumentos manuais, acima e abaixo da gengiva.</li><li>Polimento, que remove manchas superficiais e deixa a superfície lisa — dificultando a nova formação de placa.</li><li>Revisão de cáries, restaurações e próteses, antes que pequenos problemas virem grandes.</li><li>Orientação personalizada: técnica, fio, escovas interdentais e produtos adequados ao seu caso.</li></ul>
<h2>Por que 6 meses?</h2>
<p>É o intervalo em que, para a maioria das pessoas, a placa ainda não causou dano irreversível e as alterações iniciais são fáceis de tratar. Quem tem gengivite, diabetes, usa aparelho ou fuma pode precisar de intervalos menores — a dentista define isso na avaliação.</p>
<blockquote>Sangramento ao escovar não é normal. É o primeiro aviso de que a gengiva precisa de atenção.</blockquote>
<h2>Limpeza antes de clareamento e estética</h2>
<p>Qualquer tratamento estético começa com gengiva saudável e dentes sem placa: o clareamento age melhor, as facetas adaptam com precisão e o resultado dura mais.</p>
<div class="note">Conteúdo informativo. A frequência ideal de limpeza é definida individualmente, após avaliação.</div>
"""),
    dict(slug="clareamento-dental-caseiro-ou-consultorio", titulo="Clareamento dental caseiro ou em consultório: qual a diferença e qual escolher", data="2026-11-10", tempo="5 min",
         desc="Clareamento dental caseiro supervisionado, clareamento em consultório, fitas e receitas da internet: o que muda entre eles e como a dentista indica cada um.",
         corpo="""
<p>“Clareamento dental caseiro” é uma das buscas mais feitas sobre o assunto — e o termo mistura coisas muito diferentes: o tratamento caseiro supervisionado pela dentista, os produtos de prateleira e as receitas da internet. Vale separar cada um.</p>
<h2>Clareamento caseiro supervisionado</h2>
<p>É um tratamento odontológico feito em casa. A dentista avalia a boca, faz moldeiras sob medida e entrega seringas de gel clareador em concentração baixa, com orientação de quanto usar e por quanto tempo. A cor muda de forma gradual, ao longo de alguns dias ou semanas, com retornos para acompanhamento.</p>
<h2>Clareamento dental em consultório</h2>
<p>O gel tem concentração mais alta e por isso só é aplicado pela profissional, com a gengiva protegida por uma barreira. O resultado aparece mais rápido, em sessões controladas. É a opção de quem tem pouco tempo ou não se adapta ao uso diário da moldeira.</p>
<h2>Os dois combinados</h2>
<p>Em muitos casos a indicação é associar as técnicas: sessões no consultório para ganhar velocidade e o gel em casa para estabilizar a cor. Quem define é a avaliação, não a preferência por um método.</p>
<h2>E as fitas, kits e cremes dentais clareadores?</h2>
<ul><li><b>Cremes dentais “clareadores”</b> atuam sobre manchas superficiais; não mudam a cor interna do dente.</li><li><b>Fitas e kits vendidos sem avaliação</b> usam moldes genéricos: o gel escapa para a gengiva com facilidade e não há quem ajuste o uso se surgir sensibilidade.</li><li><b>Receitas caseiras</b> com bicarbonato, limão, carvão ou água oxigenada são abrasivas ou ácidas: desgastam o esmalte, que não se regenera.</li></ul>
<blockquote>O que torna o clareamento caseiro seguro não é o gel: é a avaliação antes e o acompanhamento durante.</blockquote>
<h2>Como a dentista escolhe a técnica</h2>
<ul><li>Sensibilidade prévia e retrações de gengiva.</li><li>Presença de cáries, restaurações e próteses nos dentes da frente (elas não clareiam).</li><li>Tipo e origem do escurecimento.</li><li>Rotina do paciente e prazo desejado.</li></ul>
<p>Em Sinop, a avaliação para clareamento dental na Extreme Odontologia é feita no Jardim Botânico, com hora marcada. Veja também <a href="clareamento-dental-como-funciona.html">como o clareamento funciona e quanto tempo dura</a>.</p>
<div class="note">Conteúdo informativo. A indicação da técnica de clareamento depende de avaliação clínica individual.</div>
"""),
    dict(slug="quanto-custa-clareamento-dental", titulo="Quanto custa um clareamento dental? O que define o valor", data="2026-11-10", tempo="4 min",
         desc="O valor do clareamento dental varia conforme a técnica, o número de sessões e o que a boca precisa antes. Entenda o que entra no orçamento e como comparar.",
         corpo="""
<p>“Quanto custa um clareamento dental” e “clareamento dental valor” estão entre as perguntas mais buscadas no Google sobre o tema. A resposta honesta é que não existe um preço único — e entender por quê ajuda a comparar orçamentos com segurança.</p>
<h2>Por que este artigo não traz uma tabela de preços</h2>
<p>O Código de Ética Odontológica não permite a divulgação de preços de procedimentos em publicidade. Além disso, um valor sem avaliação diria pouco: dois clareamentos com o mesmo nome podem ser tratamentos bem diferentes.</p>
<h2>O que define o valor de um clareamento</h2>
<ul><li><b>Técnica indicada:</b> caseiro supervisionado, consultório ou a combinação dos dois.</li><li><b>Número de sessões</b> ou tempo de uso do gel, que depende do tom inicial e da resposta do dente.</li><li><b>Materiais:</b> moldeiras sob medida, tipo e concentração do gel, barreira de proteção da gengiva.</li><li><b>Preparo prévio:</b> limpeza profissional e tratamento de cáries ou gengivite, quando necessários.</li><li><b>Controle de sensibilidade:</b> dessensibilizantes e ajustes de protocolo.</li><li><b>Acompanhamento:</b> consultas de retorno durante e depois do tratamento.</li></ul>
<h2>O que pode ficar de fora do orçamento</h2>
<p>Restaurações e próteses não clareiam. Se houver alguma visível no sorriso, pode ser preciso trocá-la depois para igualar a cor — e isso costuma ser orçado à parte. Pergunte antes.</p>
<blockquote>Compare o que está incluído, não apenas o número final.</blockquote>
<h2>Perguntas para fazer antes de fechar</h2>
<ol><li>A avaliação inclui exame da gengiva e das restaurações?</li><li>Quantas sessões ou dias de uso estão previstos?</li><li>O que acontece se eu tiver sensibilidade?</li><li>Há retorno de acompanhamento incluído?</li><li>Quem aplica o gel e quem responde tecnicamente pelo tratamento?</li></ol>
<p>Na Extreme Odontologia, em Sinop, o orçamento é apresentado depois da avaliação, com o protocolo explicado. Entenda antes a diferença entre <a href="clareamento-dental-caseiro-ou-consultorio.html">clareamento caseiro e em consultório</a>.</p>
<div class="note">Conteúdo informativo. Valores e protocolos são definidos individualmente, após avaliação clínica.</div>
"""),
    dict(slug="limpeza-dental-doi-clareia-os-dentes", titulo="Limpeza dental dói? Clareia os dentes? Respostas diretas", data="2026-11-10", tempo="4 min",
         desc="Limpeza dental com ultrassom dói? Clareia os dentes? Quanto tempo leva e o que define o valor? As dúvidas mais buscadas sobre profilaxia, respondidas.",
         corpo="""
<p>A limpeza dental (profilaxia) é o procedimento mais comum do consultório e, mesmo assim, cercado de dúvidas. Estas são as mais buscadas.</p>
<h2>Limpeza dental dói?</h2>
<p>Para a maioria das pessoas, não. O que se sente é vibração, água e pressão. Pode haver desconforto em quem está com a gengiva inflamada, tem muito tártaro abaixo da gengiva ou dentes sensíveis — e, nesses casos, a dentista pode usar anestésico. Gengiva que sangra na limpeza é sinal de inflamação, e ela melhora depois que o tártaro sai.</p>
<h2>Limpeza dental clareia os dentes?</h2>
<p>Ela remove tártaro e manchas superficiais de café, chá e cigarro, e por isso os dentes costumam parecer mais claros. Mas a limpeza não muda a cor interna do dente: isso é papel do <a href="clareamento-dental-como-funciona.html">clareamento dental</a>. Os dois se complementam — o clareamento é feito sobre dentes limpos.</p>
<h2>Como é a limpeza com ultrassom?</h2>
<p>Uma ponta metálica vibra em alta frequência, com irrigação de água, e solta o tártaro sem desgastar o esmalte. Depois vêm os instrumentos manuais nos pontos finos, o jato ou a pasta de polimento e a orientação de higiene.</p>
<h2>Quanto tempo leva?</h2>
<p>Em geral, uma consulta. Quando há muito tártaro ou doença periodontal, o tratamento pode ser dividido em mais sessões (raspagem).</p>
<h2>O que define o valor de uma limpeza dental?</h2>
<p>A quantidade de tártaro, a necessidade de raspagem abaixo da gengiva, o número de sessões e os exames associados. Por norma ética, clínicas odontológicas não divulgam preços em publicidade; o orçamento é dado após a avaliação.</p>
<blockquote>A limpeza não “enfraquece” nem “afasta” os dentes: o espaço que aparece era ocupado pelo tártaro.</blockquote>
<p>Procurando limpeza dental em Sinop? A Extreme Odontologia atende com hora marcada no Jardim Botânico. Veja também <a href="limpeza-dental-a-cada-6-meses.html">por que repetir a limpeza a cada 6 meses</a>.</p>
<div class="note">Conteúdo informativo. A necessidade de anestesia, raspagem e o número de sessões são definidos na avaliação.</div>
"""),
    dict(slug="tratamento-de-canal-quanto-tempo-demora", titulo="Tratamento de canal: quanto tempo demora e o que define o valor", data="2026-11-10", tempo="4 min",
         desc="Quantas sessões tem um tratamento de canal, quanto tempo dura cada consulta e o que influencia o valor: dente, número de canais, retratamento e restauração final.",
         corpo="""
<p>Depois de “dói?”, as duas perguntas mais buscadas sobre tratamento de canal são quanto tempo demora e quanto custa. As duas respostas dependem do mesmo ponto: a anatomia e a situação do dente.</p>
<h2>Quanto tempo demora um tratamento de canal</h2>
<p>Muitos casos são resolvidos em uma ou duas consultas. O que muda o tempo:</p>
<ul><li><b>O dente:</b> dentes da frente costumam ter um canal; molares têm três ou mais, e levam mais tempo.</li><li><b>Infecção:</b> com abscesso ou infecção extensa, pode ser indicada medicação dentro do canal entre as sessões.</li><li><b>Anatomia:</b> canais curvos, estreitos ou calcificados exigem mais cuidado.</li><li><b>Retratamento:</b> refazer um canal antigo é mais demorado que o primeiro tratamento.</li></ul>
<h2>O tratamento só termina com a restauração</h2>
<p>Depois de selados os canais, o dente precisa da restauração definitiva — em alguns casos, uma coroa. Sem ela, o dente fica frágil e pode fraturar. Conte esse passo no prazo e no orçamento.</p>
<h2>O que define o valor de um tratamento de canal</h2>
<ul><li>Qual é o dente e quantos canais ele tem.</li><li>Se é primeiro tratamento ou retratamento.</li><li>Radiografias e, quando necessário, tomografia.</li><li>Número de sessões.</li><li>A restauração final (resina, bloco ou coroa), normalmente orçada à parte.</li></ul>
<p>Por norma do Código de Ética Odontológica, preços não são divulgados em publicidade. O orçamento é fechado após exame e radiografia.</p>
<blockquote>Adiar o canal não faz o problema regredir: a infecção avança e o tratamento fica mais longo.</blockquote>
<h2>Quando procurar a dentista sem esperar</h2>
<p>Dor espontânea que piora à noite, dor ao morder, inchaço no rosto ou na gengiva e sensibilidade prolongada ao quente. Em Sinop, a Extreme Odontologia faz a avaliação com hora marcada. Entenda o passo a passo em <a href="tratamento-de-canal-doi.html">tratamento de canal dói?</a>.</p>
<div class="note">Conteúdo informativo. O número de sessões e o plano de tratamento são definidos após exame clínico e radiográfico.</div>
"""),
    dict(slug="dentista-em-sinop-o-que-avaliar", titulo="Dentista em Sinop: o que avaliar antes de marcar a consulta", data="2026-11-10", tempo="4 min",
         desc="Procurando dentista em Sinop? Veja o que conferir antes de agendar: registro no CRO, avaliação antes do orçamento, biossegurança, localização e canais de contato.",
         corpo="""
<p>Quem busca “dentista em Sinop” ou “dentista perto de mim” encontra muitas opções em poucos segundos. Alguns critérios objetivos ajudam a escolher com segurança, qualquer que seja a clínica.</p>
<h2>1. Registro no Conselho Regional de Odontologia</h2>
<p>Todo cirurgião-dentista tem inscrição no CRO do estado, e o número deve aparecer na comunicação da clínica. A consulta é pública no site do Conselho Federal de Odontologia.</p>
<h2>2. Avaliação antes do orçamento</h2>
<p>Um plano de tratamento sério começa com exame clínico e, quando necessário, radiografia. Desconfie de diagnóstico e preço fechados sem examinar a boca.</p>
<h2>3. Explicação clara do plano</h2>
<p>Você deve sair da avaliação sabendo o que será feito, em quantas consultas, quais são as alternativas e o que está incluído no valor.</p>
<h2>4. Biossegurança</h2>
<p>Instrumentais esterilizados e embalados, materiais descartáveis abertos na sua frente e ambiente limpo são o mínimo.</p>
<h2>5. Localização, horário e contato</h2>
<p>Tratamentos costumam exigir retornos. Clínica de fácil acesso, com horário compatível com a sua rotina e um canal de contato que responde, faz diferença para concluir o tratamento.</p>
<blockquote>Bom atendimento odontológico é aquele em que você entende o que vai ser feito antes de começar.</blockquote>
<h2>Sobre a Extreme Odontologia</h2>
<p>A clínica fica na Rua dos Cedros, 478, Sala 05, no Jardim Botânico, em Sinop/MT, e atende de segunda a sexta, das 8h às 18h, com hora marcada pelo WhatsApp. A responsável técnica é a Dra. Luana Alves de Andrade, CRO-MT 11238. Conheça os <a href="../tratamentos/">tratamentos</a> e veja <a href="../contato.html">como chegar</a>.</p>
<div class="note">Conteúdo informativo. Este texto não substitui a avaliação clínica.</div>
"""),
]

def page_artigos_index():
    root = "../"
    body = head("Artigos | Extreme Odontologia – Sinop", "Artigos e informativos da Extreme Odontologia: clareamento, tratamento de canal, limpeza dental e saúde bucal explicados com clareza pela Dra. Luana Alves.", root, "artigos/")
    body += header(root, "artigos/")
    cards = "".join(f'<article class="card"><span class="num">{a["tempo"]} de leitura</span><h3>{a["titulo"]}</h3><p>{a["desc"]}</p><a class="more" href="{root}artigos/{a["slug"]}.html">Ler artigo {ARROW}</a></article>' for a in ARTIGOS)
    body += f"""<div class="page-head"><div class="wrap"><div class="crumbs" style="color:#bdb8ac"><a href="{root}" style="color:#bdb8ac">Início</a> › Artigos</div><h1>Artigos e informativos</h1><p>Informação de qualidade para você decidir com segurança — escrita com a supervisão da Dra. Luana Alves, CRO-MT 11238.</p></div></div>
<section><div class="wrap"><div class="cards">{cards}</div></div></section>
{cta_final(root)}
"""
    body += footer(root)
    return body

def page_artigo(a):
    root = "../"
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["titulo"], "description": a["desc"], "datePublished": a["data"], "dateModified": a["data"], "inLanguage": "pt-BR",
          "author": {"@type": "Person", "name": "Dra. Luana Alves de Andrade", "jobTitle": "Cirurgiã-dentista – CRO-MT 11238"}, "publisher": {"@type": "Organization", "name": "Extreme Odontologia", "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/img/logo.png"}},
          "mainEntityOfPage": f"{SITE_URL}/artigos/{a['slug']}.html"}
    body = head(f"{a['titulo']} | Extreme Odontologia", a["desc"], root, f"artigos/{a['slug']}.html", ld)
    body += header(root, "artigos/")
    d = datetime.date.fromisoformat(a["data"]).strftime("%d/%m/%Y")
    body += f"""<section><div class="wrap"><div class="article"><div class="crumbs"><a href="{root}">Início</a> › <a href="{root}artigos/">Artigos</a></div>
<h1 style="font-size:clamp(32px,4.6vw,48px)">{a['titulo']}</h1><div class="meta">Por Dra. Luana Alves de Andrade · CRO-MT 11238 · {d} · {a['tempo']} de leitura</div>
{a['corpo']}
<p style="margin-top:34px"><a class="btn btn-dark" href="{WA_DEFAULT}" target="_blank" rel="noopener">{WA_SVG} Agendar avaliação</a></p></div></div></section>
{cta_final(root)}
"""
    body += footer(root)
    return body

def page_contato():
    root = ""
    body = head("Contato e endereço | Extreme Odontologia – Sinop", f"Extreme Odontologia: {ADDR}, {CITY}. WhatsApp {WHATS_FMT}. Segunda a sexta, 8h às 18h. Veja o mapa e como chegar.", root, "contato.html")
    body += header(root, "contato.html")
    from urllib.parse import quote
    maps_embed = "https://www.google.com/maps?q=" + quote(MAPS_Q) + "&output=embed"
    maps_link = "https://www.google.com/maps/search/?api=1&query=" + quote(MAPS_Q)
    body += f"""<div class="page-head"><div class="wrap"><div class="crumbs" style="color:#bdb8ac"><a href="{root}" style="color:#bdb8ac">Início</a> › Contato</div><h1>Contato e como chegar</h1><p>Estamos no Jardim Botânico, em Sinop. Agendamento pelo WhatsApp, com hora marcada.</p></div></div>
<section><div class="wrap info">
  <div class="box"><h3>Fale com a clínica</h3><dl>
    <dt>WhatsApp</dt><dd><a href="{WA_DEFAULT}" target="_blank" rel="noopener">{WHATS_FMT}</a></dd>
    <dt>Instagram</dt><dd><a href="{IG}" target="_blank" rel="noopener">@extreme_odontologia</a></dd>
    <dt>Endereço</dt><dd>{ADDR}<br>{CITY}</dd>
    <dt>Horário</dt><dd>Segunda a sexta, das 8h às 18h<br><span class="small">Sábados, domingos e feriados: fechado</span></dd>
    <dt>Responsável técnica</dt><dd>Dra. Luana Alves de Andrade – CRO-MT 11238</dd></dl>
    <p style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-gold" href="{WA_DEFAULT}" target="_blank" rel="noopener">{WA_SVG} Chamar no WhatsApp</a><a class="btn btn-line" href="{maps_link}" target="_blank" rel="noopener">{PIN_SVG} Abrir no Google Maps</a></p></div>
  <div><iframe class="map" src="{maps_embed}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa: Extreme Odontologia, Rua dos Cedros 478, Sinop"></iframe></div>
</div></section>
{promo_band(root)}
"""
    body += footer(root)
    return body

def page_404():
    root = ""
    body = head("Página não encontrada | Extreme Odontologia", "Página não encontrada.", root, "404.html")
    body += header(root, None)
    body += f"""<section><div class="wrap" style="text-align:center;max-width:680px"><div class="eyebrow">Erro 404</div><h1>Essa página não existe.</h1><p class="lead">Mas o seu sorriso continua em boas mãos. Volte ao início ou fale conosco.</p><p><a class="btn btn-dark" href="{root}">Ir para o início</a> <a class="btn btn-line" href="{WA_DEFAULT}" target="_blank" rel="noopener">WhatsApp</a></p></div></section>"""
    body += footer(root)
    return body

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "css"))
    write("css/site.css", CSS.strip() + "\n")
    shutil.copytree(os.path.join(os.path.dirname(__file__), "img"), os.path.join(OUT, "img"))
    for f in ["luana-recepcao.jpg"]:
        p = os.path.join(OUT, "img", f)
        if os.path.exists(p): os.remove(p)
    pages = {"index.html": page_index(), "tratamentos/index.html": page_tratamentos_index(), "duvidas.html": page_duvidas(), "artigos/index.html": page_artigos_index(), "contato.html": page_contato(), "404.html": page_404()}
    for t in TRATAMENTOS: pages[f"tratamentos/{t['slug']}.html"] = page_tratamento(t)
    for a in ARTIGOS: pages[f"artigos/{a['slug']}.html"] = page_artigo(a)
    for p, c in pages.items(): write(p, c)
    urls = ["", "tratamentos/", "duvidas.html", "artigos/", "contato.html"] + [f"tratamentos/{t['slug']}.html" for t in TRATAMENTOS] + [f"artigos/{a['slug']}.html" for a in ARTIGOS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE_URL}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    write(".nojekyll", "")
    print("ok", len(pages), "páginas")

if __name__ == "__main__":
    main()
