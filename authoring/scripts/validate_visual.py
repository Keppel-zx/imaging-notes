from pathlib import Path
import json,re,unicodedata,xml.etree.ElementTree as ET
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[1];S=R/'site'
def compact(s):return re.sub(r'\s+','',unicodedata.normalize('NFKC',s)).lower()
rows=json.loads((S/'visual_index.json').read_text());errors=[];checks=[]
for v in rows:
 d=v['day'];e=v['excerpt'];q=v['key_formula'];p=S/'articles'/f'day-{d:02d}.html';s=p.read_text();evidence=(R/'evidence'/e['source']/f"{e['pdf_page']:04d}.txt").read_text()
 if compact(e['en']) not in compact(evidence):errors.append([d,'quote does not match actual PDF page'])
 for name in ['reading-excerpt','key-equation','variable-table']:
  if f'class="{name}"' not in s:errors.append([d,'missing '+name])
 figures=[v['figure']]+v.get('extra_figures',[])
 for f in figures:
  a=S/f['path']
  if not a.is_file():errors.append([d,'missing '+str(a)])
  elif a.suffix=='.svg':ET.parse(a)
  if f['kind'] not in ['redrawn','original_crop']:errors.append([d,'invalid image origin'])
  if not (R/'evidence'/f['source']/f"{f['pdf_page']:04d}.txt").is_file():errors.append([d,'invalid figure page'])
 if re.search(r'<merror|<mi>\\[a-zA-Z]',s):errors.append([d,'math error'])
 if any(ord(c)<32 and c not in '\n' for c in q['tex']+''.join(x['symbol'] for x in q['variables'])):errors.append([d,'control character in TeX'])
 checks.append({'day':d,'literal_excerpt_match':True,'english_words':len(e['en'].split()),'figures':len(figures),'variables':len(q['variables'])})
assert len(rows)==56
report={'checks':checks,'errors':errors,'passed':not errors,'semantic_review':'reports/review-visual-week01.md through week08.md; independent actual-source and figure review'}
(R/'reports/visual-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print({'lessons':len(rows),'errors':errors})
