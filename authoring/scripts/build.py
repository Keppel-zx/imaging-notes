from pathlib import Path
import json,re,html,shutil
from html.parser import HTMLParser
import latex2mathml.converter
from visual_layout import load_visuals,enrich,citation_link,reader_shell,build_sources_page
ROOT=Path(__file__).resolve().parents[1]; SITE=ROOT/'site'
TITLES={'benchmark':'Camera Image Quality Benchmarking','ptc':'Photon Transfer: DN → λ','emva':'EMVA Standard 1288 — Release 3.1 (30 December 2016)','colour':'Fundamentals and Applications of Colour Engineering','isp':'Understanding the in-camera rendering pipeline & the role of AI and deep learning','spad':'TOF Range-Imaging Cameras','depth':'Time-of-Flight and Structured Light Depth Cameras: Technology and Applications'}
MODULES=['成像链路与 CMOS 性能','EMVA 1288 与光子转移','RAW 与 ISP 渲染链路','相机画质与视觉评价','SPAD 计数与时间测量','ToF 测距与误差机制','RGB-D、标定与点云','跨系统比较与工程选型']
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,d):self.parts.append(d)
def plain(s):
 p=Text();p.feed(s);return ' '.join(p.parts)
def readjson(p,default):
 try:return json.loads(p.read_text())
 except FileNotFoundError:return default
outline=readjson(ROOT/'outline.json',[])
visuals=load_visuals(ROOT)
citations=[]
for f in sorted((ROOT/'citations').glob('week-*.json')):
 c=readjson(f,[])
 if isinstance(c,dict):c=c.get('citations',c.get('lessons',[]))
 if isinstance(c,list):citations.extend(c)
# Integrate visible excerpt/figure/formula provenance into the same source index.
for day,v in sorted(visuals.items()):
 for role,item in [('excerpt',v['excerpt']),('formula',v['key_formula'])]+[('figure',f) for f in [v['figure']]+v.get('extra_figures',[])]:
  c={'day':day,'source':item['source'],'chapter':item.get('chapter','图文阅读卡片；具体依据见条目'),'pdf_pages':[item['pdf_page']],'record_type':'visual_'+role,'formulas':[],'figures':[]}
  if role=='excerpt':c['quote']={'text':item['en'],'translation':item['zh'],'pdf_page':item['pdf_page']}
  if role=='formula':c['formulas']=[{'label':item['label'],'tex':item['tex'],'pdf_page':item['pdf_page'],'original_number':item.get('original_number'),'kind':item['kind']}]
  if role=='figure':c['figures']=[{'number':item.get('figure_number'),'pdf_page':item['pdf_page'],'kind':item['kind'],'path':item['path'],'label':item['title']}]
  citations.append(c)
(SITE/'data').mkdir(exist_ok=True)
math_errors=[]
def mathify(s,day):
 def cv(m):
  raw=m.group(1);display=m.group(0).startswith('\\[')
  try:
   normalized=html.unescape(raw).replace(r'\begin{bmatrix}',r'\left[\begin{matrix}').replace(r'\end{bmatrix}',r'\end{matrix}\right]')
   out=latex2mathml.converter.convert(normalized,display='block' if display else 'inline')
   return '<span class="math-display">'+out+'</span>' if display else out
  except Exception as e:math_errors.append({'day':day,'latex':raw,'error':str(e)});return m.group(0)
 return re.sub(r'\\\[(.*?)\\\]|\\\((.*?)\\\)',lambda m:cv2(m),s,flags=re.S)
def cv2(m):
 raw=m.group(1) if m.group(1) is not None else m.group(2)
 raw=re.sub(r'\\arg\b',lambda m:r'\operatorname{arg}',raw)
 try:
  normalized=html.unescape(raw).replace(r'\begin{bmatrix}',r'\left[\begin{matrix}').replace(r'\end{bmatrix}',r'\end{matrix}\right]')
  out=latex2mathml.converter.convert(normalized,display='block' if m.group(1) is not None else 'inline')
  return '<span class="math-display">'+out+'</span>' if m.group(1) is not None else '<span class="math-inline">'+out+'</span>'
 except Exception as e:math_errors.append({'latex':raw,'error':str(e)});return m.group(0)
def head(title,prefix=''):
 return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="CMOS、SPAD、RGB-D、ISP 与相机画质评价，56讲成像技术精读教材"><title>'+html.escape(title)+' · Imaging Notes</title><link rel="stylesheet" href="'+prefix+'assets/style.css"><link rel="stylesheet" href="'+prefix+'assets/reader.css"></head><body><header><a class="brand" href="'+prefix+'index.html">Imaging Notes<span style="color:#146e6e"> / </span></a><nav><a href="'+prefix+'index.html">课程目录</a><a href="'+prefix+'references.html">文献索引</a><a href="'+prefix+'supplement.html">工程延伸</a><a href="'+prefix+'sources.html">原文对照</a></nav></header>'
def foot():return '<footer>Imaging Notes · 8 周成像技术精读<br>PDF 页码均为阅读器从 1 开始的页序。本站为原创学习解读，不分发原始教材或成批插图。</footer></body></html>'
def sidebar(day):
 out='<aside class="sidebar" aria-label="课程章节"><details class="mobile-contents" open><summary>课程目录 · 展开章节</summary><div>'
 for w,title in enumerate(MODULES,1):
  out+=f'<details {"open" if (day-1)//7+1==w else ""}><summary>W{w:02d} · {title}</summary>'
  for x in outline:
   if x['week']==w:out+=f'<a class="{"active" if x["day"]==day else ""}" href="day-{x["day"]:02d}.html">{x["day"]:02d} · {html.escape(x["title"])}</a>'
  out+='</details>'
 return out+'</div></details></aside>'
search=[];results=[]
for x in outline:
 day=x['day'];frag=ROOT/'lessons'/f'week-{x["week"]:02d}'/f'day-{day:02d}.html'
 if not frag.exists():results.append({'day':day,'status':'pending','han_count':0});continue
 raw=frag.read_text()
 if day in visuals:raw=enrich(raw,visuals[day],TITLES)
 prose=re.split(r'<section[^>]*class=["\']references',raw)[0];han=len(re.findall(r'[\u3400-\u9fff]',plain(prose)))
 raw=re.sub(r'\[(benchmark|ptc|emva|colour|isp|spad|depth)([^<\]]*)\]',citation_link,raw)
 rendered=mathify(re.sub(r'<h1>.*?</h1>','<h1>'+html.escape(x['title'])+'</h1>',raw,count=1,flags=re.S),day)
 page=head(x['title'],'../')+'<div class="reader-layout">'+sidebar(day)+'<main class="reader"><div class="eyebrow">'+f'WEEK {x["week"]:02d} / LESSON {day:02d}'+'</div><p class="reading-meta">器件性能 · 成像系统 · 原文与工程解释分层阅读</p>'+rendered
 page+='<nav class="course-nav" aria-label="课程前后跳转">'
 if day>1:page+=f'<a rel="prev" href="day-{day-1:02d}.html">← 上一讲 · {html.escape(outline[day-2]["title"])}</a>'
 else:page+='<span></span>'
 if day<56:page+=f'<a rel="next" href="day-{day+1:02d}.html">下一讲 · {html.escape(outline[day]["title"])} →</a>'
 page+='</nav></main></div>'+reader_shell()+'<script src="../assets/source-reader.js"></script><script>if(innerWidth<=800)document.querySelector(".mobile-contents").open=false</script>'+foot();(SITE/'articles'/f'day-{day:02d}.html').write_text(page)
 search.append({'day':day,'week':x['week'],'title':x['title'],'text':plain(raw),'url':f'articles/day-{day:02d}.html'})
 results.append({'day':day,'status':'review_ready','han_count':han,'file':str(frag.relative_to(ROOT))})
(SITE/'data'/'search.json').write_text(json.dumps(search,ensure_ascii=False))
(SITE/'data'/'lessons.json').write_text(json.dumps([{**x,'citation_sources':sorted(set(c['source'] for c in citations if c.get('day')==x['day'])),'citation_index':'../citation_index.json'} for x in outline],ensure_ascii=False,indent=2))
(SITE/'citation_index.json').write_text(json.dumps(citations,ensure_ascii=False,indent=2))
(ROOT/'citation_index.json').write_text(json.dumps(citations,ensure_ascii=False,indent=2))
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports'/'build.json').write_text(json.dumps({'lessons':results,'math_errors':math_errors},ensure_ascii=False,indent=2))
progress=readjson(ROOT/'progress.json',[]);completed=sum(x.get('status')=='completed' for x in progress)
idx=head('完整成像技术精读')+'<main class="wrap"><section class="hero"><div class="eyebrow">AN ENGINEERING READING COURSE</div><h1>从光子到图像，<br>从二维到深度。</h1><p>沿着相机的信号链路，理解 CMOS 与 SPAD 的性能边界、ISP 的渲染选择，以及画质和深度测量的评价方法。以七份原始 PDF 为依据，区分文献结论与工程推导。</p><div class="stats"><span><strong>08</strong>周 / 模块</span><span><strong>56</strong>讲课程</span><span><strong>07</strong>份原始资料</span></div></section><div class="tools"><input id="search" type="search" placeholder="搜索全文：转换增益、MTF、白平衡、多径…" aria-label="关键词搜索"><select id="module-filter" aria-label="按模块浏览"><option value="">全部模块</option>'
for w,t in enumerate(MODULES,1):idx+=f'<option value="{w}">W{w:02d} · {t}</option>'
idx+='</select></div><p id="search-count" class="meta">显示 56 / 56 讲</p><p class="notice">阅读说明：正文中的“原文信息”对应标注的 PDF 页与章节；“补充解释 / 推导”用于连接工程指标，不应视为原书实验结论。每讲包含原文短摘、译读、配图及重点公式。点击正文页码可关联本地PDF对照原页。</p><p class="meta"><a href="QUALITY_REPORT.md">56讲核查报告</a> · <a href="README.md">部署说明</a> · <a href="source_catalog.json">资料版本与章节目录</a></p>'
for w,t in enumerate(MODULES,1):
 idx+=f'<section class="module" id="week-{w}"><div class="module-title"><span>WEEK {w:02d}</span><h2>{t}</h2></div><div class="lesson-grid">'
 for x in outline:
  if x['week']!=w:continue
  d=x['day'];r=next((r for r in results if r['day']==d),{});state=next((p.get('status') for p in progress if p['day']==d),'pending');label='精读 · 已核查' if state=='completed' else '正文待验收' if r.get('han_count',0)>0 else '待编写'
  idx+=f'<a class="lesson-card" data-day="{d}" data-week="{w}" href="articles/day-{d:02d}.html"><span class="num">{d:02d}</span><div><h3>{html.escape(x["title"])}</h3><div class="meta">{r.get("han_count",0):,} 字 · 原文摘读 / 图解 / 公式与单位</div><span class="status">{label}</span></div></a>'
 idx+='</div></section>'
idx+='<p id="empty" class="empty hidden">没有找到匹配的课程。请尝试更短的关键词。</p></main><script src="assets/app.js"></script>'+foot();(SITE/'index.html').write_text(idx)
refs=head('文献出处索引')+'<main class="wrap"><section class="hero"><div class="eyebrow">SOURCE ATLAS</div><h1>每个结论，都有来处。</h1><p>按原始资料查阅课程的章节、PDF 页码、公式与图表位置。PDF 页序与印刷页码不可互换。</p><a href="citation_index.json">下载机器可读引用索引</a> · <a href="visual_index.json">图文与短摘索引</a></section>'
for key,title in TITLES.items():
 catalog=readjson(ROOT/'source_catalog.json',{});meta=next((s for s in catalog.get('sources',[]) if s['id']==key),{})
 refs+=f'<section class="source-card" id="{key}"><h2>{html.escape(title)}</h2><p class="meta">{html.escape(meta.get("authors",""))} · {html.escape(meta.get("publication",""))} · {meta.get("pdf_pages","")} PDF页</p>'
 for c in citations:
  if c.get('source')!=key:continue
  day=c.get('day');ch=c.get('chapter','');pp=c.get('pdf_pages',[])
  refs+=f'<div class="cite-entry"><a href="articles/day-{int(day):02d}.html">第 {day} 讲</a> · {html.escape(str(ch))}<br>PDF 页：{html.escape(str(pp))}'
  for f in c.get('figures',[]):refs+=f'<br>图表：{html.escape(str(f.get("number")))} · PDF p.{f.get("pdf_page")}'
  for f in c.get('formulas',[]):refs+=f'<br>公式：{html.escape(str(f.get("label")))} · PDF p.{f.get("pdf_page")} · {"补充推导" if f.get("kind")=="derived" else "原文 / 重述"}'
  refs+='</div>'
 refs+='</section>'
refs+='<section class="source-card"><h2>补充阅读</h2><p><a href="https://github.com/cruxopen/openISP">openISP 项目</a> · <a href="https://docs.imatest.com/docs">Imatest 官方文档</a></p><p><a href="supplement.html">阅读工程资料对照</a>：把具体流水线与MTF指标接到课程概念；不替代各讲所列原始 PDF 证据。</p></section></main>'+foot();(SITE/'references.html').write_text(refs)
shutil.copy2(ROOT/'source_catalog.json',SITE/'source_catalog.json')
(SITE/'visual_index.json').write_text(json.dumps(list(visuals.values()),ensure_ascii=False,indent=2))
(SITE/'sources.html').write_text(build_sources_page(head,foot,readjson(ROOT/'source_catalog.json',{})))
(SITE/'.nojekyll').touch();(SITE/'404.html').write_text(head('页面未找到')+'<main class="wrap"><h1>页面未找到</h1><p><a href="/imaging-notes/">返回课程目录</a></p></main>'+foot())
print(json.dumps({'written':len(search),'math_errors':len(math_errors),'han_min':min((r['han_count'] for r in results),default=0)}))
