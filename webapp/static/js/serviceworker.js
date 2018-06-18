var staticCacheName = 'SVF_WebApp';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/base_layout',
          '/training/'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        fetch(event.request).catch(function(){
            var requestURL = new URL(event.request.url);
            console.log('fetching' + event.request.url);
            if (requestURL.pathname === '/') {
                console.log('base');
                return caches.match('base_layout');
            }else
            if (requestURL.pathname === 'training/'){
                console.log('training');
                return caches.match('training');
            }
        })
    );
});