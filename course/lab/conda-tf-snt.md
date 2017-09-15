---
permalink: /course/lab/conda-tf-snt/
---
# Lab - Installing Sonnet and TensorFlow in a Conda Environment

*Last Updated: August 9, 2017*

First create an [f1-micro](https://cloud.google.com/compute/pricing#predefined_machine_types) virtual machine with a Ubuntu 17.04 boot image in [Google Compute Engine](http://realai.org/course/google-cloud-platform/#google-compute-engine). Upon start, the system’s `python -V` and `python3 -V` show versions “2.7.13” and “3.5.3” respectively. No administrative or root permissions are necessary for the following installations as `miniconda3` and new packages, including Python 3.6.1, will be installed under the home directory.

## Installing Conda

[Conda](http://realai.org/course/conda/) is both a package manager and an environment manager. Download the 64-bit bash installer for Linux, and install Miniconda. Remember to type `yes` when asked whether to prepend the install location to PATH:

```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Enter the command `source ~/.bashrc` for the new PATH to take effect. Now both `python` and `python3` should point to version “3.6.1.” A simple `diff .bashrc-miniconda3.bak .bashrc` shows that Miniconda automatically adds its binary directory to the PATH variable, so that `python`, `python3`, and `pip` all run from that directory. We can `rm Miniconda3-latest-Linux-x86_64.sh` now.

## Installing TensorFlow

[TensorFlow](https://www.tensorflow.org/) is an open-source software library for machine intelligence. One command `pip install tensorflow` is sufficient to install it for the conda root environment. Alternatively, we can follow the official [Installing with Anaconda](https://www.tensorflow.org/install/install_linux#InstallingAnaconda) instructions, with the [appropriate](https://www.tensorflow.org/install/install_linux#the_url_of_the_tensorflow_python_package) URL to the [wheel](http://realai.org/course/python/#wheel) for our version of Python (3.6).

```bash
conda create -n tensorflow
source activate tensorflow
pip install --ignore-installed --upgrade \
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.2.1-cp36-cp36m-linux_x86_64.whl
```

Now `import tensorflow` is a valid Python command in the root environment, and also in the `tensorflow` environment if it’s created as in the above steps. Use ` source deactivate` to return to root.

## Installing Sonnet

[Sonnet](https://github.com/deepmind/sonnet) is a library built on top of TensorFlow for building complex neural networks. TensorFlow is straightforward to install, but if we attempt to install Sonnet in the same way, `pip install dm-sonnet` returns an error message, “… No matching distribution found for dm-sonnet”. The [PyPI page](https://pypi.python.org/pypi/dm-sonnet/1.9) of `dm-sonnet` shows that it is stored as wheel files, whose ABI tags require either Python 2.7 or 3.4. Our Python is 3.6. This is where conda can be super useful, it allows us to create a Python 3.4 virtual environment:

```bash
conda create -n sonnet python=3.4
```

The `sonnet` environment will have its own set of dependencies, including pip, python, and wheel. To active it:

```bash
source activate sonnet
```

In this new environment `python -V` points to Python 3.4.5, and TensorFlow is no longer available! Now we can easily install both packages:

```bash
pip install tensorflow
pip install dm-sonnet
```

To test our installation, enter `python -c "import sonnet as snt; import tensorflow as tf; print(snt.resampler(tf.constant([0.]), tf.constant([0.])))"`, and the output should be “Tensor("resampler/Resampler:0", shape=(1,), dtype=float32).”

## (Optional) Running Differentiable Neural Computer

These packages are enough to begin running [DeepMind](http://realai.org/research-groups/deepmind/)’s [implementation](https://github.com/deepmind/dnc) of the [Differentiable Neural Computer](https://deepmind.com/research/dnc/), a memory-augmented neural network [published in Nature](https://www.nature.com/articles/nature20101.epdf?author_access_token=ImTXBI8aWbYxYQ51Plys8NRgN0jAjWel9jnR3ZoTv0MggmpDmwljGswxVdeocYSurJ3hxupzWuRNeGvvXnoO8o4jTJcnAyhGuZzXJ1GEaD-Z7E6X_a9R-xqJ9TfJWBqz) in October 2016. Within conda’s `sonnet` environment:

```bash
git clone https://github.com/deepmind/dnc.git
cd dnc
python train.py --memory_size=64 --num_bits=8 --max_length=3
```

Even on an f-1 micro instance that comes with 20% of a virtual CPU and 0.60GB of memory, the code should start generating some outputs in a few minutes:

![](http://realai.org/course/lab/conda-tf-snt-1.png)

