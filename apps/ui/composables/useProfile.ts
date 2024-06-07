import { createSharedComposable } from '@vueuse/core'

const _useProfile = () => {
  const route = useRoute()
  const router = useRouter()

  /**
   * Retrieves the authentication status, data, and token using the useAuth() function.
   *
   * @returns {{
   *   status: string,
   *   data: any,
   *   token: string
   * }} The authentication status, data, and token.
  */
  const {
    status: authStatus,
    data: authData,
    token: authToken,
    lastRefreshedAt,
  } = useAuth();


  const userInfo = authData?.value || {}
  const profileInfo = userInfo.profiles?.[0] || {}

  // console.log('authData', userInfo)
  // console.log('profile', profileInfo)

  return {
    userInfo,
    profileInfo,
    authStatus,
    authToken,
    lastRefreshedAt,
  }
}

export const useProfile = createSharedComposable(_useProfile)
