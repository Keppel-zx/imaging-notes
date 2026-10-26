from pathlib import Path
import json,re,html

def esc(s):return html.escape(str(s))
def load_visuals(root):
 data={}
 for p in sorted((root/'visuals').glob('week-*.json')):
  rows=json.loads(p.read_text())
  if isinstance(rows,dict):rows=rows.get('lessons',rows.get('records',[]))
  for row in rows:data[int(row['day'])]=row
 return data

def source_button(source,page,text='对照原页'):
 return f'<button type="button" class="source-open" data-source="{esc(source)}" data-page="{int(page)}">{esc(text)} <span aria-hidden="true">↗</span></button>'

def excerpt_block(v,titles):
 e=v['excerpt'];book=titles[e['source']]
 return f'''<section class="reading-excerpt" id="source-excerpt"><div class="section-heading"><div><div class="block-kicker">READ THE SOURCE</div><h2>原文短摘 · 对照阅读</h2></div>{source_button(e['source'],e['pdf_page'])}</div><div class="excerpt-provenance">{esc(book)} · {esc(e['chapter'])} · PDF第{e['pdf_page']}页</div><div class="parallel-reading"><blockquote lang="en"><span class="small-label">英文原文</span><p>“{esc(e['en'])}”</p></blockquote><div class="translation"><span class="small-label">中文译读</span><p>{esc(e['zh'])}</p></div></div><div class="excerpt-comment"><strong>这句话怎么读</strong><p>{esc(e['comment'])}</p></div></section>'''

def figure_block(v,titles,figure_id="{esc(figure_id)}"):
 f=v['figure'];is_original=f['kind']=='original_crop';tag='原图局部' if is_original else '自绘图解';src=f['path'].removeprefix('../').removeprefix('/')
 if src.startswith('site/'):src=src[5:]
 provenance=f'{titles[f["source"]]} · PDF第{f["pdf_page"]}页'
 if f.get('figure_number'):provenance+=' · '+('原图号 ' if is_original else '参照原图 ')+str(f['figure_number'])
 return f'''<figure class="lesson-figure" id="{esc(figure_id)}"><div class="figure-header"><span class="figure-kind {'original' if is_original else 'redrawn'}">{tag}</span><h3>{esc(f['title'])}</h3></div><button type="button" class="figure-zoom" data-zoom="../{esc(src)}" data-alt="{esc(f['alt'])}" aria-label="放大查看：{esc(f['title'])}"><img src="../{esc(src)}" alt="{esc(f['alt'])}" loading="lazy"><span class="zoom-label">放大查看 ↗</span></button><figcaption><p>{esc(f['caption'])}</p><div class="figure-source">{esc(provenance)} {source_button(f['source'],f['pdf_page'])}</div></figcaption><div class="figure-insight"><strong>看图抓住什么</strong><p>{esc(f['explanation'])}</p></div></figure>'''

def formula_block(v,titles):
 q=v['key_formula'];label='原文公式 / 等价重述' if q['kind']=='source' else '补充推导 / 教学模型';n=q.get('original_number');loc=f'{titles[q["source"]]} · PDF第{q["pdf_page"]}页'+(f' · 式({n})' if n else '')
 table=''.join('<tr><td>\\('+esc(x['symbol'])+'\\)</td><td>'+esc(x['meaning'])+'</td><td>'+esc(x['unit'])+'</td></tr>' for x in q['variables'])
 return f'''<div class="key-equation" id="key-equation"><div class="section-heading"><div><div class="block-kicker">KEY RELATION</div><h3>{esc(q['label'])}</h3></div><span class="equation-kind">{label}</span></div><div class="equation-display">\\[{q['tex']}\\]</div><div class="equation-location">{esc(loc)} {source_button(q['source'],q['pdf_page'])}</div><table class="variable-table"><thead><tr><th>符号</th><th>物理 / 工程意义</th><th>单位或量纲</th></tr></thead><tbody>{table}</tbody></table><p class="equation-meaning">{esc(q['meaning'])}</p></div>'''

def inject_after_heading_section(raw,pattern,block):
 match=re.search(r'(<section\b[^>]*>\s*<h2>[^<]*(?:'+pattern+r')[^<]*</h2>)',raw,re.S)
 if match:return raw[:match.end()]+block+raw[match.end():]
 return raw

def enrich(raw,v,titles):
 # One meaningful primary-source sentence is shown before the explanatory prose.
 m=re.search(r'<section\b[^>]*class=["\']source["\'][^>]*>.*?</section>',raw,re.S)
 block=excerpt_block(v,titles)
 if m:raw=raw[:m.end()]+block+raw[m.end():]
 else:raw=raw.replace('</h1>','</h1>'+block,1)
 figures=figure_block(v,titles)+''.join(figure_block({'figure':f},titles,f'lesson-figure-{i}') for i,f in enumerate(v.get('extra_figures',[]),2))
 raw=inject_after_heading_section(raw,'原图|图表|图解',figures)
 raw=inject_after_heading_section(raw,'公式|推导|数学|关系',formula_block(v,titles))
 # Display substantive equations separately in the derivation, preserving exact TeX.
 def promote(m):
  t=m.group(1)
  return '\\['+t+'\\]' if '=' in t and (len(t)>45 or '\\frac' in t or '\\sum' in t) else m.group(0)
 raw=re.sub(r'\\\((.*?)\\\)',promote,raw,flags=re.S)
 return raw

def citation_link(m):
 source=m.group(1);text=m.group(0);p=re.search(r'(?:p{1,2}\.?\s*|PDF\s*)(\d+)',m.group(2),re.I)
 if p:return f'<a class="cite source-cite" data-source="{source}" data-page="{p.group(1)}" href="../sources.html?source={source}&amp;page={p.group(1)}">{text}<span class="cite-icon" aria-hidden="true"> ↗</span></a>'
 return f'<a class="cite" href="../references.html#{source}">{text}</a>'

def reader_shell():
 return '''<aside class="reference-panel" id="reference-panel" hidden aria-labelledby="reference-title"><div class="reference-top"><span class="block-kicker">SOURCE COMPANION</span><button type="button" class="close-panel" aria-label="关闭原文对照">×</button></div><h2 id="reference-title">原文对照</h2><p id="reference-location"></p><div id="reference-state"></div><iframe id="reference-pdf" title="本地原始PDF对照阅读" hidden></iframe><a id="reference-newtab" target="_blank" rel="noopener" hidden>在新标签页打开原文 ↗</a><p class="privacy-note">关联的PDF仅保存在此浏览器，不上传到网站。短摘、图解与公式无需关联文件即可阅读。</p></aside><dialog id="image-lightbox"><button type="button" class="lightbox-close" aria-label="关闭放大图">×</button><img alt=""><p></p></dialog>'''

def build_sources_page(head,foot,catalog):
 cards=''
 for s in catalog['sources']:
  cards+=f'''<section class="book-binding" data-book="{esc(s['id'])}"><div class="book-number">PDF</div><div><h2>{esc(s['title'])}</h2><p class="meta">{esc(s['publication'])} · 课程采用版本 {s['pdf_pages']}页</p><p class="binding-status" data-status="{esc(s['id'])}">尚未关联本地文件</p><div class="binding-actions"><button type="button" class="bind-pdf" data-source="{esc(s['id'])}">关联本地PDF</button><button type="button" class="remove-pdf" data-source="{esc(s['id'])}">移除关联</button>{source_button(s['id'],1,'打开原书')}</div></div></section>'''
 return head('原文对照')+'''<main class="wrap sources-page"><section class="hero"><div class="eyebrow">YOUR BOOKS, SIDE BY SIDE</div><h1>让原文，留在手边。</h1><p>每讲已嵌入原文短摘、译读、图解与重点公式。需要完整上下文时，可关联你持有的对应PDF；点击课程中的页码，原页会在旁边打开。</p><p class="notice">选择文件只在此浏览器内建立关联，不会把整本书上传或发布到GitHub。PDF页序从1开始；同名书的不同版本可能具有不同页码。</p></section>'''+cards+'''<p class="meta">如果浏览器无法内嵌PDF，请使用面板中的“在新标签页打开原文”。清除浏览器网站数据会同时清除关联文件。</p></main>'''+reader_shell()+'''<script src="assets/source-reader.js"></script>'''+foot()
