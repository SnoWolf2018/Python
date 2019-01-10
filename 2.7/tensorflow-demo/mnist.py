#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


x = tf.placeholder("float",[None,784])


# In[3]:


W = tf.Variable(tf.zeros([784,10]))


# In[4]:


b = tf.Variable(tf.zeros([10]))


# In[5]:


y = tf.nn.softmax(tf.matmul(x,W)+b)


# In[6]:


y_ = tf.placeholder("float", [None,10])


# In[7]:


cross_entropy = -tf.reduce_sum(y_*tf.log(y))


# In[8]:


train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)


# In[11]:


#init = tf.initialize_all_variables()
init = tf.global_variables_initializer()


# In[12]:


sess = tf.Session()
sess.run(init)


# In[15]:


for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict = {x:batch_xs,y_:batch_ys})


# In[ ]:




