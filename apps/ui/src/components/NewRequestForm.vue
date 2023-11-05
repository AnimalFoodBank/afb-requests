<template>
    <div class="bg-white rounded-lg p-10 max-w-lg shadow-box-circle">
        <form class="w-full">
            <FormElements>

                <div class="text-xl mb-4 col-span-12">
                    <div class="border-b border-gray-300 pb-2">Basic data</div>
                </div>

                <!-- Position name -->
                <TextElement name="title" label="Position name"
                             description="Name the position (eg. Marketing intern, IT fresh graduate program)"
                             rules="required" />

                <!-- Place of work -->
                <GroupElement name="location_wrapper" label="Place of work">
                    <LocationElement name="location" floating="Address of the work"
                                     placeholder="Add the exact address of the work" provider="google" rules="required"
                                     :conditions="[
                                         ['location_wrapper.default_location', false]
                                     ]" />
                    <CheckboxElement name="default_location" add-class="-mt-2">
                        The place of work is the same as in your company profile:
                        <div class="text-gray-500 text-sm italic">{{ companyAddress }}</div>
                    </CheckboxElement>
                </GroupElement>

                <!-- Job type -->
                <RadiogroupElement name="job_type" label="Job type" rules="required"
                                   :items="['Internship', 'Graduate', 'Voluntary', 'Junior']" :override-classes="{
                                       RadiogroupElement: {
                                           wrapper: 'grid grid-flow-col grid'
                                       }
                                   }">
                    <!-- Custom radio template -->
                    <template v-slot:radio="{ items, index, item, value, el$, classes, isDisabled, id, name }">
                        <div class="flex items-center justify-center border py-1.5 w-full bg-white" :class="{
                            'border-r-0': index < Object.keys(items).length - 1,
                            'rounded-l-md': index === 0,
                            'rounded-r-md': index === Object.keys(items).length - 1,
                            'bg-green-500 text-white border-green-400': el$.value == value,
                            'border-gray-300': el$.value != value,
                            'opacity-50': isDisabled,
                        }">
                            <input type="radio" v-model="el$.model" :value="value" class="hidden" :name="name" :id="id"
                                   :disabled="isDisabled" />
                            <span :class="classes.text" v-html="item.label" />
                        </div>
                    </template>
                </RadiogroupElement>

                <!-- Job categories -->
                <TagsElement name="categories" label="Job categories" rules="required|max:3" description="Select up to 3"
                             :search="true" :items="job_categories" />

                <!-- Working hours -->
                <SliderElement name="work_hours" label="Required minimum weekly working hours" :default="20" :min="1"
                               :max="40" :format="v => v > 1 ? `${Math.round(v)} hours` : '1 hour'" :add-classes="{
                                   ElementLayout: {
                                       innerWrapper: 'mt-12'
                                   }
                               }" />

                <!-- Payment -->
                <GroupElement name="salary_settings" label="Payment">
                    <SelectElement name="has_salary" placeholder="Select" floating="Salary" rules="required" :native="false"
                                   :can-clear="false" :items="{ 1: 'Paid', 0: 'Unpaid' }" :columns="{
                                       xs: 12, sm: 12, md: 3, lg: 3
                                   }" />
                    <TextElement name="salary" placeholder="Amount" rules="integer" :can-clear="false" :conditions="[
                        ['salary_settings.has_salary', 1]
                    ]" :columns="{
    xs: 12, sm: 12, md: 3, lg: 3
}" />
                    <SelectElement name="salary_currency" default="usd" :native="false" :can-clear="false" :items="{
                        usd: 'USD',
                        eur: 'EUR'
                    }" :conditions="[
    ['salary_settings.has_salary', 1]
]" :columns="{
    xs: 12, sm: 12, md: 3, lg: 3
}" />
                    <SelectElement name="salary_period" default="weekly" :native="false" :can-clear="false" :items="{
                        hourly: '/ hour',
                        daily: '/ day',
                        weekly: '/ week',
                        monthly: '/ month'
                    }" :conditions="[
    ['salary_settings.has_salary', 1]
]" :columns="{
    xs: 12, sm: 12, md: 3, lg: 3
}" />
                </GroupElement>

                <div class="text-xl mb-4 mt-8 col-span-12">
                    <div class="border-b border-gray-300 pb-2">Schedule</div>
                </div>

                <!-- Application deadline -->
                <DateElement name="application_deadline" label="Application deadline" rules="required" :conditions="[
                    ['continuous_application', false]
                ]" />
                <CheckboxElement name="continuous_application" text="Can apply continuously" add-class="-mt-2" />

                <!-- Job period -->
                <GroupElement name="job_period">
                    <!-- Job start -->
                    <GroupElement name="job_start_group" label="Start date" :columns="6">
                        <DateElement name="job_start_date" rules="required"
                                     :conditions="[['job_period.job_start_group.job_start_immediate', false]]" />

                        <CheckboxElement name="job_start_immediate" text="Immediately" add-class="-mt-2" />
                    </GroupElement>

                    <!-- Job end -->
                    <GroupElement name="job_end_group" label="End of work" :columns="6">
                        <DateElement name="job_end_date" rules="required"
                                     :conditions="[['job_period.job_end_group.job_end_indefinite', false]]" />

                        <CheckboxElement name="job_end_indefinite" text="Indefinite" add-class="-mt-2" />
                    </GroupElement>
                </GroupElement>

                <div class="text-xl mb-4 mt-8 col-span-12">
                    <div class="border-b border-gray-300 pb-2">Requirements</div>
                </div>

                <!-- Languages -->
                <ListElement name="languages" label="Required language skills" :min="1">
                    <template #default="{ index }">
                        <ObjectElement :name="index">
                            <SelectElement name="language_id" placeholder="Language" rules="required" columns="6"
                                           :search="true" :items="langs" />
                            <SelectElement name="language_level" placeholder="Level" rules="required" columns="6" :items="{
                                25: 'Beginner',
                                50: 'Intermediate',
                                75: 'Advanced',
                                100: 'Native'
                            }" />
                        </ObjectElement>
                    </template>
                </ListElement>

                <!-- Student status -->
                <CheckboxElement name="student_status_required" label="Student status"
                                 text="Student status is required for the job" :trueValue="1" :falseValue="0" />

                <!-- Degree -->
                <CheckboxElement name="degree" label="Degree" text="Degree is required for work" :trueValue="1"
                                 :falseValue="0" />
                <SelectElement name="degree_requirement" placeholder="Degree level" :native="false" :columns="{
                    lg: 5, sm: 6
                }" :items="{
    50: 'BA/BSc',
    75: 'MA/MSc',
    100: 'PhD'
}" :conditions="[
    ['degree', 1]
]" />

                <!-- Professional skills -->
                <TagsElement name="professional_skills" label="Professional skills" description="Choose as many as you can"
                             :close-on-select="false" :create="true" :items="professional_skills" />

                <!-- Computer skills -->
                <TagsElement name="computer_skills" label="Computer skills" description="Choose as many as you can"
                             :close-on-select="false" :create="true" :items="computer_skills" />

                <!-- Soft skills -->
                <TagsElement name="soft_skills" label="Competences, soft skills" description="Choose as many as you can"
                             :close-on-select="false" :create="true" :items="soft_skills" />

                <div class="text-xl mb-4 mt-8 col-span-12">
                    <div class="border-b border-gray-300 pb-2">Job description</div>
                </div>

                <!-- Description -->
                <EditorElement name="description" label="Position description, tasks" />

                <!-- Requirements -->
                <EditorElement name="requirements" label="Requirements" />

                <!-- Offer -->
                <EditorElement name="offer" label="What we offer" />

                <div class="text-xl mb-4 mt-8 col-span-12">
                    <div class="border-b border-gray-300 pb-2">How to apply</div>
                </div>


                <!--  -->
                <RadioElement name="internal_application" radio-name="application_type"
                              text="<b>Recommended</b>: Apply with profile"
                              description="Select this if you want to rely on our internal application tracking system" />

                <!-- Internal application -->
                <GroupElement name="feedback" label="Auto reply message for applicants"
                              :conditions="[['internal_application', true]]">
                    <template #before>
                        <div class="text-sm text-gray-500 mb-2">
                            Here you can write messages in advance you would like to send out to applicants when you accept
                            or reject their application.
                        </div>
                    </template>

                    <!-- Internal application feedback -->
                    <div class="flex ml-2 -mb-2 col-span-12">
                        <div class="px-4 py-2 cursor-pointer" :class="{ 'text-green-500': feedback == 'accept' }"
                             @click="feedback = 'accept'">Successful</div>
                        <div class="px-4 py-2 cursor-pointer" :class="{ 'text-green-500': feedback == 'reject' }"
                             @click="feedback = 'reject'">Unsuccessful</div>
                    </div>
                    <EditorElement v-show="feedback == 'accept'" name="accept_feedback"
                                   placeholder="Successful application message"
                                   default="Congratulations! You're application has been accepted. We'll contact you soon."
                                   rules="required" />
                    <EditorElement v-show="feedback == 'reject'" name="reject_feedback"
                                   placeholder="Unsuccessful application message"
                                   default="Unfortunately you haven't been selected in round. We wish you the best of luck next time!"
                                   rules="required" />
                </GroupElement>

                <!-- External application -->
                <RadioElement name="external_application" radio-name="application_type"
                              text="Forward candidates to an external site"
                              description="Select this if you want to rely on an external application tracking system" />

                <!-- External link -->
                <TextElement name="external_url" label="Add link" field-name="Link"
                             placeholder="eg. https://yourcompany.com/job-title" rules="required|url" add-class="-mt-4"
                             :conditions="[
                                 ['external_application', true]
                             ]" />

                <div class="text-xl mb-4 mt-8 col-span-12">
                    <div class="border-b border-gray-300 pb-2">Pictures and videos</div>
                </div>

                <!-- Cover -->
                <GroupElement name="cover_container" label="Cover image">
                    <FileElement name="cover" view="image"
                                 description="This is the first image job seekers will see at the top of your ad. Use a high quality image. Recommended image size: 1640x720px (Similar to <a href='https://blog.snappa.com/facebook-cover-photo-size/' target='_blank' rel='nofollow noopener'>Facebook cover photo</a> size)"
                                 accept=".jpg,.png,.gif" rules="required" :conditions="[
                                     ['cover_container.default_cover', false]
                                 ]" :file="{
    rules: 'required|max:4096'
}" />
                    <CheckboxElement name="default_cover" add-class="-mt-2">
                        Use the cover image provided in your company profile
                    </CheckboxElement>
                </GroupElement>

                <!-- Gallery -->
                <MultifileElement name="gallery" label="Image gallery (optional)" accept=".jpg, .png, .gif" view="gallery"
                                  rules="max:8" :sort="true" :image="true" :file="{ rules: 'required|max:4096' }" />

                <!-- Youtube links -->
                <ListElement name="youtubes" label="Youtube Video (Optional)">
                    <template #default="{ index }">
                        <TextElement :name="index"
                                     description="Copy your Youtube video <b>ID</b> . Ex: https://www.youtube.com/watch?v= <b>welpvNwbw0E</b>"
                                     field-name="ID" rules="size:11" @change="(value) => {
                                         handleYoutubeInsert(value, index)
                                     }">
                            <template #addon-before>
                                <div class="whitespace-nowrap">https://www.youtube.com/watch?v=</div>
                            </template>
                        </TextElement>
                    </template>
                </ListElement>

                <div class="col-span-12">
                    <div class="border-t border-gray-300 pt-10 mt-6"></div>
                </div>

                <!-- Submit button -->
                <ButtonElement submits name="submit" button-label="Submit" button-class="vf-btn-primary" />

            </FormElements>
        </form>
    </div>
</template>

<script lang="ts">

import { Vueform, useVueform } from '@vueform/vueform'

export default {
    name: 'ComplexForm',
    mixins: [Vueform],
    setup: useVueform,
    data() {
        return {
            vueform: {
                addClasses: {
                    ElementLabel: {
                        container: 'font-semibold mb-2'
                    },
                },
            },
            feedback: 'accept',
            job_categories: [],
            professional_skills: [],
            computer_skills: [],
            soft_skills: [],
            langs: [],
        }
    },
    computed: {
        companyAddress() {
            return '1600 Amphitheatre Parkway in Mountain View, California, United States'
        }
    },
    methods: {
        handleYoutubeInsert(value, index) {
            let matched = value.match(/^.*(?:(?:youtu\.be\/|v\/|vi\/|u\/\w\/|embed\/)|(?:(?:watch)?\?v(?:i)?=|\&v(?:i)?=))([^#\&\?]*).*/)

            if (matched && matched[1] && value != matched[1]) {
                this.el$(`youtubes.${index}`).update(matched[1].trim())
            }
        }
    },
    mounted() {
        // Setting items' data
        ['job_categories', 'langs', 'professional_skills', 'computer_skills', 'soft_skills'].map((param) => {
            fetch(`/${param}.json`)
                .then(response => response.json())
                .then(data => this[param] = data)
        })
    }
}
</script>
