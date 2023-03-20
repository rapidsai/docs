---
layout: default
title: Visualization Guide
nav_order: 5
permalink: visualization
---

# RAPIDS Visualization Guide

RAPIDS libraries can easily fit in visualization workflows. This catalog of featured libraries offer direct cuDF support or easy integration.
{: .fs-6 .fw-300 }

<img src="/assets/images/datashader-census-rapids.png" style="width:870px">

*[330 million+ datapoints rendered in under 1.5s via RAPIDS + Plotly Dash 2020 Census Demo](https://github.com/rapidsai/plotly-dash-rapids-census-demo)*

### Featured Libraries
- **[HoloViews](#holoviews):** Declarative objects for quickly building complex interactive plots from high-level specifications. Directly uses cuDF.
- **[hvPlot](#hvplot):** Quickly return interactive plots from cuDF, Pandas, Xarray, or other data structures. Just replace `.plot()` with `.hvplot()`.
- **[Datashader](#datashader):** Rasterizing huge datasets quickly as scatter, line, geospatial, or graph charts. Directly uses cuDF.
- **[Plotly](#plotly):** Charting library that supports Plotly Dash for building complex analytics applications.
- **[Bokeh](#bokeh):** Charting library for building complex interactive visualizations.
- **[Seaborn](#seaborn):** Static single charting library that extends matplotlib.

### Other Notable Libraries
- **[Panel](#panel):** A high-level app and dashboarding solution for the Python ecosystem.
- **[PyDeck](#pydeck):** Python bindings for interactive spatial visualizations with webGL powered deck.gl, optimized for a Jupyter environment.
- **[cuxfilter](#cuxfilter):** RAPIDS developed cross filtering dashboarding tool that integrates many of the libraries above.
- **[node RAPIDS](#noderapids):** RAPIDS bindings in nodeJS, a high performance JS/TypeScript visualization alternative to using Python.


### GPU Accelerated Interaction

The below libraries directly use RAPIDS cuDF/Dask-cuDF and/or cuSpatial to create charts that support accelerated crossfiltering or rendering:
- **[Holoviews with Linked Brushing User Guide](https://holoviews.org/user_guide/Linked_Brushing.html?highlight=linked%20brushing)**
- **[Datashader User Guide](https://datashader.org/user_guide/Performance.html)**
- **[Plotly Dash with Holoviews Docs](https://dash.plotly.com/holoviews#gpu-accelerating-datashader-and-linked-selections-with-rapids)**
- **[cuxfilter GitHub](https://github.com/rapidsai/cuxfilter)**


### **Note:** Web Hosted vs Local Hosted Chart Interaction 
When interacting with this page through a website, the interactive examples below are all **static and use pre-computed data.** To run a true interactive version, host through the **active** instance found on our [cuxfilter GitHub Notebooks](https://github.com/rapidsai/cuxfilter/tree/branch-{{ site.data.releases.stable.version }}/notebooks/RAPIDS%20Visualization%20Guide).

{% include viz-cdn-js-css.html %}

<br/><br/>
# Featured Libraries

<a id='holoviews'></a><br/>
<img src="/assets/images/holoviews-logo.png" style="width:150px; display:inline-block; vertical-align:middle;">
<a href="https://holoviews.org/gallery/index.html" target="_blank" title="holoviews NYC taxi example">
<img src="/assets/images/nytaxi_hover.gif" style="width:300px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>
<br/>
- HoloViews is an open-source Python library designed to make data analysis and visualization seamless and simple. [See this diagram](https://holoviz.org/background.html#the-holoviz-ecosystem)  for an excellent architecture overview.
- With HoloViews, you can usually express what you want to do in very few lines of code, letting you focus on what you are trying to explore and convey, not on the process of plotting.
- Read about Holoviews at [holoviews.org](https://holoviews.org) and explore its gallery [holoviews.org/gallery/](https://holoviews.org/gallery/).
- Read about [RAPIDS compatibilty](https://holoviews.org/reference_manual/holoviews.core.data.html?highlight=cudf#module-holoviews.core.data.cudf).

**Run an interactive example and cpu / gpu code comparison below:**
{% include holoviews.html %}

<a id='hvplot'></a><br/>
<img src="/assets/images/hvplot-logo.png" style="width:90px; display:inline-block; vertical-align:middle;">
<a href="https://hvplot.holoviz.org/reference/index.html" target="_blank" title="hvplot heat map example">
<img src="/assets/images/heatmap.png" style="width:120px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>

- hvPlot provides an alternative for the static plotting API provided by Pandas and other libraries, with an interactive plotting API. Just replace `.plot()` with `.hvplot()`.
- hvPlot can integrate neatly with the individual libraries if an extension mechanism for the native plot APIs is offered, or it can be used as a standalone component.   
- Read about hvPlot at [holoviews.org](http://holoviews.org) and explore its gallery [hvplot.holoviz.org/reference/index.html](https://hvplot.holoviz.org/reference/index.html).
- Read about [RAPIDS compatibility](https://hvplot.holoviz.org/user_guide/Introduction.html?highlight=rapids#).
<br/>
**Run an interactive example and cpu / gpu code comparison below:**
{% include hvplot.html %}

<a id='datashader'></a><br/>
<img src="/assets/images/datashader-logo.png" style="width:150px; display:inline-block; vertical-align:middle;">
<a href="https://panel.holoviz.org/gallery/simple/clifford_interact.html" target="_blank" title="datashader clifford demo">
<img src="/assets/images/clifford_interact.png" style="width:130px; display:inline-block; vertical-align:middle; padding-left:20px; "></a>

- Datashader is a graphics pipeline system for creating meaningful representations of large datasets quickly and flexibly.
- Datashader is able to render a variety of chart types statically, and interactively when combined with other libraries like HoloViews or cuxfilter.
- Read about Datashader at [datashader.org](https://datashader.org) and explore its examples.
- Read about [RAPIDS compatibility](https://datashader.org/user_guide/Performance.html?highlight=cudf#data-objects).
<br/>
**Run an interactive example and cpu / gpu code comparison below:**
{% include datashader.html %}

                                                                                                                                                                                                             

<a id='plotly'></a><br/>
<img src="/assets/images/plotly-logo.png" style="width:160px; vertical-align:middle;"> 
<a href="https://dash.gallery/Portal/" target="_blank" title="plotly dash US Opioid Epidemic demo">
<img src="/assets/images/plotly-dash.png" style="width:230px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>
<br/>
- Plotly provides browser based graphing, analytics, and statistics tools to create powerful applications.
- Read about Plotly's Python charting library at [plotly.com/python/](https://plotly.com/python/) and explore the Plotly Dash gallery [ash.gallery/Portal/](https://dash.gallery/Portal/).
- Read about [RAPIDS compatibility](https://dash.plotly.com/holoviews#gpu-accelerating-datashader-and-linked-selections-with-rapids).

**Run an interactive example and cpu / gpu code comparison below:**
{% include plotly.html %}
                                                                                                                                                                                                             

<a id='bokeh'></a><br/>
<img src="/assets/images/bokeh-logo.svg" style="width:130px; display:inline-block; vertical-align:middle;">
<a href="https://docs.bokeh.org/en/latest/docs/gallery.html" target="_blank" title="bokeh blackbody radiation chart">
<img src="/assets/images/latex_blackbody_radiation.png" style="width:130px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>
<br/>
- Bokeh makes it simple to create common interactive plots, but also can handle custom or specialized use-cases with tools and widgets.
- Plots, dashboards, and apps can be published in web pages or Jupyter notebooks.
- Read about Bokeh at [bokeh.org/](https://bokeh.org/) and explore its demo page [demo.bokeh.org/](https://demo.bokeh.org/).
- Further [Documentation](https://docs.bokeh.org/en/latest/).

**Run an interactive example and cpu / gpu code comparison below:**
{% include bokeh.html %}

                                                                                                                                                                                                             

<a id='seaborn'></a><br/>
<img src="/assets/images/seaborn-logo.svg" style="width:200px; display:inline-block; vertical-align:middle;"> 
<a href="https://seaborn.pydata.org/examples/hexbin_marginals.html" target="_blank" title="seaborn hexbin example">
<img src="/assets/images/hexbin_marginals.png" style="width:130px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>
<br/>
- Seaborn is a Python data visualization library based on [matplotlib](https://matplotlib.org/). It provides a high-level interface for drawing static charts.
- Although not directly accelerated with GPU usage, it provides a base example of using a popular Python based visualization library with RAPIDS. 
- Read about Seaborn at [seaborn.pydata.org/](https://seaborn.pydata.org/) and explore its gallery [seaborn.pydata.org/examples/index.html](https://seaborn.pydata.org/examples/index.html).
- Further [Documentation](https://seaborn.pydata.org/api.html).

**Run an interactive example and cpu / gpu code comparison below:**
{% include seaborn.html %}

<br/><br/>

# Other Notable Libraries

<a id='panel'></a><br/>
<img src="/assets/images/panel-logo.png" style="width:100px; display:inline-block; vertical-align:middle;"> 
<a href="https://panel.holoviz.org/gallery/index.html" target="_blank" title="panel gapminder example">
<img src="/assets/images/gapminders.png" style="width:210px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>
<br/>
- Panel is a Python library that lets you create custom interactive web apps and dashboards by connecting user-defined widgets to plots, images, tables, or text.
- Panel -like holoViews, hvPlot, and datashader- is part of the [HoloViz Ecosystem](https://holoviz.org/).
- Panel works well within the Python visualization ecosystem and is **what powers the interactive tools on this page**.
- Read more about Panel at [panel.holoviz.org/](https://panel.holoviz.org/index.html) and explore its gallery [panel.holoviz.org/reference/](https://panel.holoviz.org/reference/index.html).
- Further [Documentation](https://panel.holoviz.org/user_guide/index.html).


<a id='pydeck'></a><br/>
<img src="/assets/images/pyDeck-logo.svg" style="width:200px; display:inline-block; vertical-align:middle;">
<a href="https://deckgl.readthedocs.io/en/latest/layer.html" target="_blank" title="pydeck example page">
<img src="/assets/images/hexagon-layer.jpg" style="width:140px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>
<br/>
- The pyDeck library is a set of Python bindings for making spatial visualizations with deck.gl, optimized for a Jupyter environment.
- Learn more about its core deck.gl webGL based library a [deck.gl](https://deck.gl/).
- Read about pyDeck at [pydeck.gl/](https://pydeck.gl/) and explore its gallery [pydeck gallery](https://pydeck.gl/#gallery).
- Further [Documentation](https://pydeck.gl/layer.html).


<a id='cuxfilter'></a><br/>
<img src="/assets/images/rapids_logo.png" style="width:150px; display:inline-block; vertical-align:middle;">
<span style="color:#7400ff; font-size:2.5em; vertical-align: middle;">cuxfilter</span>
<a href="https://docs.rapids.ai/api/cuxfilter/nightly/examples/examples.html" target="_blank" title="cuxfilter example page">
<img src="/assets/images/cuxfilter-demo.gif" style="width:220px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>
<br/>
- cuxfilter is a RAPIDS developed cross filtering library which enables GPU accelerated dashboards, using best in class charting libraries, with just a few lines of Python.
- Read about cuxfilter at [github.com/rapidsai/cuxfilter](https://github.com/rapidsai/cuxfilter) and explore its examples [docs.rapids.ai/api/cuxfilter/stable/examples/examples.html](https://docs.rapids.ai/api/cuxfilter/stable/examples/examples.html).
- Further [Documentation](https://docs.rapids.ai/api/cuxfilter/stable/10_minutes_to_cuxfilter.html).


<a id='noderapids'></a><br/>
<img src="/assets/images/rapids_logo.png" style="width:150px; display:inline-block; vertical-align:middle;">
<span style="color:#7400ff; font-size:2.5em; vertical-align: middle;">nodeRAPIDS</span>
<a href="https://github.com/rapidsai/node/tree/main/modules/demo" target="_blank" title="nodeRAPIDS demo page">
<img src="/assets/images/nodeRAPIDS-streaming.png" style="width:200px; display:inline-block; vertical-align:middle; padding-left:20px;"></a>
<br/>
- node RAPIDS brings GPU acceleration to the nodeJS and JS/TypeScript user ecosystem.
- Keep large datasets and complex compute processes in GPU memory while using the browser front end just for performant interactions.
- node RAPIDS is [available on NPM](https://www.npmjs.com/package/@rapidsai/core?activeTab=dependents).
- Read about node RAPIDS at [github.com/rapidsai/node ](https://github.com/rapidsai/node) and explore its demo gallery [github.com/rapidsai/node/tree/main/modules/demo](https://github.com/rapidsai/node/tree/main/modules/demo).
- Further [Documentation](https://rapidsai.github.io/node/).



<br/><br/><br/>
