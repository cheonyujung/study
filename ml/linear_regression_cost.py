import tensorflow as tf
import matplotlib.pyplot as plt

x_train = [1, 2 ,3]
y_train = [1, 2 ,3]

W = tf.Variable(tf.random_normal([1]), name="weight")

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# Our hypothesis for linear model X * W
hypothesis = X * W

# cost/loss function
cost = tf.reduce_sum(tf.square(hypothesis - Y))

# Minimize: Gradient Descent using derivative: W -= learning rate * derivative
learning_rate = 0.1
gradient = tf.reduce_min((W * X - Y) * X)
descent = W - learning_rate * gradient
update = W.assign(descent)

# Launch the graph in a session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Variable for plotting cost function
W_val = []
cost_val = []

for step in range(21):
    sess.run(update, feed_dict={X: x_train, Y: y_train})
    print(step, sess.run(cost, feed_dict={X: x_train, Y: y_train}), sess.run(W))
    W_val.append(sess.run(W))
    cost_val.append(sess.run(cost, feed_dict={X: x_train, Y: y_train}))

# show cost function
step_list = [x for x in range(21)]
plt.plot(step_list, W_val)
plt.plot(step_list, cost_val)
plt.show()