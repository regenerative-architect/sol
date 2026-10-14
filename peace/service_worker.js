/* Versioned shell cache; NO caching of off-origin sites or private state. HTTPS/localhost only. */
const CACHE='sol-peace-master-shell-v2';
const SHELL=['./','./index.html','./icon.svg','./site.webmanifest'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(SHELL)));self.skipWaiting()});
self.addEventListener('activate',e=>e.waitUntil((async()=>{const keys=await caches.keys();await Promise.all(keys.filter(k=>k.startsWith('sol-peace-master-')&&k!==CACHE).map(k=>caches.delete(k)));await self.clients.claim()})()));
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||new URL(r.url).origin!==self.location.origin)return;const u=new URL(r.url);if(!SHELL.some(s=>new URL(s,self.registration.scope).pathname===u.pathname))return;e.respondWith((async()=>{try{const res=await fetch(r);if(res.ok){const c=await caches.open(CACHE);await c.put(r,res.clone())}return res}catch{const cached=await caches.match(r,{ignoreSearch:true});return cached||new Response('This asset was not cached.',{status:503})}})())});
