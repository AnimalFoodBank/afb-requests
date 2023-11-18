from corsheaders.middleware import CorsMiddleware


class DebugCorsMiddleware(CorsMiddleware):
    def __call__(self, request):
        # import pdb; pdb.set_trace()
        return super().__call__(request)
