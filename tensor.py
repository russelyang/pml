import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node  = a + b
adder_and_triple = adder_node * 3.

sess = tf.Session()
print(sess.run(adder_and_triple, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1,3], b: [2, 4]}))
