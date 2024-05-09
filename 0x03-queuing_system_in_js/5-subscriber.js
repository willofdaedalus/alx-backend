import { createClient } from 'redis';

const client = createClient();
const holbertonChannel = 'holberton school channel';

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// stackoverflow.com/questions/4441798/
client.subscribe(holbertonChannel);

client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe(holbertonChannel);
  }
  console.log(message);
});
