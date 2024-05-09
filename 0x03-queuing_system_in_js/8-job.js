import { createQueue } from 'kue';
const queue = createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((j) => {
    const job = queue.create('push_notification_code', {
      // phoneNumber: '42069',
      // message: 'heres thorkell :D'
      phoneNumber: '4153518780',
      message: 'This is the code to verify your account'
    }).save(function(err) {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
