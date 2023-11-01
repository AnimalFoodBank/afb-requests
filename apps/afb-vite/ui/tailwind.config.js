/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,html,js,ts,jsx,tsx}",
    "./src/views/*.{vue,html,js,ts,jsx,tsx}",
    "./src/components/*.{vue,html,js,ts,jsx,tsx}",
    "../afbcore/templates/**/*.html",
    "../afbcore/templates/*.html"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio')
  ],
}
