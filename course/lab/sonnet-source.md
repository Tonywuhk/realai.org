---
permalink: /course/lab/sonnet-source/
title: Course | Lab | Installing Sonnet from Source
---
# Installing Sonnet from Source

*Last Updated: August 10, 2017*

From [Google Compute Engine](http://realai.org/course/google-cloud-platform/#google-compute-engine), create an [n1-standard-1](https://cloud.google.com/compute/pricing#predefined_machine_types) instance with a Ubunbu 16.04 boot image.

## Installing Pip and TensorFlow

```bash
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
rm get-pip.py
sudo pip install tensorflow
```

## Installing Bazel

As recommended in the official [Installing Bazel on Ubuntu](https://docs.bazel.build/versions/master/install-ubuntu.html) page, we will use a custom APT repository:

```bash
sudo apt update && sudo apt install openjdk-8-jdk
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
sudo apt update && sudo apt install bazel
```

At this point, the [GNU Compiler Collection](https://gcc.gnu.org/) `gcc --version` 5.4.0 is installed on our system. This version number affects how Sonnet will be built later.

## Installing Sonnet

[Sonnet](https://github.com/deepmind/sonnet) is a library built on top of TensorFlow for building complex neural networks. The official [installing from source](https://deepmind.github.io/sonnet/#installing-from-source) instructions need to be adapted to our setup. To get started:

```bash
git clone --recursive https://github.com/deepmind/sonnet
cd sonnet/tensorflow
```

`which python3` shows Python 3 is located in `/usr/bin/python3`, and `pip show tensorflow` shows TensorFlow is in `/usr/local/lib/python3.5/dist-packages`. In the next step, make sure that these are consistent with the options we choose. The rest can use the default choices.

```bash
./configure
```

The official [Installing TensorFlow from Sources](https://www.tensorflow.org/install/install_sources#build_the_pip_package) page notes that the binary pip packages available on the TensorFlow website are built with gcc 4. Since our gcc version is 5.4.0, to make our build compatible, we follow the instruction on the TensorFlow page to add a `--cxxopt` Bazel [flag option](https://docs.bazel.build/versions/master/bazel-user-manual.html#flags-options): 

```bash
cd ../
mkdir /tmp/sonnet
bazel build --config=opt --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" :install
./bazel-bin/install /tmp/sonnet python3
```

Now the temp directory `ls /tmp/sonnet/` should have a wheel `dm_sonnet-1.9-cp35-cp35m-linux_x86_64.whl`. `pip install` this wheel and the installation is complete.

```bash
sudo pip install /tmp/sonnet/*.whl
cd
```

### Testing

Enter `python3 -c "import sonnet as snt; import tensorflow as tf; print(snt.resampler(tf.constant([0.]), tf.constant([0.])))"`, the output should be `Tensor(“resampler/Resampler:0”, shape=(1,), dtype=float32)`. We can also run the [Differentiable Neural Computer](https://deepmind.com/research/dnc/) as in [Installing Sonnet and TensorFlow in a Conda Environment](http://realai.org/course/lab/conda-tf-snt/):

```bash
git clone https://github.com/deepmind/dnc.git
cd dnc
python train.py --memory_size=64 --num_bits=8 --max_length=3
```

Results in these two experiments should be the same. There is no speed advantage by installing Sonnet from source.

## A Little Bit of Python (Optional)

The `python3 -c "import sonnet as snt; import tensorflow as tf; print(snt.resampler(tf.constant([0.]), tf.constant([0.])))"` would fail if we didn’t `cd` out of the `sonnet/` directory at the end of “Installing Sonnet.” The error would trace to a line 27 of [sonnet/python/ops/resampler.py](https://github.com/deepmind/sonnet/blob/de33c8a538c5641be4b548abb36b089881c815fa/sonnet/python/ops/resampler.py):

```python
from sonnet.python.ops import gen_resampler
```

This line attempts to import a Python [module](https://docs.python.org/2/tutorial/modules.html) called `gen_resampler` [from a package](https://docs.python.org/2/tutorial/modules.html#importing-from-a-package) called `sonnet.python.ops`. The module is located in `ls /usr/local/lib/python3.5/dist-packages/sonnet/python/ops/`, a subdirectory that depends on our choice in the `./configure` step of “Installing Sonnet.” But if we were in a directory called `sonnet/`, Python would look for the module in `ls sonnet/python/ops/` and the file `gen_resampler.py` wouldn’t be there! This behavior is based on the [modue search path](https://docs.python.org/2/tutorial/modules.html#the-module-search-path), and can be displayed in the Python interpreter:

```python
import sys
print(sys.path)
```

We can superficially fix this problem by copying the missing files to our local directory, thus confirming that this is indeed the problem:

```bash
cp /usr/local/lib/python3.5/dist-packages/sonnet/python/ops/gen_resampler.py 
cp /usr/local/lib/python3.5/dist-packages/sonnet/python/ops/_resampler.so sonnet/python/ops/
```

But this is clearly not a good idea, and the library `pip show dm-sonnet` is supposed to reside in its rightful directory under `...python3.5/dist-packages/`. This problem will be gone if we `rm -rf sonnet/` and don’t deliberately confuse Python by using the same directory structure as the library. According to a [May 25 comment](https://github.com/deepmind/sonnet/issues/16#issuecomment-304010059) on Sonnet’s GitHub page, there should be a fix “in the following days.” Apparently it's also not a good idea to plan a fix in a GitHub issue discussing another problem that can be closed without any follow-up on the fix.

