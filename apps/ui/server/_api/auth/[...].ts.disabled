// file: ~/server/api/auth/[...].ts
import { NuxtAuthHandler } from '#auth'
import GoogleProvider from 'next-auth/providers/google'
import CredentialsProvider from 'next-auth/providers/credentials'

const runtimeConfig = useRuntimeConfig()

export default NuxtAuthHandler({
  /*
    * Secret used to encrypt the user's cookies/tokens.
    *
    * This is required and should be a secure random string, unique
    * to each environment this application runs in.
    *
    * NOTE: If this isn't set in production, throws an AUTH_NO_SECRET error.
    * In dev, it's just logged as a warning.
    *
    * @see https://sidebase.io/nuxt-auth/resources/errors

  */
  secret: runtimeConfig.AUTH_SECRET,

  providers: [
    // @ts-expect-error You need to use .default here for it
    // to work during SSR. May be fixed via Vite at some point
    GoogleProvider.default({
      clientId: runtimeConfig.public.AUTH_GOOGLE_CLIENT_ID,
      clientSecret: runtimeConfig.AUTH_GOOGLE_CLIENT_SECRET,
    }),

    CredentialsProvider.default({
      name: 'Credentials',
      authorize(credentials: any) {
        // You need to provide your own logic here that takes the credentials
        // submitted and returns either a object representing a user or value
        // that is false/null if the credentials are invalid.
        // NOTE: THE BELOW LOGIC IS NOT SAFE OR PROPER FOR AUTHENTICATION!

        const user = {
          email: 'test@email.com',
          password: 'pass',
        }

        if (
          credentials?.email === user.email &&
          credentials?.password === user.password
        ) {
          // Any object returned will be saved in `user` property of the JWT
          return user
        } else {
          // eslint-disable-next-line no-console
          console.error(
            'Warning: Malicious login attempt registered, bad credentials provided'
          )

          // If you return null then an error will be displayed advising the user to check their details.
          return null

          // You can also Reject this callback with an Error thus the user will be sent to the error page with the error message as a query parameter
        }
      },
    }),
  ],
})
