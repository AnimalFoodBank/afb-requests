import type { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'

export default <Partial<Config>>{
  content: [
    './vueform.config.ts', // or where `vueform.config.js` is located. Change `.js` to `.ts` if required.
    './node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
    './node_modules/@vueform/vueform/themes/tailwind/**/*.ts',
    './node_modules/@vueform/builder/**/*.ts',
    './node_modules/@vueform/builder/**/*.css',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['DM Sans', ...defaultTheme.fontFamily.sans]
      }
    },
    darkMode: 'class',
  },
  plugins: [
    require('@vueform/vueform/tailwind'),
    require('@vueform/builder/tailwind'),
  ],
}
