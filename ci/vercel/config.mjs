import { makeRoutes } from "./routes.mjs";

const makeConfig = () => ({
  version: 3,
  routes: makeRoutes(),
});

console.log(JSON.stringify(makeConfig(), null, 2));
