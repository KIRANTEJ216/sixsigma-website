module.exports = async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");
  if (req.method !== "POST") {res.setHeader("Allow","POST");return res.status(405).json({message:"Method not allowed"});}
  const p = typeof req.body === "string" ? (()=>{try{return JSON.parse(req.body);}catch{return null;}})() : req.body;
  if (!p || p.event !== "quote.requested" || typeof p.requestId !== "string" || p.requestId.length > 100 ||
      !p.customer || typeof p.customer.company !== "string" || !p.customer.company.trim() ||
      typeof p.customer.email !== "string" || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(p.customer.email.trim()) ||
      typeof p.customer.name !== "string" || !p.customer.name.trim() ||
      typeof p.customer.phone !== "string" || !p.quote || typeof p.quote.city !== "string" || !p.quote.city.trim() ||
      JSON.stringify(p).length > 16000) return res.status(400).json({message:"Invalid quotation details"});
  const endpoint = process.env.QUOTE_WEBHOOK_URL || "https://kktej3d.n8n-wsk.com/webhook/big9signage";
  try {
    const upstream = await fetch(endpoint, {method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(p),signal:AbortSignal.timeout(12000),redirect:"error"});
    if (!upstream.ok) return res.status(502).json({message:"WEBHOOK_UNAVAILABLE"});
    const ack = await upstream.json().catch(()=>null);
    if (!ack || ack.accepted !== true || ack.requestId !== p.requestId) return res.status(502).json({message:"Delivery could not be confirmed"});
    return res.status(200).json({accepted:true,requestId:p.requestId});
  } catch {return res.status(502).json({message:"WEBHOOK_UNAVAILABLE"});}
};
