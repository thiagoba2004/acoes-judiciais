#!/usr/bin/env python3
import argparse,json,math,re,unicodedata
from pathlib import Path

def n(s):
    return re.sub(r'\s+',' ',unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode('ascii').lower()).strip()

def tokens(s):
    return [x for x in re.findall(r'[a-z0-9]+', n(s)) if x]

def blob(r):
    x=[r.get('path',''),r.get('title',''),' '.join(r.get('headings',[])),
       ' '.join(r.get('keywords',[])),' '.join(r.get('semantic_tags',[])),
       ' '.join(r.get('external_domains',[])),' '.join(r.get('source_systems',[]))]
    for v in r.get('identifiers',{}).values():
        x.append(' '.join(v))
    return n(' '.join(x))

def field_values(r):
    return {
        'path':n(r.get('path','')),
        'title':n(r.get('title','')),
        'headings':n(' '.join(r.get('headings',[]))),
        'keywords':n(' '.join(r.get('keywords',[]))),
        'semantic_tags':n(' '.join(r.get('semantic_tags',[]))),
        'external_domains':n(' '.join(r.get('external_domains',[]))),
        'source_systems':n(' '.join(r.get('source_systems',[]))),
        'identifiers':n(' '.join(' '.join(v) for v in r.get('identifiers',{}).values())),
    }

FIELD_WEIGHTS={'title':12,'semantic_tags':10,'source_systems':10,'path':8,
               'headings':7,'identifiers':14,'keywords':5,'external_domains':3}

def legacy_score(r,terms):
    b=blob(r);f=field_values(r);s=0
    for q in terms:
        if q not in b:return 0
        s+=12 if q in f['title'] else 0
        s+=10 if q in f['semantic_tags'] else 0
        s+=10 if q in f['source_systems'] else 0
        s+=8 if q in f['path'] else 0
        s+=3
    return s

def soft_score(r,terms,phrases,idf):
    f=field_values(r);b=blob(r);matched=set();s=0.0
    for q in terms:
        hits=[]
        for name,value in f.items():
            if q in value:
                hits.append(FIELD_WEIGHTS[name])
        if hits:
            matched.add(q)
            s += max(hits) * idf.get(q,1.0)
    coverage=len(matched)/len(set(terms)) if terms else 0
    min_terms=max(1,math.ceil(len(set(terms))*0.35))
    if len(matched)<min_terms:return 0
    s += coverage*6
    for phrase in phrases:
        if phrase and phrase in b:
            s += 18 + 4*len(tokens(phrase))
    return round(s,6)

ap=argparse.ArgumentParser()
ap.add_argument('query')
ap.add_argument('indexes',nargs='+')
ap.add_argument('--limit',type=int,default=20)
ap.add_argument('--match-mode',choices=('all','soft'),default='all')
a=ap.parse_args()

terms=[n(x) for x in a.query.split() if n(x)]
records=[]
for idx in a.indexes:
    for line in Path(idx).read_text(encoding='utf-8').splitlines():
        if line.strip():records.append((idx,json.loads(line)))

if a.match_mode=='all':
    hits=[(legacy_score(r,terms),idx,r) for idx,r in records]
    hits=[x for x in hits if x[0]]
else:
    df={q:0 for q in set(terms)}
    for _,r in records:
        b=blob(r)
        for q in df:
            if q in b:df[q]+=1
    total=max(1,len(records))
    idf={q:math.log((total+1)/(df[q]+1))+1 for q in df}
    phrases=[]
    raw=n(a.query)
    if re.search(r'\b(tema|adpf|adi|adc|are|resp|rms|sumula|resolucao)\b',raw):
        phrases.append(raw)
    hits=[(soft_score(r,terms,phrases,idf),idx,r) for idx,r in records]
    hits=[x for x in hits if x[0]]

for s,idx,r in sorted(hits,key=lambda x:(-x[0],x[2].get('path','')))[:a.limit]:
    print(json.dumps({'score':s,'match_mode':a.match_mode,'index':idx,**r},ensure_ascii=False))
