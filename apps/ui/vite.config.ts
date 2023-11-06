import vue from "@vitejs/plugin-vue";
import vueform from '@vueform/vueform/vite'
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/",
  // root: "src/",
  resolve: {
    alias: {
      "@": "src",
    },
  },
  server: {
    host: "localhost",
    port: 3000,
    open: false,
    watch: {
      usePolling: false,
      disableGlobbing: false,
    },
  },
  plugins: [
    vue(),
    vueform() // https://vueform.com/docs/installation
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
});
