``

// https://vitejs.dev/guide/env-and-mode.html#env-files
// https://vitejs.dev/guide/api-javascript.html#loadenv
import { defineConfig, loadEnv } from "vite";

import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
// export default defineConfig({
export default defineConfig(({ command, mode }) => {
  // Load env file based on `mode` in the current working directory.
  // Set the third parameter to '' to load all env regardless of the `VITE_` prefix.
  // https://main.vitejs.dev/config/#using-environment-variables-in-config
  const env = loadEnv(mode, process.cwd(), '');
  return {
    base: "/",
    root: "./",
    resolve: {
      alias: {
        "@": "src",
      },
    },
    server: {
      host: "127.0.0.1",
      port: 3000,
      open: false,
      watch: {
        usePolling: false,
        disableGlobbing: false,
      },
    },
    plugins: [
      vue(),
    ],
    // https://github.com/MrBin99/django-vite#vitejs
    // https://vitejs.dev/guide/backend-integration.html
    build: {
      outDir: "dist/",
      emptyOutDir: true,

      // https://stackoverflow.com/questions/74177078/styles-is-missing-after-i-bundle-my-project-with-vite
      // https://vitejs.dev/config/build-options.html#build-csscodesplit
      // https://github.com/vitejs/vite/issues/10630
      cssCodeSplit: true,

      manifest: true,

      // TODO: See #21. This is needed to make the build work with Django.
      // // As this is in SSR and not in SPA, you don't have an index.html that
      // // ViteJS can use to determine which files to compile. You need to
      // // tell it directly.
      // rollupOptions: {
      //   input: "src/main.ts",
      //   // See: https://ilikerobots.medium.com/django-vue-vite-rest-not-required-ca63cfa558fd
      //   // output: {
      //   //   dir: '../<your_django_app_dir>/static/vue/',
      //   //   entryFileNames: '[name].js',
      //   // }
      // },
    },
  };
});
