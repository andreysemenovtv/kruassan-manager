from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
needle="location.href='training.html'"
if needle not in s:
    marker='    <button class="tile featured" data-open="schedule">'
    tile='''    <button class="tile soft-gold" type="button" onclick="location.href='training.html'">
      <span class="tile-icon">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11v16H6.5A2.5 2.5 0 0 0 4 21V5.5Zm16 0A2.5 2.5 0 0 0 17.5 3H13v16h4.5A2.5 2.5 0 0 1 20 21V5.5Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
      </span>
      <span class="tile-badge">Для менеджеров</span>
      <span class="tile-title">База обучения</span>
      <span class="tile-desc">Методички по должностям: открыть, скачать PDF и распечатать</span>
      <span class="tile-arrow">›</span>
    </button>'''
    if marker not in s:
        raise SystemExit('Homepage tile marker not found')
    s=s.replace(marker,tile+'\n'+marker,1)
    p.write_text(s,encoding='utf-8')
