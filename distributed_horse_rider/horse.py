import tensorflow as tf

from distributed_horse_rider.distributed import spec, task_index, config, Horse

with tf.Session(tf.train.Server(spec, job_name='horse', task_index=task_index, config=config).target) as sess:
	sess.run(tf.global_variables_initializer())
	size = Horse.whip.size()
	print('Horse %d ready to get whipped!' % task_index)
	whips_received = 0
	while True:
		q_size, steps_covered = sess.run((size, Horse.take_step))
		whips_received += 1
		print('I received %d whips, and we took %d steps' % (whips_received, steps_covered))
