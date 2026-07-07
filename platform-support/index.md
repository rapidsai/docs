# RAPIDS Platform Support

RAPIDS libraries are supported on a specific set of platforms for each release. RAPIDS
depends on CUDA and Python, and each release is built and tested against specific
versions of these dependencies.

RAPIDS uses [CUDA compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/) to
support a range of CUDA toolkit and driver versions. The NVIDIA Developer documentation
contains a [Compute Capability](https://developer.nvidia.com/cuda-gpus) reference for
each GPU architecture. Newer GPUs are supported through
[forward-compatible PTX instructions](https://developer.nvidia.com/blog/understanding-ptx-the-assembly-language-of-cuda-gpu-computing/)
built for the latest virtual architecture.

For installation instructions, see the [Installation Guide](/install/).

{{ platform_support_content() }}
