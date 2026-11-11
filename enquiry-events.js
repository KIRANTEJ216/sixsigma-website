// Privacy-preserving integration hooks. No analytics provider or storage by default.
// Subscribers receive event names only, never contact details or message contents.
(() => {
  const emit = name => window.dispatchEvent(new CustomEvent('big9:analytics', {detail:{event:name}}));
  let started=false;
  document.addEventListener('input', event => {
    if (!started && event.target.closest('[data-quote]')) {started=true;emit('quote_started');}
  });
  document.addEventListener('change', event => {
    if (event.target.name==='signageTypes') emit('signage_selection_changed');
  });
  document.addEventListener('click', event => {
    const link=event.target.closest('a');
    if(link && link.href.startsWith('https://wa.me/')) emit('whatsapp_handoff_clicked');
  });
})();
