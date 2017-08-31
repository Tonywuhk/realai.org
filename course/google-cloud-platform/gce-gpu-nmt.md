---
permalink: /course/google-cloud-platform/gce-gpu-nmt/
title: Course | GCP | GCE | Neural Machine Translation using GPU
---
[Home](http://realai.org/) > [Course](http://realai.org/course/) > [TensorFlow](http://realai.org/course/tensorflow/) > [GPU](http://realai.org/course/tensorflow/#gpu) >

# Neural Machine Translation using GPU on Google Compute Engine

*Last Updated: August 31, 2017*

In this experiment, we walk through the steps to train a neural machine translation model with a [GPU](http://realai.org/course/tensorflow/#gpu) on [Google Compute Engine](http://realai.org/course/google-cloud-platform/#google-compute-engine).

## Prerequisites

* A Google cloud account with at least a few US dollars of credit. Typically, a user receives [$300 free credit](https://cloud.google.com/free/) over a [12-month trial period](https://cloud.google.com/free/docs/frequently-asked-questions#free-trial). A credit card is needed to create an account.

* Join the [NVIDIA Developer Program](https://developer.nvidia.com/developer-program). Membership is required for [cuDNN download](https://developer.nvidia.com/rdp/cudnn-download). Save the [Linux version](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v6/prod/8.0_20170307/cudnn-8.0-linux-x64-v6.0-tgz) of "cuDNN v6.0 (April 27, 2017), for CUDA 8.0" in a directory on your local computer.

## VM Instance

Create a virtual machine (VM) instance in [Compute Engine](https://console.cloud.google.com/compute/). We don't need a GPU for software installation, so let's create a very cheap "f1-micro" machine in a nearby [Zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones). Select the "Ubuntu 16.04 LTS" image to create a boot disk.

## GPU Setup - CUDA

[CUDA](http://www.nvidia.com/object/cuda_home_new.html) (Compute Unified Device Architecture) is a toolkit created by [NVIDIA](http://www.nvidia.com) that allows us to use its GPUs. CUDA has an official [Installation Guide for Linux](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html). According to the Guide's [System Requirements](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements), we need to have [gcc](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) on our system:

```bash
sudo apt-get update
sudo apt-get install build-essential -y
```

Now download CUDA from [CUDA Toolkit Download](https://developer.nvidia.com/cuda-downloads), then follow the Guide's [instructions for Ubuntu](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#ubuntu-installation):

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

[cuDNN](https://developer.nvidia.com/cudnn) provides highly-tuned building blocks specifically for deep learning, such as convolution, pooling, and normalization. Click the gear icon on the upper right corner of the terminal, select the cuDNN file downloaded earlier, and upload it to the VM. After the file is transferred to the cloud, follow these steps based on the official instructions for [Installing cuDNN on Linux](http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installlinux):

```bash
tar -xzvf cudnn-8.0-linux-x64-v6.0.tgz
sudo cp cuda/lib64/* /usr/local/cuda/lib64/
sudo cp cuda/include/* /usr/local/cuda/include/
```

Now both CUDA and cuDNN are installed. Let's clean up the files:

```bash
rm cuda-repo-ubuntu1604_8.0.61-1_amd64.deb 
rm -rf cuda
rm cudnn-8.0-linux-x64-v5.1.tgz
```

The NVIDIA portion of the installation is now complete. Let's move to [TensorFlow](http://realai.org/course/tensorflow/).

## TensorFlow Setup

Following the requirements on [official TensorFlow installation instructions](https://www.tensorflow.org/install/install_linux), we first install a library:

```bash
sudo apt-get install libcupti-dev -y
```

Then we get pip from [Python Software Foundation](https://packaging.python.org/tutorials/installing-packages/):

```bash
curl https://bootstrap.pypa.io/get-pip.py | sudo python3 get-pip.py
```

### Moving VM Instance

Type 'exit' to close the terminal, then STOP (DO NOT **DELETE**) the VM instance on which we just installed GPU software. In [Snapshots](https://console.cloud.google.com/compute/snapshots), create a snapshot of this instance. Go back to "VM instances" and `DELETE` the instance if you like since we've already created a snapshot. Now it's time to get a powerful GPU computer.

In Oregon, an "n1-standard-2" machine type costs [$0.095 per hour](https://cloud.google.com/compute/pricing#predefined_machine_types) and 1 GPU processor costs [$0.70 per hour](https://cloud.google.com/compute/pricing#gpus). We create a new VM in Zone "us-west1-b" using these parameters.

![](http://realai.org/course/google-cloud-platform/gce-gpu-nmt-1.png)

On this new VM, we do a [native pip](https://www.tensorflow.org/install/install_linux#InstallingNativePip) TensorFlow installation:

```bash
sudo pip install tensorflow-gpu
```

### Jupyter Notebook (Optional)

If needed, install [Jupyter Notebook](http://realai.org/course/jupyter/):

```bash
sudo pip install jupyter
```

For readers who expect to use more VMs running TensorFlow on GPU, now is a good time to create an image or a snapshot. New VMs can be directly created in the future. To easily distinguish different installations, consider naming the image or snapshot with package names and versions such as `cuda8-0-cudnn6-0-pip3`.

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

On this instance, our model trains at around 0.20s per step, even a few times faster than what's reported in the tutorial!

![](http://realai.org/course/google-cloud-platform/gce-gpu-nmt-2.png)

