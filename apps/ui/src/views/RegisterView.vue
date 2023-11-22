
<script setup lang="ts">
import { ArrowLeftIcon, ArrowRightIcon, CheckIcon, HomeIcon } from '@heroicons/vue/20/solid';


// @see List of icons: https://unpkg.com/browse/@heroicons/vue@2.0.18/24/outline/
</script>

<template>
  <div class="flex min-h-full flex-1">
    <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <div>
          <router-link :to="{ name: 'DashboardView' }">
            <HomeIcon class="h-10 w-full" />
          </router-link>
          <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Client Registration</h2>
          <p class="mt-2 text-sm leading-6 text-gray-500">
            Already registered?
            &nbsp;
            <router-link :to="{ name: 'LoginView' }" class="font-semibold text-indigo-600 hover:text-indigo-500"> Login
            </router-link>
          </p>
        </div>

        <div class="mt-10">

          <!--

            @see https://vueform.com/docs/breaking-forms-into-steps
          -->
          <Vueform :float-placeholders="true">
            <template #empty>
              <FormSteps>
                <FormStep name="account" :elements="['email', 'name', 'terms_agreement']" :buttons="{
                  previous: false
                }">Account</FormStep>
                <FormStep name="pets" :elements="['pet1', 'pet2', 'pet3', 'pet4']">Pets</FormStep>
                <FormStep name="contacts" :elements="['phone', 'address', 'password']">Contacts</FormStep>
              </FormSteps>

              <FormElements>
                <TextElement name="email" description="Lorem ipsum dolor sit amet" label="Email" placeholder="abc@example.com" :rules="['required', 'email']"  />
                <TextElement name="name" info="Full name, first name or a nickname" label="Your Name" :rules="['required']" />
                <CheckboxElement name="terms_agreement" text="Accept our Terms of Use & Privacy Policy" :rules="['required']" />

                <TextareaElement :autogrow="true" placeholder="Dog/cat/etc, Name, Size, Date of Birth" name="pet1" label="Pet details" :rules="['required']" />
                <TextareaElement :autogrow="true" name="pet2" label="Pet details (2 of 4)" />
                <TextareaElement :autogrow="true" name="pet3" label="Pet details (3 of 4)" />
                <TextareaElement :autogrow="true" name="pet4" label="Pet details (4 of 4)" />

                <TextElement name="phone" label="Phone number" :rules="['required']" />
                <TextareaElement name="address" label="Address" :rules="['required']" />


                <TextElement input-type="password" name="password" label="Password" :rules="['required']" />
              </FormElements>

              <FormStepsControls :labels="false">

                <template #previous><div class="flex"><ArrowLeftIcon class="h-6 w-6 ml-0 mr-1 text-100" /> Previous</div></template>
                <template #next><div class="flex">Next <ArrowRightIcon class="h-6 w-6 ml-1 mr-0 text-100" /></div></template>
                <template #finish><div class="flex">Finish <CheckIcon class="h-6 w-6 ml-1 mr-0 text-100" /></div></template>
              </FormStepsControls>
            </template>
          </Vueform>

        </div>

      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block">
      <!-- <CatHeartImage class="absolute inset-0 h-full w-full object-cover" /> -->
      <img class="h-800" alt="Become an AFB member today" src='@/assets/img/Dog-Sideways-Glare-1024x1024.png'>

    </div>
  </div>
</template>


<style scoped>
</style>

<!--

  Available Validation Rules
  @see https://vueform.com/docs/validating-elements#available-validation-rules

  Accepted
  Active URL
  After (Date)
  After Or Equal (Date)
  Alpha
  Alpha Dash
  Alpha Numeric
  Array
  Before (Date)
  Before Or Equal (Date)
  Between
  Boolean
  Confirmed
  Date
  Date Equals
  Date Format
  Different
  Digits
  Digits Between
  Dimensions (Image Files)
  Distinct
  Email
  Exists (Database)
  File
  Filled
  Greater Than
  Greater Than Or Equal
  Image
  In
  In Array
  Integer
  IP Address
  IPv4
  IPv6
  JSON
  Less Than
  Less Than Or Equal
  Max
  MIME Types
  MIME Types By File Extension
  Min
  Not In
  Not Regex
  Nullable
  Numeric
  Regular Expression
  Required
  Same
  Size
  String
  Timezone
  Unique (Database)
  URL
  UUID

-->
