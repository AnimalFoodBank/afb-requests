import type { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'
import tailwindTypography from '@tailwindcss/typography'
import { iconsPlugin, getIconCollections } from '@egoist/tailwindcss-icons'

export default <Partial<Config>>{
  content: [
    `@/components/**/*.{vue,js,ts}`,
    `@/layouts/**/*.vue`,
    `@/pages/**/*.vue`,
    `@/composables/**/*.{js,ts}`,
    `@/modules/**/*.{js,ts}`,
    `@/plugins/**/*.{js,ts}`,
    `@/stores/**/*.{js,ts}`,
    `@/utils/**/*.{js,ts}`,
    `@/app.{js,ts,vue}`,
    `@/error.{js,ts,vue}`,
    `@/app.config.{js,ts}`,

    './vueform.config.ts',
    './node_modules/.pnpm/@vueform+vueform@*/node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
    './node_modules/.pnpm/@vueform+vueform@*/node_modules/@vueform/vueform/themes/tailwind/**/*.js',

  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['DM Sans', ...defaultTheme.fontFamily.sans]
      },
      colors: {
        // This is a tester, not currently used
        'custom-cancel': '#f3f4f6',
      },
    },
    darkMode: 'class',
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
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
