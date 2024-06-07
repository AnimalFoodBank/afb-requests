<template>
  <Vueform v-bind="vueform" />
</template>

<script>
import { ref } from 'vue';

export default {
  setup(props, context)
  {
    const vueform = ref({
      size: 'md',
      displayErrors: false,
      schema: {
        h1: {
          type: 'static',
          tag: 'h1',
          content: 'Find your dream destination',
          bottom: '1',
        },
        location: {
          type: 'location',
          size: 'lg',
        },
        check_in: {
          type: 'date',
          displayFormat: 'MMM DD, YYYY',
          placeholder: 'Check-in',
          columns: {
            container: 6,
          },
          size: 'lg',
          rules: [
            'after_or_equal:today',
          ],
        },
        check_out: {
          type: 'date',
          displayFormat: 'MMM DD, YYYY',
          placeholder: 'Check-out',
          columns: {
            container: 6,
          },
          size: 'lg',
          rules: [
            'after_or_equal:check_in',
          ],
        },
        adults: {
          type: 'text',
          inputType: 'number',
          rules: [
            'min:1',
            'integer',
          ],
          autocomplete: 'off',
          default: '1',
          columns: {
            container: 4,
            label: 12,
            wrapper: 12,
          },
          placeholder: 'Adults',
          size: 'lg',
        },
        kids: {
          type: 'text',
          inputType: 'number',
          rules: [
            'nullable',
            'min:0',
            'integer',
          ],
          autocomplete: 'off',
          default: '0',
          columns: {
            container: 4,
            label: 12,
            wrapper: 12,
          },
          placeholder: 'Kids',
          size: 'lg',
        },
        rooms: {
          type: 'text',
          inputType: 'number',
          rules: [
            'nullable',
            'min:0',
            'integer',
          ],
          autocomplete: 'off',
          columns: {
            container: 4,
            label: 12,
            wrapper: 12,
          },
          default: '1',
          placeholder: 'Rooms',
          size: 'lg',
        },
        is_standalone: {
          type: 'checkbox',
          text: 'Standalone only',
          rules: [
            'integer',
          ],
        },
        is_business_trip: {
          type: 'checkbox',
          text: 'Business trip',
          rules: [
            'integer',
          ],
        },
        search: {
          type: 'button',
          buttonLabel: 'Search',
          submits: true,
          size: 'lg',
          align: 'center',
          full: true,
        },
        advanced: {
          type: 'toggle',
          text: 'Advanced search',
        },
        container: {
          type: 'group',
          schema: {
            divider: {
              type: 'static',
              tag: 'hr',
            },
            guest_rating: {
              type: 'checkboxgroup',
              label: 'Guest rating',
              items: [
                '10* Excellent',
                '9* Superb',
                '8* Really good',
                '7* Good',
                '6* Pleasant',
                'Other',
              ],
              columns: {
                container: 6,
              },
            },
            divider_2: {
              type: 'static',
              tag: 'hr',
            },
            star_count: {
              type: 'checkboxgroup',
              label: 'Star count',
              items: [
                '2 stars',
                '3 stars',
                '4 stars',
                '5 stars',
                'Other',
              ],
              columns: {
                container: 6,
              },
            },
          },
          conditions: [
            [
              'advanced',
              '==',
              true,
            ],
          ],
        },
      },
    })

    return {
      vueform,
    }
  }
}
</script>
