/* SOL Peace EIE + Trystero v2.2: public static resources only. No private IndexedDB data or third-party traffic cached. */
const CACHE='sol-peace-master-shell-v5';
const SHELL=['./','./index.html','./icon.svg','./site.webmanifest','./data/integrated_public_records.json',
'./usmc/index.html','./usmc/assets/styles.css','./usmc/assets/app.js',
'./usss/index.html','./usss/assets/styles.css','./usss/assets/app.js',
'./fbi/index.html','./fbi/assets/styles.css','./fbi/assets/app.js',
'./cia/index.html','./cia/assets/styles.css','./cia/assets/app.js',
'./un/index.html','./un/assets/styles.css','./un/assets/app.js'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(SHELL)));self.skipWaiting()});
self.addEventListener('activate',e=>e.waitUntil((async()=>{const keys=await caches.keys();await Promise.all(keys.filter(k=>k.startsWith('sol-peace-master-')&&k!==CACHE).map(k=>caches.delete(k)));await self.clients.claim()})()));
self.addEventListener('fetch',e=>{
 const request=e.request,url=new URL(request.url);
 if(request.method!=='GET'||url.origin!==self.location.origin||request.mode==='navigate'&&url.search)return;
 if(!url.pathname.startsWith(new URL(self.registration.scope).pathname))return;
 const relative=url.pathname.slice(new URL(self.registration.scope).pathname.length);
 const safePublic=/^(?:[\w-]+\/)?(?:modules\/[a-z-]+\/)?(?:index\.html|assets\/(?:app\.js|styles\.css|icon\.svg)|data\/[\w-]+\.json|service_worker\.js|site\.webmanifest|icon\.svg)$/.test(relative)||relative==='';
 if(!safePublic)return;
 e.respondWith((async()=>{
  const cache=await caches.open(CACHE);
  try{const response=await fetch(request);if(response.ok&&response.type==='basic')await cache.put(request,response.clone());return response}
  catch{const cached=await cache.match(request,{ignoreSearch:true});return cached||new Response('This page was not cached. Connect and visit it online first.',{status:503,headers:{'Content-Type':'text/plain'}})}
 })());
});
