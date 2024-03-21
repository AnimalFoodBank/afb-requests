import type { ParsedContent } from '@nuxt/content/dist/runtime/types'

export interface BlogPost extends ParsedContent {
  title: string
  description: string
  date: string
  image?: HTMLImageElement
  badge?: Badge
  authors?: ({
    name: string
    description?: string
    avatar?: Avatar
  } & Link)[]
}

export interface FoodDeliveryFormState {
  // Define your state properties here
  delivery_address: {
      branch_location: string;
      location: {
        address_line1: string;
        city: string;
        divisions_level1: string;
        postcode: string;
        country: string;
      };
      building_type: string;
    },
    delivery_contact:{
      contact_number: string;
      contact_name: string;
      preferred_method: string;
    },
    your_pets: {
      pet_name: string;
      pet_breed: string;
      pet_age: string;
      pet_weight: string;
    },
    safe_drop: {
      safe_drop_policy: string;
      safe_drop: boolean;
      safe_drop_instructions: string;
    },
    confirmation: {
      confirm_correct: boolean;
      accept_terms: boolean;
    };
  // Add more properties as needed
}
