module.exports = {
  // plugins: {
    //  'postcss-import': {},
    // tailwindcss: {},
    // autoprefixer: {},
  // },
  plugins: [
    require('postcss-import'),
    require('tailwindcss'),
    require('autoprefixer'),
  ]
}
