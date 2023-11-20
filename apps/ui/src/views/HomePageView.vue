
<template>
  <!--
      This example requires updating your template:

      ```
      <html class="h-full bg-gray-50">
      <body class="h-full">
        ```
      -->

  <div class="flex min-h-full flex-1">


    What Is The Animal Food Bank?
  We are a volunteer-operated, non-funded non-profit providing pet food and supplies to pets in need. We do this through our own pet food bank program, as well as by providing pet food and supplies to other organizations helping pets in need.

  We believe in collaboration over competition, and are disrupting the sector to challenge organizations to think, and do, differently. We make access to food easy – not only for our food bank clients, but for our partner organizations. Having donated more than 300,000 lbs of food to partner organizations across Western Canada, we set the example of how collaboration works.

  We are the ONLY pet food bank in Canada operating across provincial borders, and without funding, we rely on the generosity and support of our communities to help ensure no pet goes hungry, and no pet guardian is faced with surrendering their pet due to a lack of pet food.

  </div>
</template>

<script setup lang="ts">
import router from '../router';

let requiresAuth = router.currentRoute.value.meta.requiresAuth;
console.log("HomePageView requires authentication: ${requiresAuth}");


</script>

<style scoped>
</style>
