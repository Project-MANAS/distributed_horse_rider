def main(task_index: int, log, _):
	import tensorflow as tf
	from distributed_horse_rider.distributed import config, Horse, spec
	with tf.Session(tf.train.Server(spec, job_name='horse', task_index=task_index, config=config).target) as sess:
		sess.run(tf.global_variables_initializer())
		log('Ready to get whipped!')
		whips_received = 1
		while True:
			log('I got %d whippings, and we took %d steps' % (whips_received, sess.run(Horse.take_step)))
			whips_received += 1
