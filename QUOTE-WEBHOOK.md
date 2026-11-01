# Quote webhook integration

Set BRAND.formEndpoint in index.html to the public HTTPS ingestion URL. No secrets belong in browser code.

The website posts JSON event quote.requested, version 1, requestId, submittedAt, source, customer {name, phone, email, company}, quote {city, signageTypes[], dimensions, businessType, message, requirement}, contactPreference. The endpoint must return JSON {"accepted":true,"requestId":"<matching ID>"} only after durable storage, or a durable queue entry. It must allow the deployed website origin via CORS and handle OPTIONS. Validate fields and sizes server-side, rate limit, deduplicate by requestId, and escape spreadsheet cells starting with formula characters. Never treat the public URL as authentication.

Suggested n8n flow: Webhook POST → validation and request-ID deduplication → durable lead record → Google Sheets append/update → Respond. If returning before Sheets completes, use a durable queue with retries and failure visibility. Columns: Request ID, Submitted At, Name, Phone, Email, Company, City, Signage Types, Dimensions, Business Type, Message, Requirement, Status. Store credentials in n8n or a server secret store.

Catalogue bot is a separate inbound WhatsApp integration: validate provider webhook signatures → normalize/deduplicate incoming message ID → look up published catalogue records → compose a grounded reply → send via provider API. Catalogue fields should include ID, name, description, material, lighting, dimensions/options, verified pricing or quote-required flag, image URL, active status. Do not invent prices or stock. Escalate unavailable answers to a human. A wa.me link alone is not a bot. Use customer-initiated conversations and follow the provider's messaging window/template rules.

Required configuration: ingestion URL; Google Sheet ID/tab and credential connection; catalogue database type/schema/access; WhatsApp Business provider and phone-number ID; server-side credentials and webhook verification configuration. Do not paste private keys into chat or frontend code.

Status: frontend integration prepared; endpoint, spreadsheet delivery and WhatsApp bot are NOT connected or verified. Existing WhatsApp handoff remains active until an endpoint is configured.
