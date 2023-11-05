<template>
    <div class="home">
        This is make a request
        <NewRequestForm />
    </div>
</template>

<script lang="ts">
// @ is an alias to /src
import NewRequestForm from '@/components/NewRequestForm.vue';

export default {
    name: 'MakeRequestView',
    components: {
        NewRequestForm
    },
      mounted() {
        if (!window.google) {
            var s = document.createElement('script');
            s.type = 'text/javascript';
            s.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyCQxLo0EWIz7enLLTisXadzbGf01qbzY5A`;
            var x = document.getElementsByTagName('script')[0];
            x.parentNode.insertBefore(s, x);
            // We cannot access google.maps until it's finished loading
            s.addEventListener('load', e => {
                this.initMap(); // call your init map function here
            })
        } else {
            this.initMap(); // call your init map function here
        }
    },
    methods: {
        initMap() {
            // your code to initialize map
        }
    }
}
</script>
