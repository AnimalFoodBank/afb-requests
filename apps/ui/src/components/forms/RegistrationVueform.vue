<!-- RegistrationVueform.vue -->
<template>
  <Vueform ref="form$" :display-errors="false" :float-placeholders="false" endpoint="/api/accounts/register/" validate-on="change|step" @error="handleErrorResponse" @success="handleSuccessResponse">
    <template #empty>
      <div class="mb-10 w-full">
        <FormErrors v-if="hasErrors" />
        <FormMessages v-if="showErrors" />
      </div>

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

        <!-- <TextElement input-type="password" name="password" label="Password" :rules="['required']" /> -->
      </FormElements>

      <FormStepsControls :labels="false">
        <template #previous><button class="flex"><ArrowLeftIcon class="h-6 w-6 ml-0 mr-1 text-100" /> Previous</button></template>
        <template #next><button class="flex">Next <ArrowRightIcon class="h-6 w-6 ml-1 mr-0 text-100" /></button></template>
        <template #finish><button class="flex">Finish <CheckIcon class="h-6 w-6 ml-1 mr-0 text-100" /></button></template>
      </FormStepsControls>
    </template>
  </Vueform>
</template>

<script setup lang="ts">
import { ArrowLeftIcon, ArrowRightIcon, CheckIcon } from '@heroicons/vue/20/solid';
import { VueformComponent } from '@vueform/vueform';
import { AxiosError, AxiosResponse } from 'axios';

// const form$ = ref<any>(null);

// const newUserModel = ref<any>(null);
// const hasErrors = reactive({ value: false })

const handleSuccessResponse = (response: AxiosResponse, form$: VueformComponent) => {
  console.log('RegisterView: handleSuccessResponse', response, form$);
  debugger;
};

const handleErrorResponse = (err: AxiosError, details: object, form$: any) => {
  console.log('RegisterView: handleErrorResponse', err, form$);
  const response = err.response;
  if (response) {
    console.log('RegisterView: handleErrorResponse (response)', response);
    form$.messageBag.append(response.data);
  }
  debugger;
};


interface Props {
  foo: string
  bar?: number
}

const props = defineProps<Props>()
</script>
