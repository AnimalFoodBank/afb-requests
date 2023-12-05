import type { Config } from 'tailwindcss';

const config: Config = {
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@vueform/vueform/tailwind'),
  ],
  theme: {
    //
    // re: Font settings
    //
    // See:
    // https://tailwindcss.com/docs/font-family#font-families
    // https://stackoverflow.com/questions/60692794/can-you-change-the-base-font-family-in-tailwind-config/70714843#70714843
    //
    fontFamily: {
      sans: [
        'Avenir',
        'Helvetica',
        'Arial',
        'sans-serif'
      ],
      serif: [
        'Lora',
        'Georgia',
        'Cambria',
        'Times New Roman',
        'Times',
        'serif',
      ],
      mono: [
        'Menlo',
        'Monaco',
        'Consolas',
        'Liberation Mono',
        'Courier New',
        'monospace',
      ],
    },
  },
  content: [
    "./index.html",
    "./src/**/*.{vue,html,js,ts,jsx,tsx}",
    "../afbcore/templates/**/*.html",
    './vueform.config.ts', // or where `vueform.config.js` is located
    './node_modules/@vueform/vueform/themes/tailwind/**/*.vue',
    './node_modules/@vueform/vueform/themes/tailwind/**/*.{ts,js,tsx,jsx}',
  ],
};

export default config;
