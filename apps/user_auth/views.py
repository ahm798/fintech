from django.http import JsonResponse
from django.views import View
from loguru import logger

class TestLoggerView(View):
    def get(self, request, *args, **kwargs):
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.success("This is a success message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")
        return JsonResponse({"message": "Check your logs!"})