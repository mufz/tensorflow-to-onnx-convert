from onnx_tf.frontend import tensorflow_graph_to_onnx_model
import tensorflow as tf

with tf.gfile.GFile("/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/graphs/frozen_graph.pb", "rb") as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    onnx_model = tensorflow_graph_to_onnx_model(graph_def,
                                     "global_step/read",
                                     opset=0)

    file = open("/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/graphs/mnist.onnx", "wb")
    file.write(onnx_model.SerializeToString())
    file.close()
