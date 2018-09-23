def main(task_index: int, log, prompt):
	import tensorflow as tf
	from distributed_horse_rider.distributed import config, Rider, spec

	if task_index == 0:
		tf.summary.FileWriter('./logs', graph=tf.get_default_graph()).close()

	with tf.Session(tf.train.Server(spec, job_name="rider", task_index=task_index, config=config).target) as sess:
		sess.run(tf.global_variables_initializer())
		prompt('Ready to whip!')
		for flick_intensity in range(10000):
			log('Whipping with intensity %d' % flick_intensity)
			sess.run(Rider.flick_whip, feed_dict={Rider.flick_intensity: flick_intensity})
			prompt('Total distance covered: %d' % sess.run(Rider.measure_distance_covered))
