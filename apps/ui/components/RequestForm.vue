<template>
  <Vueform v-bind="vueform" />
</template>

<script setup lang="ts">

  const vueform = ref<any>(null);

  onMounted(() => {
    console.log('Component has been mounted');

    vueform.value = {
    size: 'md',
    displayErrors: false,
    steps: {
      page0: {
        label: 'Delivery Address Verification',
        elements: [
          'h3',
          'divider',
          'accommodation_type',
          'advert_elsewhere',
          'import',
          'accommodation_name',
          'divider_1',
        ],
        buttons: {
          previous: false,
        },
      },
      page1: {
        label: 'Location',
        elements: [
          'h2_1',
          'divider_2',
          'location',
          'divider_3',
        ],
      },
      page2: {
        label: 'Rooms',
        elements: [
          'h2_2',
          'divider_4',
          'guests_count',
          'bathroom_count',
          'size',
          'h2_3',
          'divider_5',
          'rooms',
          'divider_6',
        ],
      },
      page3: {
        label: 'Equipment & facilities',
        elements: [
          'h2_4',
          'divider_7',
          'equipment',
          'divider_8',
        ],
      },
      page4: {
        label: 'Breakfast',
        elements: [
          'h2_5',
          'divider_9',
          'serve_breakfast',
          'breakfast_in_price',
          'breakfast_price',
          'breakfast_types',
          'divider_10',
        ],
      },
      page5: {
        label: 'Parking',
        elements: [
          'h2_6',
          'divider_11',
          'parking',
          'parking_price',
          'parking_interval',
          'parking_reservation',
          'parking_location',
          'parking_location_offsite_description',
          'parking_type',
          'divider_12',
        ],
      },
      page6: {
        label: 'Languages',
        elements: [
          'h2_7',
          'divider_13',
          'languages',
          'divider_14',
        ],
      },
      page7: {
        label: 'House rules',
        elements: [
          'h2_8',
          'divider_15',
          'rules',
          'check_in_from',
          'check_in_until',
          'p_1',
          'check_out_from',
          'check_out_until',
          'divider_16',
        ],
      },
      page8: {
        label: 'Host profile',
        elements: [
          'h2_9',
          'divider_17',
          'profile',
          'property',
          'host_name',
          'about_host',
          'about_neighbourhood',
          'divider_18',
        ],
      },
      page9: {
        label: 'Gallery',
        elements: [
          'h2_10',
          'divider_19',
          'gallery',
          'divider_20',
        ],
      },
      page10: {
        label: 'Payment',
        elements: [
          'h2_11',
          'divider_21',
          'can_charge_card',
          'price_per_night',
          'divider_22',
        ],
      },
      page11: {
        label: 'Rate plans',
        elements: [
          'h2_12',
          'divider_23',
          'h3',
          'p_copy5',
          'free_days_before_cancellation',
          'accidental_booking_protection',
          'standard_plan_divider',
          'h4',
          'p',
          'group_discount',
          'container',
          'divider_29',
          'h3_1',
          'p_copy',
          'p_copy2',
          'nonrefundable_rate_plan',
          'non_refundable_plan_discount',
          'divider_30',
          'h3_2',
          'p_copy3',
          'p_copy4',
          'weekly_rate_plan',
          'weekly_rate',
          'divider_24',
        ],
      },
      page12: {
        label: 'Availability',
        elements: [
          'h2_13',
          'divider_25',
          'available_from',
          'available_from_date',
          'divider_26',
        ],
      },
      page13: {
        label: 'Complete',
        elements: [
          'h2_14',
          'divider_27',
          'terms_1',
          'terms_2',
          'divider_28',
        ],
      },
    },
    schema: {
      h2: {
        type: 'static',
        content: 'Details',
        tag: 'h2',
        top: '1',
      },
      divider: {
        type: 'static',
        tag: 'hr',
      },
      accommodation_type: {
        type: 'radiogroup',
        view: 'tabs',
        items: [
          'Apartment',
          'Detached house',
          'Townhome',
          'Condo',
          'Other',
        ],
        rules: [
          'required',
        ],
        fieldName: 'Accommodation type',
        default: 'Apartment',
        label: 'Select accommodation type',
      },
      advert_elsewhere: {
        type: 'checkboxgroup',
        fieldName: 'Posted elsewhere',
        items: [
          'Airbnb',
          'Tripadvisor',
          'Vrbo',
          'Other',
        ],
        label: 'Have you posted it elsewhere?',
      },
      import: {
        type: 'group',
        schema: {
          external_url: {
            type: 'text',
            inputType: 'url',
            rules: [
              'required',
              'max:255',
              'url',
            ],
            placeholder: 'eg. http(s)://domain.com',
            floating: false,
            label: 'Import your data from Airbnb or Vrbo',
            columns: {
              container: 9,
              label: 12,
              wrapper: 12,
            },
            description: 'Ex.: https://airbnb.com/rooms/xxxxxxxxxx orhttps://vrbo.com/xxxxxx',
          },
          import_button: {
            type: 'button',
            buttonLabel: 'Import',
            columns: {
              container: 3,
              label: 12,
              wrapper: 12,
            },
            buttonType: 'anchor',
            label: '&nbsp;',
            after: '&nbsp;',
            full: true,
            align: 'center',
          },
        },
        conditions: [
          [
            'advert_elsewhere',
            'in',
            [
              'Airbnb',
              'Vrbo',
            ],
          ],
        ],
      },
      accommodation_name: {
        type: 'text',
        description: 'This name will be shown in the results.',
        rules: [
          'required',
          'max:255',
        ],
        fieldName: 'Name',
        label: 'Name of accommodation',
        default: 'Ferienwohnung auf der Hinteregg',
      },
      divider_1: {
        type: 'static',
        tag: 'hr',
        top: '1',
        bottom: '1',
      },
      h2_1: {
        type: 'static',
        content: 'Location of accommodation',
        tag: 'h2',
        top: '1',
      },
      divider_2: {
        type: 'static',
        tag: 'hr',
      },
      location: {
        type: 'object',
        schema: {
          p: {
            type: 'static',
            tag: 'p',
            content: 'Please make sure your address is correct, we will send a letter to make sure of authenticity - <b>later this is hard to modify</b>',
          },
          country: {
            type: 'select',
            search: true,
            native: false,
            inputType: 'search',
            autocomplete: 'off',
            items: '/json/countries.json',
            rules: [
              'required',
            ],
            label: 'Country',
            default: 'CH',
          },
          state: {
            type: 'select',
            search: true,
            native: false,
            inputType: 'search',
            autocomplete: 'off',
            items: '/json/states.json',
            rules: [
              'required',
            ],
            label: 'State',
            conditions: [
              [
                'location.country',
                'in',
                [
                  'US',
                ],
              ],
            ],
          },
          street: {
            type: 'text',
            label: 'Street name',
            rules: [
              'required',
              'max:255',
            ],
            columns: {
              container: 8,
              label: 12,
              wrapper: 12,
            },
            default: 'Alte Steige',
          },
          house_number: {
            type: 'text',
            label: 'House number',
            rules: [
              'required',
              'max:255',
            ],
            columns: {
              container: 4,
              label: 12,
              wrapper: 12,
            },
            default: '15',
          },
          floor: {
            type: 'text',
            label: 'Floor or door number (optional)',
            rules: [
              'nullable',
              'max:255',
            ],
          },
          zip: {
            type: 'text',
            rules: [
              'required',
              'max:255',
            ],
            columns: {
              container: 4,
              label: 12,
              wrapper: 12,
            },
            label: 'Zip code',
            default: '87629',
          },
          city: {
            type: 'text',
            rules: [
              'required',
              'max:255',
            ],
            columns: {
              container: 8,
              label: 12,
              wrapper: 12,
            },
            label: 'City',
            default: 'Füssen',
          },
        },
      },
      divider_3: {
        type: 'static',
        tag: 'hr',
        top: '1',
        bottom: '1',
      },
      h2_2: {
        type: 'static',
        tag: 'h2',
        content: 'Rooms',
        top: '1',
      },
      divider_4: {
        type: 'static',
        tag: 'hr',
      },
      guests_count: {
        type: 'text',
        inputType: 'number',
        rules: [
          'required',
          'integer',
        ],
        autocomplete: 'off',
        label: 'How many guests can stay?',
        columns: {
          wrapper: 2,
        },
        default: '4',
      },
      bathroom_count: {
        type: 'text',
        inputType: 'number',
        rules: [
          'required',
          'numeric',
        ],
        autocomplete: 'off',
        label: 'How many bathrooms?',
        columns: {
          wrapper: 2,
        },
        default: '2',
      },
      size: {
        type: 'text',
        inputType: 'number',
        rules: [
          'nullable',
          'numeric',
        ],
        autocomplete: 'off',
        label: 'How big is this apartment? (optional)',
        columns: {
          wrapper: 2,
        },
        addons: {
          after: 'm<sup>2</sup>',
        },
        default: '75',
      },
      h2_3: {
        type: 'static',
        tag: 'h2',
        content: 'Room editor',
        top: '2',
      },
      divider_5: {
        type: 'static',
        tag: 'hr',
      },
      rooms: {
        type: 'list',
        element: {
          type: 'object',
          schema: {
            h4: {
              type: 'static',
              tag: 'h4',
              content: 'Room',
            },
            room_type: {
              type: 'select',
              search: true,
              native: false,
              label: 'Room type',
              inputType: 'search',
              autocomplete: 'off',
              items: [
                'Bedroom',
                'Living room',
                'Other',
              ],
              rules: [
                'required',
              ],
              default: 'Bedroom',
            },
            html: {
              type: 'static',
              columns: {
                container: 1,
              },
            },
            container: {
              type: 'group',
              schema: {
                h4: {
                  type: 'static',
                  tag: 'h4',
                  content: 'Beds',
                },
                container: {
                  type: 'group',
                  schema: {
                    html: {
                      type: 'static',
                      content: 'Bed type',
                      columns: {
                        container: 10,
                      },
                    },
                    html_copy: {
                      type: 'static',
                      content: 'Count',
                      columns: {
                        container: 2,
                      },
                    },
                  },
                  conditions: [
                    [
                      'rooms.*.container.beds',
                      'not_empty',
                    ],
                  ],
                },
                beds: {
                  type: 'list',
                  element: {
                    type: 'object',
                    schema: {
                      bed_type: {
                        type: 'select',
                        search: true,
                        native: false,
                        inputType: 'search',
                        autocomplete: 'off',
                        columns: {
                          container: 10,
                        },
                        items: [
                          'Single bed (90 cm - 130 cm)',
                          'Big single bed (131 cm - 150 cm)',
                          'Double bed (151 cm - 180 cm)',
                          'Big double bed (181 cm - 210 cm)',
                          'Bunk-bed (variable size)',
                          'Sofa-bed (variable size)',
                          'Futon (variable size)',
                        ],
                        default: 'Single bed (90 cm - 130 cm)',
                      },
                      bed_count: {
                        type: 'text',
                        inputType: 'number',
                        rules: [
                          'required',
                          'integer',
                        ],
                        autocomplete: 'off',
                        columns: {
                          container: 2,
                        },
                        default: '1',
                      },
                    },
                  },
                  addText: '+ Add bed',
                },
              },
              columns: {
                container: 11,
              },
            },
            divider: {
              type: 'static',
              tag: 'hr',
            },
          },
        },
        addText: '+ Add room',
      },
      divider_6: {
        type: 'static',
        tag: 'hr',
        bottom: '1',
      },
      h2_4: {
        type: 'static',
        tag: 'h2',
        content: 'Equipment & facilities',
        top: '1',
      },
      divider_7: {
        type: 'static',
        tag: 'hr',
      },
      equipment: {
        type: 'object',
        schema: {
          general: {
            type: 'checkboxgroup',
            label: 'General',
            items: [
              'AC',
              'Heating',
              'Free Wifi',
              'Electric car charger',
            ],
            columns: {
              container: 6,
              label: 12,
              wrapper: 12,
            },
          },
          kitchen: {
            type: 'checkboxgroup',
            label: 'Kitchen and cleaning',
            columns: {
              container: 6,
              label: 12,
              wrapper: 12,
            },
            items: [
              'Electric kettle',
              'Tea/coffee maker',
              'Towels',
              'Washing machine',
              'Dishwasher',
            ],
          },
          entertainment: {
            type: 'checkboxgroup',
            label: 'Entertainment',
            columns: {
              container: 6,
              label: 12,
              wrapper: 12,
            },
            items: [
              'Flat screen tv',
              'Bar',
              'Hot tub',
              'Sauna',
              'Swimming pool',
            ],
          },
          outside: {
            type: 'checkboxgroup',
            label: 'Outside',
            columns: {
              container: 6,
              label: 12,
              wrapper: 12,
            },
            items: [
              'BBQ',
              'Balcony',
              'Garden',
              'Beach',
            ],
          },
        },
      },
      divider_8: {
        type: 'static',
        tag: 'hr',
        top: '1',
        bottom: '1',
      },
      h2_5: {
        type: 'static',
        tag: 'h2',
        content: 'Breakfast details',
        top: '1',
      },
      divider_9: {
        type: 'static',
        tag: 'hr',
      },
      serve_breakfast: {
        type: 'radiogroup',
        view: 'tabs',
        items: [
          'Yes',
          'No',
        ],
        default: 'No',
        rules: [
          'required',
        ],
        label: 'Do you serve breakfast?',
        fieldName: 'Breakfast',
      },
      breakfast_in_price: {
        type: 'radiogroup',
        view: 'tabs',
        items: [
          'Yes',
          'No',
        ],
        default: 'Yes',
        rules: [
          'required',
        ],
        label: 'Is it included in the price?',
        conditions: [
          [
            'serve_breakfast',
            'in',
            [
              'Yes',
            ],
          ],
        ],
      },
      breakfast_price: {
        type: 'text',
        inputType: 'number',
        rules: [
          'required',
          'numeric',
        ],
        autocomplete: 'off',
        label: 'Breakfast cost per person, per day',
        addons: {
          before: '$',
        },
        description: 'Including taxes and fees.',
        conditions: [
          [
            'breakfast_in_price',
            'in',
            [
              'No',
            ],
          ],
          [
            'serve_breakfast',
            'in',
            [
              'Yes',
            ],
          ],
        ],
      },
      breakfast_types: {
        type: 'tags',
        closeOnSelect: false,
        label: 'What types of breakfasts do you offer?',
        items: [
          'Á la carte',
          'American',
          'Asian',
          'Breakfast togo',
          'Buffet',
          'Continental',
          'Full English/Irish',
          'Gluten-free',
          'Halal',
          'Italian',
          'Kosher',
          'Vegan',
          'Vegetarian',
        ],
        rules: [
          'required',
        ],
        search: true,
        inputType: 'search',
        autocomplete: 'off',
        conditions: [
          [
            'serve_breakfast',
            'in',
            [
              'Yes',
            ],
          ],
        ],
        description: 'Select all that applies.',
      },
      divider_10: {
        type: 'static',
        tag: 'hr',
        top: '1',
        bottom: '1',
      },
      h2_6: {
        type: 'static',
        tag: 'h2',
        content: 'Parking',
        top: '1',
      },
      divider_11: {
        type: 'static',
        tag: 'hr',
      },
      parking: {
        type: 'radiogroup',
        view: 'tabs',
        label: 'Is parking available to the guests?',
        items: [
          'Yes, free',
          'Yes, paid',
          'No',
        ],
        default: 'No',
        rules: [
          'required',
        ],
      },
      parking_price: {
        type: 'text',
        inputType: 'number',
        rules: [
          'required',
          'numeric',
        ],
        autocomplete: 'off',
        label: 'Cost of parking',
        addons: {
          before: '$',
        },
        columns: {
          container: 6,
          label: 12,
          wrapper: 12,
        },
        conditions: [
          [
            'parking',
            'in',
            [
              'Yes, paid',
            ],
          ],
        ],
      },
      parking_interval: {
        type: 'select',
        search: true,
        native: false,
        inputType: 'search',
        autocomplete: 'off',
        columns: {
          container: 6,
          label: 12,
          wrapper: 12,
        },
        label: '&nbsp;',
        rules: [
          'required',
        ],
        canDeselect: false,
        items: [
          'Per hour',
          'Per day',
          'Per stay',
        ],
        default: 'Per day',
        conditions: [
          [
            'parking',
            'in',
            [
              'Yes, paid',
            ],
          ],
        ],
      },
      parking_reservation: {
        type: 'radiogroup',
        view: 'tabs',
        label: 'Do guests need to reserve a parking spot?',
        items: [
          'Yes',
          'No',
        ],
        rules: [
          'required',
        ],
        conditions: [
          [
            'parking',
            'not_in',
            [
              'No',
            ],
          ],
        ],
      },
      parking_location: {
        type: 'radiogroup',
        view: 'tabs',
        label: 'Where is the parking located?',
        rules: [
          'required',
        ],
        items: [
          'On site',
          'Off site',
        ],
        conditions: [
          [
            'parking',
            'not_in',
            [
              'No',
            ],
          ],
        ],
      },
      parking_location_offsite_description: {
        type: 'textarea',
        label: 'Offsite parking location/description',
        conditions: [
          [
            'parking_location',
            'in',
            [
              'Off site',
            ],
          ],
        ],
        rules: [
          'required',
          'min:3',
        ],
        rows: 2,
      },
      parking_type: {
        type: 'radiogroup',
        view: 'tabs',
        label: 'What type of parking is it?',
        items: [
          'Private',
          'Public',
        ],
        rules: [
          'required',
        ],
        conditions: [
          [
            'parking',
            'not_in',
            [
              'No',
            ],
          ],
        ],
      },
      divider_12: {
        type: 'static',
        tag: 'hr',
        top: '1',
        bottom: '1',
      },
      h2_7: {
        type: 'static',
        tag: 'h2',
        content: 'Spoken language',
        top: '1',
      },
      divider_13: {
        type: 'static',
        tag: 'hr',
      },
      languages: {
        type: 'tags',
        closeOnSelect: false,
        search: true,
        label: 'Select all that applies.',
        inputType: 'search',
        autocomplete: 'off',
        items: '/json/languages.json',
        rules: [
          'required',
        ],
        default: [
          'English',
        ],
      },
      divider_14: {
        type: 'static',
        tag: 'hr',
        top: '1',
        bottom: '1',
      },
      h2_8: {
        type: 'static',
        tag: 'h2',
        content: 'House rules',
        top: '1',
      },
      divider_15: {
        type: 'static',
        tag: 'hr',
      },
      rules: {
        type: 'checkboxgroup',
        items: [
          'Smoking allowed',
          'Pets allowed',
          'Children allowed',
          'Parties/events allowed',
        ],
      },
      check_in_from: {
        type: 'date',
        label: 'Check-in',
        time: true,
        date: false,
        columns: {
          container: 4,
          label: 12,
          wrapper: 12,
        },
        rules: [
          'required',
        ],
        placeholder: 'From',
        default: '15:00',
      },
      check_in_until: {
        type: 'date',
        time: true,
        date: false,
        columns: {
          container: 4,
          label: 12,
          wrapper: 12,
        },
        rules: [
          'required',
        ],
        placeholder: 'Until',
        label: '&nbsp;',
        default: '23:00',
      },
      p_1: {
        type: 'static',
        tag: 'p',
        columns: {
          container: 4,
        },
      },
      check_out_from: {
        type: 'date',
        label: 'Check-out',
        time: true,
        date: false,
        columns: {
          container: 4,
          label: 12,
          wrapper: 12,
        },
        rules: [
          'required',
        ],
        placeholder: 'From',
        default: '06:00',
      },
      check_out_until: {
        type: 'date',
        time: true,
        date: false,
        columns: {
          container: 4,
          label: 12,
          wrapper: 12,
        },
        rules: [
          'required',
        ],
        placeholder: 'Until',
        label: '&nbsp;',
        default: '10:00',
      },
      divider_16: {
        type: 'static',
        tag: 'hr',
        bottom: '1',
        top: '1',
      },
      h2_9: {
        type: 'static',
        tag: 'h2',
        content: 'Host profile',
        top: '1',
      },
      divider_17: {
        type: 'static',
        tag: 'hr',
      },
      profile: {
        type: 'checkboxgroup',
        items: [
          'The property',
          'The host',
          'The neighbourhood',
        ],
        default: [
          'The property',
        ],
      },
      property: {
        type: 'textarea',
        label: 'About the property',
        placeholder: 'What makes your place unique? What can guests expect?',
        conditions: [
          [
            'profile',
            'in',
            [
              'The property',
            ],
          ],
        ],
        rules: [
          'required',
        ],
      },
      host_name: {
        type: 'text',
        label: 'Host name',
        rules: [
          'required',
          'max:255',
        ],
        conditions: [
          [
            'profile',
            'in',
            [
              'The host',
            ],
          ],
        ],
      },
      about_host: {
        type: 'textarea',
        label: 'About the host',
        placeholder: 'What are your interests? What do you like about hosting?',
        rules: [
          'required',
          'max:1023',
        ],
        conditions: [
          [
            'profile',
            'in',
            [
              'The host',
            ],
          ],
        ],
      },
      about_neighbourhood: {
        type: 'textarea',
        label: 'About the neighbourhood',
        placeholder: 'What’s the area like? Are there any attractions nearby?',
        rules: [
          'required',
          'max:1023',
        ],
        conditions: [
          [
            'profile',
            'in',
            [
              'The neighbourhood',
            ],
          ],
        ],
      },
      divider_18: {
        type: 'static',
        tag: 'hr',
        bottom: '1',
        top: '1',
      },
      h2_10: {
        type: 'static',
        tag: 'h2',
        content: 'What does your place look like?',
        top: '1',
      },
      divider_19: {
        type: 'static',
        tag: 'hr',
      },
      gallery: {
        type: 'multifile',
        view: 'gallery',
        accept: 'image/*,image/jpeg,image/png,image/gif,image/svg+xml',
        drop: true,
        description: 'First uploaded photo will be shown in search resultsMax size is 2MB/file, accepted formats are: JPG, PNG, GIF, SVG. You’re 29% more likely to get bookings if you upload at least 5 photos.',
        file: {
          rules: [
            'mimetypes:image/jpeg,image/png,image/gif,image/svg+xml',
            'max:2048',
          ],
        },
        before: 'Add at least one photo now. You can always add more later.',
        fieldName: 'gallery',
      },
      divider_20: {
        type: 'static',
        tag: 'hr',
        top: '1',
        bottom: '1',
      },
      h2_11: {
        type: 'static',
        tag: 'h2',
        content: 'Guest payment options',
        top: '1',
      },
      divider_21: {
        type: 'static',
        tag: 'hr',
      },
      can_charge_card: {
        type: 'radiogroup',
        view: 'tabs',
        label: 'Can you charge credit cards at your property?',
        items: [
          'Yes',
          'No',
        ],
        default: 'Yes',
        rules: [
          'required',
        ],
      },
      price_per_night: {
        type: 'text',
        inputType: 'number',
        rules: [
          'required',
          'numeric',
        ],
        autocomplete: 'off',
        label: 'How much do you want to charge per night?',
        addons: {
          before: '$',
        },
        description: 'Including taxes, commission, and fees',
        columns: {
          wrapper: 3,
        },
        default: '120',
      },
      divider_22: {
        type: 'static',
        tag: 'hr',
        bottom: '1',
        top: '1',
      },
      h2_12: {
        type: 'static',
        tag: 'h2',
        content: 'Rate plans',
        top: '1',
      },
      divider_23: {
        type: 'static',
        tag: 'hr',
      },
      h3: {
        type: 'static',
        tag: 'h3',
        content: 'Standard rate plan',
        top: '1',
      },
      p_copy5: {
        type: 'static',
        tag: 'p',
        content: 'How many days before arrival can guests cancel their booking for free?',
      },
      free_days_before_cancellation: {
        type: 'text',
        inputType: 'number',
        rules: [
          'required',
          'min:1',
          'max:30',
          'integer',
        ],
        autocomplete: 'off',
        addons: {
          after: 'days',
        },
        default: '2',
        description: 'Guests love flexibility – free cancellation rates are generally the most booked rates. Get your first booking sooner by allowing guests to cancel up to one day before check-in.',
        fieldName: 'cancellation days',
        columns: {
          wrapper: 2,
        },
      },
      accidental_booking_protection: {
        type: 'toggle',
        text: 'Accidental booking protection',
        description: 'To avoid having to deal with accidental bookings, we automatically waive cancellation fees for guests who cancel within 24 hours of booking.',
        default: true,
        labels: {
          on: 'On',
          off: 'Off',
        },
      },
      standard_plan_divider: {
        type: 'static',
        tag: 'hr',
      },
      h4: {
        type: 'static',
        tag: 'h4',
        content: 'Discount',
      },
      p: {
        type: 'static',
        tag: 'p',
        content: 'Offering lower rates for groups of less than 3 makes your property more attractive to potential guests.',
      },
      group_discount: {
        type: 'toggle',
        text: 'Price per group size',
        labels: {
          on: 'On',
          off: 'Off',
        },
      },
      container: {
        type: 'group',
        schema: {
          guest_discount_1: {
            type: 'text',
            placeholder: 'Discount',
            columns: {
              container: 4,
            },
            addons: {
              after: '%',
            },
            label: '1 guest',
            rules: [
              'integer',
            ],
            default: '20',
            inputType: 'number',
          },
          guest_discount_2: {
            type: 'text',
            placeholder: 'Discount',
            columns: {
              container: 4,
            },
            addons: {
              after: '%',
            },
            label: '2 guests',
            rules: [
              'integer',
            ],
            default: '10',
            inputType: 'number',
          },
          guest_discount_3: {
            type: 'text',
            placeholder: 'Discount',
            columns: {
              container: 4,
            },
            addons: {
              after: '%',
            },
            label: '3+ guests',
            rules: [
              'integer',
            ],
            default: '0',
            inputType: 'number',
          },
        },
        conditions: [
          [
            'group_discount',
            '==',
            true,
          ],
        ],
        description: 'The recommended discounts are based on data from properties like yours. These can be updated at any time.',
      },
      divider_29: {
        type: 'static',
        tag: 'hr',
      },
      h3_1: {
        type: 'static',
        tag: 'h3',
        content: 'Non-refundable rate plan',
        top: '1',
      },
      p_copy: {
        type: 'static',
        tag: 'p',
        content: 'In addition to the standard rate plan you created for your property, you can add a non-refundable rate plan. ',
      },
      p_copy2: {
        type: 'static',
        tag: 'p',
        content: "With this, you set a discounted price but your revenue for these bookings is guaranteed because guests won't receive a refund if they cancel or no-show.",
      },
      nonrefundable_rate_plan: {
        type: 'toggle',
        text: 'Set up non-refundable rate plan',
        labels: {
          on: 'On',
          off: 'Off',
        },
      },
      non_refundable_plan_discount: {
        type: 'text',
        inputType: 'number',
        autocomplete: 'off',
        label: 'Discount for guests that book with this rate plan:',
        addons: {
          after: '%',
        },
        description: 'Guests who select non-refundable rates are usually looking for competitive prices. A discount of at least 10% will attract more guests by improving your visibility.',
        default: '10',
        columns: {
          wrapper: 2,
        },
        conditions: [
          [
            'nonrefundable_rate_plan',
            '==',
            true,
          ],
        ],
      },
      divider_30: {
        type: 'static',
        tag: 'hr',
      },
      h3_2: {
        type: 'static',
        tag: 'h3',
        content: 'Weekly rate plan',
        top: '1',
      },
      p_copy3: {
        type: 'static',
        tag: 'p',
        content: 'In addition to the standard rate plan you created for your property, you can add a weekly rate plan.',
      },
      p_copy4: {
        type: 'static',
        tag: 'p',
        content: 'For this, you set a discounted price and use the same cancellation policy as the standard rate plan. Guests who stay for at least a week are interested in discounts since they’ll be spending more on their overall booking.',
      },
      weekly_rate_plan: {
        type: 'toggle',
        text: 'Set up weekly rate',
        labels: {
          on: 'On',
          off: 'Off',
        },
      },
      weekly_rate: {
        type: 'text',
        inputType: 'number',
        rules: [
          'required',
          'integer',
        ],
        autocomplete: 'off',
        label: 'How much cheaper than the standard rate?',
        addons: {
          after: '%',
        },
        columns: {
          wrapper: 2,
        },
        default: '15',
        conditions: [
          [
            'weekly_rate_plan',
            '==',
            true,
          ],
        ],
      },
      divider_24: {
        type: 'static',
        tag: 'hr',
        bottom: '1',
        top: '1',
      },
      h2_13: {
        type: 'static',
        tag: 'h2',
        content: 'Availability',
        top: '1',
      },
      divider_25: {
        type: 'static',
        tag: 'hr',
      },
      available_from: {
        type: 'radiogroup',
        view: 'tabs',
        label: "What's the first date when guests can check in?",
        items: [
          'As soon as possible',
          'On a specific date',
        ],
        default: 'As soon as possible',
      },
      available_from_date: {
        type: 'date',
        rules: [
          'required',
        ],
        conditions: [
          [
            'available_from',
            'in',
            [
              'On a specific date',
            ],
          ],
        ],
        placeholder: 'Choose a date',
        floating: false,
        displayFormat: 'Do MMM, YYYY',
      },
      divider_26: {
        type: 'static',
        tag: 'hr',
        bottom: '1',
        top: '1',
      },
      h2_14: {
        type: 'static',
        tag: 'h2',
        content: 'Complete',
        top: '1',
      },
      divider_27: {
        type: 'static',
        tag: 'hr',
      },
      terms_1: {
        type: 'checkbox',
        text: 'I certify that this is a legitimate accommodation business with all necessary licenses and permits, which can be shown upon first request. Mydomain.com B.V. reserves the right to verify and investigate any details provided in this registration.',
        fieldName: 'Registration rights',
        rules: [
          'accepted',
        ],
      },
      terms_2: {
        type: 'checkbox',
        text: 'I have read, accepted, and agreed to the Terms and Conditions and Privacy Policy.',
        fieldName: 'Terms',
        rules: [
          'accepted',
        ],
      },
      divider_28: {
        type: 'static',
        tag: 'hr',
        bottom: '1',
        top: '1',
      },
    },
  }
  });

</script>
