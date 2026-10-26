from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
inv=json.loads((R/'source_inventory.json').read_text())
names={'benchmark':('Camera Image Quality Benchmarking','Jonathan B. Phillips; Henrik Eliasson','Wiley, 2018'),'ptc':('Photon Transfer: DN → λ','James R. Janesick','SPIE, 2007'),'emva':('EMVA Standard 1288: Standard for Characterization of Image Sensors and Cameras, Release 3.1','European Machine Vision Association','30 December 2016'),'colour':('Fundamentals and Applications of Colour Engineering','Phil Green (editor)','Wiley, 2024 (actual PDF copyright; filename says 2023)'),'isp':('Understanding the in-camera rendering pipeline & the role of AI and deep learning','Michael S. Brown','ICCV 2023 tutorial slides (uploaded PDF)'),'depth':('Time-of-Flight and Structured Light Depth Cameras: Technology and Applications','Pietro Zanuttigh; Giulio Marin; Carlo Dal Mutto; Fabio Dominio; Ludovico Minto; Guido Maria Cortelazzo','Springer, 2016'),'spad':('TOF Range-Imaging Cameras','Fabio Remondino; David Stoppa (editors)','Springer, 2013')}
items=[]
for s in inv['sources']:
 k=s['id'];title,authors,pub=names[k];toc=s['toc']
 if k=='ptc':
  # PDF contains a scrambled bookmark font. Derive verified chapter starts from page headers.
  toc=[]
  chapters=['Introduction','Photon Interaction','Photon Transfer Noise Sources','Photon Transfer Theory','Photon Transfer Curve','e−/DN Variance','Nonlinearity','Flat Fielding','Modulation Photon Transfer','Signal-to-noise Performance','Read Noise','Lux Transfer']
  for num,title2 in enumerate(chapters,1):
   for f in sorted((R/'evidence'/k).glob('*.txt')):
    text=f.read_text()
    if re.search(r'Chapter\s+'+str(num)+r'\b',text) and int(f.stem)>7:
     toc.append([1,f'{num} {title2}',int(f.stem)]);break
 if k=='benchmark' and any(str(e[1])=='ch1' for e in toc):
  chapter_titles=['Introduction','Defining Image Quality','Image Quality Attributes','The Camera','Subjective Image Quality Assessment—Theory and Practice','Objective Image Quality Assessment—Theory and Practice','Perceptually Correlated Image Quality Metrics','Measurement Protocols—Building Up a Lab','The Camera Benchmarking Process','Summary and Conclusions']
  toc=[[1,f'{i+1} {title2}',entry[2]] for i,(title2,entry) in enumerate(zip(chapter_titles,toc[2:12]))]
 if k=='isp':
  toc=[] # Slide deck has no formal embedded chapters; cited page locations live in citation_index.json
 items.append({'id':k,'title':title,'authors':authors,'publication':pub,'pdf_pages':s['pages'],'sha256':s['sha256'],'page_rule':'1-based PDF viewer page. Printed folio cited separately when checked.','chapters':toc})
(R/'source_catalog.json').write_text(json.dumps({'sources':items,'supplementary':[{'title':'openISP','url':'https://github.com/cruxopen/openISP'},{'title':'Imatest documentation','url':'https://docs.imatest.com/docs'}]},ensure_ascii=False,indent=2))
print([(x['id'],len(x['chapters'])) for x in items])
