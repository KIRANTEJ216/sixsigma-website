const menu = document.querySelector('#menu');
const nav = document.querySelector('#nav');
menu?.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
}));

const range = document.querySelector('#compareRange');
range?.addEventListener('input', () => {
  document.querySelector('#comparison').style.setProperty('--split', `${range.value}%`);
});

const demo = new URLSearchParams(location.search).get('demo') === '1';
const form = document.querySelector('#quoteForm');
const status = document.querySelector('#formStatus');
const submit = form.querySelector('[type="submit"]');
const fallback = document.querySelector('#quoteFallback');
let requestId;

if (demo) {
  const reviewStrip = document.querySelector('.review-strip');
  if (reviewStrip) reviewStrip.textContent = 'PRIVATE DESIGN REVIEW · Quotations are simulated on this preview';
  document.querySelector('.quote-layout > div > p').textContent = 'Explore the form in demo mode. No request will be sent.';
  submit.firstChild.textContent = 'Preview quote acknowledgement ';
  status.textContent = 'No request will be sent from this preview.';
}

form.addEventListener('input', () => {
  requestId = undefined;
  fallback.hidden = true;
  status.className = '';
});

form.addEventListener('submit', async event => {
  event.preventDefault();
  status.className = '';
  fallback.hidden = true;
  const data = new FormData(form);
  const required = ['name', 'phone', 'company', 'email', 'city'];
  const missing = required.find(key => !String(data.get(key) || '').trim());
  if (missing) {
    status.textContent = 'Please complete your name, phone, company, email and location.';
    status.className = 'error';
    form.elements[missing].focus();
    return;
  }
  const email = String(data.get('email')).trim();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) {
    status.textContent = 'Please enter a valid email address.';
    status.className = 'error';
    form.elements.email.focus();
    return;
  }
  if (String(data.get('phone')).replace(/\D/g, '').length < 8) {
    status.textContent = 'Please enter a number we can reach you on.';
    status.className = 'error';
    form.elements.phone.focus();
    return;
  }

  const lines = [
    `Name: ${data.get('name')}`,
    `Company: ${data.get('company')}`,
    `Phone: ${data.get('phone')}`,
    `Email: ${email}`,
    `Dimensions: ${data.get('dimensions') || 'To be measured'}`,
    `Signage types: ${data.getAll('signage').join(', ') || 'Please advise'}`,
    `City: ${data.get('city')}`,
    data.get('message') ? `Message:\n${data.get('message')}` : ''
  ].filter(Boolean);
  const whatsapp = `https://wa.me/919381556456?text=${encodeURIComponent(lines.join('\n'))}`;

  if (demo) {
    status.textContent = `Preview acknowledgement for ${String(data.get('company')).trim()}: your enquiry details look ready. No request was sent.`;
    status.className = 'success';
    return;
  }

  if (submit.disabled) return;
  requestId ||= crypto.randomUUID();
  const payload = {
    event: 'quote.requested', version: 1, requestId,
    submittedAt: new Date().toISOString(),
    source: location.origin + location.pathname,
    customer: {name: data.get('name'), phone: data.get('phone'), email, company: data.get('company')},
    quote: {city: data.get('city'), signageTypes: data.getAll('signage'), dimensions: data.get('dimensions') || '', message: data.get('message') || ''},
    contactPreference: 'customer_initiated_whatsapp'
  };
  submit.disabled = true;
  status.textContent = 'Saving your request…';
  try {
    const response = await fetch('/api/quote', {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload), signal: AbortSignal.timeout(15000)
    });
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.message || 'Request not accepted');
    }
    const ack = await response.json();
    if (ack.accepted !== true || ack.requestId !== requestId) throw new Error('Missing acknowledgement');
    status.textContent = 'Your quotation request has been received. Your details were accepted; you can continue on WhatsApp.';
    status.className = 'success';
    fallback.textContent = 'Continue on WhatsApp';
    fallback.href = whatsapp;
    fallback.hidden = false;
  } catch (error) {
    status.textContent = error.message === 'WEBHOOK_UNAVAILABLE'
      ? 'Our enquiry service is temporarily unavailable. Please continue on WhatsApp.'
      : 'We could not confirm that your request was saved. Retry, or continue on WhatsApp below.';
    status.className = 'error';
    fallback.textContent = 'Continue on WhatsApp';
    fallback.href = whatsapp;
    fallback.hidden = false;
  } finally {
    submit.disabled = false;
  }
});

const dialog = document.querySelector('#previewDialog');
document.querySelector('#waPreview')?.addEventListener('click', () => {
  if (demo) dialog.showModal();
  else location.href = 'https://wa.me/919381556456';
});
document.querySelector('#closeDialog')?.addEventListener('click', () => dialog.close());
