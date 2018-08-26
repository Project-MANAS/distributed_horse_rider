import tensorflow as tf

from distributed_horse_rider.distributed import spec, task_index, config, Horse

with tf.Session(tf.train.Server(spec, job_name='horse', task_index=task_index, config=config).target) as sess:
	sess.run(tf.global_variables_initializer())
	print('Horse %d ready to get whipped!' % task_index)
	whips_received = 1
	while True:
		print('I got %d whippings, and we took %d steps' % (whips_received, sess.run(Horse.take_step)))
		whips_received += 1
