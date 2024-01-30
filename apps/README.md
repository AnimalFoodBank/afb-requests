
# AFB Request Manager

* `auth/` - SuperTokens auth server, first pass
  * See further instructions in the [SuperTokens docs](https://supertokens.io/docs/emailpassword/quick-setup/supertokens)
* `api/` - A Django application running the REST API.
* `ui/` - A Vite+Vue+Tailwind application for the frontend UI.
* `vvs/` - A Vueform+Vite+Tailwind via [cloned starter repo](https://github.com/vueform/vite-starter#installation)
  * See further instructions in the [Vueform docs](https://vueform.com/docs/installation)

In dev, the apps run separately. In prod the Django app static directory hosts the generated build files.
