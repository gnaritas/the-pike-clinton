# DEPLOY — The Pike (the-pike-clinton)

- Live: https://the-pike-clinton-demo.up.railway.app (noindex X-Robots-Tag + per-page meta — demo host, strip only at custom-domain delivery)
- GitHub: https://github.com/gnaritas/the-pike-clinton (public, no secrets)
- Railway: project "the-plain-bar" 604a72a9-09eb-4169-920d-e64619651640 (co-host shell — account project cap hit 2026-11-23), service `the-pike-clinton-demo` id 2b02d20c-ec89-4fe6-b9c2-ffdc008c2f65; domain id 44870e98-93ee-4491-88a2-ffa7fa7f65d2 renamed from -production via `railway domain update --domain the-pike-clinton-demo <id> --service <svc>`
- Stack: static `public/` + node server.js (noindex header, /healthz, /open pixel, /contact -> Brevo HTTP API v3, no third-party JS)
- Form relay: Brevo HTTP API over 443 (Railway SMTP egress dead). BREVO_API_KEY set from `~/.hermes/secrets/brevo_smtp_key.txt` line 2 **xkeysib-onward — full token is 89 chars; a `[a-f0-9]`-class regex truncates it to 72 and Brevo 401s "Key not found" (trap hit + fixed 2026-11-24)**. Proof: POST /contact 303 -> /thanks + `MAILSENT` in `railway logs --service 2b02d20c...`
- Deploys: 06f68bd0 (first), fc0a7457 (redeploy with corrected 89-char key; forms live after this one)
- Owner domain: thepikeclinton.com — RDAP-registered, GBP-pointed, serves Wix 404 placeholder (Wayback zero captures). Pitch angle: domain live, site empty. If owner revives with brand+town content before send = HAS-SITE abort (send script liveness guard, no-redirect semantics).
- Verification (2026-11-24): _verify.py PASS 0 fails; live walk 19/19 sha==local + branded 404 + noindex headers + /open; render_sweep 22/22 DOM gates PASS (0 overflow both viewports); vision battery 22 shots via OpenRouter gemini-2.5-flash, medium/high claims adjudicated against deep per-element playwright audit (0 beyond-right, 0 clipped text, 0 footer overlaps); map embed proven loading desktop (OOPIF + tiles + marker), blank in headless-mobile = environment quirk, markup+resource 200 proven.
- Card: t_ee8b8dcc (board websites). Evidence: sites/the-pike-clinton/evidence.json + shots/vision-results.json.
