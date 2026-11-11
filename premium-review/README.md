# Big 9 premium design review

Open `/premium-review/review.html` to compare desktop, tablet, and mobile layouts, or `/premium-review/` for the standalone homepage concept. The same reviewed concept is available at the private ChatGPT Site link shared with the owner.

This folder is intentionally separate from the production homepage. Its quote form validates required name, phone, company, email, city, and signage choices, then displays a simulated acknowledgement. It does not call `/api/quote`, n8n, or WhatsApp. The before/after images are labeled as an illustrative concept.

This branch starts at draft PR #2 (`24c2dd9`) so the preserved Blogger articles, service pages, and image paths resolve. PR #2 is unmerged and has unrelated Git history from `main`; the production quote proxy merged in PR #5 is therefore not part of this branch. Reconcile these histories and the quote flow before replacing the live homepage. Do not merge this review branch directly for domain cutover.
