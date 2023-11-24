// vueform.config.js

/**
 *
 * The csrfRequest option is an endpoint object that is used to submit
 * an intermediate request to the server if an initial request returns
 * 401 or 419. The original request will be retried once after receiving
 * a response from csrfRequest endpoint.
 *
 * The onUnauthenticated option is a function that is called if the
 * request still returns 401 or 419 after calling csrfRequest and
 * repeating the original request.
 *
 * See: https://vueform.com/reference/configuration#axios
 */

import en from "@vueform/vueform/locales/en";
import tailwind from "@vueform/vueform/themes/tailwind";
import axios from "axios";
const base_url = import.meta.env.VITE_BASE_URL;

export default {
  theme: tailwind,
  locales: { en },
  locale: "en",

  axios,

  endpoints: {
    unique: {
      url: "/api/users/prove_unique/",
      method: "POST",
    },
  },

  // axios: {
  //   withCredentials: true,
  //   xsrfCookieName: 'csrftoken',
  //   xsrfHeaderName: 'x-csrftoken',
  //   baseURL: base_url,
  //   csrfRequest: {
  //     method: 'get',
  //     url: '/csrf-cookie',
  //   },
  //   onUnauthenticated() {
  //     location.href = '/login'
  //   },
  // },
};
