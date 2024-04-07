

export interface FoodRequestFormState {
  id: string;

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
    pets_blob?: string;
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
