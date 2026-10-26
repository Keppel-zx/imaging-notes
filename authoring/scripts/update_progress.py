from pathlib import Path
import json,re,datetime
R=Path(__file__).resolve().parents[1];p=R/'progress.json';data=json.loads(p.read_text())
for x in data:
 f=R/'lessons'/f'week-{x["week"]:02d}'/f'day-{x["day"]:02d}.html'
 if x.get('status')=='completed':continue
 if f.exists():
  x['status']='draft';x['file']=str(f.relative_to(R));x['han_count_preliminary']=len(re.findall('[\u3400-\u9fff]',re.sub('<[^>]+>','',f.read_text().split('<section class="references"')[0])))
 else:x['status']='pending'
 x['updated_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
p.write_text(json.dumps(data,ensure_ascii=False,indent=2));print({s:sum(x['status']==s for x in data) for s in ['pending','draft','review_ready','completed']})
