#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np


# In[2]:


x_data = np.float32(np.random.rand(2,100))
y_data = np.dot([0.100,0.200],x_data)+0.300


# In[3]:


b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1,2],-1.0,1.0))
y = tf.matmul(W,x_data)+b


# In[4]:


loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)


# In[5]:


#init = tf.initialize_all_variables()
init = tf.global_variables_initializer()


# In[6]:


sess = tf.Session()
sess.run(init)


# In[16]:


for step in xrange(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print step,sess.run(W),sess.run(b)


# In[ ]:




