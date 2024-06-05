/**
 * The `clientPetsSchema` is an object that defines the schema for the "Your Pets" section of the food request form. This schema is imported and used in the `FoodRequestForm.vue` component.

 Here's a breakdown of the `clientPetsSchema` object:

1. `which_pets`: A "radiogroup" field for selecting the pets being requested for.
2. `pets`: A "list" field for adding multiple pets (max 4). Each entry follows the schema defined in `object.schema`.

 In `FoodRequestForm.vue`, the `clientPetsSchema` is imported and used within the `schema` object of the form:

 ```js
 import clientPetsSchema from '@/modules/requests/clientPetsSchema';

 onMounted(() => {
   // ...

   schema.value = {
   // ...

   client_pets: clientPetsSchema,
   // ...
   };
 });
 */
const clientPetsSchema = {
  type: "object",
  before: "Please confirm the details of each of your pets that you're requesting for.",
  schema: {
    which_pets: {
      type: "radiogroup",
      label: "Which pets are you requesting for?",
      items: ["All", "Selected"],
      rules: ["required"],
      columns: {
        container: 12,
      },
      hidden: true,
      required: false,
    },
    pets: {
      type: "list",
      max: 4,
      min: 1,
      addClasses: {
        ListElement: {
          listItem: 'pt-6 mt-2 border- border-gray-200'
        },
        ElementLabel: {
          wrapper: 'text-[20px] font-semibold mb-4'
        },
      },
      object: {
        type: "object",
        schema: {
          pet_type: {
            type: "radiogroup",
            view: "tabs",
            label: "What kind of pet?",
            items: ["Cat", "Dog", "Other"],
            rules: ["required"],
            columns: {
              container: 12,
              wrapper: 12,
              label: 2,
            },
          },
          pet_name: {
            type: "text",
            rules: ["required", "max:32"],
            placeholder: "Name",
            columns: {
              container: 6,
              wrapper: 12,
            },
            conditions: [
              ['client_pets.pets.*.pet_type', ['Dog', 'Cat', 'Other']],
            ],
          },
          pet_dob: {
            type: "select",
            rules: ["required", "max:32"],
            placeholder: "Birth year",
            items: [
              '2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017',
              '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009',
              '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001',
              '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993',
              '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1985',
              '1984', '1983', '1982', '1981', '1980'
            ],
            columns: {
              container: 6,
            },
            conditions: [
              ['client_pets.pets.*.pet_type', ['Dog', 'Cat', 'Other']],
            ],
          },
          food_details: {
            type: "object",
            conditions: [
              ['client_pets.pets.*.pet_type', ['Dog', 'Cat']],
            ],
            schema: {
              allergies: {
                type: "text",
                placeholder: "Allergies",
                rules: [],
                description: "If your pet has any allergies, please list them here.",
                columns: {
                  container: 6,
                },
              },
              usual_brands: {
                type: "text",
                placeholder: "Usual brands",
                rules: [],
                description: "We try to match brands when possible.",
                columns: {
                  container: 6,
                },
              },
              foodtype: {
                type: "radiogroup",
                label: "Food Type",
                items: ["Either", "Dry", "Wet"],
                rules: ["required"],
                columns: {
                  container: 12,
                  label: 6,
                },
                default: "Either",
              }
            },
          },
          dog_details: {
            type: "object",
            conditions: [
              ['client_pets.pets.*.pet_type', ['Dog']],
            ],
            schema: {
              size: {
                type: "radiogroup",
                view: "default",
                rules: ["required"],
                items: ["Up to 10 lbs (Toy)", "10-20 lbs (Small)", "20-50 lbs (Medium)", "50-100 lbs (Large)", "Over 100 lbs (Extra Large)"],
                label: "Size",
                info: "If you're not sure, make a best guess.",
                columns: {
                  container: 12,
                  label: 6,
                },
              },
            }
          },
          spay_or_neutered: {
            type: "radiogroup",
            items: ["Yes", "No"],
            label: "Spayed/Neutered",
            rules: [],
            columns: {
              container: 12,
                  label: 6,
            },
            conditions: [
              ['client_pets.pets.*.pet_type', ['Dog', 'Cat']],
            ],
          },
          other_details: {
            type: "object",
            conditions: [
              ['client_pets.pets.*.pet_type', ['Other']],
            ],
            schema: {
              animal_type: {
                type: "text",
                label: "Type of animal",
                placeholder: "e.g. rabbit, bird, fish, etc.",
                rules: [],
                info: "Let us know what kind of animal and we'll do our best to accomodate",
                description: "If your pet has any allergies, please list them here.",
                columns: {
                  container: 12,
                  label: 6,
                },
              },
            }
          },
          general_notes: {
            type: "text",
            rules: ["max:100"],
            label: "Notes",
            info: "Any additional information you'd like to provide about this pet.",
            columns: {
              container: 12,
              label: 6,
            },
            conditions: [
              ['client_pets.pets.*.pet_type', ['Dog', 'Cat', 'Other']],
            ],
          },
        },
      },
    },

  },
}

export default clientPetsSchema;
