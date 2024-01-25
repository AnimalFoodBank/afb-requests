<!-- RegistrationVueform.vue -->
<template>
  <Vueform :ref="form$" :display-errors="true" :display-messages="true" :float-placeholders="false" endpoint="/api/accounts/register/" validate-on="change|step" @error="handleErrorResponse" @success="handleSuccessResponse">
    <template #empty>
      <FormErrors />
      <FormMessages />

      <FormSteps>
        <FormStep name="account" :elements="['email', 'name', 'terms_agreement']" :buttons="{ previous: false }">Account</FormStep>
        <FormStep name="pets" :elements="['pet1', 'pet2', 'pet3', 'pet4']">Pets</FormStep>
        <FormStep name="contacts" :elements="['phone', 'address']">Contacts</FormStep>
      </FormSteps>

      <FormElements>
        <TextElement name="email" label="Email address" placeholder="abc@example.com" rules="required|email" default="a@b.com" />
        <TextElement name="name" info="Full name, first name or a nickname" label="Your name" placeholder="e.g. Elrik M" :rules="['required']" default="DM" />
        <CheckboxElement name="terms_agreement" text="Accept our Terms of Use & Privacy Policy" :rules="['required']" default="true"/>

        <TextareaElement :autogrow="true" placeholder="Dog/cat/etc, Name, Size, Date of Birth" name="pet1" label="Pet details" :rules="[]" default="Dog" />
        <TextareaElement :autogrow="true" name="pet2" label="Pet details (2 of 4)" />
        <TextareaElement :autogrow="true" name="pet3" label="Pet details (3 of 4)" />
        <TextareaElement :autogrow="true" name="pet4" label="Pet details (4 of 4)" />

        <TextElement name="phone" label="Phone number" :rules="[]" />
        <TextareaElement name="address" label="Address" :rules="[]" />
      </FormElements>

      <FormStepsControls :labels="false">
        <template #previous><button class="flex"><ArrowLeftIcon class="h-6 w-6 ml-0 mr-1 text-100" /> Previous</button></template>
        <template #next><button class="flex">Next <ArrowRightIcon class="h-6 w-6 ml-1 mr-0 text-100" /></button></template>
        <template #finish><button class="flex">Register <CheckIcon class="h-6 w-6 ml-1 mr-0 text-100" /></button></template>
      </FormStepsControls>
    </template>
  </Vueform>
</template>

<script setup lang="ts">
import { ArrowLeftIcon, ArrowRightIcon, CheckIcon } from '@heroicons/vue/20/solid';
import { VueformComponent } from '@vueform/vueform';
import { AxiosError, AxiosResponse } from 'axios';


const handleSuccessResponse = (response: AxiosResponse, form$: VueformComponent) => {
  console.log('RegisterView: handleSuccessResponse', response, form$);

  form$.messageBag.clear();
  // debugger;

  // TODO: Redirect to the dashboard
  form$.messageBag.append('Your account has been created successfully.');

};

const handleErrorResponse = (err: AxiosError, details: object, form$: any) => {
  console.log('RegisterView: handleErrorResponse', err, form$);
  const response = err.response;
  form$.messageBag.clear();
  // debugger;

  if (!response) {
    console.log('RegisterView: handleErrorResponse (no response)', err);
    return;
  }

  if (response.status >= 500) {
    console.log('RegisterView: handleErrorResponse (server error)', err);

    // Definitely don't show the server error. Esp since 500 errors in Django
    // are by default regular HTML rather than JSON, even when using DRF.
    //
    form$.messageBag.append('Server error. Please try again later.');
    return;
  }

  // Add the response errors to the form, by key and value
  if (response.data) {
    console.log('RegisterView: handleErrorResponse (response)', response);

      // Iterate over the response data, and add the errors to the form message bag
    for (let [key, value] of Object.entries(response.data)) {
      // console.log(`${key}: ${value}`);
      form$.messageBag.append(`${key}: ${value}`);
    }

  }

};


interface Props {
  foo: string
  bar?: number
}

const props = defineProps<Props>();
</script>
