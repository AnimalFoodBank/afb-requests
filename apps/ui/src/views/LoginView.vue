<!--
  This example requires some changes to your config:

  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<template>
    <!--
        This example requires updating your template:
@submit="handleLogin" :validation-schema="schema"
        <html class="h-full bg-gray-50">
        <body class="h-full">
        ```
      -->
    <div class="flex min-h-full flex-1 flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <HomeIcon class="mx-auto h-10 w-auto" />

            <h2 class="mt-6 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account
            </h2>
        </div>

        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[480px]">
            <div class="bg-white px-6 py-12 shadow sm:rounded-lg sm:px-12">
                <form class="space-y-6" @submit="handleLogin" :validation-schema="schema">
                    <div>
                        <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                        <div class="mt-2">
                            <input id="email" name="email" type="email" autocomplete="email" required=""
                                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                        </div>
                    </div>

                    <div>
                        <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                        <div class="mt-2">
                            <input id="password" name="password" type="password" autocomplete="current-password" required=""
                                   class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                        </div>
                    </div>

                    <div class="flex items-center justify-between">
                        <div class="flex items-center">
                            <input id="remember-me" name="remember-me" type="checkbox"
                                   class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                            <label for="remember-me" class="ml-3 block text-sm leading-6 text-gray-900">Remember me</label>
                        </div>

                        <div class="text-sm leading-6">
                            <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
                        </div>
                    </div>

                    <div>
                        <button type="submit"
                                class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
                    </div>
                </form>

        </div>

        <p class="mt-10 text-center text-sm text-gray-500">
            Not a member?
            {{ ' ' }}
            <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"></a>
        </p>
    </div>
</div></template>

<script lang="ts">
import { HomeIcon } from '@heroicons/vue/20/solid';

export default {
    name: 'LoginView',
    components: {
        HomeIcon
    },
    computed: {
        loggedIn() {
            // return this.$store.state.auth.status.loggedIn;
        },
    },
    created() {
        // if (this.loggedIn) {
        //     this.$router.push("/profile");
        // }
    },
    methods: {
        handleLogin(user) {
            this.loading = true;

            // this.$store.dispatch("auth/login", user).then(
            //     () => {
            //         this.$router.push("/profile");
            //     },
            //     (error) => {
            //         this.loading = false;
            //         this.message =
            //             (error.response &&
            //                 error.response.data &&
            //                 error.response.data.message) ||
            //             error.message ||
            //             error.toString();
            //     }
            // );
        }
    },
    data() {
        return {
            loading: false,
            message: "",
            schema: {
                email: {
                    required: true,
                    email: true,
                    max: 255,
                },
                password: {
                    required: true,
                    min: 6,
                    max: 255,
                },
            },
        };
    },
}
</script>

<style scoped>
</style>
