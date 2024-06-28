
/**
 * AFB Request Models
 *
 * This file contains TypeScript interfaces that represent
 * the models in the AFB API.
 *
 *
 * See: ./apps/api/afbcore/models.
 *
 */


// Equivalent to Django BaseAbstractModel
export interface BaseAbstractModel {
  id: string; // UUIDField, primary key
  created: Date; // DateTimeField, auto_now_add=True
  updated: Date; // DateTimeField, auto_now=True
  is_removed: boolean; // BooleanField, default=False
}

// Equivalent to Django PhysicalLocation
export interface PhysicalLocationMixin {
  location_name: string;
  address_line1?: string | null;
  address_line2?: string | null;
  city?: string | null;
  state_or_province?: string | null;
  postal_code?: string | null;
  country?: string | null;
  ext_id?: string | null;
}

// Equivalent to Django User
export interface User extends BaseAbstractModel {
  email: string;
  name: string;
  username?: string | null;
  password?: string | null;
  is_staff?: boolean | null;
  is_active?: boolean | null;
  date_joined?: Date | null;
  last_login?: Date | null;
  first_name?: string | null;
  last_name?: string | null;
}

// Equivalent to Django Profile
export interface Profile extends BaseAbstractModel {
  user: User;
  role: Role;
  branches: Branch[];
  preferred_name: string;
  email: string;
  phone_number: string;
  address_verbatim?: string | null;
  address?: string | null;
  validated_postal_code?: string | null;
  country?: string | null;
  status: 'active' | 'on_hold' | 'banned';
  points_earned: number;
  delivery_regions: DeliveryRegion[];
}

// Equivalent to Django Role
export interface Role extends BaseAbstractModel {
  name: string;
  level: number;
}

// Equivalent to Django DeliveryRegion
export interface DeliveryRegion extends BaseAbstractModel {
  name: string;
  description?: string | null;
}

// Equivalent to Django Branch
export interface Branch extends BaseAbstractModel {
  id: string; // UUID
  display_name: string | null;
  delivery_regions: DeliveryRegion[];
  pickup_locations: string | null;
  frequency_of_requests: string;
  spay_neuter_requirement: boolean;
  pets_per_household_max: number;
  delivery_deadline_days: number;
  delivery_type: 'drop_off' | 'pick_up';
  delivery_pickup_details: string | null;
  blurb: string | null;
  blurb_image: string | null; // URL of the image
  latitude: number | null;
  longitude: number | null;
  delivery_radius: number | null;
  hidden: boolean;
  operational: boolean;

  // Fields from PhysicalLocationMixin
  location_name: string;
  address_line1: string | null;
  address_line2: string | null;
  city: string | null;
  state_or_province: string | null;
  postal_code: string | null;
  country: string | null;
  ext_id: string | null;
}

// Equivalent to Django FoodAvailable
export interface FoodAvailable extends BaseAbstractModel {
  branch: Branch;
  food_item: FoodItem;
  available_from: Date;
  available_to: Date | null;
  is_available: boolean;
}

export interface FoodRequest extends BaseAbstractModel {
  user: number; // Foreign key to User
  branch: number | null; // Foreign key to Branch
  address_text: string | null;
  address_google_place_id: string | null;
  address_canadapost_id: string | null;
  address_latitude: number | null;
  address_longitude: number | null;
  address_buildingtype: string; // Assuming this is a string representation of BUILDING_TYPE_CHOICES
  address_details: Record<string, unknown>; // JSONField
  contact_phone: string; // Assuming this is a string representation of a phone number
  contact_email: string;
  contact_name: string;
  method_of_contact: string;
  pet_details: Record<string, unknown>; // JSONField
  safe_drop_agree: boolean | null;
  safe_drop_instructions: string | null;
  confirm_correct: boolean | null;
  accept_terms: boolean | null;
  flagged: boolean;
  date_requested: string; // Assuming this is a string representation of a date
  status: string; // Assuming this is a string representation of STATUS_CHOICES
  comments: Record<string, unknown>; // JSONField
}
