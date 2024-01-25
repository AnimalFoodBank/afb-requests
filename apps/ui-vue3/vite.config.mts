
/**
 * @file ViteJS configuration file.
 *
 * re: the `vite.config.mts` file extension:
 * It resolves "This package is ESM only" error when running npx vite.
*
* @see
 *  https://vitejs.dev/guide/troubleshooting.html#this-package-is-esm-only
 *  https://devblogs.microsoft.com/typescript/announcing-typescript-4-5-beta/#new-file-extensions
 */

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueform from '@vueform/vueform/vite'
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: '127.0.0.1',
    port: 3000,
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src/"),
    },
  },
  plugins: [
    vue(),
    vueform(),
  ],
})
