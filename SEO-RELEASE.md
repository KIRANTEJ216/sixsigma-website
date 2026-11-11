# SEO release requirements

Canonical production domain: https://www.big9signages.com/ (confirm www/non-www routing before cutover).

- Keep previews out of indexing using hosting-level X-Robots-Tag: noindex. Verify production has no blocking headers, authentication or crawler challenges.
- Verify the real street address, opening hours, Google Business Profile URL and service coverage before adding them to visible content and schema. No address, reviews, coordinates or ratings have been invented.
- Point the production domain to this deployment, verify TLS and redirect alternate hosts to the canonical host.
- Export the existing Blogger post URLs/content before migration. Preserve each post and its URL, or create individually mapped permanent redirects. Do not replace the old blog before this is done; /search must remain available or be replaced with a real archive.
- Verify Search Console and Bing Webmaster Tools ownership, submit sitemap.xml and request indexing.
- Validate JSON-LD and inspect rendered pages and HTTP headers after domain cutover. LocalBusiness without a verified address may not qualify for Google local business enhancements.
- Verify Google Business Profile category, business name, phone, address/service area, hours and website against real business records. Manage genuine reviews; do not create fabricated ratings.
- Measure mobile Core Web Vitals and test real devices. No rankings, indexing, rich results or AI citations are guaranteed.
- robots.txt permits public crawlers. AI training policy is separate; revise crawler-specific rules if the owner requests restrictions.
