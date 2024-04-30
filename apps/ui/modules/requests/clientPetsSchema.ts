/**
 * The `clientPetsSchema` is an object that defines the schema for the "Your Pets" section of the food request form. This schema is imported and used in the `FoodRequestForm.vue` component.

 Here's a breakdown of the `clientPetsSchema` object:

 1. `type: "object"`: This defines the overall type of the schema as an object.
 2. `before: "Please provide information about each of your pets."`: This is a string that will be displayed before the "Your Pets" section of the form.
 3. `schema`: This is an object that contains the actual schema definition for the "Your Pets" section.
 4. `pets`: This is a nested object within the `schema` object. It defines a "list" type field, which means that it will allow the user to add multiple pet entries.
    - `type: "list"`: Specifies that this is a list field.
    - `max: 4`: Sets the maximum number of pet entries that can be added to 4.
    - `min: 1`: Sets the minimum number of pet entries required to 1.
    - `addClasses`: This object defines CSS classes to be applied to specific elements within the list field.
    - `object`: This is another nested object that defines the schema for each individual pet entry.
 5. `object.schema`: This is an object that contains the schema definition for each individual pet entry.
 6. Within `object.schema`, there are several fields defined, such as `pet_type`, `pet_name`, `pet_age`, `food_details`, `dog_details`, and `other_details`. These fields define the different properties that need to be provided for each pet, such as the type of pet, name, age, food details (if applicable), dog-specific details (if applicable), and other animal details (if applicable).

 Each field within `object.schema` has its own set of properties, such as `type` (which defines the type of input field), `rules` (which defines validation rules), `items` (for select or radio group fields), `conditions` (for conditional rendering of fields based on certain conditions), and `columns` (for layout purposes).

 In the `FoodRequestForm.vue` file, the `clientPetsSchema` is imported and used within the `schema` object of the form:

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
  before: "",
  schema: {
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
          pet_name: {
            type: "text",
            rules: ["required", "max:32"],
            placeholder: "Name",
            columns: {
              container: 6,
              wrapper: 12,
            },
          },
          pet_age: {
            type: "select",
            rules: ["required", "max:32"],
            placeholder: "Age",
            items: [
              'Up to 6 months',
              'Under 1 year',
              '2',
              '3',
              '4',
              '5',
              '6',
              '7',
              '8',
              '9',
              '10+'
            ],
            columns: {
              container: 6,
            },
          },
          pet_type: {
            type: "radiogroup",
            view: "tabs",
            items: ["Cat", "Dog", "Other"],
            rules: ["required"],
            columns: {
              container: 12,
              wrapper: 12,
            },
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
          other_details: {
            type: "object",
            conditions: [
              ['client_pets.pets.*.pet_type', ['Other']],
            ],
            schema: {
              size: {
                type: "text",
                rules: ["required"],
                label: "Details",
                info: "Let us know what kind of animal and we'll do our best to accomodate",
                columns: {
                  container: 12,
                  label: 3,
                  wrapper: 8,
                },
              },
            }
          },
        },
      },
    },

  },
}

export default clientPetsSchema;
