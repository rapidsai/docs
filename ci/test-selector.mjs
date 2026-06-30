#!/usr/bin/env node
// SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
// SPDX-License-Identifier: Apache-2.0

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import vm from "node:vm";


const renderedPath = process.argv[2] || "_site/install/index.html";
const html = readFileSync(renderedPath, "utf8");
const scripts = [...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(
  (match) => match[1],
);
const selectorScript = scripts.find((script) =>
  script.includes("Alpine.data('rapids_selector'"),
);
assert(selectorScript, `Could not find rendered selector script in ${renderedPath}`);

let selectorFactory;
const context = {
  Alpine: {
    data(name, factory) {
      assert.equal(name, "rapids_selector");
      selectorFactory = factory;
    },
  },
  document: {
    addEventListener(event, callback) {
      assert.equal(event, "alpine:init");
      callback();
    },
  },
};
vm.runInNewContext(selectorScript, context);
assert(selectorFactory, "Selector did not register with Alpine");

const selector = selectorFactory();
selector.init();
const plainText = (value) => value.replace(/<\/?span[^>]*>/g, "");
assert.equal(selector.getReleaseText("Stable"), "Stable (26.06)");
assert.equal(selector.getReleaseText("Nightly"), "Nightly (26.08a)");
assert.equal(selector.getCondaVersionSupport("13").pinning, ">=13.0,<=13.2");
assert(selector.getSelectablePackageLabels("conda").includes("cuxfilter"));

selector.active_packages = ["Choose Specific Packages", "cuxfilter"];
const stableCondaCommand = plainText(selector.getCondaCmdHtml());
assert(stableCondaCommand.includes("cuxfilter=26.06"));
selector.active_release = "Nightly";
selector.reconcileActivePackages();
assert.equal(selector.getCondaVersionSupport("13").pinning, ">=13.0,<=13.3");
assert(!selector.getSelectablePackageLabels("conda").includes("cuxfilter"));
assert(!selector.active_packages.includes("cuxfilter"));
assert(!selector.getStandardBundleDisplayNames("docker").includes("cuxfilter"));

selector.active_method = "pip";
selector.active_packages = ["Standard"];
const nightlyPipCommand = plainText(selector.getpipCmdHtml());
assert(!nightlyPipCommand.includes("cuxfilter"));
assert(nightlyPipCommand.includes("dask-cuda"));

selector.active_release = "Stable";
selector.active_packages = ["Choose Specific Packages", "cuDF"];
const pypiCommand = plainText(selector.getpipCmdHtml());
assert(!pypiCommand.includes("extra-index-url"));
selector.active_packages = ["Choose Specific Packages", "cuGraph/nx-cugraph"];
const graphCommand = plainText(selector.getpipCmdHtml());
assert(graphCommand.includes("cugraph-cu13==26.6.*"));
assert(graphCommand.includes("nx-cugraph-cu13==26.6.*"));
assert(graphCommand.includes("extra-index-url"));

selector.active_packages = ["Choose Specific Packages", "RAFT"];
const raftCommand = plainText(selector.getpipCmdHtml());
assert(raftCommand.includes("pylibraft-cu13==26.6.*"));
assert(raftCommand.includes("raft-dask-cu13==26.6.*"));

selector.active_release = "Nightly";
selector.active_packages = ["Choose Specific Packages", "cuVS"];
const cuvsCommand = plainText(selector.getpipCmdHtml());
assert(cuvsCommand.includes("cuvs-cu13>=26.8.0a0,<=26.8"));
assert(cuvsCommand.includes("pylibraft-cu13>=26.8.0a0,<=26.8"));

for (const release of selector.releases) {
  selector.active_release = release;
  selector.active_packages = ["Standard"];
  for (const method of selector.methods) {
    selector.active_method = method;
    const command = plainText(selector.getCmdHtml());
    assert(!command.includes("undefined"), `${release} ${method} command is defined`);
    assert(!command.includes("null"), `${release} ${method} command has no null values`);
    const expectedVersion = method === "pip"
      ? selector.removeLeadingZeros(selector.getReleaseVersion())
      : selector.getReleaseVersion();
    assert(command.includes(expectedVersion), `${release} ${method} command has its release`);
  }
}

assert(html.includes("CUDA 12 with Driver 535 or newer"));
assert(!html.includes("Driver 525.60.13"));
console.log("Rendered selector assertions passed.");
