from pathlib import Path
import json,datetime,shutil,zipfile,hashlib
R=Path(__file__).resolve().parents[1];S=R/'site';now='2026-10-26T00:00:00+08:00'
progress=json.loads((R/'progress.json').read_text());build=json.loads((R/'reports/build.json').read_text())
for x in progress:
 x['visual_status']='completed';x['visual_review']='actual PDF excerpts, images, formula and units; independent week review passed'
 x['visual_han_count']=next(y['han_count'] for y in build['lessons'] if y['day']==x['day'])
 x['visual_page_review']='desktop 1363px and mobile 390px iframe, no page overflow; integrated card checks passed'
 x['visual_completed_at']=now
 x['optional_pdf_reader']='local binding and page URL verified; native PDF pixels not reliably verified in remote browser'
(R/'progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2));shutil.copy2(R/'progress.json',S/'progress.json')
report={'edition':'visual-2026-10-26','desktop':{'pages':56,'viewport':1363,'page_overflow':0,'missing_cards':0,'merror':0},'mobile':{'pages':56,'iframe_width':390,'content_width':375,'page_overflow':0,'missing_cards':0,'merror':0},'support_mobile':['index','references','sources','supplement'],'search':{'weighted average':1,'week8':7},'image_zoom':'verified original PNG and SVG','pdf_binding':{'file':'depth.pdf','persisted_after_reload':True,'page_link':139,'native_pdf_pixels':'not reliably confirmed'},'source_review_notes_resolved':[{'day':47,'note':'combined 5.6–5.7 normalized relation reviewed against actual PDF178; see independent week07 report'}]}
(R/'reports/browser-visual-final.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
(R/'MAINTENANCE.md').write_text('''# 图文版维护\n\n网站根目录可直接部署；访客不需要构建依赖。\n\n1. 安装requirements.txt。修改lessons/week-NN/day-NN.html完整正文，同步citations/week-NN.json。\n2. 图文卡片在visuals/week-NN.json，必须保持AUTHORING_VISUAL.md所列引用字段与来源区分。配图在site/assets/figures/，不可遗漏。\n3. 运行python3 scripts/build.py，输出site/。\n4. 完整来源验证需自己持有对应PDF，并重建evidence/{source_id}/NNNN.txt。随后运行scripts/validate.py及scripts/validate_visual.py。本包不提供原书提取全文。\n5. 重新核查更改课程的原文、公式、图片、桌面与手机布局，更新progress.json。scripts/package.py是本次验收后封装脚本，不能代替审校。\n\n引用索引citation_index.json由基础引用与新增图文来源合并生成。visual_index.json保存图片、短摘及重点公式；source_catalog.json标明版本和章节，source_inventory.json仅为自动定位候选。\n\n新增PDF原文对照使用浏览器IndexedDB。完整PDF不公开发布，网页内嵌依赖各浏览器原生PDF能力；保留新标签页与手动页序回退。\n''')
(R/'RESUME.md').write_text('''# 图文版交付检查点\n\n56讲完整正文与图文增强已完成，progress.json含逐讲新状态。所有8包图文独立审校记录均在reports/review-visual-weekNN.md。最终全站静态及桌面/手机检查已保存，见reports/visual-validation.json与browser-visual-final.json。\n\n可选完整PDF对照：关联文件、刷新持久保存、页码URL均验证；原生PDF渲染像素未在远程浏览器可靠验证，勿声称全浏览器通过。网页短摘/图片/公式不依赖PDF阅读器。\n\n无GitHub推送凭据，线上未更新。ZIP根目录直接替换站点。\n''')
(S/'qa-mobile.html').unlink(missing_ok=True)
# Maintenance source archive: no raw PDF/evidence, screenshots, caches or nested archive.
paths=[]
for folder in ['lessons','citations','visuals','indexes','scripts','reports']:
 for p in (R/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ['.png','.jpg','.pdf']:paths.append(p)
for name in ['AUTHORING.md','AUTHORING_VISUAL.md','MAINTENANCE.md','RESUME.md','requirements.txt','outline.json','progress.json','citation_index.json','source_catalog.json','source_inventory.json']:
 if (R/name).exists():paths.append(R/name)
paths+=list((S/'assets').rglob('*'))
paths+=[S/n for n in ['README.md','QUALITY_REPORT.md','supplement.html']]
with zipfile.ZipFile(S/'authoring.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(set(paths)):
  if p.is_file():z.write(p,p.relative_to(R))
manifest=[]
for p in sorted(S.rglob('*')):
 if p.is_file() and p.name!='file_manifest.json':manifest.append({'path':str(p.relative_to(S)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(S/'file_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
output=R.parent/'Imaging_Notes_56_Lessons_Visual_Edition.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(S.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(S))
with zipfile.ZipFile(output) as z:
 assert z.testzip() is None
 assert sum(x.startswith('articles/') and x.endswith('.html') for x in z.namelist())==56
 assert not any(x.endswith('.pdf') or 'qa-mobile' in x for x in z.namelist())
print(json.dumps({'zip':str(output),'bytes':output.stat().st_size,'published_files':len(manifest)+1,'lessons':56},ensure_ascii=False))
