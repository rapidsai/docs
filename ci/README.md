# ci

## API docs

The site's `/api` page links to API documentation for many RAPIDS projects.

Those API docs are built in CI of the individual projects, published to object storage,
then pulled into builds here and integrated into the rest of the docs site.

The steps are roughly as follows.

### Step 1: determine libraries and versions to build

`get-projects-to-versions.sh` is responsible for holding all the logic relevant to the question "projects' API docs should be hosted? what versions?".

Run it from the root of the repo to see for yourself.

```shell
./ci/get-projects-to-versions.sh
```

That script is reused by other automation to determine which projects and versions to build.

### Step 2: download API docs

All of the API docs for RAPIDS projects are uploaded to an S3 bucket from those projects' CI.

To integrate them into the docs site, they need to be downloaded and placed in `_site/api/` locally.

```shell
./ci/download_from_s3.sh
```

### Step 3: post-processing

After downloading the API docs, they'll all be arranged locally in directories named with version numbers, like this:

```text
_site/api/
├── cudf
│   ├── 25.06
│   ├── 25.08
│   ├── 25.10
├── cudf-java
│   ├── 25.06
│   ├── 25.08
├── cuml
│   ├── 25.06
│   ├── 25.08
│   ├── 25.10
```

Further processing is then needed to integrate them into the docs site, including:

* mapping version numbers like `25.10` to version identifies like `"stable"` (to populate links like https://docs.rapids.ai/api/cudf/stable/)
* adding version selectors on all the docs pages
* other formatting and visual consistency changes

That is handled by the code in the `ci/customization` directory.
You can invoke it all like this:

```shell
./ci/post-process.sh
```

See the docs in `ci/customization` for more details ([customization/README.md](./customization/README.md)).
