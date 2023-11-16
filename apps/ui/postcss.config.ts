/**
 * PostCSS configuration file
 *
 * re: vite issue #11894 - TypeScript and ESM support
 *
 * Workaround is applied in tsconfig.json. The issue is
 * that PostCSS does not support ESM syntax, and the
 * workaround is to use CommonJS syntax in the config
 * file, which is transpiled to ESM syntax by TypeScript.
 * This is not ideal, but it works.
 *
 * More info:
 * TypeScript is a statically typed superset of JavaScript,
 * adding type safety to the language. ECMAScript Modules
 * (ESM) is a module system in JavaScript, introducing
 * import and export syntax for modular code. TypeScript
 * supports ESM syntax and can transpile it to other
 * module systems for compatibility.
 *
 * @see
 * https://github.com/vitejs/vite/issues/11894
 * https://tailwindcss.com/blog/tailwindcss-v3-3#esm-and-typescript-support
 * https://github.com/postcss/postcss-load-config/issues/239 - workaround
 * https://github.com/postcss/postcss-load-config/issues/246
 */
import postcssImport from 'postcss-import';
import tailwindcss from 'tailwindcss';
import autoprefixer from 'autoprefixer';

export default {
  plugins: [
    postcssImport,
    tailwindcss,
    autoprefixer,
  ]
}
