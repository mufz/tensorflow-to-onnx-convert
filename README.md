# tensorflow-to-onnx-convert

This repo documents the steps I took to convert tensorflow mnist model to onnx model

1. Train the MNIST model and save the model checkpoint in the checkpoint_data folder 
```
python tf-mnist.py
```

2. Convert the saved TensorFlow graph to graph.proto format 
#python save_graph_as_proto.py

3. Freeze the graph i.e. A single graph with all the weigths included as a one graph 
#$TENSORHOME/bazel-bin/tensorflow/python/tools/freeze_graph  --input_graph=/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/graphs/graph.proto --input_checkpoint=/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/checkpoint_data/checkpoint-1999 --output_graph=/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/graphs/frozen_graph.pb --output_node_names=global_step/read,save/control_dependency,xentropy/Shape,gradients/zeros_like,GradientDescent,gradients/hidden1/MatMul_grad/tuple/control_dependency,xentropy_mean --input_binary=True

4. Run the tf-to-onnx converter using the following cmd
#python convert_to_onnx.py
