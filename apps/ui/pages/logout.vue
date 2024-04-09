
<template>

</template>

<script setup lang="ts">

definePageMeta({
  auth: true,
});


const {
  status,
  data,
  token,
  lastRefreshedAt,
  getSession,
  signUp,
  signIn,
  signOut,
} = useAuth();

const toast = useToast()

onMounted(() => {

  const ret = signOut({
    callbackUrl: '/',
  });

  toast.add({
      id: 'signed_out',
      title: 'Signed Out.',
      description: 'You are now logged out.',
      icon: 'i-heroicons-',
      timeout: 5000,
    })

});

</script>
