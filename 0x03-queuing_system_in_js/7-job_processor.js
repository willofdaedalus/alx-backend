import { createQueue } from 'kue';
const queue = createQueue();

const blacklisted_numbers = [ '4153518780', '4153518781' ];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  // fail the job if it contains a blacklisted number
  // https://github.com/Automattic/kue/issues/191#issuecomment-20098594
  if (blacklisted_numbers.includes(phoneNumber)) {
    const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(err);
    done(err);
  }

  job.progress(50, 100);
  console.log(`Sending notificaiton to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});
