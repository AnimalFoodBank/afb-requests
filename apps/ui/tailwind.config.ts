import type { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'

export default <Partial<Config>>{
  content: [
    // ... your project files, eg.:
    // './index.html',
    // './src/**/*.{vue,js,ts,jsx,tsx}',
    './vueform.config.ts', // or where `vueform.config.js` is located. Change `.js` to `.ts` if required.
    './node_modules/.pnpm/@vueform+vueform@*/node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
    './node_modules/.pnpm/@vueform+vueform@*/node_modules/@vueform/vueform/themes/tailwind/**/*.js',
    './node_modules/.pnpm/@vueform+vueform@*/node_modules/@vueform/builder/**/*.js',
    './node_modules/.pnpm/@vueform+vueform@*/node_modules/@vueform/builder/**/*.css',
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
