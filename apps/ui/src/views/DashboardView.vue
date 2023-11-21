<template>
    <div>
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="sm:flex sm:items-center">
                <div class="sm:flex-auto">
                    <h1 class="text-base font-semibold leading-6 text-gray-900">Requests</h1>
                    <p class="mt-2 text-sm text-gray-700">A list of all open requests ready to be delivered in your area.</p>
                </div>
                <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
                    <button type="button"
                    class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
                    Contact branch manager</button>
                </div>
            </div>
        </div>
        <div class="mt-8 flow-root overflow-hidden">
            <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                <table class="w-full text-left">
                    <thead class="bg-white">
                        <tr>
                            <th scope="col"
                            class="relative isolate py-3.5 pr-3 text-left text-sm font-semibold text-gray-900">
                            Name
                            <div class="absolute inset-y-0 right-full -z-10 w-screen border-b border-b-gray-200" />
                            <div class="absolute inset-y-0 left-0 -z-10 w-screen border-b border-b-gray-200" />
                        </th>
                        <th scope="col"
                        class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 sm:table-cell">Email</th>
                        <th scope="col"
                        class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 sm:table-cell">Pets
                    </th>
                    <th scope="col"
                    class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 md:table-cell">Location
                </th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Contact via</th>
                <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Status</th>
                <th scope="col" class="relative py-3.5 pl-3">
                    <span class="sr-only">View</span>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="person in people" :key="person.email">
                <td class="relative py-4 pr-3 text-sm font-medium text-gray-900">
                    {{ person.name }}
                    <div class="absolute bottom-0 right-full h-px w-screen bg-gray-100" />
                    <div class="absolute bottom-0 left-0 h-px w-screen bg-gray-100" />
                </td>
                <td class="hidden px-3 py-4 text-sm text-gray-500 sm:table-cell">{{ person.email }}</td>
                <td class="hidden px-3 py-4 text-sm text-gray-500 md:table-cell">{{ person.pets }}</td>
                <td class="px-3 py-4 text-sm text-gray-500">{{ person.location }}</td>
                <td class="px-3 py-4 text-sm text-gray-500">{{ person.contact_method }}</td>
                <td class="px-3 py-4 text-sm text-gray-500">{{ person.status }}</td>
                <td class="relative py-4 pl-3 text-right text-sm font-medium">
                    <a href="#" class="text-indigo-600 hover:text-indigo-900">View<span class="sr-only">, {{
                        person.name }}</span></a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</div>
</template>

<script lang="ts" setup>
const people = [

{
    name: 'Lyndsai',
    email: 'lyndsai.walton@example.com',
    pets: '2 dogs (Spence, Ruffles), 1 cat (Marble)',
    location: 'Upper Crawford area',
    contact_method: 'Email',
    status: 'Open',
},
{
    name: 'Johne',
    email: 'johne.doe@example.com',
    pets: '1 dog (Max), 2 cats (Bella, Kitty)',
    location: 'Downtown area',
    contact_method: 'Phone',
    status: 'Open',
},
{
    name: 'Janel',
    email: 'janel.doe@example.com',
    pets: '2 dogs (Buddy, Daisy)',
    location: 'Eastside area',
    contact_method: 'Email',
    status: 'Closed',
},
{
    name: 'Redecca',
    email: 'redecca.builder@example.com',
    pets: '1 cat (Whiskers)',
    location: 'Westside area',
    contact_method: 'Phone',
    status: 'Open',
},
];

</script>
