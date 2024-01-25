<script lang="ts">


export default {

}
</script>


<template>
  <Vueform>
    <StaticElement
      name="personal_title"
      content="Personal details"
      tag="h2"
    />
    <StaticElement
      name="divider"
      tag="hr"
    />
    <TextElement
      name="first_name"
      label="First name"
      :rules="[
        'required',
        'max:255',
      ]"
      :columns="{
        container: 6,
        label: 12,
        wrapper: 12,
      }"
      default="John"
    />
    <TextElement
      name="last_name"
      label="Last name"
      :rules="[
        'required',
        'max:255',
      ]"
      :columns="{
        container: 6,
        label: 12,
        wrapper: 12,
      }"
      default="Doe"
    />
    <TextElement
      name="display_name"
      label="Display name"
      :rules="[
        'required',
        'max:255',
        'alpha_num',
      ]"
      default="johndoe"
      :addons="{
        before: 'mydomain.com/',
      }"
    />
    <DateElement
      name="birthday"
      label="Date of birth"
      :rules="[
        'required',
      ]"
      default="1989-07-07"
      display-format="MMMM Do, YYYY"
      :columns="{
        container: 6,
      }"
    />
    <RadiogroupElement
      name="gender"
      :items="[
        'Male',
        'Female',
        'Other',
        'I prefer not to say',
      ]"
      label="Gender"
      :rules="[
        'required',
      ]"
    />
    <StaticElement
      name="contact_title"
      content="Contact details"
      tag="h2"
      top="2"
    />
    <StaticElement
      name="divider_1"
      tag="hr"
    />
    <TextElement
      name="email"
      input-type="email"
      :rules="[
        'required',
        'max:255',
        'email',
      ]"
      label="Email"
      :columns="{
        container: 6,
      }"
      default="john@doe.com"
    />
    <TextElement
      name="phone"
      input-type="tel"
      field-name="Phone"
      label="Phone"
      :columns="{
        container: 6,
      }"
      placeholder="optional"
      :floating="false"
    />
    <ObjectElement
      name="address"
    >
      <TextElement
        name="street"
        placeholder="Street"
        :rules="[
          'required',
          'max:255',
        ]"
        label="Address"
        default="123 Maple Street"
      />
      <TextElement
        name="city"
        :columns="{
          label: 12,
          wrapper: 12,
        }"
        :rules="[
          'required',
          'max:255',
        ]"
        placeholder="City"
        default="Anytown"
      />
      <SelectElement
        name="country"
        :search="true"
        :native="false"
        input-type="search"
        autocomplete="disabled"
        placeholder="Country"
        items="/json/countries.json"
        :columns="{
          container: 6,
        }"
        :rules="[
          'required',
        ]"
        default="US"
      />
      <SelectElement
        name="state"
        :search="true"
        :native="false"
        input-type="search"
        autocomplete="disabled"
        placeholder="State"
        items="/json/states.json"
        :conditions="[
          [
            'address.country',
            'in',
            [
              'US',
            ],
          ],
        ]"
        :columns="{
          container: 6,
        }"
        :rules="[
          'required',
        ]"
        default="PA"
      />
      <TextElement
        name="zip"
        :columns="{
          container: 6,
          label: 12,
          wrapper: 12,
        }"
        :rules="[
          'required',
          'max:255',
          'alpha_num',
        ]"
        placeholder="Zip"
        default="17101"
      />
    </ObjectElement>
    <StaticElement
      name="preferences_title"
      content="Preferences"
      tag="h2"
      top="2"
    />
    <StaticElement
      name="divider_2"
      tag="hr"
    />
    <SelectElement
      name="language"
      :search="true"
      :native="false"
      label="Language"
      input-type="search"
      autocomplete="off"
      items="/json/languages.json"
      :rules="[
        'required',
      ]"
      :columns="{
        container: 6,
      }"
      default="English"
    />
    <SelectElement
      name="currency"
      :search="true"
      :native="false"
      label="Currency"
      input-type="search"
      autocomplete="off"
      items="/json/currencies_with_symbol.json"
      :rules="[
        'required',
      ]"
      :columns="{
        container: 6,
      }"
      label-prop="code"
      value-prop="code"
      default="USD"
    />
    <CheckboxElement
      name="accessible_only"
      text="Show accessible accommodations only"
    />
    <StaticElement
      name="security_title"
      content="Security"
      tag="h2"
      top="2"
    />
    <StaticElement
      name="divider_3"
      tag="hr"
    />
    <ButtonElement
      name="reset_password"
      button-label="Send email to reset password"
      button-type="anchor"
      label="Password"
      description="To change your password, we need to send a reset link to your email address."
    />
    <ButtonElement
      name="close_sessions"
      button-label="Sign out"
      button-type="anchor"
      label="Active sessions"
      description="Selecting Sign out will sign you out from all devices except this one. This can take up to 10 minutes."
    />
    <ButtonElement
      name="delete_account"
      button-label="Sign out"
      button-type="anchor"
      description="Permanently delete your mydomain.com account."
      label="Delete account"
    />
    <StaticElement
      name="fellow_title"
      content="Fellow traveller"
      tag="h2"
      top="2"
    />
    <StaticElement
      name="divider_4"
      tag="hr"
    />
    <GroupElement
      name="fellow_travellers"
      before="Enter the person's name exactly as it's written on their passport or other official travel document.
<br><br>
It's important to enter a correct date of birth because these details can be used for booking or ticketing purposes.
<br><br>"
    >
      <GroupElement
        name="container"
        :conditions="[
          [
            'fellow_travellers.fellows',
            'not_empty',
          ],
        ]"
      >
        <StaticElement
          name="first_name"
          content="First name"
          :columns="{
            container: 4,
          }"
        />
        <StaticElement
          name="date_of_birth"
          content="Date of birth"
          :columns="{
            container: 4,
          }"
        />
        <StaticElement
          name="last_name"
          content="Last name"
          :columns="{
            container: 4,
          }"
        />
      </GroupElement>
      <ListElement
        name="fellows"
        add-text="+ Add another traveler"
        :initial="0"
      >
        <template #default="{ index }">
          <ObjectElement
            :name="index"
          >
            <TextElement
              name="first_name"
              :columns="{
                container: 4,
                label: 12,
                wrapper: 12,
              }"
              :rules="[
                'required',
              ]"
            />
            <TextElement
              name="last_name"
              :rules="[
                'required',
                'max:255',
              ]"
              :columns="{
                container: 4,
                label: 12,
                wrapper: 12,
              }"
            />
            <DateElement
              name="birthday"
              :rules="[
                'required',
              ]"
              :columns="{
                container: 4,
                label: 12,
                wrapper: 12,
              }"
              display-format="MMMM Do, YYYY"
            />
          </ObjectElement>
        </template>
      </ListElement>
    </GroupElement>
  </Vueform>
</template>
