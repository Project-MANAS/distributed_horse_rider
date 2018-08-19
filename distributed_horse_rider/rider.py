import tensorflow as tf

import distributed_horse_rider.distributed as dist

if dist.task_index == 0:
	summary_writer = tf.summary.FileWriter('./logs', graph=tf.get_default_graph())
	summary_writer.close()

config = tf.ConfigProto()
config.gpu_options.allow_growth = True

driver = tf.train.Server(dist.spec, job_name="driver", task_index=dist.task_index, config=config)

with tf.Session(driver.target, config=config) as sess:
	sess.run(tf.global_variables_initializer())
	print('Rider %d ready to whip! (Press any key)' % dist.task_index)
	input()
	for flick_intensity in range(10000):
		print('Whip with intensity %d' % flick_intensity)
		sess.run(dist.Rider.flick_whip, feed_dict={dist.Rider.flick_intensity: flick_intensity})
		print('Total distance covered: %d, (Press any key for next whip!)' % sess.run(dist.Rider.measure_distance_covered))
		input()