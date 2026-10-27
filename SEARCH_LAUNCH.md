# Search and blog launch

24 articles are imported from the public Blogger feed, with original URL paths, author names and published/updated dates. Source export and URL/image manifests are in content/. Article scripts, inline styles, executable handlers and embeds are stripped. Images remain on the customer's Blogger hosting; retain that account and media until local copies are verified.

## Rebuild
Python 3 plus lxml: `python scripts/build_search.py`. Set SITE_URL to the deployed production origin. Default is the existing Vercel production site. Homepage metadata and BRAND.url must be changed to the same origin during domain cutover.

While the old blog is live, imported articles intentionally canonicalize to their originals and are excluded from the new sitemap. Do not expect duplicate article URLs to rank independently. At domain cutover, run with SITE_URL=https://www.big9signages.com; article paths stay identical and enter the sitemap. Verify all 24 paths before changing DNS. Keep an export of the Blogger account. Inventory static pages, labels, media and externally linked URLs beyond the 24 posts before cutover; this is not an exhaustive old-site migration.

## Required owner/account tasks
- Verify the domain in Google Search Console and Bing Webmaster Tools; submit sitemap.xml and inspect representative URLs.
- Confirm actual address, opening hours and Google Business Profile URL before adding them. No address, ratings or warranty has been invented.
- Check Vercel firewall rules permit Googlebot, Bingbot and OpenAI's published OAI-SearchBot IPs. robots.txt permits search bots while opting GPTBot out of training; it does not guarantee discovery or citation.
- Configure preview deployment protection/noindex so branch hosts are not indexed. Do not add noindex to the production deployment.
- Confirm WhatsApp Business/n8n integration separately. This site prepares a message; it does not send it or activate a bot.

## Measurements
`big9:analytics` CustomEvents expose event names only. Attach a consent-aware analytics sink if desired. quote_started, signage_selection_changed, whatsapp_handoff_prepared and whatsapp_handoff_clicked are not confirmed leads. Confirmed leads require a WhatsApp/n8n inbound event and an attribution design.

## Remaining launch QA
Verify desktop/mobile, reduced-motion mode, light/dark themes, article images, keyboard controls and WhatsApp message content on the deployed preview. Measure real Core Web Vitals after launch; do not infer scores from static checks. No AI-search ranking guarantee or special llms.txt requirement is claimed.
