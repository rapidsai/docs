<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<tagfile doxygen_version="1.8.20" doxygen_gitid="96e72f598f3db6894cc3227a9f7df1e612357a42*">
  <compound kind="file">
    <name>device_buffer.hpp</name>
    <path>/rapids/rmm/include/rmm/</path>
    <filename>device__buffer_8hpp.html</filename>
    <includes id="per__device__resource_8hpp" name="per_device_resource.hpp" local="no" imported="no">rmm/mr/device/per_device_resource.hpp</includes>
    <class kind="class">rmm::device_buffer</class>
  </compound>
  <compound kind="file">
    <name>exec_policy.hpp</name>
    <path>/rapids/rmm/include/rmm/</path>
    <filename>exec__policy_8hpp.html</filename>
    <class kind="class">rmm::exec_policy</class>
  </compound>
  <compound kind="file">
    <name>per_device_resource.hpp</name>
    <path>/rapids/rmm/include/rmm/mr/device/</path>
    <filename>per__device__resource_8hpp.html</filename>
    <member kind="function">
      <type>device_memory_resource *</type>
      <name>initial_resource</name>
      <anchorfile>per__device__resource_8hpp.html</anchorfile>
      <anchor>a8be55b82ca1fcd81cddd707e25dbbe8b</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>device_memory_resource *</type>
      <name>get_per_device_resource</name>
      <anchorfile>per__device__resource_8hpp.html</anchorfile>
      <anchor>af17df2d070b6befdf6343742a9391b09</anchor>
      <arglist>(cuda_device_id id)</arglist>
    </member>
    <member kind="function">
      <type>device_memory_resource *</type>
      <name>set_per_device_resource</name>
      <anchorfile>per__device__resource_8hpp.html</anchorfile>
      <anchor>a6d38bff906b6001948fd275265ebbcc0</anchor>
      <arglist>(cuda_device_id id, device_memory_resource *new_mr)</arglist>
    </member>
    <member kind="function">
      <type>device_memory_resource *</type>
      <name>get_current_device_resource</name>
      <anchorfile>per__device__resource_8hpp.html</anchorfile>
      <anchor>a95bf69637b8f3d29b13b33562370fc8f</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>device_memory_resource *</type>
      <name>set_current_device_resource</name>
      <anchorfile>per__device__resource_8hpp.html</anchorfile>
      <anchor>a3d74a9fb18c09c8f6409ac222b559d44</anchor>
      <arglist>(device_memory_resource *new_mr)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::aligned_resource_adaptor</name>
    <filename>classrmm_1_1mr_1_1aligned__resource__adaptor.html</filename>
    <templarg></templarg>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type></type>
      <name>aligned_resource_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1aligned__resource__adaptor.html</anchorfile>
      <anchor>a32642af1a577ae930d76a8aa350656a2</anchor>
      <arglist>(Upstream *upstream, std::size_t allocation_alignment=rmm::detail::CUDA_ALLOCATION_ALIGNMENT, std::size_t alignment_threshold=default_alignment_threshold)</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1aligned__resource__adaptor.html</anchorfile>
      <anchor>aa88f4b97ef458b2389251da4eb0e50a1</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1aligned__resource__adaptor.html</anchorfile>
      <anchor>ae135f9e461944cce4897117bf9547423</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1aligned__resource__adaptor.html</anchorfile>
      <anchor>a13fe7429db0d9ec7847ce8907065eb33</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::tracking_resource_adaptor::allocation_info</name>
    <filename>structrmm_1_1mr_1_1tracking__resource__adaptor_1_1allocation__info.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::detail::arena::arena</name>
    <filename>classrmm_1_1mr_1_1detail_1_1arena_1_1arena.html</filename>
    <templarg></templarg>
    <member kind="function">
      <type></type>
      <name>arena</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1arena.html</anchorfile>
      <anchor>a22599f2dab3727a7b2e1019bf5a9dfff</anchor>
      <arglist>(global_arena&lt; Upstream &gt; &amp;global_arena)</arglist>
    </member>
    <member kind="function">
      <type>void *</type>
      <name>allocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1arena.html</anchorfile>
      <anchor>a3a9cf415216f0b50104b34572e72a0bf</anchor>
      <arglist>(std::size_t bytes)</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1arena.html</anchorfile>
      <anchor>ab4ecb933435fde24875af21e457682c7</anchor>
      <arglist>(void *p, std::size_t bytes, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>clean</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1arena.html</anchorfile>
      <anchor>ab98c95b4d8f1781aabda59abc5eec4ae</anchor>
      <arglist>()</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::detail::arena::arena_cleaner</name>
    <filename>classrmm_1_1mr_1_1detail_1_1arena_1_1arena__cleaner.html</filename>
    <templarg></templarg>
  </compound>
  <compound kind="class">
    <name>rmm::mr::arena_memory_resource</name>
    <filename>classrmm_1_1mr_1_1arena__memory__resource.html</filename>
    <templarg></templarg>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type></type>
      <name>arena_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1arena__memory__resource.html</anchorfile>
      <anchor>aa7215b0de2d2d5e4b7acdcdd2ebb7b03</anchor>
      <arglist>(Upstream *upstream_mr, std::size_t initial_size=global_arena::default_initial_size, std::size_t maximum_size=global_arena::default_maximum_size)</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1arena__memory__resource.html</anchorfile>
      <anchor>a55cb4048f3e0f5fe2061ea7fc6dd478a</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1arena__memory__resource.html</anchorfile>
      <anchor>a3f7cce06d7b3f53c99a4732f7d5cd808</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::bad_alloc</name>
    <filename>classrmm_1_1bad__alloc.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::binning_memory_resource</name>
    <filename>classrmm_1_1mr_1_1binning__memory__resource.html</filename>
    <templarg></templarg>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type></type>
      <name>binning_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1binning__memory__resource.html</anchorfile>
      <anchor>a0581682b0f5da81152183901d9f5bd8d</anchor>
      <arglist>(Upstream *upstream_resource)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>binning_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1binning__memory__resource.html</anchorfile>
      <anchor>abda4ad41b064c92ff407b2d45fa00868</anchor>
      <arglist>(Upstream *upstream_resource, int8_t min_size_exponent, int8_t max_size_exponent)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>~binning_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1binning__memory__resource.html</anchorfile>
      <anchor>a0ff3bef0cfd9f5a5bf8e70fc3369b307</anchor>
      <arglist>()=default</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1binning__memory__resource.html</anchorfile>
      <anchor>af8cc76a991be58017f25bababafa84eb</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1binning__memory__resource.html</anchorfile>
      <anchor>a48667e040fe653c1a618966cbaab872b</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1binning__memory__resource.html</anchorfile>
      <anchor>aaf6724460b633bb0a4690ff8f1113efc</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>add_bin</name>
      <anchorfile>classrmm_1_1mr_1_1binning__memory__resource.html</anchorfile>
      <anchor>a238799d03cd79bef49144597c57690d1</anchor>
      <arglist>(std::size_t allocation_size, device_memory_resource *bin_resource=nullptr)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::detail::arena::block</name>
    <filename>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</filename>
    <member kind="function">
      <type></type>
      <name>block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>af0924fe6108bce7f2221b806a97a8450</anchor>
      <arglist>()=default</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>a0772c988a344aeca7d5a3ff1c6ee9bca</anchor>
      <arglist>(char *pointer, std::size_t size)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>a0c1694622727eb07b79089551ce6a8c7</anchor>
      <arglist>(void *pointer, std::size_t size)</arglist>
    </member>
    <member kind="function">
      <type>void *</type>
      <name>pointer</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>afbdb96737c2f813bf758a762543214a9</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>size</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>a0b1b32a7a18fc0e142ba278826bf7125</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_valid</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>abfaef96467aabf64f7fd82811f767646</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_superblock</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>ac45a0299e74e768af8a6adcf6ab5492c</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_contiguous_before</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>a9e4467e759b1bda668be3bb4db5933e1</anchor>
      <arglist>(block const &amp;b) const</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>fits</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>a9424b78770c5be89a0b842cbab9e51ce</anchor>
      <arglist>(std::size_t sz) const</arglist>
    </member>
    <member kind="function">
      <type>std::pair&lt; block, block &gt;</type>
      <name>split</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>a72c5731d9ae27febf1756c13d65b4f86</anchor>
      <arglist>(std::size_t sz) const</arglist>
    </member>
    <member kind="function">
      <type>block</type>
      <name>merge</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>aedf7951e414146748bc775086627034d</anchor>
      <arglist>(block const &amp;b) const</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>operator&lt;</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1block.html</anchorfile>
      <anchor>aed0d8e571e72c619a3616f4a2a705772</anchor>
      <arglist>(block const &amp;b) const</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::detail::block</name>
    <filename>structrmm_1_1mr_1_1detail_1_1block.html</filename>
    <base>rmm::mr::detail::block_base</base>
    <member kind="function">
      <type>char *</type>
      <name>pointer</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>af354da2f9960674a7d05fab654b83770</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>size</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>a95793d6bf9d616a58f07f7d4490e4f81</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_head</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>acb8376785d0e2d1e3959d2edf6d26916</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>operator&lt;</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>a82a81a79e5354b7cc3b741f19dfe1540</anchor>
      <arglist>(block const &amp;rhs) const noexcept</arglist>
    </member>
    <member kind="function">
      <type>block</type>
      <name>merge</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>af577aaaaa1d07761e84f7d67b8c02c63</anchor>
      <arglist>(block const &amp;b) const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_contiguous_before</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>a5f290516a8c26869705f2bf2629c3d91</anchor>
      <arglist>(block const &amp;b) const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>fits</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>a954249ebc3a2b2d49d41bb7f31929363</anchor>
      <arglist>(std::size_t sz) const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_better_fit</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>a553eb1612fd08d5d4c7922e0d55de3bf</anchor>
      <arglist>(std::size_t sz, block const &amp;b) const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>print</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block.html</anchorfile>
      <anchor>a889973727820b228c54e32f1553d9ece</anchor>
      <arglist>() const</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::detail::block_base</name>
    <filename>structrmm_1_1mr_1_1detail_1_1block__base.html</filename>
    <member kind="function">
      <type>void *</type>
      <name>pointer</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block__base.html</anchorfile>
      <anchor>abac93ee1f75419e2613f096b9eefd5ee</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_valid</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block__base.html</anchorfile>
      <anchor>aa2c5c4fdc11701c5f2786beca86d38f3</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>print</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block__base.html</anchorfile>
      <anchor>a0c2db264ab69751e6614c38b949462be</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="variable">
      <type>void *</type>
      <name>ptr</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1block__base.html</anchorfile>
      <anchor>a72c4e6db5cfe26694b7592b362ce3f9f</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::detail::coalescing_free_list</name>
    <filename>structrmm_1_1mr_1_1detail_1_1coalescing__free__list.html</filename>
    <base>free_list&lt; block &gt;</base>
    <member kind="function">
      <type>void</type>
      <name>insert</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1coalescing__free__list.html</anchorfile>
      <anchor>aeb512047937081188d47761829d87171</anchor>
      <arglist>(block_type const &amp;b)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>insert</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1coalescing__free__list.html</anchorfile>
      <anchor>acdeb6e92ef9584bf3c4287a1a45a92bc</anchor>
      <arglist>(free_list &amp;&amp;other)</arglist>
    </member>
    <member kind="function">
      <type>block_type</type>
      <name>get_block</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1coalescing__free__list.html</anchorfile>
      <anchor>a63bd66fe10f077cf1e1e32eac7f60669</anchor>
      <arglist>(std::size_t size)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>print</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1coalescing__free__list.html</anchorfile>
      <anchor>a650087a794307b1e49c2361bdf59ef34</anchor>
      <arglist>() const</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::detail::compare_blocks</name>
    <filename>structrmm_1_1mr_1_1detail_1_1compare__blocks.html</filename>
    <templarg></templarg>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::statistics_resource_adaptor::counter</name>
    <filename>structrmm_1_1mr_1_1statistics__resource__adaptor_1_1counter.html</filename>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::detail::crtp</name>
    <filename>structrmm_1_1mr_1_1detail_1_1crtp.html</filename>
    <templarg></templarg>
  </compound>
  <compound kind="class">
    <name>crtp&lt; fixed_size_memory_resource&lt; Upstream &gt; &gt;</name>
    <filename>structrmm_1_1mr_1_1detail_1_1crtp.html</filename>
  </compound>
  <compound kind="class">
    <name>crtp&lt; pool_memory_resource&lt; Upstream &gt; &gt;</name>
    <filename>structrmm_1_1mr_1_1detail_1_1crtp.html</filename>
  </compound>
  <compound kind="class">
    <name>crtp&lt; PoolResource &gt;</name>
    <filename>structrmm_1_1mr_1_1detail_1_1crtp.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::cuda_async_memory_resource</name>
    <filename>classrmm_1_1mr_1_1cuda__async__memory__resource.html</filename>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type></type>
      <name>cuda_async_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1cuda__async__memory__resource.html</anchorfile>
      <anchor>afc896f1fbf993cd68918a3c4779421f2</anchor>
      <arglist>(thrust::optional&lt; std::size_t &gt; initial_pool_size={}, thrust::optional&lt; std::size_t &gt; release_threshold={})</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1cuda__async__memory__resource.html</anchorfile>
      <anchor>a1f4a03ddac6152e2727d2e9d58069ea2</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1cuda__async__memory__resource.html</anchorfile>
      <anchor>a403025ec8d405306db6c7ad0119a4627</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::cuda_device_id</name>
    <filename>structrmm_1_1cuda__device__id.html</filename>
    <member kind="function">
      <type>constexpr</type>
      <name>cuda_device_id</name>
      <anchorfile>structrmm_1_1cuda__device__id.html</anchorfile>
      <anchor>a35360d244654fbaa0f8458635436195d</anchor>
      <arglist>(value_type id) noexcept</arglist>
    </member>
    <member kind="function">
      <type>constexpr value_type</type>
      <name>value</name>
      <anchorfile>structrmm_1_1cuda__device__id.html</anchorfile>
      <anchor>aa05c9581ee7b33e65872e8b9ad89f54f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::cuda_error</name>
    <filename>structrmm_1_1cuda__error.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::cuda_memory_resource</name>
    <filename>classrmm_1_1mr_1_1cuda__memory__resource.html</filename>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1cuda__memory__resource.html</anchorfile>
      <anchor>af3319eeb30d26e14eb8195e6e159d746</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1cuda__memory__resource.html</anchorfile>
      <anchor>a3563add585e326f27107a41333f11c8b</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::cuda_stream</name>
    <filename>classrmm_1_1cuda__stream.html</filename>
    <member kind="function">
      <type></type>
      <name>cuda_stream</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>ac932f583a6b7c4a25baaa3481ea18506</anchor>
      <arglist>(cuda_stream &amp;&amp;)=default</arglist>
    </member>
    <member kind="function">
      <type>cuda_stream &amp;</type>
      <name>operator=</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>a786c7c3f29323597d56519bb22206c01</anchor>
      <arglist>(cuda_stream &amp;&amp;)=default</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>cuda_stream</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>a6c804b70001045b587624e7d1fbc0205</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_valid</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>a3afde407c9080c8dee17d6cd18925c8c</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>cudaStream_t</type>
      <name>value</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>a82017e39bf917d996b424782fb2b60de</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>operator cudaStream_t</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>a635a07de639be1c20d37ea28bed8febb</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>cuda_stream_view</type>
      <name>view</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>ac8752d5c123ebf3ed8581a6f2934f907</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>operator cuda_stream_view</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>ab0138dc1162b41b00235ad898a84ef13</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>synchronize</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>a60b279c6a6ce72ddfe80b8ffe324c95c</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>synchronize_no_throw</name>
      <anchorfile>classrmm_1_1cuda__stream.html</anchorfile>
      <anchor>a1b89c54b9856ba46f547a82b3632a04e</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::cuda_stream_pool</name>
    <filename>classrmm_1_1cuda__stream__pool.html</filename>
    <member kind="function">
      <type></type>
      <name>cuda_stream_pool</name>
      <anchorfile>classrmm_1_1cuda__stream__pool.html</anchorfile>
      <anchor>a66368ae209bb22184472475fbe90cef2</anchor>
      <arglist>(std::size_t pool_size=default_size)</arglist>
    </member>
    <member kind="function">
      <type>rmm::cuda_stream_view</type>
      <name>get_stream</name>
      <anchorfile>classrmm_1_1cuda__stream__pool.html</anchorfile>
      <anchor>a9d08ead85b8cc3b430dbe3decceffcef</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>rmm::cuda_stream_view</type>
      <name>get_stream</name>
      <anchorfile>classrmm_1_1cuda__stream__pool.html</anchorfile>
      <anchor>ad9485ab27569aed524ff1d0152fca25d</anchor>
      <arglist>(std::size_t stream_id) const</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>get_pool_size</name>
      <anchorfile>classrmm_1_1cuda__stream__pool.html</anchorfile>
      <anchor>a6d368c94a0c5a6f62acb52aed34efa0f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="variable" static="yes">
      <type>static constexpr std::size_t</type>
      <name>default_size</name>
      <anchorfile>classrmm_1_1cuda__stream__pool.html</anchorfile>
      <anchor>a3b2ccc40ad090b9172493134df1949b3</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::cuda_stream_view</name>
    <filename>classrmm_1_1cuda__stream__view.html</filename>
    <member kind="function">
      <type>constexpr</type>
      <name>cuda_stream_view</name>
      <anchorfile>classrmm_1_1cuda__stream__view.html</anchorfile>
      <anchor>a4ae6cba0b4329610296d2dc97a0eba91</anchor>
      <arglist>(cudaStream_t stream) noexcept</arglist>
    </member>
    <member kind="function">
      <type>constexpr cudaStream_t</type>
      <name>value</name>
      <anchorfile>classrmm_1_1cuda__stream__view.html</anchorfile>
      <anchor>a17aac270b340f8d9f73ad88c9636954f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>constexpr</type>
      <name>operator cudaStream_t</name>
      <anchorfile>classrmm_1_1cuda__stream__view.html</anchorfile>
      <anchor>abd4d537ed87e1c1cefccdfd210a4ba1e</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_per_thread_default</name>
      <anchorfile>classrmm_1_1cuda__stream__view.html</anchorfile>
      <anchor>a9a02dc7d011ac52c4c65d8765342437b</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_default</name>
      <anchorfile>classrmm_1_1cuda__stream__view.html</anchorfile>
      <anchor>adf1adb7e26fb605ce52bc23cb914c604</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>synchronize</name>
      <anchorfile>classrmm_1_1cuda__stream__view.html</anchorfile>
      <anchor>a20c55f7dd2db68e9accf33564448ba9c</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>synchronize_no_throw</name>
      <anchorfile>classrmm_1_1cuda__stream__view.html</anchorfile>
      <anchor>ac41b02768d2afeba32d766db722748c0</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::device_buffer</name>
    <filename>classrmm_1_1device__buffer.html</filename>
    <member kind="function">
      <type></type>
      <name>device_buffer</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a6bd6712c7a8ad6810145856f73066f94</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_buffer</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a36ffe1d525da56c1e8266d15e5d593bb</anchor>
      <arglist>(std::size_t size, cuda_stream_view stream, mr::device_memory_resource *mr=mr::get_current_device_resource())</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_buffer</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a7bc59ca0c76410a5178b24ca2b5c070d</anchor>
      <arglist>(void const *source_data, std::size_t size, cuda_stream_view stream, mr::device_memory_resource *mr=mr::get_current_device_resource())</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_buffer</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a368193ff6b77c4bf1dcc2ba57e6daaef</anchor>
      <arglist>(device_buffer const &amp;other, cuda_stream_view stream, rmm::mr::device_memory_resource *mr=rmm::mr::get_current_device_resource())</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_buffer</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>abc92e1e7ea3c5658de821da1f78704ac</anchor>
      <arglist>(device_buffer &amp;&amp;other) noexcept</arglist>
    </member>
    <member kind="function">
      <type>device_buffer &amp;</type>
      <name>operator=</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a5ce2f5ed5babb13e7750d9a255297b11</anchor>
      <arglist>(device_buffer &amp;&amp;other) noexcept</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>~device_buffer</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a361c327d720bb5916e7b09748d8806fd</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>resize</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a183ba74b4fb130feadcfceabe08150b3</anchor>
      <arglist>(std::size_t new_size, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>shrink_to_fit</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>ac34d5ed42d76731b9e63f4766271d7d4</anchor>
      <arglist>(cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type>void const  *</type>
      <name>data</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a7e22e7428462ff6447d43a3ff035570c</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void *</type>
      <name>data</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a2a724b2e0647ee56f5be27efaf6cc60f</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>size</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>ab6c9cb10ec73d49b75fba12d32e4faa5</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_empty</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>ae650c01f3157e358bb06b2654ba70fdb</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>capacity</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a6f10a1f11dc186eeb6493980ab3d7fc5</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>cuda_stream_view</type>
      <name>stream</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a0d80c18fa46c00c73b9757f1945e892f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>set_stream</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>ab271ced85f304e3061a3ff72526dbc37</anchor>
      <arglist>(cuda_stream_view stream) noexcept</arglist>
    </member>
    <member kind="function">
      <type>mr::device_memory_resource *</type>
      <name>memory_resource</name>
      <anchorfile>classrmm_1_1device__buffer.html</anchorfile>
      <anchor>a66482dd6bb2c4a551c992c74b3a5b766</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::device_memory_resource</name>
    <filename>classrmm_1_1mr_1_1device__memory__resource.html</filename>
    <member kind="function">
      <type>void *</type>
      <name>allocate</name>
      <anchorfile>classrmm_1_1mr_1_1device__memory__resource.html</anchorfile>
      <anchor>a54b78031deb92654df581d496b9b8099</anchor>
      <arglist>(std::size_t bytes, cuda_stream_view stream=cuda_stream_view{})</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1device__memory__resource.html</anchorfile>
      <anchor>a38c7c6a0c4bbb2d3c9ac7aaafda1c8e6</anchor>
      <arglist>(void *p, std::size_t bytes, cuda_stream_view stream=cuda_stream_view{})</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_equal</name>
      <anchorfile>classrmm_1_1mr_1_1device__memory__resource.html</anchorfile>
      <anchor>aeaed913bfdd02266062b7880d5bb350f</anchor>
      <arglist>(device_memory_resource const &amp;other) const noexcept</arglist>
    </member>
    <member kind="function" virtualness="pure">
      <type>virtual bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1device__memory__resource.html</anchorfile>
      <anchor>a04598a0abd19625d081a69599360b215</anchor>
      <arglist>() const noexcept=0</arglist>
    </member>
    <member kind="function" virtualness="pure">
      <type>virtual bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1device__memory__resource.html</anchorfile>
      <anchor>a96e73e2a8eca60ee7b1c86ed03d7538b</anchor>
      <arglist>() const noexcept=0</arglist>
    </member>
    <member kind="function">
      <type>std::pair&lt; std::size_t, std::size_t &gt;</type>
      <name>get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1device__memory__resource.html</anchorfile>
      <anchor>a017ba1b464063d71942875a5178f8668</anchor>
      <arglist>(cuda_stream_view stream) const</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::device_scalar</name>
    <filename>classrmm_1_1device__scalar.html</filename>
    <templarg></templarg>
    <member kind="function">
      <type></type>
      <name>device_scalar</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>a8541298147e83da303be0487106e501e</anchor>
      <arglist>(device_scalar const &amp;)=delete</arglist>
    </member>
    <member kind="function">
      <type>device_scalar &amp;</type>
      <name>operator=</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>ada75c148a079dca2456332bc1f80abc9</anchor>
      <arglist>(device_scalar const &amp;)=delete</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_scalar</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>aee123349af188b9f06329e7e8d6680c2</anchor>
      <arglist>()=delete</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_scalar</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>aa9ebaac490a1ab5c4f38ab98445cf0ed</anchor>
      <arglist>(cuda_stream_view stream, rmm::mr::device_memory_resource *mr=rmm::mr::get_current_device_resource())</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_scalar</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>ae1ea9cb2d465578acd5e7ee220cd30a6</anchor>
      <arglist>(value_type const &amp;initial_value, cuda_stream_view stream, rmm::mr::device_memory_resource *mr=rmm::mr::get_current_device_resource())</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_scalar</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>a7d3727d0234de959c8e8efad43d94ccb</anchor>
      <arglist>(device_scalar const &amp;other, cuda_stream_view stream, rmm::mr::device_memory_resource *mr=rmm::mr::get_current_device_resource())</arglist>
    </member>
    <member kind="function">
      <type>value_type</type>
      <name>value</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>accaba5c261ea7f8d3252ae255f30d9ac</anchor>
      <arglist>(cuda_stream_view stream) const</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>set_value_async</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>a8720eef38de810004965e485706b5e31</anchor>
      <arglist>(value_type const &amp;v, cuda_stream_view s)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>set_value_to_zero_async</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>ac9ddf59c74d16d83c670f9752b0397f0</anchor>
      <arglist>(cuda_stream_view s)</arglist>
    </member>
    <member kind="function">
      <type>pointer</type>
      <name>data</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>abcc1af62f0c6a80c6bbf29e80a6a75bf</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_pointer</type>
      <name>data</name>
      <anchorfile>classrmm_1_1device__scalar.html</anchorfile>
      <anchor>a34979514a931225e7c14c65472323c1b</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::device_uvector</name>
    <filename>classrmm_1_1device__uvector.html</filename>
    <templarg></templarg>
    <member kind="function">
      <type></type>
      <name>device_uvector</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a28ced74941f677048210e45bc851b87b</anchor>
      <arglist>(device_uvector const &amp;)=delete</arglist>
    </member>
    <member kind="function">
      <type>device_uvector &amp;</type>
      <name>operator=</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a991948318367bfff1d768ee91438371d</anchor>
      <arglist>(device_uvector const &amp;)=delete</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_uvector</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>ace41a8c2cdfb33b0ff01ca699527416d</anchor>
      <arglist>()=delete</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_uvector</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>aaf8e36f398137fea17b8403908c817e8</anchor>
      <arglist>(std::size_t size, cuda_stream_view stream, rmm::mr::device_memory_resource *mr=rmm::mr::get_current_device_resource())</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>device_uvector</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a6e637517602312be687f5231bd20d7cc</anchor>
      <arglist>(device_uvector const &amp;other, cuda_stream_view stream, rmm::mr::device_memory_resource *mr=rmm::mr::get_current_device_resource())</arglist>
    </member>
    <member kind="function">
      <type>pointer</type>
      <name>element_ptr</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a736cb6f26d05740356b2250383154275</anchor>
      <arglist>(std::size_t element_index) noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_pointer</type>
      <name>element_ptr</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a268f1916ed433f16fdbd1a1e62ded7fc</anchor>
      <arglist>(std::size_t element_index) const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>set_element_async</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>afbdc625ba4fd0d5c3f87e364bd8c65f6</anchor>
      <arglist>(std::size_t element_index, value_type const &amp;v, cuda_stream_view s)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>set_element_to_zero_async</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a61e085520deb7a6f0b0c316b1ca799f6</anchor>
      <arglist>(std::size_t element_index, cuda_stream_view s)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>set_element</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a80ff08f7195e98e7de1176097c6651c0</anchor>
      <arglist>(std::size_t element_index, T const &amp;v, cuda_stream_view s)</arglist>
    </member>
    <member kind="function">
      <type>value_type</type>
      <name>element</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>adbf5097fbf94b7f147aea7fb571fc3ea</anchor>
      <arglist>(std::size_t element_index, cuda_stream_view s) const</arglist>
    </member>
    <member kind="function">
      <type>value_type</type>
      <name>front_element</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a71df23a3dc3cba930dd70b7cd73d4947</anchor>
      <arglist>(cuda_stream_view s) const</arglist>
    </member>
    <member kind="function">
      <type>value_type</type>
      <name>back_element</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a01fc23eb75b33021fd2281f6c7941c6e</anchor>
      <arglist>(cuda_stream_view s) const</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>resize</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a12352ccb04d368540eb7ebf0ceb6ef20</anchor>
      <arglist>(std::size_t new_size, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>shrink_to_fit</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a58322e351f40b7419c2e09da3a8a6f47</anchor>
      <arglist>(cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type>device_buffer</type>
      <name>release</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a90d5b1937703ac8befe42807d5686e4a</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>capacity</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a11ada0f15bf7d25a70b6a3c6b4f52f8f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>pointer</type>
      <name>data</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a53e0aa307e0cc93c4fef5e410f1f40d1</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_pointer</type>
      <name>data</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a2f2100a00c59ae071568812aec023fbd</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>iterator</type>
      <name>begin</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>afd66a263437a87ff6ec1f3c33f61c589</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>cbegin</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a7de2d89114f7b7aaee795e5d22ebce68</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>begin</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>afd5e157b76dcdc58696b5891ee25a3ae</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>iterator</type>
      <name>end</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a5acf12a008a67f827cfa61db0ae1e8b1</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>cend</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a03e450d354cd8264cb3e9645a7fde54c</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>end</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>ab92af2fe8fc1cdf6060524659247c611</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>size</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a4d87b3421b2c9608115709351fa0b693</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_empty</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>a2d90e6e8ac5ce64b1562f494113ced94</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>mr::device_memory_resource *</type>
      <name>memory_resource</name>
      <anchorfile>classrmm_1_1device__uvector.html</anchorfile>
      <anchor>ab816bd74178d12d004a6bac4b1b43a34</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::exec_policy</name>
    <filename>classrmm_1_1exec__policy.html</filename>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::detail::fixed_size_free_list</name>
    <filename>structrmm_1_1mr_1_1detail_1_1fixed__size__free__list.html</filename>
    <base>free_list&lt; block_base &gt;</base>
    <member kind="function">
      <type></type>
      <name>fixed_size_free_list</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1fixed__size__free__list.html</anchorfile>
      <anchor>a0f8a012b96b6fce0013f14b407352c90</anchor>
      <arglist>(InputIt first, InputIt last)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>insert</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1fixed__size__free__list.html</anchorfile>
      <anchor>a5145c5fd0d20f515f8d9b16fa8aa8738</anchor>
      <arglist>(block_type const &amp;b)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>insert</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1fixed__size__free__list.html</anchorfile>
      <anchor>a169372023c146f5a466b8f8f2ec6450e</anchor>
      <arglist>(free_list &amp;&amp;other)</arglist>
    </member>
    <member kind="function">
      <type>block_type</type>
      <name>get_block</name>
      <anchorfile>structrmm_1_1mr_1_1detail_1_1fixed__size__free__list.html</anchorfile>
      <anchor>ae95497f34d4a1b34d878b99eb6174ba1</anchor>
      <arglist>(std::size_t size)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::fixed_size_memory_resource</name>
    <filename>classrmm_1_1mr_1_1fixed__size__memory__resource.html</filename>
    <templarg></templarg>
    <base>stream_ordered_memory_resource&lt; fixed_size_memory_resource&lt; Upstream &gt;, detail::fixed_size_free_list &gt;</base>
    <member kind="function">
      <type></type>
      <name>fixed_size_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>ac25e15734526ef7a80bb41bb3c12403b</anchor>
      <arglist>(Upstream *upstream_mr, std::size_t block_size=default_block_size, std::size_t blocks_to_preallocate=default_blocks_to_preallocate)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>~fixed_size_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>aa0c748d2c233130b3c54fb3ee7c80e19</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>ada97a74ce70102a1d45f02b9bfda4d10</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a2a829ee055652e87a5f373d3179743df</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a0f7e90b96e45548c24c744a2a84799ba</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>get_block_size</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a51987bd460b28bd0616f21f967d1b32f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::size_t</type>
      <name>get_maximum_allocation_size</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a728048c50f75c713fae3bf3641fa7b6e</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>block_type</type>
      <name>expand_pool</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a88b9ebfa1082ab6ae577fc55c18a6b26</anchor>
      <arglist>(std::size_t size, free_list &amp;blocks, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>free_list</type>
      <name>blocks_from_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a971b75ce7dda5cb23c15351f84902234</anchor>
      <arglist>(cuda_stream_view stream)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>split_block</type>
      <name>allocate_from_block</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a0c7cc01a60a03aabf1bb70d24357083d</anchor>
      <arglist>(block_type const &amp;b, std::size_t size)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>block_type</type>
      <name>free_block</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a78378668a5525d5a8b709003ba11c486</anchor>
      <arglist>(void *p, std::size_t size) noexcept</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::pair&lt; std::size_t, std::size_t &gt;</type>
      <name>do_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a366918431b3b9f5867e5d8fd7186f35a</anchor>
      <arglist>(cuda_stream_view stream) const override</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>release</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>aa511834124f63d82abfd7831dda483d8</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::pair&lt; std::size_t, std::size_t &gt;</type>
      <name>free_list_summary</name>
      <anchorfile>classrmm_1_1mr_1_1fixed__size__memory__resource.html</anchorfile>
      <anchor>a03ae72bfe093dcdb6e24df2ef6c58632</anchor>
      <arglist>(free_list const &amp;blocks)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::detail::free_list</name>
    <filename>classrmm_1_1mr_1_1detail_1_1free__list.html</filename>
    <templarg></templarg>
    <templarg></templarg>
    <member kind="function">
      <type>const_iterator</type>
      <name>begin</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a854a2a281e59d69752250f6a71bcff98</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>cbegin</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>aa528a1938cf8845f283fc03a0ca1f846</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>iterator</type>
      <name>end</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>ac9912eb22e2a5e1630e19453fbf80c5d</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>end</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>af658f86c5295bb4cb367e214d840d7f8</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>cend</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>ab4831094eea523cbbe8e2a4a505e0032</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>size_type</type>
      <name>size</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a88c37c7d5b2d845c638c5864c26b97bd</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_empty</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a4362cf121d720b25ad30d6c9bb6b315f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>erase</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a6408611a33c6ef1f61250466cce38ecb</anchor>
      <arglist>(const_iterator iter)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>clear</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a07019a2a1f959e0780d5f7299b023ff7</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>print</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a332374ffd8df897ffe7a3147cc35694c</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>insert</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a8924e9ebac8e1cbf2060d1077f207246</anchor>
      <arglist>(const_iterator pos, block_type const &amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>splice</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a87b61292ae9d22f48c5b91826113606f</anchor>
      <arglist>(const_iterator pos, free_list &amp;&amp;other)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>push_back</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a74c8c201a1f6f0c6315cf5dbf10fe13a</anchor>
      <arglist>(const block_type &amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>push_back</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a4863fa0900b34113d6824753258d2536</anchor>
      <arglist>(block_type &amp;&amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>pop_front</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a111f7ea85a2b7c99f135834657519923</anchor>
      <arglist>()</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>free_list&lt; block &gt;</name>
    <filename>classrmm_1_1mr_1_1detail_1_1free__list.html</filename>
    <member kind="function">
      <type>const_iterator</type>
      <name>begin</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a854a2a281e59d69752250f6a71bcff98</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>cbegin</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>aa528a1938cf8845f283fc03a0ca1f846</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>iterator</type>
      <name>end</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>ac9912eb22e2a5e1630e19453fbf80c5d</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>end</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>af658f86c5295bb4cb367e214d840d7f8</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>cend</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>ab4831094eea523cbbe8e2a4a505e0032</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>size_type</type>
      <name>size</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a88c37c7d5b2d845c638c5864c26b97bd</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_empty</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a4362cf121d720b25ad30d6c9bb6b315f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>erase</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a6408611a33c6ef1f61250466cce38ecb</anchor>
      <arglist>(const_iterator iter)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>clear</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a07019a2a1f959e0780d5f7299b023ff7</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>print</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a332374ffd8df897ffe7a3147cc35694c</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>insert</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a8924e9ebac8e1cbf2060d1077f207246</anchor>
      <arglist>(const_iterator pos, block_type const &amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>splice</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a87b61292ae9d22f48c5b91826113606f</anchor>
      <arglist>(const_iterator pos, free_list &amp;&amp;other)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>push_back</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a74c8c201a1f6f0c6315cf5dbf10fe13a</anchor>
      <arglist>(const block_type &amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>push_back</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a4863fa0900b34113d6824753258d2536</anchor>
      <arglist>(block_type &amp;&amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>pop_front</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a111f7ea85a2b7c99f135834657519923</anchor>
      <arglist>()</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>free_list&lt; block_base &gt;</name>
    <filename>classrmm_1_1mr_1_1detail_1_1free__list.html</filename>
    <member kind="function">
      <type>const_iterator</type>
      <name>begin</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a854a2a281e59d69752250f6a71bcff98</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>cbegin</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>aa528a1938cf8845f283fc03a0ca1f846</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>iterator</type>
      <name>end</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>ac9912eb22e2a5e1630e19453fbf80c5d</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>end</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>af658f86c5295bb4cb367e214d840d7f8</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>const_iterator</type>
      <name>cend</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>ab4831094eea523cbbe8e2a4a505e0032</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>size_type</type>
      <name>size</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a88c37c7d5b2d845c638c5864c26b97bd</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_empty</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a4362cf121d720b25ad30d6c9bb6b315f</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>erase</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a6408611a33c6ef1f61250466cce38ecb</anchor>
      <arglist>(const_iterator iter)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>clear</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a07019a2a1f959e0780d5f7299b023ff7</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>print</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a332374ffd8df897ffe7a3147cc35694c</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>insert</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a8924e9ebac8e1cbf2060d1077f207246</anchor>
      <arglist>(const_iterator pos, block_type const &amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>splice</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a87b61292ae9d22f48c5b91826113606f</anchor>
      <arglist>(const_iterator pos, free_list &amp;&amp;other)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>push_back</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a74c8c201a1f6f0c6315cf5dbf10fe13a</anchor>
      <arglist>(const block_type &amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>push_back</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a4863fa0900b34113d6824753258d2536</anchor>
      <arglist>(block_type &amp;&amp;b)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>pop_front</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1free__list.html</anchorfile>
      <anchor>a111f7ea85a2b7c99f135834657519923</anchor>
      <arglist>()</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::detail::arena::global_arena</name>
    <filename>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</filename>
    <templarg></templarg>
    <member kind="function">
      <type></type>
      <name>global_arena</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</anchorfile>
      <anchor>a3adf37bcf129f2c4ea78384ffe8d3fe6</anchor>
      <arglist>(Upstream *upstream_mr, std::size_t initial_size, std::size_t maximum_size)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>~global_arena</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</anchorfile>
      <anchor>a16bbded32f0ed473296d5ad10dfc0b64</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>block</type>
      <name>allocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</anchorfile>
      <anchor>a4daf92d526f65fd05478410ce0e8ba72</anchor>
      <arglist>(std::size_t bytes)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</anchorfile>
      <anchor>ad5c0b09745292c68e49a820ff7a3b746</anchor>
      <arglist>(block const &amp;b)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</anchorfile>
      <anchor>a1927ecc632589a7ada324082e2d056da</anchor>
      <arglist>(std::set&lt; block &gt; const &amp;free_blocks)</arglist>
    </member>
    <member kind="variable" static="yes">
      <type>static constexpr std::size_t</type>
      <name>default_initial_size</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</anchorfile>
      <anchor>a21deaed7471c49faf3de1433ac6b4401</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable" static="yes">
      <type>static constexpr std::size_t</type>
      <name>default_maximum_size</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</anchorfile>
      <anchor>a829283bd76a5e81912380a369bd4d6e5</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable" static="yes">
      <type>static constexpr std::size_t</type>
      <name>reserved_size</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1arena_1_1global__arena.html</anchorfile>
      <anchor>aa7ca12862921fb184159b304b7afae4c</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::host_memory_resource</name>
    <filename>classrmm_1_1mr_1_1host__memory__resource.html</filename>
    <member kind="function">
      <type>void *</type>
      <name>allocate</name>
      <anchorfile>classrmm_1_1mr_1_1host__memory__resource.html</anchorfile>
      <anchor>ad108db441d07a844552e86dd7c017d87</anchor>
      <arglist>(std::size_t bytes, std::size_t alignment=alignof(std::max_align_t))</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1host__memory__resource.html</anchorfile>
      <anchor>ab10391d28793937d14ebfeb1a2495a0f</anchor>
      <arglist>(void *p, std::size_t bytes, std::size_t alignment=alignof(std::max_align_t))</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>is_equal</name>
      <anchorfile>classrmm_1_1mr_1_1host__memory__resource.html</anchorfile>
      <anchor>a2d5e32a5c97753ea04b0645384a182cc</anchor>
      <arglist>(host_memory_resource const &amp;other) const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::limiting_resource_adaptor</name>
    <filename>classrmm_1_1mr_1_1limiting__resource__adaptor.html</filename>
    <templarg></templarg>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type></type>
      <name>limiting_resource_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1limiting__resource__adaptor.html</anchorfile>
      <anchor>a185d1deae69ab1c8ffa112d6e588db1b</anchor>
      <arglist>(Upstream *upstream, std::size_t allocation_limit, std::size_t allocation_alignment=rmm::detail::CUDA_ALLOCATION_ALIGNMENT)</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1limiting__resource__adaptor.html</anchorfile>
      <anchor>ae526e32f9abeddcc167eefc82559ac6a</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1limiting__resource__adaptor.html</anchorfile>
      <anchor>a7fc7fddb6c8d37572915be3cf7e08f89</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1limiting__resource__adaptor.html</anchorfile>
      <anchor>a682e865a6eda4c433dd194eaffe7beb6</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>get_allocated_bytes</name>
      <anchorfile>classrmm_1_1mr_1_1limiting__resource__adaptor.html</anchorfile>
      <anchor>a6722cea7ff47b3d7e8bcbb4e776c4fe7</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>get_allocation_limit</name>
      <anchorfile>classrmm_1_1mr_1_1limiting__resource__adaptor.html</anchorfile>
      <anchor>ac1dc1c11b46e05da35941ad5ebb2699a</anchor>
      <arglist>() const</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::detail::logger_wrapper</name>
    <filename>structrmm_1_1detail_1_1logger__wrapper.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::logging_resource_adaptor</name>
    <filename>classrmm_1_1mr_1_1logging__resource__adaptor.html</filename>
    <templarg></templarg>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type></type>
      <name>logging_resource_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1logging__resource__adaptor.html</anchorfile>
      <anchor>a67c7dfb43ee4d2fbf35c8b44d8bbd40e</anchor>
      <arglist>(Upstream *upstream, std::string const &amp;filename=get_default_filename(), bool auto_flush=false)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>logging_resource_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1logging__resource__adaptor.html</anchorfile>
      <anchor>a9e4d1ec70c8a7a873721772b75abd00a</anchor>
      <arglist>(Upstream *upstream, std::ostream &amp;stream, bool auto_flush=false)</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1logging__resource__adaptor.html</anchorfile>
      <anchor>a384edb8f34f873726d25bd66cf1cc7db</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1logging__resource__adaptor.html</anchorfile>
      <anchor>ae8b0851574e6a8932ad42e90f3b349ff</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1logging__resource__adaptor.html</anchorfile>
      <anchor>ab32833b8b28d244b6f803679e0bbeb98</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>flush</name>
      <anchorfile>classrmm_1_1mr_1_1logging__resource__adaptor.html</anchorfile>
      <anchor>a6089e298e3a32cd991d5bbbb5e9aeeb6</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>std::string</type>
      <name>header</name>
      <anchorfile>classrmm_1_1mr_1_1logging__resource__adaptor.html</anchorfile>
      <anchor>a14366e2436a1b8308e689b98f18e01b7</anchor>
      <arglist>() const</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::logic_error</name>
    <filename>structrmm_1_1logic__error.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::managed_memory_resource</name>
    <filename>classrmm_1_1mr_1_1managed__memory__resource.html</filename>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1managed__memory__resource.html</anchorfile>
      <anchor>ad01bf649a47380eef0bff9fb37d94a23</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1managed__memory__resource.html</anchorfile>
      <anchor>a37a79f2bf38945d0b3e6da64f7de4be0</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::new_delete_resource</name>
    <filename>classrmm_1_1mr_1_1new__delete__resource.html</filename>
    <base>rmm::mr::host_memory_resource</base>
  </compound>
  <compound kind="class">
    <name>rmm::out_of_range</name>
    <filename>classrmm_1_1out__of__range.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::owning_wrapper</name>
    <filename>classrmm_1_1mr_1_1owning__wrapper.html</filename>
    <templarg></templarg>
    <templarg>Upstreams</templarg>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type></type>
      <name>owning_wrapper</name>
      <anchorfile>classrmm_1_1mr_1_1owning__wrapper.html</anchorfile>
      <anchor>af02e7a0b6fef16159600c0edfe3f74da</anchor>
      <arglist>(upstream_tuple upstreams, Args &amp;&amp;... args)</arglist>
    </member>
    <member kind="function">
      <type>Resource const  &amp;</type>
      <name>wrapped</name>
      <anchorfile>classrmm_1_1mr_1_1owning__wrapper.html</anchorfile>
      <anchor>a053fcafbdc67ed937985e8ab265f8d4b</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>Resource &amp;</type>
      <name>wrapped</name>
      <anchorfile>classrmm_1_1mr_1_1owning__wrapper.html</anchorfile>
      <anchor>aba7b29a702573246825e6ec801770fc4</anchor>
      <arglist>() noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1owning__wrapper.html</anchorfile>
      <anchor>a0a31a8f02fc0bab64ceffca94d83ef1f</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1owning__wrapper.html</anchorfile>
      <anchor>a262d009ddfec9775a30bd6a7032d959a</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::pinned_memory_resource</name>
    <filename>classrmm_1_1mr_1_1pinned__memory__resource.html</filename>
    <base>rmm::mr::host_memory_resource</base>
  </compound>
  <compound kind="class">
    <name>rmm::mr::polymorphic_allocator</name>
    <filename>classrmm_1_1mr_1_1polymorphic__allocator.html</filename>
    <templarg></templarg>
    <member kind="function">
      <type></type>
      <name>polymorphic_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1polymorphic__allocator.html</anchorfile>
      <anchor>a5e490c15da8bd354f95e5a7957968737</anchor>
      <arglist>()=default</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>polymorphic_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1polymorphic__allocator.html</anchorfile>
      <anchor>a488eefb766f35c438c87b45aabe023ee</anchor>
      <arglist>(polymorphic_allocator&lt; T &gt; const &amp;other)=default</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>polymorphic_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1polymorphic__allocator.html</anchorfile>
      <anchor>a526ae5aa78d7214575d5104bc7f68da2</anchor>
      <arglist>(device_memory_resource *mr)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>polymorphic_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1polymorphic__allocator.html</anchorfile>
      <anchor>af13c4708d7d023a1afd923f039727e8e</anchor>
      <arglist>(polymorphic_allocator&lt; U &gt; const &amp;other) noexcept</arglist>
    </member>
    <member kind="function">
      <type>value_type *</type>
      <name>allocate</name>
      <anchorfile>classrmm_1_1mr_1_1polymorphic__allocator.html</anchorfile>
      <anchor>a8ed74cac43e985427c0ec7e239ae3444</anchor>
      <arglist>(std::size_t n, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1polymorphic__allocator.html</anchorfile>
      <anchor>af0546981bd5e56bedbcc425d6bfd4574</anchor>
      <arglist>(value_type *p, std::size_t n, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type>device_memory_resource *</type>
      <name>resource</name>
      <anchorfile>classrmm_1_1mr_1_1polymorphic__allocator.html</anchorfile>
      <anchor>a11266207e5674d321df50e76d626d28d</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::pool_memory_resource</name>
    <filename>classrmm_1_1mr_1_1pool__memory__resource.html</filename>
    <templarg></templarg>
    <base>stream_ordered_memory_resource&lt; pool_memory_resource&lt; Upstream &gt;, detail::coalescing_free_list &gt;</base>
    <member kind="function">
      <type></type>
      <name>pool_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>afe379e73e90282a0efd2ef1569ce22a5</anchor>
      <arglist>(Upstream *upstream_mr, thrust::optional&lt; std::size_t &gt; initial_pool_size=thrust::nullopt, thrust::optional&lt; std::size_t &gt; maximum_pool_size=thrust::nullopt)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>~pool_memory_resource</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>afcc226c485d432831a431edeffc58753</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a3984b5b250cf0380ba36b03fe62d4f6a</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a7bc1a125d8ac7fbcb8df3057865357a0</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a7d8ad0f62b020049239f1642a1099039</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::size_t</type>
      <name>get_maximum_allocation_size</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a6d0c0b77cfb7db5e1ef9e4bee8b29102</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>block_type</type>
      <name>try_to_expand</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a9cf3b3ae8e75322c61ef8514b3f400be</anchor>
      <arglist>(std::size_t try_size, std::size_t min_size, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>initialize_pool</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a04d480a01723347527c62772c2c7e8b9</anchor>
      <arglist>(thrust::optional&lt; std::size_t &gt; initial_size, thrust::optional&lt; std::size_t &gt; maximum_size)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>block_type</type>
      <name>expand_pool</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a6fc2f58dc325d8d5851ba0b40c952f5e</anchor>
      <arglist>(std::size_t size, free_list &amp;blocks, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::size_t</type>
      <name>size_to_grow</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a2fab047603acc9b8152b691881476da8</anchor>
      <arglist>(std::size_t size) const</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>thrust::optional&lt; block_type &gt;</type>
      <name>block_from_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a4c687e04a1cc07fe5f9cfee3105f5335</anchor>
      <arglist>(std::size_t size, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>split_block</type>
      <name>allocate_from_block</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>adf121431db4c29ba60afec6799c6369c</anchor>
      <arglist>(block_type const &amp;b, std::size_t size)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>block_type</type>
      <name>free_block</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a6b1c4771645a9ba477d145ece03d5919</anchor>
      <arglist>(void *p, std::size_t size) noexcept</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::size_t</type>
      <name>pool_size</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>ac7159078675d349b7fe7a8b3429339c6</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>release</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a9b2f74a2c248a1b9224c169b8b9e3fa2</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>print</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a35fd06297ddb9833893cbda4a2f52ff5</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::pair&lt; std::size_t, std::size_t &gt;</type>
      <name>free_list_summary</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a5b75713a57836096f79d00c1544d314e</anchor>
      <arglist>(free_list const &amp;blocks)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::pair&lt; std::size_t, std::size_t &gt;</type>
      <name>do_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1pool__memory__resource.html</anchorfile>
      <anchor>a5cac2b0ee64cf7458934f6d7393c40a3</anchor>
      <arglist>(cuda_stream_view stream) const override</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::stream_allocator_adaptor::rebind</name>
    <filename>structrmm_1_1mr_1_1stream__allocator__adaptor_1_1rebind.html</filename>
    <templarg></templarg>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::thrust_allocator::rebind</name>
    <filename>structrmm_1_1mr_1_1thrust__allocator_1_1rebind.html</filename>
    <templarg></templarg>
  </compound>
  <compound kind="class">
    <name>rmm::detail::stack_trace</name>
    <filename>classrmm_1_1detail_1_1stack__trace.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::statistics_resource_adaptor</name>
    <filename>classrmm_1_1mr_1_1statistics__resource__adaptor.html</filename>
    <templarg></templarg>
    <base>rmm::mr::device_memory_resource</base>
    <class kind="struct">rmm::mr::statistics_resource_adaptor::counter</class>
    <member kind="function">
      <type></type>
      <name>statistics_resource_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1statistics__resource__adaptor.html</anchorfile>
      <anchor>a88a2ca8cadf12ef993fcf8c4f06342c5</anchor>
      <arglist>(Upstream *upstream)</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1statistics__resource__adaptor.html</anchorfile>
      <anchor>af8171ad982915f245712ed534aae3746</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1statistics__resource__adaptor.html</anchorfile>
      <anchor>a31f60fa392e7c7fdf513153bbd678a52</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1statistics__resource__adaptor.html</anchorfile>
      <anchor>a417b71f7b0227c8ef20e6dd927011910</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>counter</type>
      <name>get_bytes_counter</name>
      <anchorfile>classrmm_1_1mr_1_1statistics__resource__adaptor.html</anchorfile>
      <anchor>aedc33e395d5d57722cfa73aaf4b180ea</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>counter</type>
      <name>get_allocations_counter</name>
      <anchorfile>classrmm_1_1mr_1_1statistics__resource__adaptor.html</anchorfile>
      <anchor>ac1975964bdde941d509e59b1a18223db</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::stream_allocator_adaptor</name>
    <filename>classrmm_1_1mr_1_1stream__allocator__adaptor.html</filename>
    <templarg></templarg>
    <class kind="struct">rmm::mr::stream_allocator_adaptor::rebind</class>
    <member kind="function">
      <type></type>
      <name>stream_allocator_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1stream__allocator__adaptor.html</anchorfile>
      <anchor>ad778ea42f846c929de5cc75529b95884</anchor>
      <arglist>(Allocator const &amp;a, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>stream_allocator_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1stream__allocator__adaptor.html</anchorfile>
      <anchor>a7d63aa675abca0fe5556e263ffe33666</anchor>
      <arglist>(stream_allocator_adaptor&lt; Allocator &gt; const &amp;other)=default</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>stream_allocator_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1stream__allocator__adaptor.html</anchorfile>
      <anchor>abb31ffde4198967b649b321657db4f5b</anchor>
      <arglist>(stream_allocator_adaptor&lt; OtherAllocator &gt; const &amp;other)</arglist>
    </member>
    <member kind="function">
      <type>value_type *</type>
      <name>allocate</name>
      <anchorfile>classrmm_1_1mr_1_1stream__allocator__adaptor.html</anchorfile>
      <anchor>a9a57f674e68f383306c129636ec4eb48</anchor>
      <arglist>(std::size_t n)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1stream__allocator__adaptor.html</anchorfile>
      <anchor>ab370892a0be86f6af0fd6b4142c10bb2</anchor>
      <arglist>(value_type *p, std::size_t n)</arglist>
    </member>
    <member kind="function">
      <type>cuda_stream_view</type>
      <name>stream</name>
      <anchorfile>classrmm_1_1mr_1_1stream__allocator__adaptor.html</anchorfile>
      <anchor>ae7a231016c0280b7c0a18258ee7895a7</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>Allocator</type>
      <name>underlying_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1stream__allocator__adaptor.html</anchorfile>
      <anchor>a6fcfed17210df922e935a51615ec47b8</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>rmm::mr::detail::stream_ordered_memory_resource::stream_event_pair</name>
    <filename>structrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource_1_1stream__event__pair.html</filename>
  </compound>
  <compound kind="class">
    <name>rmm::mr::detail::stream_ordered_memory_resource</name>
    <filename>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</filename>
    <templarg></templarg>
    <templarg></templarg>
    <base>crtp&lt; PoolResource &gt;</base>
    <base>rmm::mr::device_memory_resource</base>
    <class kind="struct">rmm::mr::detail::stream_ordered_memory_resource::stream_event_pair</class>
    <member kind="typedef" protection="protected">
      <type>std::pair&lt; block_type, block_type &gt;</type>
      <name>split_block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a80561e617cbaf5a13aafe4e76593367f</anchor>
      <arglist></arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>insert_block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a02c26669d357d8cee1a1776389945054</anchor>
      <arglist>(block_type const &amp;b, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::mutex &amp;</type>
      <name>get_mutex</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a115882e92e73a7e76cf51537dbceab9b</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected" virtualness="virtual">
      <type>virtual void *</type>
      <name>do_allocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a098b2f8a485e8f5ec1768f1969e65917</anchor>
      <arglist>(std::size_t bytes, cuda_stream_view stream) override</arglist>
    </member>
    <member kind="function" protection="protected" virtualness="virtual">
      <type>virtual void</type>
      <name>do_deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>af262b6323118ca0ec996b29a80f22d9c</anchor>
      <arglist>(void *p, std::size_t bytes, cuda_stream_view stream) override</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>stream_ordered_memory_resource&lt; fixed_size_memory_resource&lt; Upstream &gt;, detail::fixed_size_free_list &gt;</name>
    <filename>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</filename>
    <base>crtp&lt; fixed_size_memory_resource&lt; Upstream &gt; &gt;</base>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="typedef" protection="protected">
      <type>std::pair&lt; block_type, block_type &gt;</type>
      <name>split_block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a80561e617cbaf5a13aafe4e76593367f</anchor>
      <arglist></arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>insert_block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a02c26669d357d8cee1a1776389945054</anchor>
      <arglist>(block_type const &amp;b, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::mutex &amp;</type>
      <name>get_mutex</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a115882e92e73a7e76cf51537dbceab9b</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected" virtualness="virtual">
      <type>virtual void *</type>
      <name>do_allocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a098b2f8a485e8f5ec1768f1969e65917</anchor>
      <arglist>(std::size_t bytes, cuda_stream_view stream) override</arglist>
    </member>
    <member kind="function" protection="protected" virtualness="virtual">
      <type>virtual void</type>
      <name>do_deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>af262b6323118ca0ec996b29a80f22d9c</anchor>
      <arglist>(void *p, std::size_t bytes, cuda_stream_view stream) override</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>stream_ordered_memory_resource&lt; pool_memory_resource&lt; Upstream &gt;, detail::coalescing_free_list &gt;</name>
    <filename>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</filename>
    <base>crtp&lt; pool_memory_resource&lt; Upstream &gt; &gt;</base>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="typedef" protection="protected">
      <type>std::pair&lt; block_type, block_type &gt;</type>
      <name>split_block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a80561e617cbaf5a13aafe4e76593367f</anchor>
      <arglist></arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>insert_block</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a02c26669d357d8cee1a1776389945054</anchor>
      <arglist>(block_type const &amp;b, cuda_stream_view stream)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>std::mutex &amp;</type>
      <name>get_mutex</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a115882e92e73a7e76cf51537dbceab9b</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected" virtualness="virtual">
      <type>virtual void *</type>
      <name>do_allocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>a098b2f8a485e8f5ec1768f1969e65917</anchor>
      <arglist>(std::size_t bytes, cuda_stream_view stream) override</arglist>
    </member>
    <member kind="function" protection="protected" virtualness="virtual">
      <type>virtual void</type>
      <name>do_deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1detail_1_1stream__ordered__memory__resource.html</anchorfile>
      <anchor>af262b6323118ca0ec996b29a80f22d9c</anchor>
      <arglist>(void *p, std::size_t bytes, cuda_stream_view stream) override</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::thread_safe_resource_adaptor</name>
    <filename>classrmm_1_1mr_1_1thread__safe__resource__adaptor.html</filename>
    <templarg></templarg>
    <base>rmm::mr::device_memory_resource</base>
    <member kind="function">
      <type></type>
      <name>thread_safe_resource_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1thread__safe__resource__adaptor.html</anchorfile>
      <anchor>af8f6d1c09a0300879e90f3b76b26f3da</anchor>
      <arglist>(Upstream *upstream)</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1thread__safe__resource__adaptor.html</anchorfile>
      <anchor>a4507cfd77cf2b60c9b91cadcdee39376</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1thread__safe__resource__adaptor.html</anchorfile>
      <anchor>a1b5fb9d43b53b01c3538f40e7d3b536c</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1thread__safe__resource__adaptor.html</anchorfile>
      <anchor>a9c2a3deb1d4b560d4bef91c96a006788</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::thrust_allocator</name>
    <filename>classrmm_1_1mr_1_1thrust__allocator.html</filename>
    <templarg></templarg>
    <class kind="struct">rmm::mr::thrust_allocator::rebind</class>
    <member kind="function">
      <type></type>
      <name>thrust_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1thrust__allocator.html</anchorfile>
      <anchor>aac2c72560df6ba48d2268a1d1c803141</anchor>
      <arglist>()=default</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>thrust_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1thrust__allocator.html</anchorfile>
      <anchor>acf8ab1c7aac21a788e58d2368a860d1c</anchor>
      <arglist>(cuda_stream_view stream)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>thrust_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1thrust__allocator.html</anchorfile>
      <anchor>aa7be443679542701c128b0d302180e64</anchor>
      <arglist>(cuda_stream_view stream, device_memory_resource *mr)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>thrust_allocator</name>
      <anchorfile>classrmm_1_1mr_1_1thrust__allocator.html</anchorfile>
      <anchor>a4a534791b81bda2d8f9ef268115cd045</anchor>
      <arglist>(thrust_allocator&lt; U &gt; const &amp;other)</arglist>
    </member>
    <member kind="function">
      <type>pointer</type>
      <name>allocate</name>
      <anchorfile>classrmm_1_1mr_1_1thrust__allocator.html</anchorfile>
      <anchor>aa4820af9c1e3fbbf26c6a14338cb8feb</anchor>
      <arglist>(size_type n)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>deallocate</name>
      <anchorfile>classrmm_1_1mr_1_1thrust__allocator.html</anchorfile>
      <anchor>ae5510aa288a2e1875b66c330feecf2ad</anchor>
      <arglist>(pointer p, size_type n)</arglist>
    </member>
    <member kind="function">
      <type>device_memory_resource *</type>
      <name>resource</name>
      <anchorfile>classrmm_1_1mr_1_1thrust__allocator.html</anchorfile>
      <anchor>aa36bf648f33309f8fadda7e449224970</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>cuda_stream_view</type>
      <name>stream</name>
      <anchorfile>classrmm_1_1mr_1_1thrust__allocator.html</anchorfile>
      <anchor>a7ce75803be86e42062fb6fef8fdbf1b8</anchor>
      <arglist>() const noexcept</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>rmm::mr::tracking_resource_adaptor</name>
    <filename>classrmm_1_1mr_1_1tracking__resource__adaptor.html</filename>
    <templarg></templarg>
    <base>rmm::mr::device_memory_resource</base>
    <class kind="struct">rmm::mr::tracking_resource_adaptor::allocation_info</class>
    <member kind="function">
      <type></type>
      <name>tracking_resource_adaptor</name>
      <anchorfile>classrmm_1_1mr_1_1tracking__resource__adaptor.html</anchorfile>
      <anchor>a1468a4721e3aef90c8a7e8ae7c1ddb63</anchor>
      <arglist>(Upstream *upstream, bool capture_stacks=false)</arglist>
    </member>
    <member kind="function">
      <type>Upstream *</type>
      <name>get_upstream</name>
      <anchorfile>classrmm_1_1mr_1_1tracking__resource__adaptor.html</anchorfile>
      <anchor>ab8db48a4ec09d8320e6249c96f23970a</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_streams</name>
      <anchorfile>classrmm_1_1mr_1_1tracking__resource__adaptor.html</anchorfile>
      <anchor>a40c082c925f47ef950d840e018db2737</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>bool</type>
      <name>supports_get_mem_info</name>
      <anchorfile>classrmm_1_1mr_1_1tracking__resource__adaptor.html</anchorfile>
      <anchor>a320c93def56d9dbd8ac04574086fa349</anchor>
      <arglist>() const noexcept override</arglist>
    </member>
    <member kind="function">
      <type>std::map&lt; void *, allocation_info &gt; const  &amp;</type>
      <name>get_outstanding_allocations</name>
      <anchorfile>classrmm_1_1mr_1_1tracking__resource__adaptor.html</anchorfile>
      <anchor>acf0c2d6a5269b0e3b8f38cec015f0662</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>std::size_t</type>
      <name>get_allocated_bytes</name>
      <anchorfile>classrmm_1_1mr_1_1tracking__resource__adaptor.html</anchorfile>
      <anchor>a4e0080b11d7b81019246f2e36f1b3e69</anchor>
      <arglist>() const noexcept</arglist>
    </member>
    <member kind="function">
      <type>std::string</type>
      <name>get_outstanding_allocations_str</name>
      <anchorfile>classrmm_1_1mr_1_1tracking__resource__adaptor.html</anchorfile>
      <anchor>aaa72c3a87b4374b91e8f5ac13fc1752d</anchor>
      <arglist>() const</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>log_outstanding_allocations</name>
      <anchorfile>classrmm_1_1mr_1_1tracking__resource__adaptor.html</anchorfile>
      <anchor>adae81547e8ea0e045b786d24b3162656</anchor>
      <arglist>() const</arglist>
    </member>
  </compound>
</tagfile>
