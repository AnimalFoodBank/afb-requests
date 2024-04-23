

// import { BlogPost } from '.content/BlogPost';
// import { SessionData } from './SessionData';

// import { User } from './models/index.d.ts';
// import { FoodAvailable, DeliveryRegion, Branch } from './models/index.d.ts';

export interface FoodRequestFormState {
  id: string;
  user_id: string;
  delivery_address: {
    branch_location: string;
    location: {
      interactive_address?: string;
      country: string;
      building_type?: string;
    };
  };
  delivery_contact: {
    contact_name: string;
    preferred_method: string;
    contact_email?: string;
    contact_phone?: string;
    alt_contact_phone?: string;
  };
  client_pets: {
    pets: {
      pet_type: string;
      pet_name: string;
      pet_age: string;
      food_details?: {
        allergies?: string;
        usual_brands?: string;
        foodtype?: string;
      };
      dog_details?: {
        size: string;
      };
      other_details?: {
        size?: string;
      };
    }[];
  };
  safe_drop: {
    safe_drop_policy?: string;
    safe_drop: boolean;
    safe_drop_instructions: string;
  };
  confirmation: {
    confirm_correct: boolean;
    accept_terms: boolean;
  };
}
