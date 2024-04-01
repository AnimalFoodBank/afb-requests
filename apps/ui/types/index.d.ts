
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

import '@types/google.maps';

declare global {
  interface Window {
    google: typeof google;
  }
}

export interface SessionData {
  id: string
  email: string
  name: string
  role: 'admin' | 'guest' | 'account'
  is_staff: boolean
}


export interface FoodRequestFormState {
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
    interactive_address?: string;
    building_type: string;
  },
  delivery_contact: {
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
    // Policy is expected to be not set since it's a text
    // paragraph defined within the form component. It's not
    // a form field in that sense, but a feature of Vueform.
    safe_drop_policy?: string;
    safe_drop: boolean;
    safe_drop_instructions: string;
  },
  confirmation: {
    confirm_correct: boolean;
    accept_terms: boolean;
  };
}
