import type { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'
import { iconsPlugin, getIconCollections } from '@egoist/tailwindcss-icons'

export default <Partial<Config>>{
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",

    './vueform.config.ts',
    './node_modules/.pnpm/@vueform+vueform@*/node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
    './node_modules/.pnpm/@vueform+vueform@*/node_modules/@vueform/vueform/themes/tailwind/**/*.js',

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
    require("@tailwindcss/forms"),
    require('@vueform/vueform/tailwind'),
    // require('@vueform/builder/tailwind'),
    iconsPlugin({
      // re: "Include Icons in build instead of doing network requests #34"
      // @see https://github.com/nuxt-modules/icon/issues/34#issuecomment-2003339110
      //
      // Select the icon collections you want to use
      // You can also ignore this option to automatically discover all individual icon packages you have installed
      // If you install @iconify/json, you should explicitly specify the collections you want to use, like this:
      // collections: getIconCollections(["heroicons", "streamline", "ph", "game-icons"]),
    })
  ],
}
