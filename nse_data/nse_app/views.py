from decimal import Decimal
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Index, DailyPrice
from .serializers import DailyPriceSerializer
from django.db.models import Max, Min
from rest_framework import status
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound



# The `DailyPriceListView` class is a view that retrieves and filters daily price data, paginates the
# results, and calculates data ranges for different price attributes.
class DailyPriceListView(ListAPIView):
    serializer_class = DailyPriceSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """
        The  code is a Python function that retrieves and filters daily price data based on user
        input, and returns the data along with pagination information and data ranges.
        :return: The `list` method is returning a `Response` object with the following data:
        """
        # index_name = self.kwargs['index_name']
        start_date = self.request.GET.get('start_date', None)
        end_date = self.request.GET.get('end_date', None)
        open_price = self.request.GET.get('open', None)
        high_price = self.request.GET.get('high', None)
        low_price = self.request.GET.get('low', None)
        close_price = self.request.GET.get('close', None)
        shares_traded = self.request.GET.get('shares_traded', None)
        turnover = self.request.GET.get('turnover', None)

        queryset = DailyPrice.objects.all()

        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        numeric_filters = {
            'open_price': open_price,
            'high_price': high_price,
            'low_price': low_price,
            'close_price': close_price,
            'shares_traded': shares_traded,
            'turnover': turnover,
        }
        for col, value in numeric_filters.items():
            if value:
                filter_condition = f"{col}__gte" if '>=' in value else f"{col}__lte"
                value = float(value)  # Convert the value to float\
                queryset = queryset.filter(**{filter_condition: value})

        queryset = queryset.order_by('date')

        return queryset
    def handle_exception(self, exc):
        """
        The function handles the exception of type NotFound and returns a response with a message
        indicating that the requested page data was not found.
        
        :param exc: The `exc` parameter is the exception that was raised. In this code snippet, the
        `handle_exception` method is used to handle exceptions that occur during the execution of the
        code
        :return: The code is returning a Response object with a dictionary containing various data
        fields. The "start_date" and "end_date" fields are populated with the values from the request's
        GET parameters. The "data" field is an empty list. The "pagination" field contains the "page",
        "total_pages", and "total_rows" fields, which are empty strings. The "ranges" field is
        """
        if isinstance(exc, NotFound):
            page = self.request.GET.get('page', 1)
            return Response({
                "start_date": self.request.GET.get('start_date', None),
                "end_date": self.request.GET.get('end_date', None),
                "data": [],
                "pagination": {
                    "page": "",
                    "total_pages": "",  
                    "total_rows": "",
                },
                "ranges": "", 
                "messages": f"Page no {page} data not found"
            })

        return super().handle_exception(exc)

    def list(self, request, *args, **kwargs):
        """
        The function retrieves a paginated queryset of data, calculates data ranges for different
        fields, and returns the data along with pagination information and the calculated ranges.
        
        :param request: The `request` parameter is an object that represents the HTTP request made by
        the client. It contains information such as the request method (GET, POST, etc.), headers, query
        parameters, and body
        :return: The code is returning a response containing the following data:
        - "start_date": the value of the 'start_date' parameter from the request's GET parameters
        - "end_date": the value of the 'end_date' parameter from the request's GET parameters
        - "data": a serialized representation of the paginated queryset
        - "pagination": information about the pagination, including the current page number
        """
        queryset = self.get_queryset()

        # Calculate data ranges here
        ranges = {
            "open": {"lowest": queryset.aggregate(Min('open_price'))['open_price__min'], "highest": queryset.aggregate(Max('open_price'))['open_price__max']},
            "high": {"lowest": queryset.aggregate(Min('high_price'))['high_price__min'], "highest": queryset.aggregate(Max('high_price'))['high_price__max']},
            "low": {"lowest": queryset.aggregate(Min('low_price'))['low_price__min'], "highest": queryset.aggregate(Max('low_price'))['low_price__max']},
            "close": {"lowest": queryset.aggregate(Min('close_price'))['close_price__min'], "highest": queryset.aggregate(Max('close_price'))['close_price__max']},
            "shares_traded": {"lowest": queryset.aggregate(Min('shares_traded'))['shares_traded__min'], "highest": queryset.aggregate(Max('shares_traded'))['shares_traded__max']},
            "turnover": {"lowest": queryset.aggregate(Min('turnover'))['turnover__min'], "highest": queryset.aggregate(Max('turnover'))['turnover__max']},
        }



        # page = self.request.GET.get('page', 1)
        paginator = self.pagination_class()

        paginated_queryset = paginator.paginate_queryset(queryset, self.request)

        serializer = self.serializer_class(paginated_queryset, many=True)

        response_data = {
            "start_date": self.request.GET.get('start_date', None),
            "end_date": self.request.GET.get('end_date', None),
            "data": serializer.data,
            "pagination": {
                "page": paginator.page.number,
                "total_pages": paginator.page.paginator.num_pages,
                "total_rows": paginator.page.paginator.count
            },
            "ranges": ranges,
            "messages": "Data retrieved successfully"
        }

        return Response(response_data)
