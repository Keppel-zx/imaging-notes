from pathlib import Path
from html.parser import HTMLParser
import json,re,collections,urllib.parse,xml.etree.ElementTree as ET,unicodedata
ROOT=Path(__file__).resolve().parents[1];SITE=ROOT/'site'
class Doc(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.links=[];self.tags=collections.Counter();self.stack=[];self.errors=[]
 def handle_starttag(self,t,a):
  self.tags[t]+=1;a=dict(a)
  if 'href' in a:self.links.append(a['href'])
  if 'src' in a:self.links.append(a['src'])
 def handle_data(self,d):self.text.append(d)
def text(s):p=Doc();p.feed(s);return ' '.join(p.text)
def compact(s):return re.sub(r'\s+','',unicodedata.normalize('NFKC',s)).lower()
checks=[];errors=[];notes=[]
for day in range(1,57):
 p=SITE/'articles'/f'day-{day:02d}.html'
 if not p.exists():errors.append({'day':day,'error':'missing page'});continue
 s=p.read_text();d=Doc();d.feed(s)
 frag=ROOT/'lessons'/f'week-{(day-1)//7+1:02d}'/f'day-{day:02d}.html';raw=frag.read_text();body=re.split(r'<section[^>]*class=["\']references',raw)[0]
 han=len(re.findall(r'[\u3400-\u9fff]',text(body)))
 if han<2000 or han>3200:errors.append({'day':day,'error':'Han prose count outside 2000–3200 tolerance','count':han})
 for term in ['阅读定位','核心结论','文献出处']:
  if term not in raw:errors.append({'day':day,'error':'missing section '+term})
 if re.search(r'<mi>\\[A-Za-z]',s):errors.append({'day':day,'error':'unsupported math command in MathML'})
 if re.search(r'\\\[|\\\(',s):errors.append({'day':day,'error':'unconverted TeX delimiter'})
 if 'name="viewport"' not in s:errors.append({'day':day,'error':'no viewport'})
 if day>1 and f'href="day-{day-1:02d}.html"' not in s:errors.append({'day':day,'error':'previous link missing'})
 if day<56 and f'href="day-{day+1:02d}.html"' not in s:errors.append({'day':day,'error':'next link missing'})
 for u in d.links:
  if not u or u.startswith(('http:','https:','mailto:','#','data:')):continue
  target=(p.parent/urllib.parse.unquote(u.split('#')[0].split('?')[0])).resolve()
  if not target.is_file():errors.append({'day':day,'error':'broken link','url':u})
 if re.search(r'待补充|TODO|占位|尚未编写',raw,re.I):errors.append({'day':day,'error':'placeholder marker'})
 checks.append({'day':day,'han_count':han,'math_elements':d.tags['math'],'links':len(d.links),'page_bytes':p.stat().st_size})
cites=json.loads((ROOT/'citation_index.json').read_text());by=collections.defaultdict(list)
for c in cites:
 day=c.get('day');by[day].append(c);source=c.get('source');pp=c.get('pdf_pages',[])
 for n in pp:
  if not isinstance(n,int) or not (ROOT/'evidence'/str(source)/f'{n:04d}.txt').is_file():errors.append({'day':day,'error':'invalid PDF page','source':source,'page':n})
 for group in ['formulas','figures']:
  for a in c.get(group,[]):
   n=a.get('pdf_page');p=ROOT/'evidence'/str(source)/f'{n:04d}.txt' if isinstance(n,int) else None
   if not p or not p.exists():errors.append({'day':day,'error':'invalid anchor page','anchor':a});continue
   txt=p.read_text();number=a.get('original_number') if group=='formulas' else a.get('number')
   if number and group=='figures':
    # Candidate presence is a text-level check; figure identity is reviewed separately.
    digits=re.findall(r'\d+(?:\.\d+)?',str(number))
    if digits and not all(n in txt for n in digits):notes.append({'day':day,'note':'figure label requires visual verification','anchor':a})
   if number and group=='formulas' and not all(n in txt for n in re.findall(r'\d+(?:\.\d+)?',str(number))):notes.append({'day':day,'note':'equation number text not found, visual check','anchor':a})
 q=c.get('quote')
 if q and q.get('text'):
  n=q.get('pdf_page');p=ROOT/'evidence'/str(source)/f'{n:04d}.txt'
  if p.exists() and compact(q['text']) not in compact(p.read_text()):notes.append({'day':day,'note':'quote text requires manual check','quote':q})
for day in range(1,57):
 if not by[day]:errors.append({'day':day,'error':'citation entry missing'})
report={'scope':'Static links, 56 course bodies, Han count, citation page existence, formula conversion, navigation and responsive markup. Text label checks do not replace semantic/visual source review.','checks':checks,'errors':errors,'manual_review_notes':notes,'citation_entries':len(cites),'passed_automated':not errors}
(ROOT/'reports'/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps({'pages':len(checks),'errors':len(errors),'notes':len(notes),'citations':len(cites)}))
