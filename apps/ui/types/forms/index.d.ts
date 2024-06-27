export interface FoodRequestFormState {
  id: string;
  user_id: string;
  delivery_address: {
    branch_location: string;
    interactive_address: string;
    building_type: string;
    instructions: string;
    country: string;  // all user addresses assumed to be in the same country
    location: {
      address_line1: string;
      address_line2?: string;
      city: string;
      prov_or_state: string;
      postcode: string;
      lat?: number;
      lon?: number;
    }
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
      pet_dob: string;
      food_details?: {
        allergies?: string;
        usual_brands?: string;
        foodtype?: string;
      };
      dog_details?: {
        size: string;
      };
      other_details?: {
        animal_description: string;
      };
      details?: string;
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
