import {defineStore} from 'pinia'
import { type Ref, ref, reactive } from "vue";

export const useUserStore = defineStore("auth", () => {
  const is_authenticated = ref(false);
  const isLoading = ref(false);
  const persist = ref(true); // TODO: Double check this
  const state = reactive({
    // user: "",
    bearerToken: "",
  });

  async function login(email: string, password: string) {

    state.bearerToken = "1234567890";
  }

  async function logout() {
    isLoading.value = true;

    // Check if the email is already in use
    try {
      await axios.post("login", {
        email: email,
        password: password,
      });
      await getUser();
      $bus.$emit(eventTypes.logged_in);
      return true;
    } catch (error) {
      return false;
    } finally {
      isLoading.value = false;
    }
    state.bearerToken = null;
  }

  async function is_authenticated() {
    return !!state.bearerToken;
  }


};

export const authStore = defineStore('auth', {
  state: () => ({
    token: ''
  }),
  getters: {

  },
  actions: {
    login(token: string) {
      this.token = token
    },
    logout() {
      this.token = ''
    },
  },
  persist: true
})

// The userEmail is meant for keeping email state across auth pages, for example when going from login to forgot-password page
const userEmail = ref(null) as Ref<string | null>;

  /**
   * Log in the user
   *
   * @param {string} email
   * @param {string} password
   * @return {*}
   */
  async function login(email: string, password: string) {
    // Check if the email is valid
    if (!email) {
      return false;
    }

    // Check if the password is valid
    if (!password) {
      return false;
    }

    isLoading.value = true;

    // Check if the email is already in use
    try {
      await axios.post("login", {
        email: email,
        password: password,
      });
      await getUser();
      $bus.$emit(eventTypes.logged_in);
      return true;
    } catch (error) {
      return false;
    } finally {
      isLoading.value = false;
    }
  }

/**
* Get the user
*
*/
async function getUser() {
  isLoading.value = true;
  try {
    const response = await axios.get("api/user");
    user.value = response.data;
    isAuthenticated.value = true;
    await getCsrfToken();
  } catch (error) {
    console.log(error);
  } finally {
    attemptedToFetchUser.value = true;
    isLoading.value = false;
  }
}
