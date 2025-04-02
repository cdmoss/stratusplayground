from dandy.llm import LlmBot
from customergen.CustomerIntel import CustomerIntel
from core.models import Customer
from django.template.response import TemplateResponse
from django_glue import glue_model_object, glue_query_set
from django.shortcuts import redirect

# Create your views here.
def generate_customer_view(request):
    customers = Customer.objects.all()
    glue_query_set(request, unique_name='customers', target=customers)

    return TemplateResponse(request, 'index.html', context={})


def edit_customer(request):
    if request.method == 'GET':
        customer_id = request.GET.get('customer_id')
        print(customer_id)
        customer = Customer.objects.get(id=customer_id)
        glue_model_object(request, 'customer', customer, access='change')
        return TemplateResponse(request, 'customer_edit.html', {'customer': customer})
    
    if request.method == 'POST':
        prompt = request.POST.get('prompt') 
        print(prompt)
        new_customer_intel = LlmBot.process(prompt=prompt, intel_class=CustomerIntel)
        new_customer = Customer.objects.create(
            first_name=new_customer_intel.first_name,
            last_name=new_customer_intel.last_name,
            email=new_customer_intel.email,
            phone=new_customer_intel.phone,
            address=new_customer_intel.address,
            city=new_customer_intel.city,
            state=new_customer_intel.state,
            zip_code=new_customer_intel.zip_code,
            country=new_customer_intel.country
        )

        glue_model_object(request, 'customer', new_customer, access='change')

        return TemplateResponse(request, 'customer_edit.html', {'customer': new_customer})
    else:
        return redirect('/')

