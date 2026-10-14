/* Versioned same-origin offline shell; no external fetches or agency connections.
   Updating a cache does not force activation while users still have open tabs. */
const VERSION='public_integrity_os_v1_20261014';
const CORE=[
 './index.html','./assets/styles.css','./assets/app.js','./assets/icon.svg',
 './site.webmanifest','./modules/sitrep/index.html','./modules/review/index.html',
 './modules/evidence/index.html','./modules/framework/index.html',
 './modules/nodes/index.html','./modules/governance/index.html',
 './data/sources.json','./data/handoff_schema.json'
];
self.addEventListener('install',event=>{
 event.waitUntil(caches.open(VERSION).then(cache=>cache.addAll(CORE)));
});
self.addEventListener('activate',event=>{
 event.waitUntil(caches.keys().then(names=>Promise.all(names.filter(n=>n.startsWith('public_integrity_os_')&&n!==VERSION).map(n=>caches.delete(n)))).then(()=>self.clients.claim()));
});
self.addEventListener('fetch',event=>{
 const request=event.request;
 if(request.method!=='GET')return;
 const url=new URL(request.url);
 if(url.origin!==self.location.origin)return; // Never cache off-site references.
 if(!url.pathname.startsWith(new URL(self.registration.scope).pathname))return;
 event.respondWith(caches.match(request).then(cached=>cached||fetch(request).then(response=>{
   if(response.ok&&response.type==='basic'){
     const copy=response.clone();caches.open(VERSION).then(cache=>cache.put(request,copy)).catch(()=>{});
   }
   return response;
 }).catch(()=>new Response('Offline: this resource was not previously cached.',{status:503,headers:{'content-type':'text/plain'}}))));
});
self.addEventListener('message',event=>{
 if(event.data?.type==='SKIP_WAITING')self.skipWaiting();
});
