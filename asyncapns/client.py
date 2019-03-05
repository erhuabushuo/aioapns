from asyncapns.connection import APNsConnectionPool
from asyncapns.logging import logger


class APNs:
    def __init__(self, client_cert, cert_pass=None, max_connections=10, loop=None,
                 use_sandbox=False):
        self.pool = APNsConnectionPool(
            client_cert, cert_pass, max_connections, loop, use_sandbox)

    async def send_notification(self, request):
        response = await self.pool.send_notification(request)
        if not response.is_successful:
            logger.error(
                'Status of notification %s is %s (%s)',
                request.notification_id, response.status, response.description
            )
        return response
