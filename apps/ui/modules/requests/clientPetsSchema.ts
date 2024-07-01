import { generateYearRange } from '@/utils/timeTools';
import type { PetInfo } from '@/types';

/**
 * This schema is used to collect information about the pets of a client.
 * It is used in the `FoodRequestForm` and `PetsForm` interfaces.
 * @param defaultPets - An array of `PetInfo` objects to be used as the default values for the form.
 * @param withControls - If `true` (default), the form will include controls for adding and removing pets.
 * @returns - A schema object that can be used to generate a form.
 */
const clientPetsSchema = (defaultPets: PetInfo[] = [], withControls: boolean = true) => {
  console.log("Creating client pets schema with default pets:", defaultPets);
  return {
    type: "object",
    before: "Please confirm the details of each of your pets. ",
    schema: {
      pets: {
        type: "list",
        max: 4,
        min: 1,
        sort: true,
        controls: {
          add: withControls,
        },
        storeOrder: "order",
        addClasses: {
          ListElement: {
            listItem: 'pt-6 mt-2 border- border-gray-200 bg-gray-200 dark:bg-gray-800 rounded p-6',
          },
          ElementLabel: {
            wrapper: 'text-[20px] font-semibold mb-4',

          },
        },
        default: defaultPets,
        object: {
          type: "object",
          schema: {
            pet_id: {
              type: "hidden",
              default: null,
            },
            pet_type: {
              type: "radiogroup",
              view: "tabs",
              size: 'xs',
              //label: "What kind of pet?",
              addClass: "text-sm font-light",
              items: {
                cat: "Cat",
                dog: "Dog",
                other: "Other",
              },
              rules: ["required"],
              columns: {
                container: 12,
                wrapper: 12,
                label: 2,
              },
            },
            pet_name: {
              type: "text",
              size: "lg",
              rules: ["required", "max:32"],
              placeholder: "Name (required)",
              columns: {
                container: 6,
                wrapper: 12,
              },
              addClass: "text-4xl font-bold",
              conditions: [
                ['client_pets.pets.*.pet_type', ['dog', 'cat', 'other']],
              ],
            },
            pet_dob: {
              type: "select",
              size: "lg",
              rules: ["required", "max:32"],
              placeholder: "Birth year (required)",
              items: generateYearRange(),
              columns: {
                container: 6,
              },
              conditions: [
                ['client_pets.pets.*.pet_type', ['dog', 'cat', 'other']],
              ],
            },
            food_details: {
              type: "object",
              conditions: [
                ['client_pets.pets.*.pet_type', ['dog', 'cat']],
              ],
              schema: {
                allergies: {
                  type: "text",
                  size: "sm",
                  placeholder: "Allergies",
                  rules: [],
                  description: "If your pet has any allergies, please list them here.",
                  columns: {
                    container: 6,
                  },
                },
                general_notes: {
                  type: "text",
                  size: "sm",
                  rules: ["max:100"],
                  placeholder: "Notes",
                  description: "Any additional information you'd like to provide about this pet.",
                  columns: {
                    container: 6,
                    label: 6,
                  },
                  conditions: [
                    ['client_pets.pets.*.pet_type', ['dog', 'cat', 'other']],
                  ],
                },
                foodtype: {
                  type: "radiogroup",
                  size: "sm",
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
            /**
             * There are no specific details for cats at this time.
             * cat_details: {
             *
             * },
             */
            dog_details: {
              type: "object",
              conditions: [
                ['client_pets.pets.*.pet_type', ['dog']],
              ],
              schema: {
                size: {
                  type: "radiogroup",
                  size: "sm",
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
              size: "sm",
              items: {
                true: "Yes",
                false: "No"
              },
              label: "Spayed/Neutered*",
              rules: ["required"],
              columns: {
                container: 12,
                label: 6,
              },
              conditions: [
                ['client_pets.pets.*.pet_type', ['dog', 'cat']],
              ],
            },
            animal_details: {
              type: "object",
              conditions: [
                ['client_pets.pets.*.pet_type', ['other']],
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
          },
        },
      },
    },
  }
};

export default clientPetsSchema;
