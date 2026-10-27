# Big 9 domain cutover and search launch

The Vercel build is prepared for **https://www.big9signages.com**. It preserves 24 Blogger article paths, their original publication dates and author data. The site also includes six signage service pages, a gallery, about page, contact page, sitemap and crawler instructions. `content/blogger-posts.json` is the source snapshot; `scripts/build_search.py` rebuilds static pages without network access. The 25 distinct customer images are optimized and hosted locally in `assets/customer/`; `scripts/localize_images.py` is only needed when refreshing the source images.

## Cutover sequence

1. Review the Vercel preview on desktop and mobile. Check every navigation and quote action. Check all 24 old article paths against `content/url-map.json`, including links and gallery assets. Keep a backup of Blogger export and images.
2. Add **www.big9signages.com** to this Vercel project and verify the required DNS records in Vercel before changing them at the domain provider. Keep the apex domain redirected to the same primary host. DNS and old-site publishing are managed outside this repository.
3. Route the existing domain to the new Vercel deployment. The new pages already use the production domain as their canonical URL. Do not remove the old Blogger site or its media until production URLs, redirects, and search indexing have been checked.
4. Confirm article paths return 200, legacy `/p/about.html`, `/p/categorie.html`, `/p/contact-us.html`, `/p/big-9-signages-image-gallery.html` redirect to relevant new pages, and `/sitemap.xml` and `/robots.txt` load on the domain. Verify exact article URL matching; no blanket redirect to the homepage.
5. Verify big9signages.com in Google Search Console and Bing Webmaster Tools. Submit the sitemap and inspect a few important article and service URLs. Update the Google Business Profile with the new website. Check for crawl failures and broken links over the following weeks.

Preview hosts need deployment protection or an account-level noindex setting. Production pages must remain crawlable. The production robots.txt permits OAI-SearchBot for ChatGPT search and blocks GPTBot training by choice. This does not guarantee citation or ranking. Confirm that any Vercel firewall policy allows the legitimate crawler IPs.

## Business information and leads

The number currently shown is +91 9381 556 456, the number published on the existing customer site. Address and hours have not been added because the source did not provide a verified street address or schedule. The contact email on the old site is big9signages@gmail.com; the new quote flow uses WhatsApp. The page prepares the visitor's selections for WhatsApp, where the visitor presses Send. The site does not process or confirm the message, and an n8n bot requires the WhatsApp Business API connection and its own inbound event workflow.

`big9:analytics` events expose event names only. Add a consent-aware analytics provider if required; a WhatsApp handoff event is not a confirmed lead. Real user Core Web Vitals and indexing need measurement after production launch. The site uses locally optimized customer images; source archive remains in `content/` for reproducible builds.
