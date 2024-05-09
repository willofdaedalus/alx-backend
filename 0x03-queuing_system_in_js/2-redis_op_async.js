const redis = require('redis');
import { createClient } from 'redis';
const util = require('util');

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err);
      return;
    }
    redis.print(`Reply: ${reply}`);
  });
}


async function displaySchoolValue(schoolName) {
  const getAsync = util.promisify(client.get).bind(client);
  try {
    console.log(await getAsync(schoolName));
  } catch (err) {
    console.log(err.message);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
