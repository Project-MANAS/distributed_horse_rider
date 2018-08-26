import tensorflow as tf

from distributed_horse_rider.distributed import spec, task_index, config, Rider

if task_index == 0:
	tf.summary.FileWriter('./logs', graph=tf.get_default_graph()).close()

with tf.Session(tf.train.Server(spec, job_name="driver", task_index=task_index, config=config).target) as sess:
	sess.run(tf.global_variables_initializer())
	input('Rider %d ready to whip! (Press any key)' % task_index)
	for flick_intensity in range(10000):
		print('Whipping with intensity %d' % flick_intensity)
		sess.run(Rider.flick_whip, feed_dict={Rider.flick_intensity: flick_intensity})
		input('Total distance covered: %d, (Press any key for next whip!)' % sess.run(Rider.measure_distance_covered))
