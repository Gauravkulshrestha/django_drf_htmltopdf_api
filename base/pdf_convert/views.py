from rest_framework.views import APIView
from .serializers import Html_to_PDFSerializer
from weasyprint import HTML
from django.http import HttpResponse

class HTML_to_PDFView(APIView):
    serializer_class = Html_to_PDFSerializer

    def post(self, request, format=None):
        serializer = Html_to_PDFSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           pdf = HTML(self.request.data.get('url')).write_pdf(optimize_size=('fonts', 'images'))
           response = HttpResponse(pdf,content_type='application/pdf')
           response['Content-Disposition'] = 'attachment; filename="report.pdf"'
           serializer.save()
        return response