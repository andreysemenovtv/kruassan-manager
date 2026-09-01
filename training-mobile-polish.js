(()=>{
  const shortLabel=(text)=>text==='Специалист по активным продажам'?'Активные продажи':text;
  function polishTabs(){
    document.querySelectorAll('#tabs .tab').forEach(btn=>{
      const full=btn.dataset.fullLabel||btn.textContent.trim();
      btn.dataset.fullLabel=full;
      btn.textContent=shortLabel(full);
      if(full!==btn.textContent) btn.setAttribute('aria-label',full);
    });
    const active=document.querySelector('#tabs .tab.active');
    if(active) requestAnimationFrame(()=>active.scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'}));
  }
  const tabs=document.getElementById('tabs');
  if(tabs){new MutationObserver(polishTabs).observe(tabs,{childList:true,subtree:true});polishTabs();}
})();
