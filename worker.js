// TODO dummy fetch to meet Chrome's criteria
self.addEventListener( "fetch", event => {
  console.log('WORKER: Fetching', event.request);
});
