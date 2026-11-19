const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const html = fs.readFileSync('_includes/selector.html', 'utf8');
const script = html.match(/<script type="text\/javascript">([\s\S]*?)<\/script>/)[1];
let selector;
vm.runInNewContext(script, {
    document: {addEventListener: (_, callback) => callback()},
    Alpine: {data: (_, factory) => { selector = factory(); }},
});

for (const release of ['Stable', 'Nightly']) {
    for (const version of ['26.10', '26.12', '27.02', '27.2', '28.02']) {
        selector.active_release = release;
        selector.getStableVersion = () => version;
        selector.getNightlyVersion = () => version;
        const included = version.startsWith('26.');
        assert.equal(selector.hasNxCugraph(), included);
        assert.equal(selector.additional_packages.includes('NetworkX + nx-cugraph'), included);
        assert.equal(selector.rapids_meta_pkgs.includes('nx-cugraph'), included);
        for (const cuda of ['12', '13']) {
            selector.active_pip_cuda_ver = cuda;
            selector.active_packages = ['Standard'];
            const command = selector.getpipCmdHtml();
            assert.equal(command.includes('nx-cugraph'), included);
            assert.equal((command.match(/nx-cugraph/g) || []).length, included ? 1 : 0);
            selector.active_packages = ['cuGraph/nx-cugraph'];
            assert.equal(selector.getpipCmdHtml().includes('nx-cugraph'), included);
        }
        assert.equal(selector.getAdditionalPkgName('NetworkX + nx-cugraph').includes('nx-cugraph'), included);
        selector.active_packages = ['Standard'];
        assert.equal(selector.getCondaNotes().join('').includes('nx-cugraph'), included);
        assert.equal(selector.getDockerNotes().join('').includes('nx-cugraph'), included);
    }
}
console.log('Install selector: stable/nightly, CUDA 12/13, legacy/current versions passed');
