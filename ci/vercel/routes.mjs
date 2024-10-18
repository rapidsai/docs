import { getTransformedRoutes } from "@vercel/routing-utils";
import { convertTrailingSlash } from "@vercel/routing-utils/dist/superstatic.js";
import { readFileSync } from "node:fs";
import path from "node:path";

const DEFAULT_REDIRECT_CODE = 301;

const makeRedirectsFromFile = () => {
  const redirectsFile = path.join(
    import.meta.dirname,
    "..",
    "..",
    "_redirects"
  );
  const redirectsFileContents = readFileSync(redirectsFile, "utf8");
  const redirects = redirectsFileContents
    .split("\n")
    .filter(Boolean)
    .map((line) => {
      const [source, destination] = line.split(/\s+/).filter(Boolean);
      return {
        source,
        destination,
        statusCode: DEFAULT_REDIRECT_CODE,
      };
    });
  return redirects;
};

const makeRedirects = () => {
  const redirects = [];
  redirects.push(...makeRedirectsFromFile());
  return redirects;
};

export const makeRoutes = () => {
  const { routes, error } = getTransformedRoutes({
    redirects: makeRedirects(),
  });

  if (error) throw error;
  return [
    ...convertTrailingSlash(true, 301),
    ...routes,
    {
      handle: "error",
    },
    {
      status: 404,
      src: "^.*$",
      dest: "/404.html",
    },
  ];
};
