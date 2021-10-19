from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import response, permissions
from rest_framework.decorators import renderer_classes, api_view, permission_classes
from rest_framework_swagger import renderers

from app2.models import employee
from app2.models import partners
from app2.models import merchants
from app2.models import manufacturer
from django.contrib import messages
from datatableview.views import DatatableView
from datatableview import Datatable
from djangoProject.forms import EmpForms, MerchantForms, PartnerForms, ManufacturerForms
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger import renderers as swagger_renderer
from rest_framework import renderers
import coreapi
from djangoProject.tables import employeeTable
from table.views import FeedDataView

@api_view()
@permission_classes((permissions.AllowAny,))
@renderer_classes([renderers.CoreJSONRenderer,
                   swagger_renderer.OpenAPIRenderer,
                   swagger_renderer.SwaggerUIRenderer,
                   ])
def schema_view(request):
    api_schema = api_schema_generator()
    return response.Response(api_schema)

def api_schema_generator():
    api_schema = coreapi.Document(
        title="My Swagger",
        content={
            "User Addresses": {

                "int_api_get": coreapi.Link(
                    url="/int_api/v1/addresses/",
                    action="get",
                    description="Get addresses of a user",
                    fields=[
                        coreapi.Field(
                            name="user_id",
                            required=True,
                            location="path",
                            description="Unique ID of the user whose addresses are to be found"
                        ),
                    ]
                ),
                "int_api_post": coreapi.Link(
                    url="/int_api/v1/addresses/",
                    action="post",
                    description="Add address for a user",
                    fields=[
                        coreapi.Field(
                            name="user_id",
                            required=True,
                            location="path",
                            description="Unique ID of the user"
                        ),
                        coreapi.Field(
                            name="address",
                            required=True,
                            location="path",
                            description="Address of the user"
                        ),
                    ]
                )
            }
        }
    )
    return api_schema

# def addpartners(request):
#     # today = datetime.datetime.now().date()
#     # return render(request, "homepage.html", {"today": "today"})
#     showAll = employee.objects.all()
#     return render(request, "addpartners.html", {"data": showAll})

# class MyDataView(FeedDataView):
#     token = employeeTable.token
#     # template_name = 'sample3.html'
#
#     def get_queryset(self):
#         return super(MyDataView, self).get_queryset().filter(id__gt=5)

class MyDatatable(Datatable):
    class Meta:
        columns = ["name", "address", "salary", "status"]
        search_fields = ["name", "address"]


class MyView(DatatableView):
    template_name = 'employee_list.html'
    model = employee
    datatable_class = MyDatatable


    # datatable_options = {
    #     'columns': [
    #         'name',
    #         'address',
    #         'salary',
    #         'status',
    #         ]
    # }

# class MyView(TemplateView):


def viewmerchant(request):

    showAll = merchants.objects.all()
    return render(request, "viewmerchant.html", {"data": showAll})

def viewmanufacture(request):

    showAll = manufacturer.objects.all()
    return render(request, "viewmanufacture.html", {"data": showAll})

# def addmerchant(request):
#     # today = datetime.datetime.now().date()
#     # return render(request, "homepage.html", {"today": "today"})
#     showAll = employee.objects.all()
#     return render(request, "addmerchant.html", {"data": showAll})



def addmain(request):
    # today = datetime.datetime.now().date()
    # return render(request, "homepage.html", {"today": "today"})
    showAll = employee.objects.all()
    return render(request, "main.html", {"data": showAll})


def pie_chart(request):
    labels = []
    data = []

    queryset = partners.objects.order_by('-id')[:9]
    for city in queryset:
        labels.append(city.name)
        data.append(city.id)

    return render(request, 'piechart.html', {
        'labels': labels,
        'data': data,
    })

def chart_data(request):
    dataset = partners.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')

    port_display_name = dict()
    for port_tuple in partners.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'series': [{
            'name': 'Embarkation Port',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)

def student_show(request):
    # today = datetime.datetime.now().date()
    # return render(request, "homepage.html", {"today": "today"})
    # x = []
    # for i in range(10):
    #     x.append(i)
        # text = "<h1>welcome to my app number %s!</h1>" % number
        # return HttpResponse(text)
    # return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))

     showAll = employee.objects.all()
     return render(request, "main.html", {"data": showAll})



def Editemp(request,id):
     editempobj = employee.objects.get(id=id)
     return render(request, "Edit1.html", {"employee": editempobj})


def editmerchant(request, id):
    editmerchant = merchants.objects.get(id=id)
    return render(request, "addmerchant.html", {"merchants": editmerchant})


def editmanufacture(request, id):
    editmanufacture = manufacturer.objects.get(id=id)
    return render(request, "addmanufacture.html", {"manufacturer": editmanufacture})

def editpartner(request, id):
    editpartners = partners.objects.get(id=id)
    return render(request, "addpartners.html", {"partners": editpartners})


def viewpartner(request):
    showAll = partners.objects.all()
    return render(request, "viewpartner.html", {"data": showAll})

def updateemp(request,id):
    updateempobj = employee.objects.get(id=id)
    form = EmpForms(request.POST, instance=updateempobj)
    if form.is_valid():
        form.save()
        messages.success(request,"record updated successfully")
        return render(request, "Edit1.html", {"employee": updateempobj})

def updatemerchant(request,id, ss3):
    updatemerchant = merchants.objects.get(id=id)
    form = MerchantForms(request.POST, instance=updatemerchant)
    if form.is_valid() and ss3 == 2:
        form.save()
        messages.success(request,"record updated successfully")
        return render(request, "addmerchant.html", {"merchants": updatemerchant})
    else:
        return render(request, 'addmerchant.html')

def updatemanufacturer(request,id, ss4):
    updatemanufacturer = manufacturer.objects.get(id=id)
    form4 = ManufacturerForms(request.POST, instance=updatemanufacturer)
    # messages.success(request, "record updated successfully")
    if form4.is_valid() and ss4 == 2:
        form4.save()
        messages.success(request,"record updated successfully")
        return render(request, "addmanufacture.html", {"manufacturer": updatemanufacturer})
    else:
         return render(request, 'addmanufacture.html')

def updatepartner(request, id, ss1):
        updatepartner = partners.objects.get(id=id)
        form = PartnerForms(request.POST, instance=updatepartner)
        if form.is_valid() and ss1 == 2:
            form.save()
            messages.success(request, "Record updated successfully")
            return render(request, "addpartners.html", {"partners": updatepartner})
        else:
         return render(request, 'addpartners.html')
# def student_show(request):
#     # data = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Tom'}]
#     student_show = employeeTable()
#     return render(request, "sample3.html", {"student_show": student_show})

def addmerchant(request, ss2):
        if request.method == 'POST' and ss2 == 2:
         if request.POST.get('id1') and request.POST.get('placeorderid') and request.POST.get('offerid') \
            and request.POST.get('typeofpackage') and request.POST.get('quantity') and request.POST.get('itemprice') \
            and request.POST.get('comment') and request.POST.get('merchantname') and request.POST.get('emailid') \
            and request.POST.get('phonenumber') and request.POST.get('address') or request.POST.get('billingtype'):
                saverecord2 = merchants()
                saverecord2.id1 = request.POST.get('id1')
                saverecord2.placeorderid = request.POST.get('placeorderid')
                saverecord2.offerid = request.POST.get('offerid')
                saverecord2.typeofpackage = request.POST.get('typeofpackage')
                saverecord2.quantity = request.POST.get('quantity')
                saverecord2.itemprice = request.POST.get('itemprice')
                saverecord2.comment = request.POST.get('comment')
                saverecord2.merchantname = request.POST.get('merchantname')
                saverecord2.emailid = request.POST.get('emailid')
                saverecord2.phonenumber = request.POST.get('phonenumber')
                saverecord2.address = request.POST.get('address')
                saverecord2.billingtype = request.POST.get('billingtype')
                saverecord2.save()
                messages.success(request, "Inserted successfully to database")

         context = {
             "data": 99,
         }

         return render(request, 'addmerchant.html', context)
        else:
         return render(request, 'addmerchant.html')


def addpartners(request, ss):
    if request.method == 'POST' and ss == 2:

     if request.POST.get('name') and request.POST.get('buisnessname') and request.POST.get('contactperson1') \
     and request.POST.get('contactdetails1') and request.POST.get('contactemail1')and request.POST.get('contactperson2')\
     and request.POST.get('contactdetails2') and request.POST.get('contactemail2') and request.POST.get('mailingaddress') \
     and request.POST.get('zipcode1') and request.POST.get('billingaddress') and request.POST.get('zipcode2'):

            saverecord1 = partners()
            saverecord1.name = request.POST.get('name')
            saverecord1.buisnessname = request.POST.get('buisnessname')
            saverecord1.contactperson1 = request.POST.get('contactperson1')
            saverecord1.contactdetails1 = request.POST.get('contactdetails1')
            saverecord1.contactemail1 = request.POST.get('contactemail1')
            saverecord1.contactperson2 = request.POST.get('contactperson2')
            saverecord1.contactdetails2 = request.POST.get('contactdetails2')
            saverecord1.contactemail2 = request.POST.get('contactemail2')
            saverecord1.mailingaddress = request.POST.get('mailingaddress')
            saverecord1.zipcode1 = request.POST.get('zipcode1')
            saverecord1.billingaddress = request.POST.get('billingaddress')
            saverecord1.zipcode2 = request.POST.get('zipcode2')
            saverecord1.save()
            messages.success(request, "Inserted")

     context = {
         "data": 99,
     }

     return render(request, 'addpartners.html', context)
    elif ss == 1:
     return render(request, 'addpartners.html')

def addmanufacturer(request, ss5):
    if request.method == 'POST' and ss5 == 2:
        if request.POST.get('id1') and request.POST.get('name') and request.POST.get('emailid') \
                and request.POST.get('address') and request.POST.get('passcode') \
                or request.POST.get('billingtype') or request.POST.get('materialtype') or request.POST.get('addonstype') \
                or request.POST.get('addonsnumber') and request.POST.get('phoneno'):
            saverecord3 = manufacturer()
            saverecord3.id1 = request.POST.get('id1')
            saverecord3.name = request.POST.get('name')
            saverecord3.emailid = request.POST.get('emailid')
            saverecord3.phoneno = request.POST.get('phoneno')
            saverecord3.address = request.POST.get('address')
            saverecord3.passcode = request.POST.get('passcode')
            saverecord3.billingtype = request.POST.get('billingtype')
            saverecord3.materialtype = request.POST.get('materialtype')
            saverecord3.addonstype = request.POST.get('addonstype')
            saverecord3.addonsnumber = request.POST.get('addonsnumber')
            saverecord3.save()
            messages.success(request, "Inserted successfully to database")

            context = {
                "data": 99,
            }

        return render(request, 'addmanufacture.html' , context)
    else:
        return render(request, 'addmanufacture.html')

def Insertemp(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('address') and request.POST.get('salary') \
                and request.POST.get('status'):
            saverecord = employee()
            saverecord.name = request.POST.get('name')
            saverecord.address = request.POST.get('address')
            saverecord.salary = request.POST.get('salary')
            saverecord.status = request.POST.get('status')
            saverecord.save()
            messages.success(request, 'Employee '+saverecord.name + "is saved succesfully")
        return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

