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
 6. Within `object.schema`, there are several fields defined, such as `pet_type`, `pet_name`, `pet_dob`, `food_details`, `dog_details`, and `other_details`. These fields define the different properties that need to be provided for each pet, such as the type of pet, name, age, food details (if applicable), dog-specific details (if applicable), and other animal details (if applicable).

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
              '2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000',
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
