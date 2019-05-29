from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'data': data
        })

    def get_current_page(self):
        if self.page.has_next():
            return self.page.next_page_number()
        else:
            return self.page.has_previous() and self.page.previous_page_number()+1 or 1
