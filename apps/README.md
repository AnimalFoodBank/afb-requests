
# AFB Requests

* `auth/` - Zitadel auth server
  * See further instructions in the [Zitadel docs](https://docs.zitadel.ch/docs/installation/installation)
* `api/` - A Django application running the REST API.
* `ui/` - A Vite+Vue+Tailwind application for the frontend UI.
* `vvs/` - A Vueform+Vite+Tailwind via [cloned starter repo](https://github.com/vueform/vite-starter#installation)
  * See further instructions in the [Vueform docs](https://vueform.com/docs/installation)

In dev, the apps run separately. In prod the Django app static directory hosts the generated build files.
