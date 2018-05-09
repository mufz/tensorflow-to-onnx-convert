import math
import os
from six.moves import xrange  # pylint: disable=redefined-builtin
import numpy as np
import tensorflow as tf


CHKPT_DIR="/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/checkpoint_data"

with tf.Session(graph=tf.Graph()) as sess:
    saver = tf.train.import_meta_graph(
        os.path.join(CHKPT_DIR, "checkpoint-1999.meta"))
    saver.restore(
        sess, os.path.join(CHKPT_DIR, "checkpoint-1999"))

    with open("/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/graphs/graph.proto", "wb") as file:
        graph = tf.get_default_graph().as_graph_def(add_shapes=True)
        file.write(graph.SerializeToString())
