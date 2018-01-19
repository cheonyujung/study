import tensorflow as tf

x_train = [1, 2 ,3]
y_train = [1, 2 ,3]

W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

# Our Hypothesis Wx+b
hypothesis = x_train * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Launch the graph in a session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Fit
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
       print(step, sess.run(cost), sess.run(W), sess.run(b))
