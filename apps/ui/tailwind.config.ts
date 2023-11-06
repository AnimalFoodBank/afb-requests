/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,html,js,ts,jsx,tsx}",
    "./src/views/*.{vue,html,js,ts,jsx,tsx}",
    "./src/components/*.{vue,html,js,ts,jsx,tsx}",
    "../afbcore/templates/**/*.html",
    "../afbcore/templates/*.html",
    './vueform.config.ts', // or where `vueform.config.js` is located
    './node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
    './node_modules/@vueform/vueform/themes/tailwind/**/*.{ts,js,tsx,jsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@vueform/vueform/tailwind')
  ],
}
