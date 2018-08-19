import tensorflow as tf

import distributed_horse_rider.distributed as dist

config = tf.ConfigProto()
config.gpu_options.allow_growth = True

horse = tf.train.Server(dist.spec, job_name="horse", task_index=dist.task_index, config=config)

with tf.Session(horse.target, config=config) as sess:
	# summary_writer = tf.summary.FileWriter('./logs', graph=sess.graph)
	# summary_writer.add_graph(sess.graph)
	# summary_writer.close()
	sess.run(tf.global_variables_initializer())
	size = dist.Horse.whip.size()
	print('Horse %d ready to get whipped!' % dist.task_index)
	whips_received = 0
	while True:
		q_size, steps_covered = sess.run((size, dist.Horse.take_step))
		whips_received += 1
		print('I received %d whips, and we took %d steps' % (whips_received, steps_covered))
