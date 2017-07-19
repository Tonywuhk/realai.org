---
permalink: /course/tpu-tf-nmt/
---
# Lab - Neural Machine Translation on Cloud GPU

*DRAFT - Last Updated: July 19, 2017*

In this experiment, we walk through the steps to train a neural machine translation model with a [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) on [Google cloud](https://cloud.google.com/).

## Prerequisites

* A Google cloud account with at least a few US dollars of credit. Typically, a user receives [$300 free credit](https://cloud.google.com/free/) over a [12-month trial period](https://cloud.google.com/free/docs/frequently-asked-questions#free-trial). A credit card is needed to create an account.

* Join the [NVIDIA Developer Program](https://developer.nvidia.com/developer-program). Membership is required for [cuDNN download](https://developer.nvidia.com/rdp/cudnn-download). Save the [Linux version](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v5.1/prod_20161129/8.0/cudnn-8.0-linux-x64-v5.1-tgz) of cuDNN v5.1 (Jan 20, 2017) for CUDA 8.0 in a directory on your local computer.

## VM Instance

Create a virtual machine (VM) instance in [Compute Engine](https://console.cloud.google.com/compute/). We don't need a GPU for software installation, so let's create a very cheap "f1-micro" machine in a nearby [Zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones). Select the "Ubuntu 16.04 LTS" image to create a boot disk.

## GPU Setup - CUDA

[CUDA](https://en.wikipedia.org/wiki/CUDA) is a software created by NVIDIA that allows us to use its GPUs. First we need to ensure that our system has [gcc](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) installed:

```bash
sudo apt-get update
sudo apt-get install build-essential -y
```

Now follow the [NVIDIA CUDA Installation Guide for Linux](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html):

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1604_8.0.61-1_amd64.deb
sudo apt-get update
sudo apt-get install cuda -y
```

The last step above can take a long time. Then there are a few [post-installation actions](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions):

```bash
export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

## GPU Setup - cuDNN

Click the gear icon on the upper right corner of the terminal, select the cuDNN file downloaded earlier, and upload it to the virtual machine. After the file is transferred to the cloud:

```bash
tar -xzvf cudnn-8.0-linux-x64-v5.1.tgz
sudo cp cuda/lib64/* /usr/local/cuda/lib64/
sudo cp cuda/include/* /usr/local/cuda/include/
```

Now both CUDA and cuDNN are installed. Let's clean up the files:

```bash
rm cuda-repo-ubuntu1604_8.0.61-1_amd64.deb 
rm -rf cuda
rm cudnn-8.0-linux-x64-v5.1.tgz
```

## TensorFlow Setup

Following the requirements on [official TensorFlow installation instructions](https://www.tensorflow.org/install/install_linux), we first install a library:

```bash
sudo apt-get install libcupti-dev -y
```

Then we get pip from [Python Software Foundation](https://packaging.python.org/tutorials/installing-packages/):

```bash
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
rm get-pip.py
```

### Moving VM Instance

Type 'exit' to close the terminal, then STOP (DO NOT **DELETE**) the VM instance on which we just installed GPU software. In [Snapshots](https://console.cloud.google.com/compute/snapshots), create a snapshot of this instance. Go back to "VM instances" and shut down the instance for which we already created a snapshot. Now it's time to get a powerful GPU computer.

In Oregon, an "n1-standard-2" machine type costs [$0.095 per hour](https://cloud.google.com/compute/pricing#predefined_machine_types) and 1 GPU processor costs [$0.70 per hour](https://cloud.google.com/compute/pricing#gpus). We create a new VM in Zone "us-west1-b" using these parameters.

![](http://realai.org/assets/images/course-tpu-tf-nmt-1.png)

On this new VM, we do a [native pip](https://www.tensorflow.org/install/install_linux#InstallingNativePip) TensorFlow installation:

```bash
sudo pip install tensorflow-gpu
```

## Basic Neural Machine Translation

In July 2017, Google Brain's Thang Luong and Eugene Brevdo posted a [blog](https://research.googleblog.com/2017/07/building-your-own-neural-machine.html) announcing a Neural Machine Translation (NMT) [tutorial](https://github.com/tensorflow/nmt) for TensorFlow. We will follow their intial steps to build a basic NMT system.

```bash
git clone https://github.com/tensorflow/nmt/
cd nmt
nmt/scripts/download_iwslt15.sh /tmp/nmt_data
mkdir /tmp/nmt_model
```

Finally, we are just one big command away from training an NMT model! The model will train 12000 steps. On our powerful GPU computer, it should just take a little more than one hour!

```bash
python -m nmt.nmt \
    --src=vi --tgt=en \
    --vocab_prefix=/tmp/nmt_data/vocab  \
    --train_prefix=/tmp/nmt_data/train \
    --dev_prefix=/tmp/nmt_data/tst2012  \
    --test_prefix=/tmp/nmt_data/tst2013 \
    --out_dir=/tmp/nmt_model \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=2 \
    --num_units=128 \
    --dropout=0.2 \
    --metrics=bleu
```

On this instance, our model trains at less than 0.30s per 100 steps, even a few times faster than what's reported in the tutorial!

![](http://realai.org/assets/images/course-tpu-tf-nmt-2.png)

