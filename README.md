# tensorflow-to-onnx-convert

This repo documents the steps I took to convert tensorflow mnist model to onnx model

1. Train the tensorflow MNIST model and save the model checkpoint in the checkpoint_data folder 
```
python tf-mnist.py
```

2. Convert the saved tensorflow graph to graph.proto format. 

```
python save_graph_as_proto.py
```

3. Freeze the graph i.e. A single graph with all the weigths included as one graph. This graph will be fed to ONNX coverter utility.

```
$TENSORHOME/bazel-bin/tensorflow/python/tools/freeze_graph  --input_graph=/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/graphs/graph.proto --input_checkpoint=/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/checkpoint_data/checkpoint-1999 --output_graph=/home/muffadall/work/github_repo/tensorflow-to-onnx-convert/graphs/frozen_graph.pb --output_node_names=global_step/read,save/control_dependency,xentropy/Shape,gradients/zeros_like,GradientDescent,gradients/hidden1/MatMul_grad/tuple/control_dependency,xentropy_mean --input_binary=True
```

4. Run the tf-to-onnx converter using the following cmd

```
python convert_to_onnx.py
```

5. A more detailed description on each step can be found at https://github.com/tjingrant/tutorials/blob/patch-2/tutorials/OnnxTensorflowExport.ipynb
