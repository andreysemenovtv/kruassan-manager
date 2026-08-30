from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')

def once(old,new,label):
    global s
    c=s.count(old)
    if c!=1:
        raise SystemExit(f'{label}: expected 1 anchor, found {c}')
    s=s.replace(old,new,1)

once('''function getPin(force=false){
  const pin = "123";

  try {
    localStorage.setItem(PIN_KEY, pin);
  } catch(e) {}

  return pin;
}''','''function getPin(){return "123"}''','remove sync PIN storage write')
once('''    jsonpQueue.push(done=>{
      let pin;''','''    const enqueue=action==='write'?'unshift':'push';
    jsonpQueue[enqueue](done=>{
      let pin;''','write priority')
once('''const READ_CACHE_TTL=15000;
const readCache=new Map();
const readInflight=new Map();''','''const READ_CACHE_TTL=15000;
const readCache=new Map();
const readInflight=new Map();
let readGeneration=0;''','cache generation')
once('''  const req=jsonpRequest(type,params,'read').then(data=>{readCache.set(key,{at:Date.now(),data});return data}).finally(()=>readInflight.delete(key));
  readInflight.set(key,req);return req;
}
function clearReadCaches(){readCache.clear();readInflight.clear()}''','''  const generation=readGeneration;
  const req=jsonpRequest(type,params,'read').then(data=>{if(generation===readGeneration)readCache.set(key,{at:Date.now(),data});return data}).finally(()=>{if(readInflight.get(key)===req)readInflight.delete(key)});
  readInflight.set(key,req);return req;
}
function clearReadCaches(){readGeneration++;readCache.clear();readInflight.clear()}''','stale cache protection')
p.write_text(s,encoding='utf-8')
scripts=re.findall(r'<script>(.*?)</script>',s,re.S)
if len(scripts)!=1: raise SystemExit('invalid inline script count')
Path('/tmp/app.js').write_text(scripts[0],encoding='utf-8')
print('Final hotfix prepared')
