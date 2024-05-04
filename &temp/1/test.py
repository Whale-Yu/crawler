# import tensorflow as tf
#
# '''
# 均方差损失函数
# '''
#
# out = tf.random.normal([2, 10])
# y = tf.constant([1, 3])
# y = tf.one_hot(y, 10)
#
# criteon = tf.keras.losses.MeanSquaredError()
# loss = criteon(y, out)
# print(loss)
#
# '''
# 交叉熵损失函数
# '''
#
# y_true = [[0., 1.], [0., 0.]]
# y_pred = [[0.6, 0.4], [0.4, 0.6]]
# # Using 'auto'/'sum_over_batch_size' reduction type.
# bce = tf.keras.losses.BinaryCrossentropy()
# print(bce(y_true, y_pred).numpy())
#
#
# # Calling with 'sample_weight'.
# print(bce(y_true, y_pred, sample_weight=[1, 0]).numpy())
#
# # Using 'none' reduction type.
# bce = tf.keras.losses.BinaryCrossentropy(
#     reduction=tf.keras.losses.Reduction.NONE)
# print(bce(y_true, y_pred).numpy())
#
#
#
#
#
#
# # Calling with 'sample_weight'.
# bce(y_true, y_pred, sample_weight=[1, 0]).numpy()


import json

f = open('contry.json', 'r')
file = f.read()
data=json.loads(file)
print(len(data['features']))

for i in range(len(data['features'])):
    print(data['features'][i]['properties']['name'])
